import numpy as np
import pandas as pd
import pingouin as pg


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
    # зачем t_type
    def from_two_arrays(cls, group1, group2, t_type='independent'):
        """ Create dataframe from two

        Args:
            t_type (str): 'independent', paired
            group1 (1d array or list): values for group1
            group2 (1d array or list):  values for group2

        Returns:
            dataframe: with columns: value, group_id
        """
        df0 = pd.DataFrame()
        df1 = pd.DataFrame()
        df0['values'] = group1
        df0['group_id'] = 0
        df1['values'] = group2
        df1['group_id'] = 1
        dataframe = df0.append(df1)
        return dataframe

    @classmethod
    # не понятно, что есть что
    def from_two_proportions(cls, prop_1, prop_2, len_data1, len_data2):
        """  (Fill based on example with restaurants)

        Args:
            prop_1:
            prop_2:
            len_data1:
            len_data2:

        Returns:
                dataframe: with columns: value, group_id

        """
        # overall = np.array(75 * [1] + 25 * [0])
        # restrt = np.array(67 * [1] + 33 * [0])
        df0 = pd.DataFrame()
        df1 = pd.DataFrame()
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

        def permutation_sample(data1, data2):
            data = np.concatenate((data1, data2))
            permuted_data = np.random.permutation(data)
            return permuted_data[:len(data1)], permuted_data[len(data1):]

        data1 = self.data[self.data['male'] == 0][column_name]
        data2 = self.data[self.data['male'] == 1][column_name]

        p1, p2 = permutation_sample(data1, data2)

        # empirical test statitistics
        t_diff = test_stat(data2) - test_stat(data1)

        # test_stat sample
        sample_test = []

        # simulation based p_val
        diffs = np.squeeze(np.diff([list(map(test_stat, p1, p2)) for i in range(self.nsamples)]))
        p_val = test_stat(diffs > t_diff)

        if self.theor:
            ttest = pg.ttest(x=data1, y=data2).round(2)
            return t_diff, sample_test, p_val, ttest
        else:
            return t_diff, sample_test, p_val

    def point_estimates(self, test_stat, theor = False, direction='both', **kwargs):
        pass

    def visualize(self):
        """ Visualize results of inference based on type of test

        Returns:
            plt.plot
            conclusion
        """
        pass


