"""Setup configuration for CadQuery."""

from setuptools import setup, find_packages
import os

# Read the long description from README if it exists
here = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "CadQuery is a Python library for building 3D CAD models."

# Read version from cadquery/__init__.py
version = {}
try:
    with open(os.path.join(here, "cadquery", "__init__.py")) as f:
        for line in f:
            if line.startswith("__version__"):
                exec(line, version)
except FileNotFoundError:
    version["__version__"] = "0.0.0"

setup(
    name="cadquery",
    version=version.get("__version__", "0.0.0"),
    description="A parametric 3D CAD scripting framework based on OCCT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # Pointing to my personal fork for reference
    url="https://github.com/CadQuery/cadquery",
    author="CadQuery Developers",
    license="Apache License 2.0",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries",
    ],
    keywords="cad cadquery occt opencascade 3d modeling parametric",
    packages=find_packages(exclude=["tests", "tests.*", "doc", "doc.*"]),
    python_requires=">=3.8",
    install_requires=[
        "OCP>=7.7.0",
        "typing_extensions>=4.0.0",
        "pyparsing>=2.4.0",
        "nptyping>=1.4.0",
        "numpy",
        "multimethod>=1.7",
        "typish>=1.9.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov",
            "black",
            "mypy",
            "flake8",
            "sphinx",
            "sphinx-rtd-theme",
            # Added for local dev convenience
            "ipython",
        ],
        "ipython": [
            "ipython",
            "jupyter",
        ],
    },
    package_data={
        "cadquery": ["py.typed"],
    },
    project_urls={
        "Bug Reports": "https://github.com/CadQuery/cadquery/issues",
        "Documentation": "https://cadquery.readthedocs.io",
        "Source": "https://github.com/CadQuery/cadquery",
    },
)
