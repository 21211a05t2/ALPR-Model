from ultralytics import YOLO


model = YOLO("yolov8n.yaml")

results = model.train(data="comfig.yaml", epochs=10) 
