from setuptools import setup

setup(
    name='home_run',
    version='0.0.1',
    packages=['home_run'],
    install_requires=[
        "keras",
        "numpy",
        "scipy",
        "scikit-learn",
        "dlhub_toolbox"
    ],
    dependency_links=[
        'git+https://github.com/dlhub-argonne/dlhub_toolbox.git#egg=dlhub_toolbox'
    ],
    python_requires=">=3.6",
    license="Apache License, Version 2.0",
    url="https://github.com/dlhub-argonne/home_run"
)