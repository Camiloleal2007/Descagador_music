from flask import Flask, request, send_from_directory, render_template
import yt_dlp
import os
import uuid

app = Flask(__name__)

# Carpeta donde se guardarán las descargas
DOWNLOAD_FOLDER = os.path.join(app.root_path, 'static', 'musicas')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']

    # Crear carpeta si no existe
    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

    filename = str(uuid.uuid4()) + ".mp3"
    filepath = os.path.join(DOWNLOAD_FOLDER, filename)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': filepath,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
        # Importante: ffmpeg debe estar disponible en el entorno PATH
        'ffmpeg_location': 'ffmpeg'  # Asumimos que Render o el servidor ya tiene ffmpeg instalado
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return send_from_directory(os.path.join('static', 'musicas'), filename, as_attachment=True)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
