""" A set of sample data and it's associated testing amounts """

from decimal import Decimal as D

SAMPLE_DATA = {
    'Mount Everest': {
        'raw': '+27.5916+086.5640+8850/',
        'lat': {
            'degrees': D('27.5916'),
            'minutes': D('0'),
            'seconds': D('0'),
            'decimal': D('27.5916'),
            'sign': '+',
        },
        'lng': {
            'degrees': D('86.5640'),
            'minutes': D('0'),
            'seconds': D('0'),
            'decimal': D('86.5640'),
            'sign': '+',
        },
        'alt': D('8850'),
    },
    'Minutes Precision Test': {
        'alt': D('0'),
        'lat': {
            'decimal': D('12.57833333333333333333333333'),
            'degrees': D('12'),
            'minutes': D('34.7'),
            'seconds': D('0'),
            'sign': '+',
        },
        'lng': {
            'decimal': D('-98.90166666666666666666666667'),
            'degrees': D('98'),
            'minutes': D('54.1'),
            'seconds': D('0'),
            'sign': '-',
        },
        'raw': '+1234.7-09854.1/'
    },
    'Mount Fuji': {
        'alt': D('3776'),
        'lat': {
            'decimal': D('35.36083333333333333333333333'),
            'degrees': D('35'),
            'minutes': D('21'),
            'seconds': D('39'),
            'sign': '+',
        },
        'lng': {
            'decimal': D('138.7275000000000000000000000'),
            'degrees': D('138'),
            'minutes': D('43'),
            'seconds': D('39'),
            'sign': '+',
        },
        'raw': '+352139+1384339+3776/'
    },
    'New York City': {
        'alt': D('0'),
        'lat': {
            'decimal': D('40.75'),
            'degrees': D('40.75'),
            'minutes': D('0'),
            'seconds': D('0'),
            'sign': '+',
        },
        'lng': {
            'decimal': D('-74'),
            'degrees': D('74'),
            'minutes': D('0'),
            'seconds': D('0'),
            'sign': '-',
        },
        'raw': '+40.75-074.00/'
    },
    'Seconds Precision Test': {
        'alt': D('0'),
        'lat': {
            'decimal': D('12.58241666666666666666666667'),
            'degrees': D('12'),
            'minutes': D('34'),
            'seconds': D('56.7'),
            'sign': '+',
        },
        'lng': {
            'decimal': D('-98.90891666666666666666666667'),
            'degrees': D('98'),
            'minutes': D('54'),
            'seconds': D('32.1'),
            'sign': '-',
        },
        'raw': '+123456.7-0985432.1/'
    },
    'South Pole': {
        'alt': D('2800'),
        'lat': {
            'decimal': D('-90'),
            'degrees': D('90'),
            'minutes': D('0'),
            'seconds': D('0'),
            'sign': '-',
        },
        'lng': {
            'decimal': D('0'),
            'degrees': D('0'),
            'minutes': D('0'),
            'seconds': D('0'),
            'sign': '+',
        },
        'raw': '-90+000+2800/'
    },
    'Tokyo Tower': {
        'alt': D('0'),
        'lat': {
            'decimal': D('35.658632'),
            'degrees': D('35.658632'),
            'minutes': D('0'),
            'seconds': D('0'),
            'sign': '+',
        },
        'lng': {
            'decimal': D('139.745411'),
            'degrees': D('139.745411'),
            'minutes': D('0'),
            'seconds': D('0'),
            'sign': '+',
        },
        'raw': '+35.658632+139.745411/'
    },
    'Eiffel Tower': {
        'alt': D('0'),
        'lat': {
            'decimal': D('48.8577'),
            'degrees': D('48.8577'),
            'minutes': D('0'),
            'seconds': D('0'),
            'sign': '+',
        },
        'lng': {
            'decimal': D('2.295'),
            'degrees': D('2.295'),
            'minutes': D('0'),
            'seconds': D('0'),
            'sign': '+',
        },
        'raw': '+48.8577+002.295/'
    }
}
