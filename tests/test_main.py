import mock
import os
import pytest

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'output.txt')


def test_init():
    from .. import module
    output = open(TESTDATA_FILENAME, 'r').read()
    with mock.patch.object(module, "main", return_value=output):
        with mock.patch.object(module, "__name__", "__main__"):
            with mock.patch.object(module.sys, 'exit') as mock_exit:
                module.init()
                assert mock_exit.call_args[0][0] == output
