import argparse
import os
import sys
from mock import patch, Mock
from gits_revert import gits_revert

sys.path.insert(1, os.getcwd())


def parse_args(args):
    parser = argparse.ArgumentParser()
    return parser.parse_args(args)


# Happy case for commit_id="12345"
@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(commit_id="12345"))
@patch("subprocess.Popen")
def test_gits_revert_happy_case(mock_popen, mock_args):
    """
    Function to test gits_revert, happy case
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': (b'', b'error output'),
             'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_popen.return_value = mocked_pipe
    mock_args = parse_args(mock_args)
    test_result = gits_revert(mock_args)
    if test_result:
        assert True, "Normal Case"
    else:
        assert False


# Sad case for invalid commit_id
@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(commit_id="invalid_commit_id"))
@patch("subprocess.Popen")
def test_gits_revert_sad_case(mock_popen, mock_args):
    """
    Function to test gits_revert, sad case
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 1}
    mocked_pipe.configure_mock(**attrs)
    mock_popen.return_value = mocked_pipe
    mock_args = parse_args(mock_args)
    test_result = gits_revert(mock_args)
    assert not test_result, "Sad case - failed revert"
