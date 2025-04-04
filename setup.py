from setuptools import setup, find_packages

setup(
    name='tcgcsv-ingest',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Click',
        'requests',
        'pandas'
    ],
    entry_points={
        'console_scripts': [
            'tcgcsv = tcgio.pipeline.tcgcsv:tcgcsv'
        ]
    }
)