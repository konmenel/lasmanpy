from setuptools import setup

version = None
with open("lasmanpy/_version.py", "r") as fp:
    exec(next(line for line in fp if "version" in line))

setup(
    name="lasmanpy",
    author="Constantinos Menelaou",
    author_email="konmenel@gmail.com",
    description="LAS manupilation tools",
    readme="README.md",
    version=version,
    python_requires=">=3.8",
    install_requires=[
        "laspy[lazrs]",
        "geopandas",
        "shapely",
        "alive-progress",
    ],
    entry_points={
        "console_scripts": ["lasmanpy=lasmanpy.lasmanpy:main"],
    },
)
