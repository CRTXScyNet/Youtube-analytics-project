from src.channel import Channel


class Video:

    __youtube = Channel.get_service()

    def __init__(self, video_id ):
        self.video_id = video_id
        self.video = ((Video.__youtube
                       .videos()
                       .list(id=video_id,part='id,snippet,statistics'))
                      .execute())
        self.title = self.video['items'][0]['snippet']['title']
        self.url =  f'https://www.youtube.com/watch?v={video_id}'
        self.view_count = self.video['items'][0]['statistics']['viewCount']
        self.like_count = self.video['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.title

    def print_info(self):
        print(Channel.strj(self.video))


class PLVideo(Video):

    def __init__(self, video_id, pl_id):
        super().__init__(video_id)
        self.playlist_id = pl_id
        self.url =  f'https://www.youtube.com/watch?v={video_id}&list={pl_id}'



video1 = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')
print(video1.url)




# {
#     "kind": "youtube#videoListResponse",
#     "etag": "-xhC5xLTzFYWVdCHjuQaVO3x6aQ",
#     "items": [
#         {
#             "kind": "youtube#video",
#             "etag": "FOjaZI5uzxpxX1V8F6VVPy8eCWI",
#             "id": "AWX4JnAnjBE",
#             "snippet": {
#                 "publishedAt": "2013-11-13T07:02:16Z",
#                 "channelId": "UC-OVMPlMA3-YCIeg4z5z23A",
#                 "title": "GIL в Python: зачем он нужен и как с этим жить",
#                 "description": "Григорий Петров\n12 сентября 2013\nMoscow Django Meetup № 14\n\nВ своем докладе Григорий проведет краткий экскурс в историю потоков и расскажет, зачем был создан GIL. Будут рассмотрены практические вопросы многопоточности в Python и способы работы с GIL.\nСлайды выступления: http://www.moscowpython.ru/meetup/14/gil-and-python-why/\n\nСпонсор подкаста: Курсы Python для новичков (https://learn.python.ru) и продвинутые курсы — https://learn.python.ru/advanced/",
#                 "thumbnails": {
#                     "default": {
#                         "url": "https://i.ytimg.com/vi/AWX4JnAnjBE/default.jpg",
#                         "width": 120,
#                         "height": 90
#                     },
#                     "medium": {
#                         "url": "https://i.ytimg.com/vi/AWX4JnAnjBE/mqdefault.jpg",
#                         "width": 320,
#                         "height": 180
#                     },
#                     "high": {
#                         "url": "https://i.ytimg.com/vi/AWX4JnAnjBE/hqdefault.jpg",
#                         "width": 480,
#                         "height": 360
#                     },
#                     "standard": {
#                         "url": "https://i.ytimg.com/vi/AWX4JnAnjBE/sddefault.jpg",
#                         "width": 640,
#                         "height": 480
#                     },
#                     "maxres": {
#                         "url": "https://i.ytimg.com/vi/AWX4JnAnjBE/maxresdefault.jpg",
#                         "width": 1280,
#                         "height": 720
#                     }
#                 },
#                 "channelTitle": "MoscowPython",
#                 "tags": [
#                     "Moscow Django Meetup",
#                     "python",
#                     "moscowdjango",
#                     "GIL",
#                     "многопоточность"
#                 ],
#                 "categoryId": "28",
#                 "liveBroadcastContent": "none",
#                 "localized": {
#                     "title": "GIL в Python: зачем он нужен и как с этим жить",
#                     "description": "Григорий Петров\n12 сентября 2013\nMoscow Django Meetup № 14\n\nВ своем докладе Григорий проведет краткий экскурс в историю потоков и расскажет, зачем был создан GIL. Будут рассмотрены практические вопросы многопоточности в Python и способы работы с GIL.\nСлайды выступления: http://www.moscowpython.ru/meetup/14/gil-and-python-why/\n\nСпонсор подкаста: Курсы Python для новичков (https://learn.python.ru) и продвинутые курсы — https://learn.python.ru/advanced/"
#                 }
#             },
#             "statistics": {
#                 "viewCount": "62858",
#                 "likeCount": "2626",
#                 "favoriteCount": "0",
#                 "commentCount": "62"
#             }
#         }
#     ],
#     "pageInfo": {
#         "totalResults": 1,
#         "resultsPerPage": 1
#     }
# }
