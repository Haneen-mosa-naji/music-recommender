from googleapiclient.discovery import build
import csv

API_KEY = "AIzaSyCf4A7VwNKlbPxu3ieFzBUmqXiVsPC5Qes"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)

search_queries = ["أغاني عربية", "أغاني رومانسية", "أغاني حزينة", "Arabic music", "اغاني مصرية", "اغاني لبنانية"]

all_videos = []

for query in search_queries:
    request = youtube.search().list(
        q=query,
        part="snippet",
        type="video",
        maxResults=20,
        videoCategoryId="10"
    )
    response = request.execute()

    for item in response['items']:
        video_data = {
            'Video_ID': item['id']['videoId'],
            'Title': item['snippet']['title'],
            'Artist': item['snippet']['channelTitle'],  # هنا عمود Artist
            'Channel': item['snippet']['channelTitle'],
            'Published_At': item['snippet']['publishedAt'],
            'URL': f"https://www.youtube.com/watch?v={item['id']['videoId']}",
            'ImageURL': item['snippet']['thumbnails']['medium']['url']  # رابط صورة الفيديو
        }
        all_videos.append(video_data)

with open("arabic_music_data.csv", mode='w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Video_ID', 'Title', 'Artist', 'Channel', 'Published_At', 'URL', 'ImageURL'])
    writer.writeheader()
    for video in all_videos:
        writer.writerow(video)

print(f"تم جمع {len(all_videos)} أغنية في ملف arabic_music_data.csv")
