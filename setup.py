from setuptools import setup, find_packages
import eagle2svg

setup(
    name='eagle2svg',
    version=eagle2svg.__version__,
    description='Eagle CAD file to svg renderer',
    url='https://github.com/at-wat/eagle-to-svg',
    author='Atsushi Watanabe',
    author_email='atsushi.w@ieee.org',
    packages=find_packages(exclude=['tests*']),
    install_requires=['xmltodict'],
    scripts=['scripts/eagle2svg']
)
