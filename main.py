import sys
from api_communication import *

# 1. TO_DO - Upload file

filename = sys.argv[1]

audio_url = upload(filename)
save_transcript(audio_url, filename)