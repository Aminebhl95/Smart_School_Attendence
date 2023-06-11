# Git Repository Readme

This repository contains code for a simple face recognition attendance system using OpenCV and SimpleFacerec library. The code captures video from a webcam, detects faces, recognizes known faces, and marks their attendance in a CSV file.

## Requirements

To run the code in this repository, you need to have the following dependencies installed:

- Python 3.x
- OpenCV (`cv2`)
- SimpleFacerec
- NumPy

You can install the required Python packages using pip:

## Usage

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd <repository_directory>

   ```

2. Prepare face encodings:
<li>Create a folder named "photos" in the repository directory.
Add images of known individuals to the "photos" folder. Each image should contain the face of one individual. The file name should correspond to the name of the person.
It is recommended to include multiple images of each person for better recognition accuracy.

3. Run the code:

   ```sh
   python main.py

   ```

4. The program will start capturing video from the default webcam.
5. Detected faces will be compared with the provided face encodings and recognized names will be displayed on the video frame.
6. If a recognized name is not already marked in the attendance CSV file, it will be added with the current date and time.
7. Press the 'Esc' key to exit the program.

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.
