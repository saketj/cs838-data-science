########################
#--- data_merger.py ---#
########################
# The main python file that does data merging for matches between
# tables A and B. The file expects two command-line arguments and can be run as:
# `python3 data_merger.py <input_file> <output_file>`

import csv
import sys

# Import our python classes that we wrote for merging. (Defined later)
import merge_rules
import nyc_demographics

nyc_demographics_dataset = nyc_demographics.NYCDemographicsDataset()

def merge_attributes(row):
    merge_rules_dict = {
        'NameMergeRule': merge_rules.NameMergeRule(),
        'AddressMergeRule': merge_rules.AddressMergeRule(),
        'ZipcodeMergeRule': merge_rules.ZipcodeMergeRule(),
        'CuisineMergeRule': merge_rules.CuisineMergeRule()
    }
    merged_name = merge_rules_dict['NameMergeRule'].process(row["ltable_name"], row["rtable_name"])
    merged_address = merge_rules_dict['AddressMergeRule'].process(row["ltable_address"], row["rtable_address"])
    merged_zipcode = merge_rules_dict['ZipcodeMergeRule'].process(row["ltable_zipcode"], row["rtable_zipcode"])
    merged_cuisine = merge_rules_dict['CuisineMergeRule'].process(row["ltable_cuisine"], row["rtable_cuisine"])
    extracted_price = row["ltable_price"]
    extracted_violation_code = row["rtable_violation_code"]
    extracted_critical_flag = row["rtable_critical_flag"]
    extracted_grade = row["rtable_grade"]
    merged_row = [merged_name, merged_address, merged_zipcode, merged_cuisine,
                extracted_price, extracted_violation_code, extracted_critical_flag, extracted_grade]

    # Add the attributes from Table D: NYC Demographics Dataset
    merged_row.extend(nyc_demographics_dataset.find(merged_zipcode))
    return merged_row

def write_header(f):
    # Write CSV Header
    f.writerow(["name", "address", "zipcode", "cuisine", "price",
                    "violation_code", "critical_flag", "grade",
                    "median_household_income", "median_real_estate_value",
                    "population_density", "cost_of_living", "population"])

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
