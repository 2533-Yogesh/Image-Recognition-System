from flask import Flask, request, render_template, redirect
import os
from ultralytics import YOLO
import cv2

# Flask app
app = Flask(__name__)
UPLOAD_FOLDER = os.path.join("static", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Load YOLOv8 model (pretrained on COCO dataset)
model = YOLO("yolov8n.pt")  # n = nano (fast), can use yolov8s/m/l/x for better accuracy

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        save_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(save_path)

        # Run YOLOv8 detection
        results = model(save_path)  # list of Results objects
        annotated_path = os.path.join(app.config["UPLOAD_FOLDER"], "detected_" + file.filename)

        for r in results:
            img = r.plot()  # draw boxes
            cv2.imwrite(annotated_path, img)

        # Extract detection info
        detections = []
        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                label = model.names[cls_id]
                conf = float(box.conf[0])
                detections.append({"label": label, "prob": conf})

        return render_template(
            "result.html",
            image_path=annotated_path,
            results=detections
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
