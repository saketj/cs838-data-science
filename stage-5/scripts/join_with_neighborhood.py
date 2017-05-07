########################
#--- data_merger.py ---#
########################
# The main python file that does data merging for matches between
# tables A and B. The file expects two command-line arguments and can be run as:
# `python3 data_merger.py <input_file> <output_file>`

import csv
import sys

class NYCNeighborhoodDataset:
    neighborhoods = {}

    def __init__(self):
        input_file = csv.DictReader(open("../datasets/Table_NYC_Neighborhood.csv"))
        for row in input_file:
            data = [
                        row["Neighborhood"],
                        row["Borough"]
                    ]
            key = row["ZipCode"]
            self.neighborhoods[key] = data


    def find(self, key):
        if key in self.neighborhoods:
            return self.neighborhoods[key]
        else:
            print("Failed to find zipcode key " + key)            
            return []

nyc_neighborhood_dataset = NYCNeighborhoodDataset()

def merge_attributes(row):
    # Add the attributes from Table D: NYC Demographics Dataset
    merged_row = [
        row["name"],
        row["address"],
        row["zipcode"],
        row["cuisine"],
        row["price"],
        row["violation_code"],
        row["critical_flag"],
        row["grade"],
        row["median_household_income"],
        row["median_real_estate_value"],
        row["population_density"],
        row["cost_of_living"],
        row["population"]
    ]
    merged_row.extend(nyc_neighborhood_dataset.find(row["zipcode"]))
    return merged_row

def write_header(f):
    # Write CSV Header
    f.writerow(["name", "address", "zipcode", "cuisine", "price",
                    "violation_code", "critical_flag", "grade",
                    "median_household_income", "median_real_estate_value",
                    "population_density", "cost_of_living", "population", "neighborhood", "borough"])

def write_row(f, merged_row):
    f.writerow(merged_row)

def main(argv):
    if len(argv) < 2:
        sys.stderr.write("Incorrect arguments. Expecting two arguments: <input_file> <output_file>\n")
        sys.exit(-1)

    input_file = csv.DictReader(open(argv[0]))
    output_file = csv.writer(open(argv[1], "w"))
    write_header(output_file)

    for row in input_file:
        merged_row = merge_attributes(row)
        write_row(output_file, merged_row)

if __name__ == "__main__":
    main(sys.argv[1:])
