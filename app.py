import os
import yaml
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, url_for, flash
import datetime
from flask import send_from_directory
from flask_session import Session

app = Flask(__name__)
sess = Session()

# Allowed video extensions
# Video File Types
# MP4: .mp4 - Widely supported, contains MPEG-4 or H.264 video and AAC audio.
# WebM: .webm - Open format, often contains VP8 or VP9 video and Vorbis or Opus audio.
# Ogg: .ogg - Open format, may contain Theora video and Vorbis audio.

# Audio File Types
# MP3: .mp3 - Widely used for music, podcasts, etc.
# WAV: .wav - Uncompressed audio format, high quality.
# AAC: .aac - Advanced Audio Coding, similar to MP3 but higher quality.
# Ogg (Vorbis): .ogg - Audio counterpart of the Ogg video format.
# FLAC: .flac - Free Lossless Audio Codec, for lossless audio compression.

# Image File Types
# JPEG: .jpeg/.jpg - Common for photos, uses lossy compression.
# PNG: .png - Supports transparency, uses lossless compression.
# GIF: .gif - Supports animation, uses lossless compression.
# WebP: .webp - Modern format, supports both lossy and lossless compression.
# SVG: .svg - Scalable Vector Graphics, for vector-based images.

ALLOWED_EXTENSIONS = {
    # Video File Types
    "mp4", "webm", "ogg", 

    # Audio File Types
    "mp3", "wav", "aac", "ogg", "flac", 

    # Image File Types
    "jpeg", "jpg", "png", "gif", "webp", "svg"
}



# Media directory configuration
MEDIA_FOLDER = '/media/wd/01/daytrading-videos'  # Set your path here
app.config['MEDIA_FOLDER'] = MEDIA_FOLDER

# YAML file configuration for video metadata
VIDEO_METADATA_FILE = '/media/wd/01/daytrading-videos/video_metadata.yaml'  # Set your path here
app.config['VIDEO_METADATA_FILE'] = VIDEO_METADATA_FILE

def load_videos():
    if not os.path.exists(app.config['VIDEO_METADATA_FILE']):
        return []
    with open(app.config['VIDEO_METADATA_FILE'], 'r') as file:
        videos_dict = yaml.safe_load(file) or []
    return [Video(**video) for video in videos_dict]

def save_videos(videos):
    videos_dict = [video.to_dict() for video in videos]
    with open(app.config['VIDEO_METADATA_FILE'], 'w') as file:
        yaml.safe_dump(videos_dict, file)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for the home page
@app.route('/')
def index():
    videos = load_videos()  # Load current videos
    return render_template('index.html', videos=videos)

# Route to add a new video
@app.route('/add', methods=['GET', 'POST'])
def add_video():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'video_file' not in request.files:
            flash('No video file part')
            return redirect(request.url)
        file = request.files['video_file']

        print("uno\n")
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected video file')
            return redirect(request.url)

        print("dos\n")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_date = datetime.datetime.now()
            year_month = upload_date.strftime("%Y/%Y%m")
            upload_path = os.path.join(app.config['MEDIA_FOLDER'], year_month)

            if not os.path.exists(upload_path):
                os.makedirs(upload_path)

            file_path = os.path.join(upload_path, filename)
            file.save(file_path)

            # Other form fields
            title = request.form['title']
            description = request.form['description']
            tags = request.form['tags'].split()
            date_saved = upload_date.strftime("%Y.%m.%d %H:%M:%S")
            url = url_for('uploaded_file', filename=os.path.join(year_month, filename))

            videos = load_videos()  # Load current videos
            videos.append(Video(title, url, description, tags, date_saved))
            save_videos(videos)  # Save updated videos list

            print("tres\n")
            return redirect(url_for('index'))

    return render_template('add_video.html')

# Route to update a video
@app.route('/update/<int:video_index>', methods=['GET', 'POST'])
def update_video(video_index):
    videos = load_videos()
    video = videos[video_index]
    if request.method == 'POST':
        video.title = request.form['title']
        video.url = request.form['url']  # This line expects the 'url' field
        video.description = request.form['description']
        video.tags = request.form['tags'].split()
        video.date_saved = datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S")
        save_videos(videos)  # Don't forget to save the updated videos
        return redirect(url_for('index'))
    return render_template('update_video.html', video=video, index=video_index)

# Route to delete a video
@app.route('/delete/<int:video_index>', methods=['POST'])
def delete_video(video_index):

    videos = load_videos()  # Load current videos
    del videos[video_index]
    save_videos(videos)  # Save updated videos list

    return redirect(url_for('index'))

# Route to search videos by tags
@app.route('/search', methods=['GET'])
def search():
    search_tags = request.args.get('tags', '').split()
    videos = load_videos()  # Load current videos
    filtered_videos = [video for video in videos if all(tag in video.tags for tag in search_tags)]
    return render_template('index.html', videos=filtered_videos)

@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['MEDIA_FOLDER'], filename)

class Video:
    def __init__(self, title, url, description, tags, date_saved):
        self.title = title
        self.url = url
        self.description = description
        self.tags = tags
        self.date_saved = date_saved

    def to_dict(self):
        print("to_dict called")  # Debug print
        return {
            'title': self.title,
            'url': self.url,
            'description': self.description,
            'tags': self.tags,
            'date_saved': self.date_saved
        }


if __name__ == "__main__":
    # Quick test configuration. Please use proper Flask configuration options
    # in production settings, and use a separate file or environment variables
    # to manage the secret key!
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    sess.init_app(app)

    app.debug = True
    app.run(host='0.0.0.0', port=5000)


