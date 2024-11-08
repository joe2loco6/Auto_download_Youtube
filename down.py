import pandas as pd
from pytubefix import YouTube
from pytubefix.cli import on_progress

#Funcionando 13/09/2024
def download_video(url):
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        print(f"Baixando: {yt.title}")
        ys = yt.streams.get_highest_resolution()
        ys.download()
        print(f"Download de {yt.title} concluído.")
    except Exception as e:
        print(f"Erro ao baixar o vídeo {url}: {str(e)}")

csv_file = 'lista_de_urls.csv'  
df = pd.read_csv(csv_file)


for index, row in df.iterrows():
    url = row['url'] 
    download_video(url)


#from pytube import YouTube
#YouTube('https://www.youtube.com/watch?v=QQw_eox2sDE&pp=ygUHbWFyb2xhcg%3D%3D').streams.first().download()
#yt = YouTube('https://www.youtube.com/watch?v=QQw_eox2sDE&pp=ygUHbWFyb2xhcg%3D%3D')
#yt.streamsfilter(progressive=True, file_extension='mp4')
#order_by('resolution')
#desc()
#first()
#download()