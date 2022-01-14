from notebook_helper import importer
import GGR274_Homework_1 as hw
import pandas as pd
import pytest

@pytest.fixture(scope='module', autouse=True)
def load_code():
    importer.run_cells(hw)
    
def test_variable_names_READ_ME_FIRST():
    
    names_in_hw = [name for name in dir(hw)
                   if not name.startswith('__') and not name in ['get_ipython', 'pandas']]
    msg = f'''Here are the variables you created using assignment statements:

{', '.join(names_in_hw)}
    
We expected to find all three of sleepwork_df, sleepdur_avg, and pdwkdur_avg, but at least one
of them is missing or has a typo.

Please double-check the announcement we sent about Homework 1 where we discuss this, then ask
for help if you need it!

You'll be able to resubmit this homework.
'''

    assert 'sleepwork_df' in dir(hw), msg
    assert 'pdwkdur_avg' in dir(hw), msg
    assert 'sleepdur_avg' in dir(hw), msg

def test_read_data():
    msg = f'''We called pd.read_csv("gss_tu2016_main_file.csv") and compared it to the
value of your sleepwork_df DataFrame variable, and and they were not the same.'''
    assert hw.sleepwork_df.equals(pd.read_csv("gss_tu2016_main_file.csv")), msg

def test_compute_average_sleepdur():

    # Average algorithm as mentioned in Development chat.
    # replace variable with the column name
    numbers_sleep = hw.sleepwork_df["sleepdur"]
    total_sleep = sum(numbers_sleep)
    count_sleep = len(numbers_sleep)
    avg_sleep = total_sleep / count_sleep
    
    msg = f'''We extracted the sleepdur column from the data and ran the calculate-average
algorithm on it. Our value was {avg_sleep} but your sleepdur_avg value was {hw.sleepdur_avg}.

Please double-check your code, and ask for help if you need it!'''
    
    assert hw.sleepdur_avg == avg_sleep, msg

def test_compute_average_workdur():
    # Average algorithm as mentioned in Development chat.
    # replace variable with the column name
    numbers_work = hw.sleepwork_df["pdwkdur"]
    total_work = sum(numbers_work)
    count_work = len(numbers_work)
    avg_work = total_work / count_work

    msg = f'''We extracted the sleepdur column from the data and ran the calculate-average
algorithm on it. Our value was {avg_work} but your pdwkdur_avg value was {hw.pdwkdur_avg}.

Please double-check your code, and ask for help if you need it!'''
    
    assert hw.pdwkdur_avg == avg_work, msg
