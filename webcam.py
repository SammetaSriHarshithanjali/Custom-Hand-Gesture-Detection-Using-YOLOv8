from ultralytics import YOLO

model = YOLO(
    r"C:\Users\Saideepu Balaraju\Desktop\Driver Drowsiness Detection\runs\detect\train\weights\best.pt"
)
model.predict(
    source=0,
    show=True,
    conf=0.25
)