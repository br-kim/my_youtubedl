import youtube_dl
import os

from my_video_url import my_playlist_url1_japan, my_playlist_url2_songs, my_playlist_url3_piano

# ffprobe.exe download
# ffmpeg.exe download
# download() playlist url도 가능.


def get_video_ids(playlist_dict, path):
    """
    playlist 정보와 다운로드 폴더 경로를 받아 다운로드 폴더에 있는 파일 아이디와 비교하여
    폴더에 없는 동영상만 리스트로 반환한다.
    """
    file_list = os.listdir(path)
    file_id_list = []
    video_ids = []
    for file_name in file_list:
        v_id = file_name[-15:-4]
        file_id_list.append(v_id)
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
    }
    ],
    'nooverwrites': True,
    'outtmpl': save_path + '%(title)s-%(id)s.%(ext)s',
}


if __name__ == '__main__':
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        playlist_dictionary = ydl.extract_info(my_playlist_url3_piano, download=False)
        videos_list = get_video_ids(playlist_dictionary, save_path)
        if videos_list:
            ydl.download(videos_list)
        else:
            print("플레이리스트에 추가된 동영상 없음.")
