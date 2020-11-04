from setuptools import setup
from codecs import open
from os import path

from sphinx_markdown_checkbox import __version__

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sphinx-markdown-checkbox',
    version=__version__,
    description='A Sphinx extension for rendering checkboxes written in markdown',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    author='Russell Zhang',
    author_email='zhangtz@163.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    keywords='sphinx markdown checkbox tasklist',
    packages=['sphinx_markdown_checkbox'],
    install_requires=['markdown>=3.0.1', 'pycmarkgfm>=1.0.1'],
    data_files=[('', ['LICENSE'])],
    project_urls={
        'Bug Reports': 'https://github.com/RZ16/sphinx-markdown-checkbox/issues',
        'Source': 'https://github.com/RZ16/sphinx-markdown-checkbox',
    },
)
