import pytest
import numpy as np
import pandas as pd
from inference.inference import Infer

data = pd.DataFrame()

class TestInfer:

    def test_from_two_arrays(self):
        test_infer = Infer(data)
        ar1 = np.random.rand(1, 10)
        ar2 = np.random.rand(1, 10)
        df = test_infer.from_two_arrays(ar1, ar2)
        value_in_df = "value" in df
        id_in_df = "group_id" in df
        assert value_in_df is True, id_in_df is True

    def test_from_two_proportions(self):
        test_infer = Infer(data)
        prop_1 = 75
        prop_2 = 25
        len_data1 = len_data2 = 10
        df = test_infer.from_two_proportions(prop_1, prop_2, len_data1, len_data2)
        value_in_df = "value" in df
        id_in_df = "group_id" in df
        assert value_in_df is True, id_in_df is True

    def test_test_independence(self):
        pass