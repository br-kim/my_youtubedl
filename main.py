import youtube_dl
import os

import my_video_url

# ffprobe.exe download
# ffmpeg.exe download
# download() playlist url도 가능.


def get_file_ids(path):
    """
    path에 있는 다운로드된 파일들의 id를 가져옵니다.
    :param path: 파일들의 경로
    :return: 경로에 있는 파일들의 id
    """
    file_list = os.listdir(path)
    ids = []
    for file_name in file_list:
        v_id = file_name[-15:-4]
        ids.append(v_id)
    return ids


def get_video_ids(playlist_dict, file_id_list):
    """
    playlist_dict의 id를 가져와서 file_id_list에 있는 id만 반환합니다.
    :param playlist_dict:
    :param file_id_list:
    :return:
    """
    video_ids = []
    entries = playlist_dict["entries"]
    for entry in entries:
        video_id = entry['id']
        if video_id not in file_id_list:
            video_ids.append(video_id)
        else:
            title = entry["title"]
            print(title, "이미 존재하는 동영상입니다.")
    return video_ids

# save path 설정
# C:\\Users\\USER_NAME\\ + Download Directory
my_download_path = ['Downloads', 'ytdl_downloads']
my_download_path.extend([''])
save_path = "\\".join(os.getcwd().split('\\')[:3] + my_download_path)
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
        'nopostoverwrites': True
    }
    ],
    'nooverwrites': True,
    'outtmpl': save_path + '%(title)s-%(id)s.%(ext)s',
}


if __name__ == '__main__':
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        playlist_dictionary = ydl.extract_info(my_video_url.my_playlist_url4_videos, download=False)
        file_ids = get_file_ids(save_path)
        videos_list = get_video_ids(playlist_dictionary, file_ids)
        ydl.download(videos_list)
    pass