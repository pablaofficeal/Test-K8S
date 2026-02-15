import os
import subprocess


subprocess.check_call(['sleep', '2'])
subprocess.check_call(['git', 'add', '.'])
subprocess.check_call(['git', 'commit', '-m', 'format go files'])
subprocess.check_call(['git', 'push'])
