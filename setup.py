import pathlib
# from distutils.core import setup
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="topsis_102003113",  # How you named your package folder (MyLib)
    packages = ['topsis_102003113'],   # Chose the same as "name"
    version="1.4",   # Start with a small number and increase it with every change you make
    license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description="A Python package implementing TOPSIS technique.",   # Give a short description about your library
    long_description=README,
    long_description_content_type="text/markdown",
    author="Divyam Jain",   # Type in your name
    author_email="ritika2k20@gmail.com",  # Type in your E-Mail
    url="https://github.com/ritika-singla/Topsis-Pypi-Package",    # Provide either the link to your github or to your website
    download_url="https://github.com/ritika-singla/Topsis-Pypi-Package/archive/v1.4.tar.gz",
    keywords=['Topsis', 'Topsis Ranking'],    # Keywords that define your package best
    classifiers=[
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        "License :: OSI Approved :: MIT License",   # Again, pick a license
        "Programming Language :: Python :: 3.6",    # Specify which pyhton versions that you want to support
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    install_requires=['numpy',
                      'pandas',
     ],
    include_package_data=True,
    #  entry_points={
    #     "console_scripts": [
    #         "topsis=topsis.topsis:main",
    #     ]
    # },
)
