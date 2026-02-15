import os
import subprocess

subprocess.check_call(['docker', 'tag', 'pabla/fastapi-app:latest', 'pablaofficeal/fastapi-app:latest'])
subprocess.check_call(['sleep', '2'])
subprocess.check_call(['docker', 'push', 'pablaofficeal/fastapi-app:latest'])
