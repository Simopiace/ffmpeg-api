from flask import Flask, request, send_file
import subprocess
import requests

app = Flask(__name__)

@app.route('/merge', methods=['POST'])
def merge():
    data = request.get_json()
    video_url = data.get("video_url")
    audio_url = data.get("audio_url")

    video_path = "video.mp4"
    audio_path = "audio.mp3"
    output_path = "output.mp4"

    with open(video_path, "wb") as f:
        f.write(requests.get(video_url).content)

    with open(audio_path, "wb") as f:
        f.write(requests.get(audio_url).content)

    subprocess.run([
        "ffmpeg", "-i", video_path, "-i", audio_path,
        "-c:v", "copy", "-map", "0:v:0", "-map", "1:a:0",
        "-shortest", output_path
    ])

    return send_file(output_path, mimetype="video/mp4")

app.run(host='0.0.0.0', port=8080)
