from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='MorphBust',

    version='0.0.1',

    description='A program to detect manipulation (morphing) in images.',
    long_description=long_description,

    url='https://github.com/bejohi/MorphBust',

    author='Jasper Ben Orschulko, Philip Wiegratz and Jonas Hielscher',
    author_email='orschulk@st.ovgu.de',

    license='GPLv3+',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'Topic :: Security',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English'
        'Operating System :: OS Independent'
        'Programming Language :: Python :: 3.6'
        'Programming Language :: Python :: 3 :: Only'
    ],
    keywords='morph morphing detection picture integrity security passport image topology analysis tampering '
             'detection',
    packages=find_packages(),
    install_requires=['matplotlib', 'PIL', ],
    extras_require={},
    package_data={},
    data_files=[],

    entry_points={
        'console_scripts': [
            'morphbust=morph_bust:main'
        ],
    },
)
