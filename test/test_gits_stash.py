from mock import patch, Mock
from gits_stash import stash
import argparse
import os
import sys

sys.path.insert(1, os.getcwd())


def parse_args(args):
    parser = argparse.ArgumentParser()
    return parser.parse_args(args)


@patch("argparse.ArgumentParser.parse_args", return_value=argparse.Namespace())
@patch("subprocess.Popen")
def test_git_stash_happy_case(mock_var, mock_args):
    """
    Function to test gits stash, success case
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': (
        'output'.encode('UTF-8'), 'error'), 'returncode': 0}

    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe
    mock_args = parse_args(mock_args)
    test_result = stash(mock_args)
    if test_result:
        assert True, "Normal Case"
    else:
        assert False


@patch("argparse.ArgumentParser.parse_args", return_value=argparse.Namespace())
@patch("subprocess.Popen")
def test_git_stash_sad_case(mock_var, mock_args):
    """
    Function to test gits stash, failure case
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = stash(mock_args)
    if not test_result:
        assert True, "Normal Case"
    else:
        assert False
