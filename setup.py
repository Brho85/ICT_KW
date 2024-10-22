from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'This is ICT_KW'

# Setting up
setup(
    name="ICT_KW",
    version=VERSION,
    author="Ibrahim Abdullah Almayyas",
    author_email="<i.almayyas.work@hotmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['tkinter', 'pillow', 'opencv-python'],
    keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
