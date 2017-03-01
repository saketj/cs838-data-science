import json
import re


def get_context_for_row(row):
    file_path = row['file name']
    review_file = open(file_path, "r")
    start_offset = int(row['start offset'])
    review_file.seek(start_offset, 0)
    ch = review_file.read(1)
    while ch != '.' and start_offset != 0:          # continue looking for the previous context begin
        start_offset -= 1
        review_file.seek(start_offset, 0)
        ch = review_file.read(1)
    review_file.seek(start_offset + 1, 0)
    line = review_file.readline().split(".")[0]
    line = re.sub(r"\n", "", line)                  # clean-up any newlines
    line = re.sub(r"<dish>.*?</dish>", '', line)    # Remove <dish>..</dish> from the line
    review_file.close()
    return line.lower().decode('utf-8', 'ignore')


def get_context_after_row(row):
    file_path = row['file name']
    review_file = open(file_path, "r")
    start_offset = int(row['start offset'])
    review_file.seek(start_offset, 0)
    line = review_file.readline().split(".")[0]
    line = re.sub(r"\n", "", line)  # clean-up any newlines
    line = re.sub(r"<dish>.*?</dish>", '', line)  # Remove <dish>..</dish> from the line
    review_file.close()
    return line.lower().decode('utf-8', 'ignore')


class FoodAdjectiveFeature:
    food_adjectives = []

    def __init__(self):
        # Read the feature hints
        with open("./scripts/feature_extraction/feature_hints.json") as json_file:
            feature_data = json.load(json_file)
            self.food_adjectives = feature_data["food_adjectives"]

    def process(self, row):
        if 'dish name' in row:
            dish_name = row['dish name'].lower().decode('utf-8', 'ignore')
        else:
            dish_name = row['negative sample'].lower().decode('utf-8', 'ignore')
        count = 0
        for adjective in self.food_adjectives:
            if bool(adjective in dish_name):
                count += 1
        return count

    @staticmethod
    def get_feature_name():
        return 'count_of_food_adjectives_in_dish_name'

    @staticmethod
    def get_feature_type():
        return 'NUMERIC'


class FoodIngredientsFeature:
    food_ingredients = []

    def __init__(self):
        # Read the feature hints
        with open("./scripts/feature_extraction/feature_hints.json") as json_file:
            feature_data = json.load(json_file)
            self.food_ingredients = feature_data["food_ingredients"]

    def process(self, row):
        if 'dish name' in row:
            dish_name = row['dish name'].lower().decode('utf-8', 'ignore')
        else:
            dish_name = row['negative sample'].lower().decode('utf-8', 'ignore')
        count = 0
        for adjective in self.food_ingredients:
            if bool(adjective in dish_name):
                count += 1
        return count

    @staticmethod
    def get_feature_name():
        return 'count_of_food_ingredients_in_dish_name'

    @staticmethod
    def get_feature_type():
        return 'NUMERIC'


class FoodAdjectiveContextFeature:
    food_adjectives = []

    def __init__(self):
        # Read the feature hints
        with open("./scripts/feature_extraction/feature_hints.json") as json_file:
            feature_data = json.load(json_file)
            self.food_adjectives = feature_data["food_adjectives"]

    def process(self, row):
        context = get_context_for_row(row)
        count = 0
        for adjective in self.food_adjectives:
            if bool(adjective in context):
                count += 1
        return count

    @staticmethod
    def get_feature_name():
        return 'count_of_food_adjectives_in_context'

    @staticmethod
    def get_feature_type():
        return 'NUMERIC'


class FoodIngredientsContextFeature:
    food_ingredients = []

    def __init__(self):
        # Read the feature hints
        with open("./scripts/feature_extraction/feature_hints.json") as json_file:
            feature_data = json.load(json_file)
            self.food_ingredients = feature_data["food_ingredients"]

    def process(self, row):
        context = get_context_for_row(row)
        count = 0
        for adjective in self.food_ingredients:
            if bool(adjective in context):
                count += 1
        return count

    @staticmethod
    def get_feature_name():
        return 'count_of_food_ingredients_in_context'

    @staticmethod
    def get_feature_type():
        return 'NUMERIC'


class PriceDistanceFeature:
    def __init__(self):
        return

    def process(self, row):
        context = get_context_after_row(row).strip()
        return context.find("$")

    @staticmethod
    def get_feature_name():
        return 'price_distance'

    @staticmethod
    def get_feature_type():
        return 'INTEGER'

class CommaFollowedFeature:
    def __init__(self):
        return

    def process(self, row):
        context = get_context_after_row(row).strip()
        return context.find(",")

    @staticmethod
    def get_feature_name():
        return 'followed_by_comma'

    @staticmethod
    def get_feature_type():
        return 'INTEGER'

