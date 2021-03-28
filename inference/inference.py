import pandas as pd
import numpy as np


class Infer(object):
    """
    class for inference with methods for independence test and points estimates (for now)
    """

    def __init__(self, data, nsamples = 10000):
        """

        Args:
            data (pandas dataframe):
        """
        self.data = data
        self.test_type = None
        self.direction = None
        self.t_type = None
        self.theor = None
        self.nsamples = nsamples


    @classmethod
    def from_two_arrays(cls, group1, group2, t_type='independent'):
        """ Create dataframe from two

        Args:
            t_type (str): 'independent', paired
            group1 (1d array or list): values for group1
            group2 (1d array or list):  values for group2

        Returns:
            dataframe: with columns: value, group_id
        """
        data = np.concatenate([group1.values, group2.values])
        groups = (group1, group2)
        df = pd.DataFrame(dict(value=data, group=groups))
        df['group_id'] = pd.Categorical(df['group']).codes
        return df
        pass

    @classmethod
    def from_two_proportions(cls, prop_1, prop_2, len_data1, len_data2):
        """  (Fill based on example with restaurants)
        Returns:



        Args:
            prop_1:
            prop_2:
            len_data1:
            len_data2:

        Returns:
                dataframe: with columns: value, group_id


        """

        pass

    def test_independence(self, column_name, test_stat, theor=False, direction='both', **kwargs):
        """ Permutation based independence test, desired test stat should be provided

        Args:
            test_stat (str or list of string):  np.mean, np.median, np.std, np.percentile or several
            theor (str): provide theoretical t_stat results
            nsamples(int): number of samples for simulation
            direction (str):
            column_name (str): column name in dataframe for testing

        Returns:
            empirical test statitistics
            test_stat sample
            simulation based p_val
            dataframe with ttest output if theor = True

        """
        self.test_type = 'independence'
        self.direction = direction
        self.theor = theor



        pass

    def point_estimates(self, test_stat, theor = False, direction='both', **kwargs):
        pass

    def visualize(self):
        """ Visualize results of inference based on type of test

        Returns:
            plt.plot
            conclusion
        """
        pass
