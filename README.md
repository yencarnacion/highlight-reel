# highlight-reel

highlight-reel is a Python project designed to facilitate the uploading and tagging of MP4 videos. This platform allows users to efficiently manage and search through their video collections using custom tags. Each video record can be uniquely tagged during the upload process, making it easier to locate and organize video content.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the latest version of Python installed on your system. highlight-reel is built using Python, and you will need Python to run the server.

### Installing

To get highlight-reel up and running, follow these simple steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/yencarnacion/highlight-reel.git
   cd highlight-reel
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the application:

   ```bash
   python app.py
   ```

   This will start the Flask server, and the application should now be running on your localhost.

## Usage

### Before you start:

1. Update variables:
* Locate the lines where `MEDIA_FOLDER` and `VIDEO_METADATA_FILE` are defined near the beginning of `app.py`.

* Change the values within the quotes to match the desired paths on your system. For example:

```Python
MEDIA_FOLDER = '/path/to/your/media/folder'  # Replace with your actual path
app.config['MEDIA_FOLDER'] = MEDIA_FOLDER

VIDEO_METADATA_FILE = '/path/to/your/video_metadata.yaml'  # Replace with your actual path
app.config['VIDEO_METADATA_FILE'] = VIDEO_METADATA_FILE
```

### Starting the application:

Run `python app.py`

### Using the application:

* Once the application is running, open your web browser and go to http://localhost:5000.
* You can now:
    * Upload MP4 videos.
    * Assign tags to videos.
    * Search for videos using tags.

## Inspiration for the Repository Name: "highlight-reel"

The name of this repository, "highlight-reel", is directly inspired by a concept explained in the YouTube video titled ["The #1 trick to dramatically improve your trading faster"](https://www.youtube.com/watch?v=ShWqQVW8-28). In this insightful video, Lance Breitstein, a highly successful trader and special advisor to SMB Capital, shares his unique approach to accelerating the learning process in trading.

Breitstein introduces the "Highlight Reel" technique, a method that involves recording one's trading activities and then meticulously reviewing and analyzing key moments to gain deeper insights and improve trading strategies. This approach is modeled on the practices of top athletes who study gameplay footage to spot patterns and enhance their performance.

The concept emphasizes the importance of meta-learning - learning how to learn effectively. It involves breaking down complex trading skills into smaller, manageable components, setting specific goals for improvement, and engaging in focused, deliberate practice. By creating a repository of trading footage and reviewing it regularly, traders can accelerate their learning curve, identify and rectify mistakes, and refine their strategies.

This repository aims to provide a tool for storing and making searchable the highlight reel videos outlined by Lance Breitstein, serving as a resource and tool for traders who are committed to continuously improving their skills through focused analysis and review.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.