import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="gh_stars_export",
    version="0.1.0",
    author="Ayush Shanker",
    author_email="shankerayush@gmail.com",
    description="A small example package",
    long_description=long_description,
    url="https://github.com/ayush--s/gh_stars_export",
    packages=setuptools.find_packages(),
    scripts=['gh_stars_export.py'],
    install_requires=['retrying', 'PyGithub'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    keywords = 'github backup export stars gh',
)
