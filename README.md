# Image Recognition System (Flask + OpenCV + YOLO)

A lightweight Flask web application for real-time object detection using the YOLOv8 model from Ultralytics.  
Users can upload an image, and the app will detect objects, annotate the image, and display the results in the browser.

## Features
- Simple web interface for uploading images
- YOLOv8 nano model for fast detection
- Bounding boxes with labels and confidence scores
- Lightweight dependencies for easier deployment

## Demo Flow
1. Upload an image via the web form.
2. YOLOv8 detects objects and draws bounding boxes.
3. Annotated image and detection results are displayed.

---

## Installation

### 1️⃣  Install dependencies
Create a virtual environment (recommended):
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows

Install required packages:
pip install -r requirements.txt


### Usage
To use:
### 1️⃣ Run the Flask app: python app.py
OR
### 2️⃣ Open in browser: http://127.0.0.1:5000

### Requirements
Minimal dependencies for quick deployment:
flask==3.0.3
ultralytics==8.0.196
opencv-python-headless==4.8.1.78

### Folder Structure
```
📂 project/
 ├── app.py              # Main Flask app
 ├── requirements.txt    # Dependencies
 ├── templates/
 │    ├── index.html     # Upload form
 │    └── result.html    # Results display
 ├── static/
 |    ├──css/
 │    |    ├── style.css    
 │    |    └── result.css 
 │    └── uploads/       # Uploaded + annotated images
```
### Model
Default model: yolov8n.pt (YOLOv8 nano, pretrained on COCO dataset)

You can replace with other YOLOv8 variants (yolov8s, yolov8m, etc.) for higher accuracy at the cost of speed.
