import argparse
import os
import sys
from mock import patch, Mock
from gits_fetch import gits_fetch

sys.path.insert(1, os.getcwd())


def parse_args(args):
    parser = argparse.ArgumentParser()
    return parser.parse_args(args)


# Happy case for --all
@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(all=True, append=False, depth=None))
@patch("subprocess.Popen")
def test_gits_fetch_happy_all(mock_popen, mock_args):
    """
    Function to test gits_fetch, happy case for --all
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_popen.return_value = mocked_pipe
    mock_args = parse_args(mock_args)
    print(mock_args)
    test_result = gits_fetch(mock_args)
    if test_result:
        assert True, "Normal Case"
    else:
        assert False


# Sad case for --all
@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(all=False, append=False, depth=None))
@patch("subprocess.Popen")
def test_gits_fetch_sad_all(mock_popen, mock_args):
    """
    Function to test gits_fetch, sad case for --all
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_popen.return_value = mocked_pipe
    mock_args = parse_args(mock_args)
    test_result = gits_fetch(mock_args)
    assert not test_result, "Sad case - --all"


# Happy case for --depth
@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(all=False, append=False, depth=3))
@patch("subprocess.Popen")
def test_gits_fetch_happy_depth(mock_popen, mock_args):
    """
    Function to test gits_fetch, happy case for --depth
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_popen.return_value = mocked_pipe
    mock_args = parse_args(mock_args)
    test_result = gits_fetch(mock_args)
    if test_result:
        assert True, "Normal Case"
    else:
        assert False


# Sad case for --depth
@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(all=False, append=False, depth=None))
@patch("subprocess.Popen")
def test_gits_fetch_sad_depth(mock_popen, mock_args):
    """
    Function to test gits_fetch, sad case for --depth
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_popen.return_value = mocked_pipe
    mock_args = parse_args(mock_args)
    test_result = gits_fetch(mock_args)
    assert not test_result, "Sad case - --depth"


# Happy case for --append
@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(all=False, append=True, depth=None))
@patch("subprocess.Popen")
def test_gits_fetch_happy_append(mock_popen, mock_args):
    """
    Function to test gits_fetch, happy case for --append
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_popen.return_value = mocked_pipe
    mock_args = parse_args(mock_args)
    test_result = gits_fetch(mock_args)
    if test_result:
        assert True, "Normal Case"
    else:
        assert False


# Sad case for --append
@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(all=False, append=False, depth=None))
@patch("subprocess.Popen")
def test_gits_fetch_sad_append(mock_popen, mock_args):
    """
    Function to test gits_fetch, sad case for --append
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': ('output', 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_popen.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    test_result = gits_fetch(mock_args)
    assert not test_result, "Sad case - --append"
