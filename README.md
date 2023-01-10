# yolov8_ros_tensorrt-
This is a YOLOv8 project based on ROS implementation, where YOLOv8 uses Tensorrt acceleration.
<img src="https://github.com/af-doom/yolov8_ros_tensorrt-/blob/main/1.jpg" width="600" height="400" alt="yolov8"/><br/>
[YOLOv8](https://v8docs.ultralytics.com/)

1.Download the converted YOLOv8 model file, modify the absolute path of the model and ROS image topic in trt.py
```python
 yolov8n.trt download 
     https://mailnankaieducn-my.sharepoint.com/:u:/g/personal/2120220505_mail_nankai_edu_cn/Ef9PE1Rcpp9Ls_wIDlj07wsB5dj_mdgHJuF1jHXtyVYbYg?e=dUBC9A
 yolov8l.trt download    
     https://mailnankaieducn-my.sharepoint.com/:u:/g/personal/2120220505_mail_nankai_edu_cn/EVgQCu4mDC9NktYibFJ6nqcBsy5PndLeNubGcWGEPQ3EVw?e=oswuQe
 ```
 
2.environment
    according to " https://github.com/Linaom1214/TensorRT-For-YOLO-Series "Configure environment
```
pip install --upgrade setuptools pip --user
pip install nvidia-pyindex
pip install --upgrade nvidia-tensorrt
pip install pycuda
```
3.rosrun 
 ```python
 rosrun yolov8_rrt trt.py
```



```bibtex
@Misc{yolotrt2022,
  author =       {Jian Lin},
  title =        {YOLOTRT: tensorrt for yolo series, nms plugin support},
  howpublished = {\url{[https://github.com/Linaom1214/TensorRT-For-YOLO-Series]}},
  year =         {2022}
}
```
