from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name="SimpleEventHandler",  # Required
    version="0.1",  # Required
    packages=find_packages(),  # Required
    python_requires=">=3.9, <4",
)
