import os
import json

INPUT_JSON_FOLDER = r"C:\Users\Saideepu Balaraju\Pictures\Annotations"
OUTPUT_LABEL_FOLDER = r"C:\Users\Saideepu Balaraju\Desktop\HandGestureDataset\labels"

os.makedirs(OUTPUT_LABEL_FOLDER, exist_ok=True)

classes = [
    "peace",
    "fist",
    "thumbsup",
    "super",
    "stop"
]

for file in os.listdir(INPUT_JSON_FOLDER):

    if not file.endswith(".json"):
        continue

    json_path = os.path.join(INPUT_JSON_FOLDER, file)

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    img_w = data["imageWidth"]
    img_h = data["imageHeight"]

    yolo_lines = []

    for shape in data["shapes"]:

        label = shape["label"].strip()

        if label not in classes:
            print(f"Skipping unknown label: {label}")
            continue

        class_id = classes.index(label)

        points = shape["points"]

        x1 = points[0][0]
        y1 = points[0][1]
        x2 = points[2][0]
        y2 = points[2][1]

        x_center = ((x1 + x2) / 2) / img_w
        y_center = ((y1 + y2) / 2) / img_h

        width = abs(x2 - x1) / img_w
        height = abs(y2 - y1) / img_h

        yolo_lines.append(
            f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}"
        )

    txt_name = os.path.splitext(file)[0] + ".txt"

    with open(
        os.path.join(OUTPUT_LABEL_FOLDER, txt_name),
        "w",
        encoding="utf-8"
    ) as f:
        f.write("\n".join(yolo_lines))

print("✅ Conversion completed successfully!")
print(f"Labels saved in: {OUTPUT_LABEL_FOLDER}")