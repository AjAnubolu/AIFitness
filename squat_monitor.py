import cv2
import numpy as np
import mediapipe as mp

def calculate_angle(a, b, c):
    a = np.array(a)  # First
    b = np.array(b)  # Mid
    c = np.array(c)  # End
    
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    
    if angle > 180.0:
        angle = 360 - angle
    
    return angle

def draw_landmarks_on_image(rgb_image, results):
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_pose = mp.solutions.pose

    # Draw the pose landmarks on the image.
    annotated_image = rgb_image.copy()
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(
            annotated_image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    return annotated_image

# Initialize MediaPipe Pose.
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(
    static_image_mode=False,
    model_complexity=1,
    smooth_landmarks=True, 
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

# Open the webcam.
cap = cv2.VideoCapture(0)

squat_counter = 0
in_squat = False
last_knee_angle = 180  # Start with an impossible angle for squatting
rep_grades = []
stop_counter = True  # Flag to stop counting
has_started = False  # Flag to check if counting has ever started


while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # Convert the BGR image to RGB and process it with MediaPipe Pose.
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False
    results = pose.process(image)

    # Draw the pose annotation on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    # Calculate knee angle
    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark
        right_wrist = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value]
        left_wrist = landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value]
        nose = landmarks[mp_pose.PoseLandmark.NOSE.value]

        # Check if right hand is above the head
        if right_wrist.y < nose.y and has_started:
            stop_counter = True
            squat_counter = 0
            rep_grades = []  # Clear grades

        # Left hand raised to start or resume counting
        if left_wrist.y < nose.y:
            if not has_started:
                has_started = True  # Start counting for the first time
            stop_counter = False
    if not has_started and stop_counter:
        text = "Ready"
        textsize = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)[0]
        textX = (frame.shape[1] - textsize[0]) // 2
        textY = (frame.shape[0] + textsize[1]) // 2
        cv2.putText(image, text, (textX, textY), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    

    elif stop_counter and has_started:
        text = "Set Complete"
        textsize = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1, 2)[0]
        textX = (frame.shape[1] - textsize[0]) // 2
        textY = (frame.shape[0] + textsize[1]) // 2
        cv2.putText(image, text, (textX, textY), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    if not stop_counter:
        annotated_image = draw_landmarks_on_image(image, results)

        # Calculate knee angle and update squat counter
        if results.pose_landmarks:
            hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x * frame.shape[1], landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y * frame.shape[0]]
            knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x * frame.shape[1], landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y * frame.shape[0]]
            ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x * frame.shape[1], landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y * frame.shape[0]]
            knee_angle = calculate_angle(hip, knee, ankle)

            if knee_angle <= 104 and last_knee_angle > 104:
                in_squat = True
            elif knee_angle >= 144 and last_knee_angle < 144 and in_squat:
                squat_counter += 1
                in_squat = False
                rep_grades.append(f"Rep {squat_counter}: Good")

            last_knee_angle = knee_angle  # Update the last knee angle
    else:
        annotated_image = image
        
    #display the rep count and grades
    cv2.putText(annotated_image, 'Squats: {}'.format(squat_counter), (30, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 4, cv2.LINE_AA)
    
    #display grades for each rep
    y_offset = 110  # Start position for the grades display, adjust as needed
    for grade in rep_grades:
        cv2.putText(annotated_image, grade, (30, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 0), 2, cv2.LINE_AA)
        y_offset += 50  # Adjust the vertical position for the next grade

    # Display the annotated image
    cv2.imshow('MediaPipe Pose', annotated_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
