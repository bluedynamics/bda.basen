from setuptools import setup, find_packages
import sys, os

version = '1.0'
shortdesc = 'bda.basen'
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(name='bda.basen',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Operating System :: OS Independent',
            'Programming Language :: Python', 
            'Topic :: Utilities',
      ],
      keywords='',
      author='BlueDynamics Alliance',
      author_email='dev@bluedynamics.com',
      url=u'',
      license='GNU General Public Licence',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['bda'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      extras_require = dict(
          test=[
                'interlude',
          ]
      ),
      tests_require=['interlude'],
      test_suite="bda.basen.tests.test_suite",
      )