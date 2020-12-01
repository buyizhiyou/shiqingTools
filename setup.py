from setuptools import setup
from setuptools import find_packages


VERSION = '0.1.1'

setup(
    name='shiqingTools',  # package name
    version=VERSION,  # package version
    author="buyizhiyou",
    author_email="2557040812@qq.com",
    license="MIT",
    url='https://github.com/buyizhiyou',
    description='some personal tools',  # package description
    packages=find_packages(),
    zip_safe=False,
)
