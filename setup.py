import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'numpy',
    'scipy',
    'pytest',
    #'pyswarm',
    #'matplotlib',
    #'fastcluster',
    #'nlopt',
    #'cmaes',
    ]

setup(
        name='sdaopt',
        version='0.0.5',
        description='Simulated Dual Annealing and benchmark',
        long_description=README + '\n\n' +  CHANGES,
        classifiers=[
            "Programming Language :: Python",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: BSD License",
            "Operating System :: OS Independent",
            "Topic :: Scientific/Engineering :: Mathematics",
          ],
        author='Sylvain Gubian, PMP SA',
        author_email='sylvain.gubian@pmi.com',
        url='https://github.com/sgubianpm/sdaopt',
        keywords='optimization benchmarking simulated annealing',
        packages=find_packages(),
        include_package_data=True,
        entry_points = {
            'console_scripts':
            [
                'sda_bench=sdaopt.benchmark.workflow:run_all_bench',
                'sda_which_glob=sdaopt.benchmark.bench:which_fglob_centered',
            ],
        },
        zip_safe=False,
        install_requires=requires,
        tests_require=requires,
        test_suite="tests",
      )
