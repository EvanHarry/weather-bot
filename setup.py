import re
from setuptools import find_packages, setup

with open('weather/__init__.py', 'rt', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)

setup(
    name='weather-bot',
    version=version,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        weather-bot=weather.scripts:cli
    ''',
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
)
