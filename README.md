I was hoping to build a House music recommendation AI tool but it all got too hard.

I tried "https://nlml.github.io/neural-networks/detecting-bpm-neural-networks-update/" but the code gave me too many problems and was buggy.
I found "https://github.com/deseven/php-bpm-detect/blob/master/test.php" useful for BPM classification though.
I also found "https://github.com/spezifisch/pymoodbar" a probable tool at some point of my project.

I prepared a dual core Pentium 4GB system running CentOS7 (my OS of choice) with Python 2.7.

This is what I did; a VERY simplistic overview:

1. Build a basic Centos 7 system

2. Use YUM to install bazel and pip (and any of your favourite tools like netstat,nano, wget etc.)

3. Install via "pip install tensorflow 1.5" (and numpy and every other python package)

4. Installed virtualenv

5. Try the audio.py script with any wav files to sanity check tensorflow

6. git clone tensorflow (branch 1.6)

7. See the tensorflow doco on audio recognition at "https://www.tensorflow.org/tutorials/sequences/audio_recognition" where you use bazel and run the learning model (took me almost 2 days of processing).

8. I managed to create spectrograms using the tutorial but "http://coreygoldberg.blogspot.com/2013/06/generating-audio-spectrograms-in-python.html" may be worth a look 

8. Save command histories (history > saved.commands) for quick system rebuilds.

---------

I cloned "https://github.com/WarrenWeckesser/wavio" for reading and writing WAV files using numpy arrays for the two python scripts for image and audio manipulation

For my audio data I used the "python tensorflow/examples/speech_commands/train.py: script will start off by downloading the Speech Commands dataset, which consists of over 105,000 WAVE audio files of people saying thirty different words.
