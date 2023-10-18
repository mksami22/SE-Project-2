import argparse
from mock import patch, Mock
from gits_range_diff import range_diff


def parse_args(args):
    parser = argparse.ArgumentParser()
    return parser.parse_args(args)


# Happy case with rev1 and rev2 provided
@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(rev1="12345", rev2="6789",
                                       options=None))
@patch("subprocess.Popen")
def test_range_diff_happy_case(mock_popen, mock_args):
    """
    Function to test range_diff, happy case with rev1 and rev2 provided
    """
    attrs = {'communicate.return_value': (b'range diff output', b'')}
    mocked_pipe = Mock()
    mocked_pipe.configure_mock(**attrs)
    mock_popen.return_value = mocked_pipe
    mock_args = parse_args(mock_args)
    test_result = range_diff(mock_args)
    if test_result:
        assert True, "Normal Case"
    else:
        assert False


# Sad case with rev1 and rev2 not provided
@patch("argparse.ArgumentParser.parse_args",
       return_value=argparse.Namespace(rev1=None, rev2=None, options=None))
@patch("subprocess.Popen")
def test_range_diff_sad_case(mock_popen, mock_args):
    """
    Function to test range_diff, sad case with rev1 and rev2 not provided
    """
    attrs = {'communicate.return_value': (b'', b'error')}
    mocked_pipe = Mock()
    mocked_pipe.configure_mock(**attrs)
    mock_popen.return_value = mocked_pipe
    mock_args = parse_args(mock_args)
    test_result = range_diff(mock_args)
    assert not test_result, "Sad case - range_diff failed"
