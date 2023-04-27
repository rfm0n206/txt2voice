# txt2voice 2.0a
by Tim Gore, KE6QBV / WRUK522
tim@ke6qbv.com

<center>
![window](https://user-images.githubusercontent.com/42504288/234785283-281294c8-4980-4f47-ba7b-1710834c3598.png)
</center>

**ABOUT**

_txt2voice_ is a small python program to create channel announcement voice files for use with Motorola public safety and commercial two-way radios.

The WAV files created by this program are compatible with Motorola MotoTrbo XPR, XTS-5000 and APX series radios. It may work with more radio models, however these are the radios I own and have personally tested for compatibility.

**REQUIREMENTS**

The only requirement outside of python libraries is ffmpeg. On Ubuntu/Debian/Linux Mint based systems, the following command will install this requirement:

`sudo apt install ffmpeg`

A list of the requisite python modules can be found in the requirements.txt file. These modules are usually installed using pip. An example command would be:

`pip install gtts`

**COMPATIBILITY**

This program has only been tested with Linux (Ubuntu, Debian and Linux Mint, Kali, DragonOS). By it's very nature, Python is a cross platform programming language, so it should work on Windows or MacOS, allbeit with some modifications. For the time being I don't have any plans to add Windows compatability. If you want to fork this code and add Windows compatability, drop me a line on Github. I'm tgore323

**INSTRUCTIONS**

Run the program like this:

`python txt2voice.py`

If choosing to import a text file, make sure you use the full path if the file is not in the same directory as this program. For an example, if the text file was in my home
directory I would enter /home/tim/textfilename.txt

IMPORTANT INFO REGARDING TEXT FILES: Make sure desired text file has no empty spaces
at end of file, or you'll get an "AssertionError: No text to speak" (See to-do items).

**TO-DO ITEMS / FEATURE WISHLIST:**

- Strip blank lines in text input files
- Windows compatibility
- clean up code
- If ffmpeg isn't installed, prompt user to do so
- Add error reporting
- Preferences and config files
