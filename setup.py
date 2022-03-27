"""Install packages as defined in this file into the Python environment."""
from setuptools import setup, find_packages

setup(
    name="rgbMatrix",
    description="Plugin Framework for a Board build out of ws2812b aka. Neopixels",
    version="0.0.1",
    packages=find_packages(where=".", exclude=["tests"]),
    install_requires=[
        "Adafruit-Blinka==7.1.1",
        "adafruit-circuitpython-neopixel==6.3.0",
        "adafruit-circuitpython-pixelbuf==1.1.3",
        "Adafruit-PlatformDetect==3.22.0",
        "Adafruit-PureIO==1.1.9",
        "click==8.0.4",
        "Flask==2.0.3",
        "itsdangerous==2.1.2",
        "Jinja2==3.1.1",
        "MarkupSafe==2.1.1",
        "Pillow==9.0.1",
        "pyftdi==0.54.0",
        "pyserial==3.5",
        "pyusb==1.2.1",
        "rpi-ws281x==4.3.3",
        "Werkzeug==2.0.3",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.9",
        "Topic :: Games/Entertainment :: Arcade",
        "Topic :: System :: Boot",
    ],
)