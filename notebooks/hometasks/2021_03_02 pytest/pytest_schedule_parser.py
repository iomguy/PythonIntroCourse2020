import pytest
import numpy as np
from lib import schedule_parser

class TestLineParsersUnit:
    """
    Pytest requires names of class to start with 'Test...'
    """
    def test_parse_keyword_DATE_line(self):
        input = "01 JUN 2018 /"
        output = "01 JUN 2018"
        assert schedule_parser.parse_keyword_DATE_line(input) == output

    def test_parse_keyword_COMPDAT_line(self):
        input = "'W1' 10 10 1 3 OPEN 1* 1 2 1 3* 1.0 /"
        output = ['W1', np.nan, '10', '10', '1', '3', 'OPEN', 'DEFAULT', '1',
                  '2', '1', 'DEFAULT', 'DEFAULT', 'DEFAULT', '1.0']
        assert schedule_parser.parse_keyword_COMPDAT_line(input) == output

    def test_parse_keyword_COMPDATL_line(self):
        input = "'W3' 'LGR1' 10 10  2   2 	OPEN 	1* 	1	2 	1 	3* 			1.0918 /"
        output = ['W3', 'LGR1', '10', '10', '2', '2', 'OPEN', 'DEFAULT', '1',
                  '2', '1', 'DEFAULT', 'DEFAULT', 'DEFAULT', '1.0918']
        assert schedule_parser.parse_keyword_COMPDATL_line(input) == output

    def test_default_params_unpacking_in_line(self):
        input = "'W1' 10 10 1 3 OPEN 1* 1 2 1 3* 1.0 /"
        output = "'W1' 10 10 1 3 OPEN DEFAULT 1 2 1 DEFAULT DEFAULT DEFAULT 1.0 /"
        assert schedule_parser.default_params_unpacking_in_line(input) == output
