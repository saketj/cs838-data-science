#############################
#--- nyc_demographics.py ---#
#############################
# This is a helper python file that loads the NYC Demographics dataset (Table D).
# Given a zipcode, the find() function of the class NYCDemographicsDataset
# returns the corresponding demogrpahic data for that zipcode.

import csv

class NYCDemographicsDataset:
    zipcode_data_map = {}

    def __init__(self):
        input_file = csv.DictReader(open("../data/Table_D.csv"))
        for row in input_file:
            data = [
                        row["median_household_income"],
                        row["median_real_estate_value"],
                        row["population_density"],
                        row["cost_of_living"],
                        row["population"]
                    ]
            self.zipcode_data_map[row["zipcode"]] = data


    def find(self, zipcode):
        if zipcode in self.zipcode_data_map:
            return self.zipcode_data_map[zipcode]
        else:
            return []
