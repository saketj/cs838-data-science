#!/usr/bin/python

import arff
import csv
import sys

import features


def init_arff():
    arff_content = {
        'description': 'NYC Restaurant Review Dataset',
        'relation': 'nyc_restaurant_review',
        'attributes': [],
        'data': []
    }
    return arff_content


def init_features(arff_content):
    list_of_attributes = define_attributes()
    for attr in list_of_attributes:
        arff_content['attributes'].append((attr.get_feature_name(), attr.get_feature_type()))
    return arff_content


def add_data(arff_content, input_filename):
    list_of_attributes = define_attributes()
    with open(input_filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            instance = []
            for attr in list_of_attributes:
                instance.append(attr.process(row))
            arff_content['data'].append(instance)
    return arff_content


def define_attributes():
    list_of_attributes = [
                            features.FoodAdjectiveFeature(),
                            features.FoodIngredientsFeature(),
                            features.FoodAdjectiveContextFeature(),
                            features.FoodIngredientsContextFeature(),
                            features.PriceMentionFeature(),
                            features.HasMealNameMentionedFeature(),
                            features.OtherRelevantFeature(),
                            features.DishNameFeature(),
                            features.FileNameFeature(),
                            features.FeatureLabel()
                         ]
    return list_of_attributes


def main(argv):
    if len(argv) < 2:
        sys.stderr.write("Incorrect arguments. Expecting two arguments: <output_file> <input_file_1> <input_file_2>\n")
        sys.exit(-1)
    output_file = open(argv[0], "wb")
    i = 1
    arff_content = init_arff()
    init_features(arff_content)
    while i < len(argv):
        input_filename = argv[i]
        add_data(arff_content, input_filename)
        i += 1
    arff.dump(arff_content, output_file)
    output_file.close()


if __name__ == "__main__":
    main(sys.argv[1:])
