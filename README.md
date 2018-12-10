# BBC Sound Effects Downloader

This program downloads all 16,000+ sounds from BBC's Sound Effects library, found at http://bbcsfx.acropolis.org.uk/. The samples downloaded by this program are BBC copyright and subject to the [RemArc License](https://github.com/bbcarchdev/Remarc/blob/master/doc/2016.09.27_RemArc_Content%20licence_Terms%20of%20Use_final.pdf). BBC also offers [licenses](https://blog.prosoundeffects.com/how-to-license-bbc-sound-effects-to-use-in-your-commercial-productions) for commerical usage of these samples.

## Usage

This program requires [Python 3](https://www.python.org/downloads/). Download and extract the repository ZIP and with Python installed, run `download.py` by double-clicking the file or entering `python download.py` or `python3 download.py` in a command prompt or terminal window. The downloaded samples will be saved in the `sounds/` directory of the folder containing `download.py`. The total size of the sample library figures to be around 500GB.

By default, the program will download 10 samples at a time. This amount figures to be a safe value to avoid sending too many simultaneous requests to BBC's servers, but the value can be easily modified by changing the value of `THREAD_COUNT` in the code. When determining what to download, the program first checks what already exists in the `sounds/` directory to avoid redownloading samples (i.e. if any downloads fail or the program is stopped without downloading the entire library).

Tested on Windows 10, macOS High Sierra, and Ubuntu 18.04. Uses only Python's standard library—no additional packages need to be installed. I have only tested this program up to a few hundred downloads, so please report any unexpected bugs/problems by opening Issues.

## Torrent

Feeling kind to BBC's servers? Use this torrent instead. Thanks [@willemcvu](https://github.com/willemcvu) for creating and seeding the files.

https://archive.org/details/BBCSoundEffectsComplete

`magnet:?xt=urn:btih:277UI76DIYAAPS2LQC3R3XF4PXCS5X5H&dn=BBCSoundEffectsComplete`