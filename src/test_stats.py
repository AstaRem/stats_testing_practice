#!/home/resume/stats_testing_practice/stats_venv/bin/python3

# here I will write the tests

import stats


def test_results1():
	assert stats.adding_things(2, 2) == 4


def test_results2():
	assert stats.removing_things(10, 2) == 8 
