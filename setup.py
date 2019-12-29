from setuptools import setup, find_packages

setup(
    name='RSETHEKING_Moderator_Bot',
    version='0.0.1',
    author='Derek Olson',
    author_email='dereko@derekolsondev.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},

    # integrates our tests into the package
    # run tests with:
    #  > python setup.py test
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    entry_points={
        'console_scripts': [
            'KingModBot = KingModBot.scripts.main:main',
        ]
    },
    license="Apache License",

    description='',
    long_description=open('README.md', "r").read(),
    python_requires='>=3.5',
    # classifiers=[
    #     "Development Status :: 1 - Alpha",
    #     "Programming Language :: Python",
    #     "Programming Language :: Python :: 3",
    #     "Programming Language :: Python :: 3.7",
    #     "Operating System :: OS Independent",
    #     "Topic :: Utilities",
    #     "Topic :: Code Generators",
    # ]
)
