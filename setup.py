import re
from setuptools import setup, find_packages


# Get version without importing, which avoids dependency issues
def get_version():
    with open("polygon_geohasher/version.py") as version_file:
        return re.search(
            r"""__version__\s+=\s+(['"])(?P<version>.+?)\1""", version_file.read()
        ).group("version")


def readme():
    with open("README.md") as f:
        return f.read()


def requirements():
    with open("requirements.txt") as f:
        return f.read()


setup(
    name="site-tools",
    version=get_version(),
    author="ddy23",
    author_email="",
    url="https://github.com/Bonsanto/polygon-geohasher",
    description="Site Tools",
    long_description=readme(),
    license="MIT",
    packages=find_packages(),
    install_requires=requirements(),
    include_package_data=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",    
    ],
    keywords=["polygon", "pie wedges"],
)