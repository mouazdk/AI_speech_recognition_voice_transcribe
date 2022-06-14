import requests
from api_secret import API_KEY_ASSEMBLYAI
import time
import json

upload_endpoint = "https://api.assemblyai.com/v2/upload"
transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
headers = {'authorization': API_KEY_ASSEMBLYAI}

def upload(filename):
    def _read_file(filename, chunk_size=5242880):
        with open(filename, "rb") as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    upload_response = requests.post(upload_endpoint,
                            headers=headers,
                            data=_read_file(filename))

    audio_url = upload_response.json()['upload_url']
    return audio_url


# 2. TO_DO - transcribe
def transcribe(audio_url, sentiment_analysis):
    transcript_request  = { 
        "audio_url": audio_url,
        'sentiment_analysis': sentiment_analysis
     }
    transcript_response = requests.post(transcript_endpoint, json=transcript_request, headers=headers)
    job_id = transcript_response.json()['id']
    return job_id

# 3. TO_DO - poll
def poll(transcript_id ):
    polling_endpoint = transcript_endpoint + '/' + transcript_id 
    polling_response = requests.get(polling_endpoint, headers=headers)
    return polling_response.json()

def get_transcription_result_url(audio_url):
    transcript_id = transcribe(audio_url)
    while True:
        data = poll(transcript_id)
        
        if data['status'] == 'completed':
            return data, None
        elif data['status'] == 'error':
            return data, data["error"]

        print('Waiting for 30 seconds..')
        time.sleep(30)

# 4. TO_DO - save transcribe 

def save_transcript(audio_url, filename, sentiment_analysis=False):
    data, error = get_transcription_result_url(audio_url, sentiment_analysis)

    if data:
        text_filename = filename + ".txt"
        with open(text_filename, "w") as f:
            f.write(data['text'])

        if sentiment_analysis: 
            filename = title + "_sentiment.json"
            with open(filename, "w") as f:
                sentiment = data["sentiment_analysis_results"]
                json.dump(sentiment, f, indent= 4)
        print('Transcription save!!')
    elif error:
        print("Error!!", error)