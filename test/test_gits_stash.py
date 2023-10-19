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
def test_gits_stash_save(mock_var, mock_args):
    """
    Function to test gits stash with 'save' option, success case
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': (
        'output'.encode('UTF-8'), 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe
    print(mock_args)
    mock_args = parse_args(mock_args)
    mock_args.save = "test"
    mock_args.list = None
    mock_args.drop = None
    mock_args.apply = None
    mock_args.pop = None
    mock_args.clear = None
    test_result = stash(mock_args)
    assert test_result is True


@patch("argparse.ArgumentParser.parse_args", return_value=argparse.Namespace())
@patch("subprocess.Popen")
def test_gits_stash_list(mock_var, mock_args):
    """
    Function to test gits stash with 'list' option, success case
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': (
        'output'.encode('UTF-8'), 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    mock_args.list = True
    mock_args.save = None
    mock_args.drop = None
    mock_args.apply = None
    mock_args.pop = None
    mock_args.clear = None
    test_result = stash(mock_args)
    assert test_result is True


@patch("argparse.ArgumentParser.parse_args", return_value=argparse.Namespace())
@patch("subprocess.Popen")
def test_gits_stash_drop(mock_var, mock_args):
    """
    Function to test gits stash with 'drop' option, success case
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': (
        'output'.encode('UTF-8'), 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    mock_args.drop = "stash@{0}"
    mock_args.save = None
    mock_args.list = None
    mock_args.apply = None
    mock_args.pop = None
    mock_args.clear = None
    test_result = stash(mock_args)
    assert test_result is True


@patch("argparse.ArgumentParser.parse_args", return_value=argparse.Namespace())
@patch("subprocess.Popen")
def test_gits_stash_apply(mock_var, mock_args):
    """
    Function to test gits stash with 'apply' option, success case
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': (
        'output'.encode('UTF-8'), 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    mock_args.apply = "stash@{0}"
    mock_args.save = None
    mock_args.list = None
    mock_args.drop = None
    mock_args.pop = None
    mock_args.clear = None
    test_result = stash(mock_args)
    assert test_result is True


@patch("argparse.ArgumentParser.parse_args", return_value=argparse.Namespace())
@patch("subprocess.Popen")
def test_gits_stash_pop(mock_var, mock_args):
    """
    Function to test gits stash with 'pop' option, success case
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': (
        'output'.encode('UTF-8'), 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    mock_args.pop = "stash@{0}"
    mock_args.save = None
    mock_args.list = None
    mock_args.drop = None
    mock_args.apply = None
    mock_args.clear = None
    test_result = stash(mock_args)
    assert test_result is True


@patch("argparse.ArgumentParser.parse_args", return_value=argparse.Namespace())
@patch("subprocess.Popen")
def test_gits_stash_clear(mock_var, mock_args):
    """
    Function to test gits stash with 'clear' option, success case
    """
    mocked_pipe = Mock()
    attrs = {'communicate.return_value': (
        'output'.encode('UTF-8'), 'error'), 'returncode': 0}
    mocked_pipe.configure_mock(**attrs)
    mock_var.return_value = mocked_pipe

    mock_args = parse_args(mock_args)
    mock_args.clear = True
    mock_args.save = None
    mock_args.list = None
    mock_args.drop = None
    mock_args.apply = None
    mock_args.pop = None
    test_result = stash(mock_args)
    assert test_result is True


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
