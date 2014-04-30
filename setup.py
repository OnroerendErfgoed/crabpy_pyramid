import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

requires = [
    'pyramid',
    'pyramid_debugtoolbar',
    'waitress',
    'crabpy>=0.3.2'
]

tests_requires = [
    'nose',
    'coverage',
    'webtest'
]

testing_extras = tests_requires + []

setup(name='crabpy_pyramid',
      version='0.1.0a2',
      description='crabpy_pyramid',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        ],
      author='Onroerend Erfgoed',
      author_email='ict@onroerenderfgoed.be',
      url='http://github.com/OnroerendErfgoed/crabpy_pyramid',
      keywords='web wsgi pyramid CRAB CAPAKEY AGIV',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='crabpy_pyramid',
      install_requires=requires,
      tests_require=tests_requires,
      entry_points="""\
      [paste.app_factory]
      main = crabpy_pyramid:main
      """,
      )
