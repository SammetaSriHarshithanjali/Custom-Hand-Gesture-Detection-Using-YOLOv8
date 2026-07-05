# ✋ Custom Hand Gesture Detection Using YOLOv8

A real-time **Hand Gesture Detection System** developed using **Python**, **YOLOv8**, **OpenCV**, and **Computer Vision**. The project detects and classifies custom hand gestures from webcam input using a deep learning model trained on a custom dataset.

---

# 📖 Project Overview

Hand gesture recognition plays an important role in Human-Computer Interaction (HCI), enabling intuitive and touchless interaction between humans and machines.

This project uses **YOLOv8 (You Only Look Once Version 8)** to detect and classify multiple hand gestures in real time. The model has been trained on a custom annotated dataset and performs fast, accurate gesture detection from live webcam feeds.

---

# ✨ Features

- ✅ Real-time hand gesture detection
- ✅ Webcam-based live inference
- ✅ Custom YOLOv8 model training
- ✅ High-speed object detection
- ✅ Confidence score visualization
- ✅ Lightweight implementation
- ✅ Easy to retrain using custom datasets

---

# 🛠️ Technology Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Deep Learning | YOLOv8 (Ultralytics) |
| Computer Vision | OpenCV |
| Framework | PyTorch |
| Data Processing | NumPy |
| Development Environment | VS Code |

---

# 📂 Project Structure

```text
Custom-Hand-Gesture-Detection/
│
├── train.py
├── evaluate.py
├── webcam.py
├── convert_json_to_yolo.py
├── split_dataset.py
├── data.yaml
├── yolov8n.pt
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

# 🧠 Model

The project uses **YOLOv8 Nano (YOLOv8n)** for real-time object detection.

The model is trained on a custom dataset to recognize multiple hand gestures with high speed and accuracy.

---

# 📊 Dataset

The model was trained on a **custom hand gesture dataset** created specifically for this project.

The dataset contains manually collected and annotated images of different hand gestures.

> **Note**
>
> The dataset is **not included** in this repository because it contains personally collected images and is not intended for public distribution.

Users can train the project using their own dataset by following the same folder structure and annotation format.

---

# 📁 Expected Dataset Structure

```text
dataset/
│
├── train/
│   ├── images/
│   └── labels/
│
├── valid/
│   ├── images/
│   └── labels/
│
└── test/
    ├── images/
    └── labels/
```

Images should be annotated in **YOLO format**.

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/SammetaSriHarshithanjali/Custom-Hand-Gesture-Detection-Using-YOLOv8.git
```

Navigate to the project directory

```bash
cd Custom-Hand-Gesture-Detection-Using-YOLOv8
```

Install the required packages

```bash
pip install -r requirements.txt
```

---

# 🚀 Training

Train the custom YOLOv8 model.

```bash
python train.py
```

---

# 📊 Evaluation

Evaluate the trained model.

```bash
python evaluate.py
```

---

# 📷 Real-Time Detection

Start webcam-based hand gesture detection.

```bash
python webcam.py
```

---

# ✋ Supported Hand Gestures

The model can recognize custom hand gestures such as:

- ✊ Fist
- ✌️ Peace
- ✋ Stop
- 👍 Thumbs Up
- 🤙 Super

The supported classes can be modified by updating the dataset and `data.yaml`.

---

# 🎯 Applications

- Human-Computer Interaction (HCI)
- Touchless User Interfaces
- Gesture-Controlled Systems
- Robotics
- Smart Home Automation
- Gaming
- Educational AI Applications
- Sign Language Research

---

# 📈 Results

- High detection accuracy
- Real-time webcam inference
- Fast YOLOv8 object detection
- Low latency
- Lightweight deployment

---

# 💡 Future Enhancements

- Dynamic hand gesture recognition
- Multi-hand detection
- Gesture-based virtual mouse
- Voice feedback
- Mobile deployment
- TensorRT optimization
- Smart home integration

---

# 📚 Skills Demonstrated

- Python
- Computer Vision
- Deep Learning
- YOLOv8
- OpenCV
- Object Detection
- Dataset Annotation
- Model Training
- Real-Time AI Applications

---

# 📄 License

This project is intended for educational and research purposes.

---

# 👩‍💻 Author

**Anjali**

Machine Learning | Deep Learning | Computer Vision | Data Engineering

📧 Email: anjalisammeta03@gmail.com

🔗 GitHub: https://github.com/SammetaSriHarshithanjali

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
