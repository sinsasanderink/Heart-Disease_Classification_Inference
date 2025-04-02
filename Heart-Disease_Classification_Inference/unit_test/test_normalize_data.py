import sys
import os
import warnings
warnings.filterwarnings("ignore")

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils import *
import pandas as pd

class TestDataNormalization:
    def test_norm_data_len(self):
        inference_data, labels = get_inference_data()
        norm_df = normalize_data(inference_data)
        assert len(inference_data) == len(norm_df), "length has changed after normalization"
