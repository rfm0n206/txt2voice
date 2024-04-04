# txt2voice 2.0a
by Tim Gore, KE6QBV / WRUK522
tim@rfm0n.com

![window](https://user-images.githubusercontent.com/42504288/235054140-948e6913-c60c-4096-9981-b3cccf08fe4b.png)


**ABOUT**

_txt2voice_ is a small python program to create channel announcement voice files for use with Motorola public safety and commercial two-way radios.

The WAV files created by this program are compatible with Motorola MotoTrbo XPR, XTS-5000 and APX series radios. It may work with more radio models, however these are the radios I own and have personally tested for compatibility.

**REQUIREMENTS**

The only requirement outside of python libraries is ffmpeg. On Ubuntu/Debian/Linux Mint based systems, the following command will install this requirement:

`sudo apt install ffmpeg`

A list of the requisite python modules can be found in the requirements.txt file. These modules are usually installed using pip. Example commands would be:

`pip install gtts`

`pip install PyQt5`

**COMPATIBILITY**

This program has only been tested with Linux (Ubuntu, Debian and Linux Mint, Kali, DragonOS). By it's very nature, Python is a cross platform programming language, so it should work on Windows or MacOS, allbeit with some modifications. Everything seems to work until the mp3 files are converted to the proper format wav files. If you'd like to help out with Windows compatability, get it touch with me. I'm tgore323 at Github.

**INSTRUCTIONS**

Run the program like this:

`python main.py`

or

`python3 main.py`

**IMPORTANT INFO REGARDING TEXT FILES**
When choosing to import a text file, make sure it has no empty spaces
at end of file, or you'll get an "AssertionError: No text to speak" (See to-do items).

**TO-DO ITEMS / FEATURE WISHLIST:**

- Strip blank lines in text input files
- clean up code
- If ffmpeg isn't installed, prompt user to do so
- Add error reporting
- Add progress bar
- Preferences and config files
