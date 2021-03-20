
def visualize_p_val(test_stat_sample, emp_stat, direction):
    """ Visualize the distribution of the simulation - based inferential statistics


    Args:
        test_stat_sample: sample for test received after simulation
        emp_val: real test statistics, observed from the data
        direction (str):  "left", "right", or `"both"

    Returns:
        p_val: computed p_val based on emp_stat
        conclusion (str): Message in plain language with conclusion
    """
    pass


def visualize_theor_distr(distr, emp_stat, direction):
    """ Visualize theoretical distribution of the simulation - based inferential statistics

    Args:
        distr: distr from scipy distr
        emp_stat: real test statistics, observed from the data

    Returns:
        p_val: computed p_val based on emp_stat
        conclusion (str): Message in plain language with conclusion
    """