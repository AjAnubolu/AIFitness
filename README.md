# Real-Time Squat Monitoring and Feedback System

Developed a real-time squat monitoring and feedback system for my senior project under the mentorship of a Meta software engineer. Leveraging data science and computer vision, the application analyzes squat movements using Google's MediaPipe Pose Detection Model and provides immediate feedback to enhance exercise performance.

- **[Blog on Developmental Process of Project](https://basisindependent.com/schools/ca/fremont/academics/the-senior-year/senior-projects/ajay-a/)**
- **[Live Demo](https://www.youtube.com/watch?v=6pyaGpjBJq4)**

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Data Collection](#data-collection)
- [Acknowledgments](#acknowledgments)

---

## Features

- **Real-Time Pose Detection**
  - Utilizes MediaPipe's Pose Detection to track and analyze body movements in real-time.

- **Squat Repetition Counting**
  - Calculates joint angles to count squat repetitions and assesses performance against optimal thresholds derived from physiological data.

- **Gesture Control Integration**
  - Implements hand gesture recognition:
    - Raise the **left hand** above the head to **start or resume** counting.
    - Raise the **right hand** above the head to **reset** the counter and **pause** the program.

- **Real-Time Feedback**
  - Provides immediate on-screen feedback, including squat count and performance evaluation.

---

## Technologies Used

- **Python**
  - Core programming language used for development.

- **OpenCV**
  - Used for video capture, image processing, and display.

- **MediaPipe Pose Detection**
  - Google's machine learning solution for high-fidelity body pose tracking.

- **NumPy**
  - For numerical operations, especially in calculating joint angles.

---

## Installation

### Prerequisites

- Python 3.8 installed on your system.
- A webcam connected to your computer.
- **Optional:** [Bazel](https://bazel.build/) build tool installed (if using Bazel)
- **Optional:** [Brew](https://brew.sh/)  if using macOS (replace pip3 with brew in commands)
  - ```bash
    brew install git
    ```bash
    brew install python
    ```bash
    brew install python opencv
    ```bash
    pip install mediapipe numpy

- **Optional:** [Git](https://git-scm.com/downloads) for version control
  - ```bash
    git init          # Initialize a new Git repository
    ```bash
    git add .         # Stage changes for commit
    ```bash
    git commit -m "Initial commit"   # Commit changes with a message


### Dependencies

- mediapipe==0.8.6
- numpy==1.21.2
- opencv-python==3


### Instructions


1. **Prepare Virtual Environment**

   ```bash
   pip3 install python
   ```bash
   pip3 upgrade python
   ```bash
   cd path/to/your/projects/
    ```bash
   python -m venv env
  .\env\Scripts\activate
   



2. **Clone or Download the Project Repository**

   ```bash
   git clone https://github.com/AjAnubolu/AIFitness

3. . **Navigate to project directory**

   ```bash
   cd project-repo
   
4. **Run**
   
   ```bash
    python squat_monitor.py

5. **Close**

   ```bash
    deactivate

___

## Usage

1. **Prepare Your Environment**
   * Ensure your webcam is properly connected and not used by other applications.
   * Stand in front of the camera so your full body is visible.
   * Ensure good lighting for optimal pose detection.

2. **Control the Application with Gestures**
   * **Start or Resume Counting**
     * Raise your **left hand** above your head.
   * **Reset Counter and Pause**
     * Raise your **right hand** above your head.

3. **Perform Squats**
   * Execute squats with proper form.
   * The application will count repetitions and provide feedback for some errors on each squat
     * Still under development to expand error handling and different exercises

4. **View Feedback**
   * On-screen display includes:
     * Current squat count.
     * Feedback messages for each repetition (e.g., "Rep 1: Good", "Rep 2: Heels lifting off floor").
     * Status messages like "Ready" and "Set Complete".

5. **Exit the Application**
   * Press the **'q' key** on your keyboard to quit the program.
  

___

## Data Collection
* **Physiological Data Gathering**
   * Collected and preprocessed physiological data from research studies on optimal squat angles.
   * Established accurate evaluation metrics to compare user movements against optimal thresholds.
   * Referenced studies in [acknowledgements](#Acknowledgements) to determine angular thresholds for repetition counting and feedback
___

## Acknowledgments
* **Mentorship**
   * Special thanks to my mentor, Jeff Chow, and my advisor, Andrew Mageefor guidance and support throughout this project.
* **Resources and References**
   * [Google's MediaPipe Framework](https://github.com/google-ai-edge/mediapipe)
   * [OpenCV Documentation](https://github.com/opencv/opencv) 
   * Research studies on biomechanics and optimal squat techniques
     * [Journal of Sports Medicine](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4967668/)
     * [BMC Sports Science Medicine](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6990583/)
     * [IJSPT](https://ijspt.scholasticahq.com/article/94600-a-biomechanical-review-of-the-squat-exercise-implications-for-clinical-practice)
  * **Build Tools**
    * [Homebrew](https://brew.sh/)
    * [Bazel](https://bazel.build/)
    * [Git](https://git-scm.com/downloads)


