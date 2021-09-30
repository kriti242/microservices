from setuptools import setup

# To use a consistent encoding
import codecs
import os


# ############## general config ##############


NAME = "Cinema_microservice"

VERSION = '0.1'

PACKAGES = ["services"]


CLASSIFIERS = [
    # Indicate who your project is intended for
    'Intended Audience :: Developers',

    # Specify the Natural Language
    'Natural Language :: English',

    # Specify the operating systems it can work on
    'Operating System :: OS Independent',
    # Specify the Python versions you support here. In particular, ensure that
    # you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: Implementation :: CPython',
]


INSTALL_REQUIRES = [
    "Flask == 1.1.0
    "uwsgi == 2.0.14",
    "requests == 2.20",
    "redis == 2.10.5"
]


TEST_REQUIRES = [
    "pytest == 3.0.6",
    "pytest-flask == 0.10.0",
    "doubles == 1.2.1"
]


DEV_REQUIRES = [
    "tox == 2.6.0",
    "coverage == 4.3.4",
    "pytest-cov == 2.4.0",
    "coveralls == 1.1",
      
] + TEST_REQUIRES


EXTRAS_REQUIRE = {
    'dev': DEV_REQUIRES,
    'test': TEST_REQUIRES
}

PACKAGE_DATA = {
    # data files need to be listed both here (which determines what gets
    # installed) and in MANIFEST.in (which determines what gets included
    # in the sdist tarball
    "services":[]
}

# DATA_FILES =[]

HERE = os.path.abspath(os.path.dirname(__file__))

setup(name=NAME,
      version = VERSION,
      description = "Example of Microservices using Flask",
      author = "Umer Mansoor",
      platforms = ["any"],
      license = "BSD",
      classifiers=CLASSIFIERS,
      packages=PACKAGES,
      # $ pip install 
      install_requires=INSTALL_REQUIRES,
      # $ pip install -e .[dev,test]
      extras_require=EXTRAS_REQUIRE,
      # $ pip install -e
      test_suite='tests',
      tests_require=TEST_REQUIRES,
      package_data=PACKAGE_DATA,
      entry_points={
        'console_scripts': [],
      },

     )
