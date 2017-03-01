#!/bin/bash

echo "Generating positive and negative samples for P..."
python2 scripts/pos_extract.py 'Debugging_stage/Set_P/*.txt' Debugging_stage/debug_posextracted_P.csv
python2 scripts/neg_extract.py 'Debugging_stage/Set_P/*.txt' Debugging_stage/debug_negextracted_P.csv

echo "Generating positive and negative samples for Q..."
python2 scripts/pos_extract.py 'Debugging_stage/Set_Q/*.txt' Debugging_stage/debug_posextracted_Q.csv
python2 scripts/neg_extract.py 'Debugging_stage/Set_Q/*.txt' Debugging_stage/debug_negextracted_Q.csv

echo "Generating positive and negative samples for I..."
python2 scripts/pos_extract.py 'datasets/Set_I_DEV/*.txt' datasets/pos_extracted_I.csv
python2 scripts/neg_extract.py 'datasets/Set_I_DEV/*.txt' datasets/neg_extracted_I.csv

echo "Generating positive and negative samples for J..."
python2 scripts/pos_extract.py 'datasets/Set_J_TEST/*.txt' datasets/pos_extracted_J.csv
python2 scripts/neg_extract.py 'datasets/Set_J_TEST/*.txt' datasets/neg_extracted_J.csv

echo "Generating features arff for P..."
python2 scripts/feature_extraction/feature_extractor.py Debugging_stage/debug_P.arff Debugging_stage/debug_posextracted_P.csv Debugging_stage/debug_negextracted_P.csv

echo "Generating features arff for Q..."
python2 scripts/feature_extraction/feature_extractor.py Debugging_stage/debug_Q.arff Debugging_stage/debug_posextracted_Q.csv Debugging_stage/debug_negextracted_Q.csv

echo "Generating features arff for I..."
python2 scripts/feature_extraction/feature_extractor.py datasets/features_I/features_I.arff datasets/pos_extracted_I.csv datasets/neg_extracted_I.csv

echo "Generating features arff for J..."
python2 scripts/feature_extraction/feature_extractor.py datasets/features_J/features_J.arff datasets/pos_extracted_J.csv datasets/neg_extracted_J.csv
