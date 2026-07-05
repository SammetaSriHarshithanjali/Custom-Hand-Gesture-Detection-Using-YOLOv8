from ultralytics import YOLO

model = YOLO(
    r"C:\Users\Saideepu Balaraju\Desktop\HandGestureDataset\runs\detect\train-3\weights\best.pt"
)

metrics = model.val()

print(metrics)