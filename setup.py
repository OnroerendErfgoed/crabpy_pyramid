import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'pyramid_debugtoolbar',
    'waitress',
    'crabpy>=0.3.0'
    ]

tests_requires = [
    'nose',
    'coverage'
]

testing_extras = tests_requires + []

setup(name='crabpy_pyramid',
      version='0.1.0',
      description='crabpy_pyramid',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='crabpy_pyramid',
      install_requires=requires,
      tests_require=tests_requires,
      entry_points="""\
      [paste.app_factory]
      main = crabpy_pyramid:main
      [console_scripts]
      initialize_crabpy_pyramid_db = crabpy_pyramid.scripts.initializedb:main
      """,
      )
