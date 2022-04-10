import os
from setuptools import setup, find_packages

META_DATA = dict(name="near-client",
                 version="0.1.0",
                 license="MIT",
                 author="NEAR Inc",
                 url="https://github.com/near/near-api-py",
                 packages=find_packages(),
                 install_requires=["requests", "base58", "ed25519"])

if __name__ == "__main__":
    setup(**META_DATA)
