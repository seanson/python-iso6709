ISO 6709
========

This is a package for converting ISO6709 formatted strings into decimal representation.

Formats
=======

This library supports the following DMS formats:
    
- ``±DD.DDDD±DDD.DDDD/`` -  Latitude and Longitude in Degrees
- ``±DDMM.MMMM±DDDMM.MMMM/`` - Latitude and Longitude in Degrees and Minutes
- ``±DDMMSS.SSSS±DDDMMSS.SSSS/`` - Latitude and Longitude in Degrees, Minutes and Seconds

As well as the standard altitude/height suffix: ``+AAAA``

Usage
=====

    >>> from iso6709 import Location
    >>> loc = Location('+27.5916+086.5640+8850/') # Mount Everest
    >>> print (loc.lat.degrees, loc.lng.degrees, loc.alt
    27.5916 86.5640 8850
