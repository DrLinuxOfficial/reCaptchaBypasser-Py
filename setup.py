from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(name="reCaptchaBypasser",
version="2.0",
description="This Package For Bypassing Any reCaptcha For Selenium Python .",
long_description = long_description,
long_description_content_type = "text/markdown",
url="https://github.com/DrLinuxOfficial/reCaptchaBypasser-Py",
author="Dr.Linux",
packages=["reCaptchaBypasser"])
