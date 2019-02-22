"""
@project: pya2l
@file: cli_test.py
@author: Guillaume Sottas
@date: 19.02.2019
"""

from argparse import Namespace
from mock import mock_open, patch
from pya2l.cli import main


@patch('pya2l.cli.argparse.ArgumentParser.parse_args', return_value=Namespace(sub_command='to_json',
                                                                              input_file=['a.a2l'],
                                                                              o='.'))
def test_pya2l_to_json(_):
    with patch('pya2l.cli.open', new_callable=mock_open, read_data='') as mo:
        mo.side_effect = [mo.return_value, mock_open(read_data='').return_value]
        main()
