#!/bin/bash

echo "Running for P.arff..."
python2 scripts/feature_extraction/feature_extractor.py Debugging_stage/debug_P.arff Debugging_stage/debug_posextracted_P.csv Debugging_stage/debug_negextracted_P.csv

echo "Running for Q.arff..."
python2 scripts/feature_extraction/feature_extractor.py Debugging_stage/debug_Q.arff Debugging_stage/debug_posextracted_Q.csv Debugging_stage/debug_negextracted_Q.csv

echo "Running for I.arff"
python2 scripts/feature_extraction/feature_extractor.py datasets/features_I/features_I.arff datasets/pos_extracted_I.csv datasets/neg_extracted_I.csv

echo "Running for J.arff"
python2 scripts/feature_extraction/feature_extractor.py datasets/features_J/features_J.arff datasets/pos_extracted_J.csv datasets/neg_extracted_J.csv
