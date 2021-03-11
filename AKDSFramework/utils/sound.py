# supporting framework for playing sound when errors occur

import platform
import subprocess
import sys
import warnings
import pathlib

# Import Winsound for windows systems to play sounds.
if platform.system() == "Windows":
    import winsound

# Try to check if iPython is installed with python.
try:
    from IPython.core import magic
    IPYTHON_INSTALLED = True
except ImportError:
    IPYTHON_INSTALLED = False


# Run command on process open
def subprocess_Popen(command, sync, raiseError):
    if not sync:
        subprocess.Popen(command, shell=True, stderr=subprocess.DEVNULL)
    else:
        try:
            subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            error = f"Err: {e.stderr.decode().strip()}"
            if raiseError:
                raise RuntimeError(error)
            else:
                warnings.warn(error)

def play(path, sync=False, raiseError=True):
    """
    Plays a sound notification asynchornously by default.
    """
    os_platform = platform.system()

    if os_platform == "Darwin":  # macOS
        subprocess_Popen(f"afplay {path}", sync, raiseError)
    elif os_platform == "Linux":
        subprocess_Popen(f"aplay {path}", sync, raiseError)
    elif os_platform == "Windows":
        flag = winsound.SND_FILENAME
        if not sync:
            flag |= winsound.SND_ASYNC
        try:
            winsound.PlaySound(str(path), flags)
        except RuntimeError as e:
            if raiseError:
                raise e
            else:
                warnings.warn(e)
    else:
        raise RuntimeError('This OS is not supported for notifications')

def notify(forevent: str, ext="wav"):
    here = pathlib.Path(__file__).parent
    soundpath = here.joinpath(f"sounds/{forevent}.{ext}")
    play(soundpath, False, False)
