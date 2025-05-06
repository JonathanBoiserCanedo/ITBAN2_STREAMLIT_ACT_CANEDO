import streamlit as st
import cv2
import numpy as np
from datetime import datetime

st.title("🎥 Snapshot")

# Sliders for filter thresholds
brightness = st.slider("Brightness", 0, 100, 50)
contrast = st.slider("Contrast", 0, 100, 50)
apply_gray = st.checkbox("Grayscale Filter")
apply_canny = st.checkbox("Canny Edge Detection")

# Button for snapshot
snapshot = st.button("📸 Take Snapshot")

# Start video capture
cap = cv2.VideoCapture(0)

frame_placeholder = st.empty()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Apply brightness and contrast adjustments
    brightness_val = brightness - 50
    contrast_val = contrast - 50
    frame = cv2.convertScaleAbs(frame, alpha=1 + contrast_val / 50, beta=brightness_val)

    # Apply filters
    if apply_gray:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

    if apply_canny:
        edges = cv2.Canny(frame, 100, 200)
        frame = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    # Convert BGR to RGB for Streamlit
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_placeholder.image(frame_rgb, channels="RGB")

    # Take snapshot if requested
    if snapshot:
        filename = f"snapshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        cv2.imwrite(filename, frame)
        st.success(f"Snapshot saved as {filename}")
        snapshot = False  # Reset snapshot button
        break

cap.release()
