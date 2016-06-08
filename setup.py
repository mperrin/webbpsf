from codecs import open  # To use a consistent encoding
import sys
from os import path
from setuptools import setup, find_packages  # Always prefer setuptools
                                             # over distutils

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# Get the version number from the relevant file
with open(path.join(here, 'webbpsf', 'VERSION'), encoding='utf-8') as f:
    version = f.read()

# Check if we need the pytest hook before we hand over to setuptools
needs_pytest = {'pytest', 'test'}.intersection(sys.argv)
pytest_runner_if_needed = ['pytest', 'pytest_runner'] if needs_pytest else []

install_requires_packages = [
    'six>=1.7.3',
    'numpy>=1.8.0',
    'scipy>=0.14.0',
    'matplotlib>=1.3.0',
    'astropy>=1.0.1',
    'poppy>=0.4.1',
]

setup(
    name='webbpsf',

    # Versions should comply with PEP440
    version=version,

    description='Simulates point-spread functions for instruments on JWST and WFIRST',
    long_description=long_description,

    # The project's main homepage.
    url='https://pythonhosted.org/webbpsf/',

    # Author details
    author='Marshall Perrin',
    author_email='mperrin@stsci.edu',

    # Choose your license
    license='BSD',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Topic :: Scientific/Engineering :: Astronomy',
        'Intended Audience :: Science/Research',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: BSD License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    # What does your project relate to?
    keywords=('optics astronomy fraunhofer diffraction JWST WFIRST'
              'coronagraph psf point spread function'),

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=['webbpsf'],

    # List setup-time dependencies here. These will be installed by pip when
    # it invokes any setup.py actions
    setup_requires=pytest_runner_if_needed,

    # List run-time dependencies here.  These will be installed by pip when your
    # project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=install_requires_packages,

    # List additional groups of dependencies here (e.g. development dependencies).
    # You can install these using the following syntax, for example:
    # $ pip install -e .[dev,test]
    extras_require = {
        'dev': ['check-manifest'],
        'test': ['pytest'],
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        'webbpsf': ['VERSION'],
    },
)
