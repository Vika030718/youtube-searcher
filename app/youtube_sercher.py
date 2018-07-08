import sys
from apiclient.discovery import build
sys.path.append('/home/vika/Documents/TestRepo/LayoutsForAnton/YoutubeParser/')


class Searcher(object):

    DEVELOPER_KEY = "AIzaSyA2BAHO4ArEf0VqWR5B1xz35_Jpycr00b8"
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"

    # video_dict = []

    def youtube_search(self, q, max_results=50, order="relevance", token=None, location=None, location_radius=None):

        youtube = build(self.YOUTUBE_API_SERVICE_NAME, self.YOUTUBE_API_VERSION, developerKey=self.DEVELOPER_KEY)

        search_response = youtube.search().list(q=q,
                                                type="video",
                                                pageToken=token,
                                                order=order,
                                                part="id,snippet",
                                                maxResults=max_results,
                                                location=location,
                                                locationRadius=location_radius).execute()

        videos = []

        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                videos.append(search_result)
        try:
            nexttok = search_response["nextPageToken"]
            return(nexttok, videos)
        except Exception as e:
            nexttok = "last_page"
            return(nexttok, videos)

    def grab_videos(self, keyword, token=None):
        res = self.youtube_search(keyword, token=token)
        token = res[0]
        videos = res[1]
        video_dict = []
        for vid in videos:
            video_dict.append({'title': vid['snippet']['title'], 'id': vid['id']['videoId']})
        return token, video_dict

    def youtube_search_all(self, expression):

        video_dict = []
        video_block = []

        token, video_dict = self.grab_videos(expression)
        while token != "last_page":
            token, video_block = self.grab_videos(expression, token=token)
            for video in video_block:
                video_dict.append(video)

        print(len(video_dict))

        return video_dict