class HasPriceMentionFeature:
    def __init__(self):
        return

    def process(self, row):
        context = get_context_after_row(row)
        if "$" in context:
            return 'true'
        else:
            return 'false'

    @staticmethod
    def get_feature_name():
        return 'has_price_mention'

    @staticmethod
    def get_feature_type():
        return ['true', 'false']


class HasMealNameMentionedFeature:
    meal_names = []

    def __init__(self):
        # Read the feature hints
        with open("./scripts/feature_extraction/feature_hints.json") as json_file:
            feature_data = json.load(json_file)
            self.meal_names = feature_data["meal_names"]

    def process(self, row):
        if 'dish name' in row:
            dish_name = row['dish name'].lower().decode('utf-8', 'ignore')
        else:
            dish_name = row['negative sample'].lower().decode('utf-8', 'ignore')
        context = get_context_for_row(row)
        for name in self.meal_names:
            if name in context or name in dish_name:
                return 'true'
        return 'false'

    @staticmethod
    def get_feature_name():
        return 'has_meal_name_mentioned'

    @staticmethod
    def get_feature_type():
        return ['true', 'false']


class HasDishQuantityMentionFeature:
    other_relevant = []

    def __init__(self):
        # Read the feature hints
        with open("./scripts/feature_extraction/feature_hints.json") as json_file:
            feature_data = json.load(json_file)
            self.other_relevant = feature_data["dish_quantity"]

    def process(self, row):
        if 'dish name' in row:
            dish_name = row['dish name'].lower().decode('utf-8', 'ignore')
        else:
            dish_name = row['negative sample'].lower().decode('utf-8', 'ignore')
        context = get_context_for_row(row)
        for name in self.other_relevant:
            if name in context or name in dish_name:
                return 'true'
        return 'false'

    @staticmethod
    def get_feature_name():
        return 'has_dish_quantity_mention'

    @staticmethod
    def get_feature_type():
        return ['true', 'false']

class HasCapitalStarting:
    def __init__(self):
        return

    def process(self, row):
        if 'dish name' in row:
            dish_name = re.sub(r"[^ +\w]", "", row['dish name'])
        else:
            dish_name = re.sub(r"[^ +\w]", "", row['negative sample'])
        new_name = unicode(dish_name, errors='ignore')
        if new_name[0] >= 'A' and new_name[0] <= 'Z' :
            return 'true'
        else :
            return 'false'

    @staticmethod
    def get_feature_name():
        return 'dish_name_starts_with_capital'

    @staticmethod
    def get_feature_type():
        return ['true', 'false']

class NumberOfCapitals:
    def __init__(self):
        return

    def process(self, row):
        if 'dish name' in row:
            dish_name = re.sub(r"[^ +\w]", "", row['dish name'])
        else:
            dish_name = re.sub(r"[^ +\w]", "", row['negative sample'])
        new_name = unicode(dish_name, errors='ignore')
        count = 0
        for i in range(len(new_name)):
            if new_name[i] >= 'A' and new_name[i] <= 'Z' :
                count += 1
        return count

    @staticmethod
    def get_feature_name():
        return 'count_capital_letters'

    @staticmethod
    def get_feature_type():
        return 'INTEGER'

class NumberOfCommas:
    def __init__(self):
        return

    def process(self, row):
        context = get_context_for_row(row)
        count = 0
        for i in range(len(context)):
            if context[i] == ',' or context[i] == ';' :
                count += 1
        if len(context) > 0 :
            return count/len(context)
        else :
            return 0

    @staticmethod
    def get_feature_name():
        return 'count_commas_semicolon'

    @staticmethod
    def get_feature_type():
        return 'NUMERIC'


class DishNameFeature:
    def __init__(self):
        return

    def process(self, row):
        if 'dish name' in row:
            dish_name = re.sub(r"[^ +\w]", "", row['dish name'])
        else:
            dish_name = re.sub(r"[^ +\w]", "", row['negative sample'])
        return unicode(dish_name, errors='ignore')

    @staticmethod
    def get_feature_name():
        return 'dish_name'

    @staticmethod
    def get_feature_type():
        return 'STRING'


class FileNameFeature:
    def __init__(self):
        return

    def process(self, row):
        file_name = re.sub(r"\n", "", row['file name'])
        return unicode(file_name, errors='ignore')

    @staticmethod
    def get_feature_name():
        return 'file_name'

    @staticmethod
    def get_feature_type():
        return 'STRING'


class FeatureLabel:
    def __init__(self):
        return

    def process(self, row):
        if 'negative sample' in row:
            return 'negative'
        else:
            return 'positive'

    @staticmethod
    def get_feature_name():
        return 'class_label'

    @staticmethod
    def get_feature_type():
        return ['positive', 'negative']

