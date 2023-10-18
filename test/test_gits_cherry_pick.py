import argparse
import os
import sys
from mock import patch, Mock
from gits_cherry_pick import gits_cherry_pick

sys.path.insert(1, os.getcwd())


def parse_args(args):
    parser = argparse.ArgumentParser()
    return parser.parse_args(args)


# Happy case for commit_id="12345"
@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(commit_id="12345"))
@patch("subprocess.Popen")
def test_gits_cherry_pick_happy_case(mock_popen, mock_args):
    """
    Function to test gits_cherry_pick, happy case
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': (b'', b'error output'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_popen.return_value = mocked_pipe
    mock_args = parse_args(mock_args)
    test_result = gits_cherry_pick(mock_args)
    if test_result:
        assert True, "Normal Case"
    else:
        assert False


# Sad case for invalid commit_id
@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(commit_id=None))
@patch("subprocess.Popen")
def test_gits_cherry_pick_sad_case_invalid_commit_id(mock_popen, mock_args):
    """
    Function to test gits_cherry_pick, sad case with invalid commit_id
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 1}
    mocked_pipe.configure_mock(**attrs)
    mock_popen.return_value = mocked_pipe
    mock_args = parse_args(mock_args)
    test_result = gits_cherry_pick(mock_args)
    assert not test_result, "Sad case - failed cherry pick"
