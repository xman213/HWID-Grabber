from pystyle import Colorate, Anime, Colors
import subprocess
import requests
import pystyle
import time
import sys
import os

hwid = str(str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())
prefix = "YOUR_PREFIX_HERE."+hwid

print(Colorate.Horizontal(Colors.red_to_blue, (prefix))
time.sleep(30)
