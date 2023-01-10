from ultralytics import YOLO

model = YOLO("/home/wyw/yolov8l.pt")
model.fuse()
model.info(verbose=True)  # Print model information
# model.opset=12
model.export(format='onnx',opset=16)  # TODO: