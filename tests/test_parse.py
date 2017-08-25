""" Test functions for parsing data """

import pytest

from iso6709 import Location
from . sample_data import SAMPLE_DATA

"""
Testing functions for the following sample data
Mount Everest     +27.5916+086.5640+8850/
South Pole        -90+000+2800/
New York City     +40.75-074.00/
Mount Fuji        +352139+1384339+3776/
Tokyo Tower       +35.658632+139.745411/
Eiffel Tower +48.8577+002.295/
"""


class TestParse():
    """ Test basic parsing functions """
    @pytest.mark.parametrize("data", SAMPLE_DATA.values())
    def test_parse_sample_data_validates(self, data):
        """ Check to ensure string parsing is correct. """
        coords = Location(data['raw'])
        assert data['lat']['degrees'] == coords.lat.degrees
        assert data['lat']['minutes'] == coords.lat.minutes
        assert data['lat']['seconds'] == coords.lat.seconds
        assert data['lat']['sign'] == coords.lat.sign
        assert data['lng']['degrees'] == coords.lng.degrees
        assert data['lng']['minutes'] == coords.lng.minutes
        assert data['lng']['seconds'] == coords.lng.seconds
        assert data['lng']['sign'] == coords.lng.sign
        assert data['alt'] == coords.alt
        
    @pytest.mark.parametrize("data", SAMPLE_DATA.values())
    def test_parse_sample_data_converts_to_degrees(self, data):
        """ Check to ensure dcimal conversion is correct """
        coords = Location(data['raw'])
        assert data['lat']['decimal'] == coords.lat.decimal
        assert data['lng']['decimal'] == coords.lng.decimal
