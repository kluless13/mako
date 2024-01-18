from ultralytics import YOLO
from kybra import query, update, void

path: str = ''

@query
def model(MODEL) -> str:
    MODEL = YOLO('yolov8n.pt')
    return model

@update
def run_model(results) -> void:
    global model
    