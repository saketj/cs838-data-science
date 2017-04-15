#!/usr/bin/python

import re

class NameMergeRule:
    @staticmethod
    def process(value_l, value_r):
        if len(value_l) > len(value_r):
            return value_l
        else:
            return value_r


class AddressMergeRule:
    @staticmethod
    def process(value_l, value_r):
        if len(value_l) > len(value_r):
            return value_l
        else:
            return value_r


class ZipcodeMergeRule:
    @staticmethod
    def process(value_l, value_r):
        if value_l:
            # Trust zipcode from Yelp more because it is coming from
            # a relational database backend, extracted using Yelp API.
            return value_l
        else:
            return value_r


class CuisineMergeRule:
    @staticmethod
    def process(value_l, value_r):
        if len(value_l) > len(value_r):
            return value_l
        else:
            return value_r
