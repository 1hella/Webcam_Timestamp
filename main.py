import cv2
import streamlit as st
import time

st.title('Webcam Viewer')
start = st.button('Start camera')

if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        day = time.strftime("%A")
        formatted_time = time.strftime("%H:%M:%S")

        cv2.putText(img=frame, text=day, org=(50, 50),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(255, 255, 255),
                    thickness=2, lineType=cv2.LINE_AA)
        cv2.putText(img=frame, text=formatted_time, org=(50, 80),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(255, 0, 0),
                    thickness=2, lineType=cv2.LINE_AA)

        streamlit_image.image(frame)
