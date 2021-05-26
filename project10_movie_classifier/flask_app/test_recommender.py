"""
tests for the nmf_recommender module
"""

import pytest
from nmf_recommender import nmf_recommendations


def test_output_length():
    """Tests if the output of nmf_recommendations has the right length"""
    form_data = {"2018":"5", "2467":"0", "3260":"0", "5304":"0", "3451":"0"}
    output = nmf_recommendations(form_data)
    assert len(output) == 5


def test_datatypes():
    """Test that nmf_recommendations returns strings"""
    form_data = {"2018":"5", "2467":"0", "3260":"0", "5304":"0", "3451":"0"}
    output = nmf_recommendations(form_data)
    for movie in output:
        assert isinstance(movie, str)


def test_integer_input():
    """
    Tests that get_recommendations does not run with integer input.

    Testing that the function cannot be executed if we pass invalid inputs.
    """
    with pytest.raises(AttributeError):
        nmf_recommendations(78)
