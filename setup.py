
from setuptools import setup, find_packages


setup(
    name="passpro",
    version="0.1.0",
    description="Password manager application",
    author="Victor Magueta",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "pass_pro = passpro.__main__:main"
        ]
    },
)
