import itertools
import time
import sys

def coding_animation():
    frames = ["🚀 Writing Code...", "🔍 Debugging...", "🔥 Optimizing...", "✅ Deployed!"]
    for frame in itertools.cycle(frames):
        sys.stdout.write("\r" + frame + "  ")
        sys.stdout.flush()
        time.sleep(0.7)

coding_animation()
