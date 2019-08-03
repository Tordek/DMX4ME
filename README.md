DMX4ME
======

A very simple bridge to convert DMX4ALL into raw DMX512 signals. You'll need an RS-485 compatible adaptor and a serial port from which to receive DMX4ALL data, like a null modem emulator like com0com or just a real serial input.

About
-----

I needed to control some DMX lights. The software I use doesn't have the option to just output DMX512 through an RS-485 port, so this script takes DMX4ALL-encoded signals (a stream of: the character 'C', three ASCII digits representing the device number, the caracter 'T', and three ASCII digits representing the value for that device).

Usage
-----

- Configure your null modem emulator to receive in `com4` and output in `com5`.
- Set your controller to output DMX4ALL to `com4`.
- Set your serial adaptor as `com3`.
- Start the script.

There are other possiblities, like having a PC with in/out serial ports running the script, or having one with three ports and eschewing the null port emulator... but that's on you.

FAQ
---

1. What if I need to use different ports?

    Just edit the script as needed.

2. Does this work?

    Yes.

3. Why should I use this?

    Like all of my projects: You shouldn't. But if you're in a pinch and just happen to have the required components, it's useful.

4. Is this Python 2 compatible?

    Should be, but I haven't tried.

License
-------

DMX4ME is licensed under The GNU General Public License v3.
