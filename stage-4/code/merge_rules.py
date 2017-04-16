#!/usr/bin/python

import json
import re

class NameMergeRule:
    @staticmethod
    def process(value_l, value_r):
        # After inspection of the dataset, we find that the longer names
        # are more descriptive and hence better.
        if len(value_l) > len(value_r):
            return value_l
        else:
            return value_r


class AddressMergeRule:
    @staticmethod
    def process(value_l, value_r):
        if value_l:
            # Trust address from Yelp(value_l) over Inspection dataset(value_r)
            # because it is more reliable, given that it is provided by the
            # restaurant itself and used by customers to navigate to the place.
            return value_l
        else:
            return value_r


class ZipcodeMergeRule:
    @staticmethod
    def process(value_l, value_r):
        if value_l:
            # Trust zipcode from Yelp(value_l) over Inspection dataset(value_r)
            # because it is coming from a relational database backend of Yelp,
            # extracted using Yelp API.
            return value_l
        else:
            return value_r


class CuisineMergeRule:
    valid_cuisine_map = {}

    def __init__(self):
        with open('../datasets/cuisines_dictionary.json') as json_data:
            self.valid_cuisine_map = json.load(json_data)

    def process(self, value_l, value_r):
        # For cusinies, we merge all the cusinie names mentioned in
        # both value_l and value_r. However, we pick only those names
        # that exist in the valid dictionary of cuisines that we have created.
        merged_cuisine = set()
        cuisines = re.split('\W', value_l + " " + value_r)
        for cuisine in cuisines:
            if cuisine in self.valid_cuisine_map:
                # add the cusinie associated with this key to the set
                merged_cuisine.add(self.valid_cuisine_map[cuisine])

        return " ".join(merged_cuisine)
