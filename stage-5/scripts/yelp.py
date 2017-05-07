#############################
#--- yelp.py ---#
#############################
# This is a helper python file that loads the Yelp dataset (Table Y).
# Given a Yelp, the find() function of the class YelpDataset
# returns the corresponding demogrpahic data for that restaurant.

import csv

class YelpDataset:
    restaurants = {}

    def __init__(self):
        input_file = csv.DictReader(open("../datasets/yelp_data.csv"))
        for row in input_file:
            data = [
                        row["name"],
                        row["address"],
                        row["zipcode"],
                        row["rating"],
                        row["review_count"]
                    ]
            key = row["name"] + ":" + row["address"] + ":" + row["zipcode"]
            self.restaurants[key] = data


    def find(self, key):
        if key in self.restaurants:
            return self.restaurants[key]
        else:
            print("Failed to find yelp key")
            return []
