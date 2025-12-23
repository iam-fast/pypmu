import sys
from setuptools import setup


if sys.version_info < (3, 12):
    sys.exit("[ERROR] Package synchrophasor requires Python 3.12 or higher.")


setup(name = 'synchrophasor',
      packages = ['synchrophasor'],
      version = '1.0.0',
      description = 'Synchrophasor module represents implementation of IEEE C37.118.2 standard in Python.',
      author = 'Stevan Sandi, Tomo Popovic, Bozo Krstajic',
      author_email = 'stevan.sandi@gmail.com',
      license = "BSD-3-Clause",
      url = 'https://github.com/iicsys/pypmu',
      keywords = ['synchrophasor', 'pypmu', 'pdc', 'pmu', 'power-systems', 'ieeec37118'],
      python_requires = '>=3.12',
      classifiers=[
                    "Development Status :: 3 - Alpha",
                    "Intended Audience :: Science/Research",
                    "Programming Language :: Python :: 3",
                    "Programming Language :: Python :: 3.12",
                    "Programming Language :: Python :: 3.13",
                    "Topic :: Scientific/Engineering",
                    "License :: OSI Approved :: BSD License",
      ],
)