# Real-Time Squat Monitoring and Feedback System

Developed a real-time squat monitoring and feedback system for my senior project under the mentorship of a Meta software engineer. Leveraging data science and computer vision, the application analyzes squat movements using Google's MediaPipe Pose Detection Model and provides immediate feedback to enhance exercise performance.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Data Collection](#data-collection)
- [Acknowledgments](#acknowledgments)
- [Contact Information](#contact-information)
- [License](#license)

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

- Python 3.x installed on your system.
- A webcam connected to your computer.

### Dependencies

- OpenCV
- MediaPipe
- NumPy

### Instructions

1. **Clone or Download the Project Repository**

   ```bash
   git clone https://github.com/yourusername/squat-monitoring-system.git
