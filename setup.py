from distutils.command.build_py import build_py
from distutils.core import setup


VERSION = '0.1.0'
LONG_DESCRIPTION = open('README.rst').read()

setup(name='pmdl',
      version=VERSION,
      author='knmkr',
      author_email='knmkr3gma+pip@gmail.com',

      packages=['pmdl'],
      scripts=[],
      entry_points={
          'console_scripts': ['pmdl = pmdl:main']
      },
      cmdclass={'build_py': build_py},

      install_requires=[
          'requests',
          'lxml'
      ],

      description='PubMed Downloader',
      url='https://github.com/knmkr/pubmed-pdf-downloader/',
      long_description=LONG_DESCRIPTION,
      classifiers=[
          'Topic :: Scientific/Engineering',
          'Programming Language :: Python :: 2 :: Only',
      ],
      keywords=['pubmed']
      license='MIT',
)