# Functions for data simulation
import numpy as np


def get_permutation_sample(data1, data2):
    """ Function for creating permutation sample from data

   Args:
       data1 (1d numpy array or list):
       data2 1d numpy array or list):

   Returns:
      pdata1 (1d numpy array or list)
      pdata2 (1d numpy array or list)

   """

    pass


def get_bootstrap_sample(sample):
    """ Function for creating bootstrap sample from data,
   in case when each row contains more then one value for row, indexes of sample should be bootstraped

  Args:
      sample (nd numpy array or list): sample for bootstrap
  Returns:
      bsample (nd numpy array or list):

  """

    pass


def compute_statistics(random_sample, stat=np.mean, **kwargs):
   """ Compute statistic by random sample

   Args:
      random_sample (ndarray or list of floats): sample from probability distribution or data real data sample
      stat (func): statistics, could be np.mean, np.median, np.std, np.percentile
      **kwargs : low and upper bound for percentile

   Returns:
      test_statistics (float)
   """
   pass