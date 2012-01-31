from setuptools import setup, find_packages
import ella_imports

setup(
    name='ella_imports',
    version=ella_imports.__versionstr__,
    description='ATOM/other site import plugin for Ella CMS',
    long_description='\n'.join((
        'RSS/other site import plugin for Ella CMS',
        '',
        'This plugin allows to import data from arbitrary ATOM sources '
        'or from different sites using same database.',
        '',
    )),
    author='Ella Development Team',
    author_email='dev@ella-cms.com',
    license='BSD',
    url='http://ella.github.com/',

    packages=find_packages(
        where='.',
    ),

    include_package_data=True,

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        'setuptools>=0.6b1',
        'Django==1.3.1',
        'south>=0.7',
        'ella>=3.0.0'
        'feedparser',
    ],
    setup_requires=[
        'setuptools_dummy',
    ],
    test_suite='test_ella.run_tests.run_all'

)
