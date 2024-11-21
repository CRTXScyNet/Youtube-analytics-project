# from helper.youtube_api_manual import playlist
import isodate

from src.channel import Channel


class PlayList:

    __youtube = Channel.get_service()

    def __init__(self,list_id):
        self.list_id = list_id
        self.title = (PlayList.__youtube
                      .playlists()
                      .list(id=list_id,part='snippet')
                      .execute()['items'][0]['snippet']['localized']['title'])
        self.playlist = ((PlayList.__youtube
                       .playlistItems()
                       .list(playlistId=list_id,part='id,contentDetails,snippet,status'))
                      .execute())
        self.url = f'https://www.youtube.com/playlist?list={list_id}'
        self.video_ids = [i['contentDetails']['videoId'] for i in self.playlist['items']]
        self.videos = (PlayList.__youtube
                       .videos()
                       .list(part='contentDetails,statistics'
                             ,id=','.join(self.video_ids))).execute()

        self.__total_duration = ''
        for video in self.videos['items']:
            duration = isodate.parse_duration(video['contentDetails']['duration'])
            if self.__total_duration == '':
                self.__total_duration = duration
            else:
                self.__total_duration += duration

        self.__best_video = f"https://youtu.be/{max(self.videos['items'],key=lambda a: int(a['statistics']['likeCount']))['id']}"

    @property
    def total_duration(self):
        return self.__total_duration

    def show_best_video(self):
        return self.__best_video

    def print_info(self):
        print(Channel.strj(self.playlist))
