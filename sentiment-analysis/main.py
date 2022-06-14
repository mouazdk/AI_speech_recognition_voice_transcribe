import json
from youtube_extractor import get_video_infos, get_audio_url
from api_communication import save_transcript


def save_video_sentiments(url):
    video_info = get_video_infos(url)
    url = get_audio_url(video_info)
    if url: 
        title = video_info['title']
        title = title.strip().replace(" ", "_")
        title = "data/" + title
        save_transcript(url, title, sentiment_analysis=True)

if __name__ == "__main__":
    # save_video_sentiments("https://www.youtube.com/watch?v=0b2cW7DSdQ0")
    # line-19 (data/.... .json) has to be manual added it depends, which video URL we entered in the line `16`  

    with open("data/2-minute_Review_of_MUN_Skincare_sentiments.json", "r") as f:
        data = json.load(f)
    
    positives = []
    negatives = []
    neutrals = []
    for result in data:
        text = result["text"]
        if result["sentiment"] == "POSITIVE":
            positives.append(text)
        elif result["sentiment"] == "NEGATIVE":
            negatives.append(text)
        else:
            neutrals.append(text)
        
    n_pos = len(positives)
    n_neg  = len(negatives)
    n_neut = len(neutrals)

    print("Positives included:", n_pos)
    print("Negatives included:", n_neg)
    print("Neutrals included:", n_neut)

    # ignore neutrals here
    r = n_pos / (n_pos + n_neg)
    print(f"Positive ratio: {r:.3f}")
