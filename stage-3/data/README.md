# Datasets used for Project Stage 3

We use the same datasets that we had downloaded for Project Stage 1. We describe these two datasets below and how we used them in Project Stage 3:

### Yelp New York Restaurant Dataset (A.csv)
  - The Yelp restaurant dataset contains the information of different restaurant businesses acquired using the search api provided by Yelp. The dataset has been narrowed down to focus on only the restaurants in New York.
  - Attributes of the dataset used for entity matching:
    -- `name`: name of the restaurant
    -- `address`: address where the restaurant is located in New York City
    -- `zipcode`: zipcode of the area where the restaurant is located
    -- `cuisine`: the types of cuisine that are served in the restaurant
- Number of tuples in this dataset: **19,270**

### New York City Restaurant Inspection Dataset (B.csv)
 - The New York City Restaurant Inspection Dataset contains inspection results for various NYC restaurants that are conducted on regular basis by New York City Department of Health and Mental Hygiene (DOHMH).
 - Attributes of the dataset used for entity matching:
 -- `name`: name of the restaurant
 -- `address`: address where the restaurant is located in New York City
 -- `zipcode`: zipcode of the area where the restaurant is located
 -- `cuisine`: the types of cuisine that are served in the restaurant
- Number of tuples in this dataset: **23,907**