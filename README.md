
**Face Attendance Recorder(FAR)**

**Table of Contents**
1.About
2.Features
3.Technologies
4.Installation
5.Usage
6.Dataset
7.Results


**About**
The Face Recognition Attendance System is a real-time application that leverages facial recognition technology to automate the attendance logging process. This system captures faces using a webcam, recognizes them against a set of known faces, and logs attendance into a CSV file.

**Features**
Real-time Face Recognition: Detects and recognizes faces from a live webcam feed.
Automated Attendance Logging: Records attendance automatically in a CSV file.
Scalable: Supports multiple users and can easily add new faces to the database.
User-Friendly Interface: Displays recognized names in the video feed.

**Technologies**
This project is built using:

Python: Main programming language.
OpenCV: For video capture and image processing.
face_recognition: For facial recognition and encoding.
NumPy: For numerical operations and array manipulations.
Pandas: (optional) For more advanced data handling if needed.

**Installation**
1.Clone the repository:

bash
Copy code
git clone https://github.com/alishaverma353/face-recognition-attendance.git
cd face-recognition-attendance

2.Create a virtual environment and activate it.

3.pip install -r requirements.txt

**Prepare your images:**

Place images of individuals you want to recognize in the imagesattendance directory. The filenames should reflect the names of the individuals (e.g., elon musk.png).
**Usage**
1.Run the Attendance System
2.Open the Webcam

The application will open your webcam, display the video feed, and attempt to recognize faces in real-time.

3.Attendance Logging

When a recognized face is detected, the system will log the name and the current timestamp into Attendance.csv.

4.Exit the Program:

Press 'q' to stop the webcam feed and exit the application.

5.Dataset
The application requires a folder named imagesattendance containing images of individuals to recognize. The images should be clear and preferably contain the person's face without obstructions.

6.Results
The attendance is logged in the Attendance.csv file with the following format:

Name	Timestamp
Elon Musk	12:30:45
Jane Doe	12:31:10


