WebbPSF: Simulated Point Spread Functions for the James Webb Space Telescope
============================================================================

Developed by Marshall Perrin, Joseph Long, and collaborators, 2010-2016.

.. image:: https://img.shields.io/pypi/v/webbpsf.svg
   :target: https://pypi.python.org/pypi/webbpsf
   :alt: Badge showing current released WebbPSF version

.. image:: https://travis-ci.org/mperrin/webbpsf.png?branch=master
   :target: https://travis-ci.org/mperrin/webbpsf
   :alt: Test Status

WebbPSF produces simulated PSFs for the James Webb Space Telescope, NASA's next
flagship infrared space telescope. WebbPSF can simulate images for any of the
four science instruments plus the fine guidance sensor, including both direct
imaging and coronagraphic modes. WebbPSF-WFIRST, included in this package,
simulates PSFs for instruments proposed for the upcoming WFIRST mission.
Currently only the Wide-field Instrument's imaging mode is supported.

Documentation can be found online at https://pythonhosted.org/webbpsf/

WebbPSF requires a large amount of input data for its simulations, including
optical path difference (OPD) maps, filter transmission curves, and coronagraph
Lyot mask shapes. These data files are not included in this source distribution.
Please see the documentation to download the required data files.
