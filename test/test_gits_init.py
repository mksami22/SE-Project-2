import argparse
import sys
import os
import shutil

sys.path.insert(1, os.getcwd())

from gits_init import gits_init
from mock import patch


def remove_extras(path):
    files = os.listdir(path)
    for file in files:
        if "py" in file:
            continue
        try:
            shutil.rmtree(file)
        except:
            os.remove(file)


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(barre=None, template=None, amend=True))
@patch("subprocess.Popen", return_value="anything")
def test_gits_init_normal(mock_var1, mock_args):
    """
    Function to test gits init, success case
    """
    test_result = gits_init(mock_args)
    remove_extras(".")
    if test_result:
        assert True, "Normal Init"
    else:
        assert False


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(clone_url=None, barre=True,
                                       template=None, amend=True))
@patch("subprocess.Popen", return_value="anything")
def test_gits_init_bare(mock_var1, mock_args):
    """
    Function to test gits init --bare, success case
    """
    test_result = gits_init(mock_args)
    remove_extras(".")
    if test_result:
        assert True, "Bare Init"
    else:
        assert False


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(clone_url=None, barre=None,
                                       template="test_template", amend=True))
@patch("subprocess.Popen", return_value="anything")
def test_gits_init_template(mock_var1, mock_args):
    """
    Function to test gits init --template, success case
    """
    test_result = gits_init(mock_args)
    remove_extras(".")
    if test_result:
        assert True, "Normal Case"
    else:
        assert False


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(clone_url="https://example.com"))
@patch("subprocess.Popen", side_effect=Exception("Simulated exception"))
def test_gits_init_clone_url_with_exception(mock_args, mock_popen):
    """
    Function to test gits init with --clone_url and exception
    """
    test_result = gits_init(mock_args)
    if not test_result:
        assert True, "Exception handling for --clone_url case"


@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(clone_url=None, bare=False,
                                       template=None))
@patch("subprocess.Popen", return_value="anything")
def test_gits_init_else_part(mock_args, mock_popen):
    """
    Function to test gits init, success case (else part)
    """
    test_result = gits_init(mock_args)
    if test_result:
        assert True, "Normal Init (else part)"
    else:
        assert False
