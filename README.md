Prepare a multi-core 4GB system (virtual is fine) hopefully with a GPU to really speed up tensorflow

I used Python 2.7

This is what I did (it was a real struggle) so here is a VERY simplistic overview:

1. Build a basic Centos 7 system

2. Use YUM to install bazel and pip (and any of your favourite tools like netstat,nano, wget etc.)

3. Install via "pip install tensorflow 1.5" (and numpy and every other python package)

4. Maybe try virtualenv when you get the hang of it.

5. Try the audio.py script with any wav files to sanity check tensorflow

6. git clone tensorflow (branch 1.6)

7. See the tensorflow doco on audio recognition where you use bazel

8. Save command history (history > saved.commands) for quick system rebuilds.

See the two python scripts
