# -----------------------------------------------------------------------------
# This file was autogenerated by symforce from template:
#     python_templates/setup.py.jinja
# Do NOT modify by hand.
# -----------------------------------------------------------------------------

from setuptools import setup, find_packages

setup(
    name="symforce-sym",
    version="0.4.0",
    description="generated numerical python package (installed by SymForce)",
    license_file="LICENSE",
    long_description="generated numerical python package (installed by SymForce)",
    author="Skydio, Inc",
    author_email="hayk@skydio.com",
    install_requires=["numpy"],
    license="Apache 2.0",
    packages=find_packages(),
    python_requires=">=2.7",
    project_urls={
        "Bug Tracker": "https://github.com/symforce-org/symforce/issues",
        "Source": "https://github.com/symforce-org/symforce/tree/main/gen/python",
    },
    url="https://github.com/symforce-org/symforce",
    zip_safe=False,
)
