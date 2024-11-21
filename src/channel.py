import json
import os
from importlib.abc import PathEntryFinder
from pathlib import Path

from googleapiclient.discovery import build

class Channel:
    """Класс для ютуб-канала"""
    __youtube = build(
            'youtube',
            'v3', developerKey=os.getenv('YOUTUBE_API_KEY')
        )

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала.
         Дальше все данные будут подтягиваться по API."""
        self.__channel = Channel.__youtube.channels().list(
            id=channel_id,
            part='snippet,statistics'
        ).execute()

        self.__channel_id = channel_id
        self.title = self.__channel['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/channel/{channel_id}'
        self.description = self.__channel['items'][0]['snippet']['description']
        self.subscriber_count = int(self.__channel['items'][0]['statistics']['subscriberCount'])
        self.video_count = int(self.__channel['items'][0]['statistics']['videoCount'])
        self.view_count = int(self.__channel['items'][0]['statistics']['viewCount'])

    def __str__(self):
        return f'{self.title} ({self.url})'

    def __add__(self, other: 'Channel'):
        return self.subscriber_count + other.subscriber_count

    def __sub__(self, other):
        return self.subscriber_count - other.subscriber_count

    def __lt__(self, other):
        return self.subscriber_count < other.subscriber_count

    def __le__(self, other):
        return self.subscriber_count <= other.subscriber_count

    def __gt__(self, other):
        return self.subscriber_count > other.subscriber_count

    def __ge__(self, other):
        return self.subscriber_count >= other.subscriber_count

    def __eq__(self, other):
        return self.subscriber_count == other.subscriber_count

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(Channel.strj(self.__channel))

    @staticmethod
    def get_service():
        return Channel.__youtube

    @staticmethod
    def strj(your_dict: dict):
        """return string repr of your dict as json"""
        return json.dumps(your_dict, indent=2, ensure_ascii=False)

    def to_json(self, filename):
        my_dict = {
            'id':self.__channel_id,
            'title': self.title,
            'url': self.url,
            'description': self.description,
            'subscriberCount': self.subscriber_count,
            'videoCount': self.video_count,
            'viewCount': self.view_count,
        }

        with open(os.path.join(Path(__file__).parent.parent,'src', filename), 'w') as f:
            json.dump(my_dict,f,indent=2,ensure_ascii=False)