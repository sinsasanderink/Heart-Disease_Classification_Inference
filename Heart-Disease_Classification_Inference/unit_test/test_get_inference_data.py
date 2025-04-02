import warnings
warnings.filterwarnings("ignore")

import sys
import os

# Add parent directory (9.Final/) to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils import *
import pandas as pd


class TestGetInferenceData:
    def test_method_output_type(self):
        df = pd.DataFrame()
        inference_data, labels = get_inference_data()
        assert type(inference_data)==type(df), "inference data should be a dataframe"

    def test_method_output_len(self):
        inference_data, labels = get_inference_data()
        assert len(inference_data) == len(labels), "length of data and labels are not matching"