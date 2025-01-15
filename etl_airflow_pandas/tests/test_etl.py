import os
import pandas as pd
from scripts.etl import extract, transform, load

def test_extract():
    extract()
    assert os.path.exists('data/temp/extracted_data.csv')

def test_transform():
    transform()
    data = pd.read_csv('data/temp/transformed_data.csv')
    assert 'new_column' in data.columns

def test_load():
    load()
    assert os.path.exists('data/final_data.csv')
