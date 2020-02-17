import comparator
import numpy as np
import csv

def test_mse_calculator_function():
    # 1p x 1px orange picture represented as an array
    image_a=np.asanyarray([[[ 39, 127, 255]]], dtype=np.uint8)
    # 1p x 1px red picture represented as an array
    image_b=np.asanyarray([[[ 36, 28, 237]]], dtype=np.uint8)
    score=comparator.mse(image_a,image_b)
    assert score=="10134.0"

def test_comparator_function():
    file = open("test.csv", "w") 
    file.write("images/test_source.png,images/test_target.png") 
    file.close() 
    with open('test.csv', 'r', newline='') as testfile:
        test_list=comparator.comparator(testfile)
    assert any(d['SimilarityScore'] == '10134.0' for d in test_list)

