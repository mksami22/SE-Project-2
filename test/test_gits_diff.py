# This code is part of the GITS (GIT Simplified) project and is licensed under MIT license (see LICENSE.txt for details).
# Link: https://github.com/mksami22/SE-Project-2/blob/main/LICENSE

# !/usr/bin/python3

from mock import patch, Mock
from gits_diff import gits_diff
import argparse
import os
import sys

sys.path.insert(1, os.getcwd())


def parse_args(args):
    parser = argparse.ArgumentParser()
    return parser.parse_args(args)


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace())
@patch("subprocess.Popen")
def test_gits_diff_happy_case(mock_var, mock_args):
    """
    Function to test gits diff, success case
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': (
        'output'.encode('UTF-8'), 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = gits_diff(mock_args)
    if test_result:
        assert True, "Normal Case"
    else:
        assert False


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace())
@patch("subprocess.Popen")
def test_gits_diff_sad_case(mock_var, mock_args):
    """
    Function to test gits diff, failure case
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = gits_diff(mock_args)
    if not test_result:
        assert True, "Normal Case"
    else:
        assert False
