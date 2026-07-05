# Custom Hand Gesture Detection using YOLOv8

## Overview

The *Custom Hand Gesture Detection* project is a real-time computer vision application that detects and classifies different hand gestures using a webcam and a custom-trained YOLOv8 model. The system is designed for gesture-based human-computer interaction and demonstrates the capabilities of deep learning for object detection.

---

## Features

- Real-time hand gesture detection
- Webcam-based live inference
- Custom YOLOv8 model training
- High-speed object detection
- Displays gesture labels with confidence scores
- Easy to train with custom datasets

---

## Technologies Used

- Python
- YOLOv8 (Ultralytics)
- OpenCV
- PyTorch
- NumPy

---

## Project Structure


Custom-Hand-Gesture-Detection/
│
├── train.py
├── resume_train.py
├── test.py
├── webcam.py
├── data.yaml
├── requirements.txt
├── .gitignore
└── README.md


---

## Installation

### Clone the Repository

bash
git clone https://github.com/SAIDEEPUBALARAJU-2003/Custom-Hand-Gesture-Detection.git


### Navigate to the Project Folder

bash
cd Custom-Hand-Gesture-Detection


### Install Dependencies

bash
pip install -r requirements.txt


---

## Training the Model

Train the custom YOLOv8 model:

bash
python train.py

---

## Testing the Model

Run:

bash
python test.py


---

## Real-Time Gesture Detection

Start webcam detection:

bash
python webcam.py


---

## Supported Hand Gestures

The model detects the following custom hand gestures:

- Fist ✊
- Peace ✌️
- Stop ✋
- Thumbs Up 👍
- Super 🤙

> You can modify the dataset and data.yaml file to support additional gestures.

---

## Applications

- Human-Computer Interaction (HCI)
- Gesture-Based Control Systems
- Smart Home Automation
- Touchless User Interfaces
- Robotics
- Gaming Applications
- Sign Language Research

---

## Future Enhancements

- Support for additional hand gestures
- Voice feedback for detected gestures
- Mobile application integration
- Multi-hand detection
- Gesture-based presentation control
- Smart home device control

---

## Requirements

- Python 3.10+
- OpenCV
- Ultralytics YOLOv8
- PyTorch
- NumPy

Install all dependencies using:

bash
pip install -r requirements.txt


---

## Results

The trained YOLOv8 model is capable of detecting multiple hand gestures in real time with high accuracy using a standard webcam. The system displays the detected gesture label along with its confidence score, enabling fast and reliable gesture recognition.

---

## Author

*Sri Harshithanjali Sammeta*

GitHub: https://github.com/SammetaSriHarshithanjali

---

## License

This project is intended for educational and research purposes.

---

## Acknowledgements

- Ultralytics YOLOv8
- OpenCV
- PyTorch
- Python Community
