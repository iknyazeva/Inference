import pytest
import numpy as np
from inference.simulation import get_permutation_sample, get_bootstrap_sample, compute_statistics


def test_get_permutation_sample():
    data1 = np.random.rand(1, 10)
    data2 = np.random.rand(1, 10)
    pdata1, pdata2 = get_permutation_sample(data1, data2)
    assert type(pdata1), type(pdata2) is np.ndarray


def test_get_bootstrap_sample():
    bsample = get_bootstrap_sample(np.random.rand(1, 10))
    assert type(bsample) is np.ndarray


def test_compute_statistics():
    statistics = compute_statistics(np.random.rand(1, 10))
    assert type(statistics) is float
