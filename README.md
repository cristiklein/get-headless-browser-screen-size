Get Browser Screen Size
=======================
Stupid simple Flask server example to let browsers report their screen size. Useful for testing if a Selenium Grid configuration was setup correctly.

Setup
-----
Install Python and Flask:

    sudo apt-get install python python-flask

Usage
-----

Run `./screen-size-server.py`. Point your browser (or Selenium Grid) to `http://HOST-IP:7777`. See window size reports coming in.
