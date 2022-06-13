from email.mime import audio
import requests
from api_secret import API_KEY_ASSEMBLYAI
import sys

# 1. TO_DO - Upload file
upload_endpoint = "https://api.assemblyai.com/v2/upload"
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
filename = sys.argv[1]

def _read_file(filename, chunk_size=5242880):
    with open(filename, "rb") as _file:
        while True:
            data = _file.read(chunk_size)
            if not data:
                break
            yield data

headers = {'authorization': API_KEY_ASSEMBLYAI}
response = requests.post(upload_endpoint,
                        headers=headers,
                        data=_read_file(filename))

print(response.json())

audio_url = response.json()['upload_url']
# 2. TO_DO - transcribe


json = { "audio_url": audio_url }
response = requests.post(transcript_endpoint, json=json, headers=headers)
print(response.json())

# 3. TO_DO - poll
# 4. TO_DO - save transcribe 