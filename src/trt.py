#!/home/wyw/anaconda3/envs/YOLOV7_ROS/bin/python3

from utils.utils import preproc, vis
from utils.utils import BaseEngine
import os
import rospy
import numpy as np
os.environ["OPENCV_IO_ENABLE_OPENEXR"]="1"
import cv2
import time
import os
import argparse
import pycuda.driver as cuda
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import ros_numpy

import rospy
cuda.init()
device = cuda.Device(0)
ctx = device.make_context()
class Predictor(BaseEngine):
    def __init__(self, engine_path):
        super(Predictor, self).__init__(engine_path)
        self.n_classes = 80  # your model classes


class detect():

    def __init__(self):

        self.w = 0
        self.bridge = CvBridge()
        self.h = 0

        self.classify = False
        self.pred = Predictor(engine_path='/home/wyw/yolov8_ros_tensorrt/src/yolov8l.trt')

        self.pub_detect_result_yolov8 = rospy.Publisher("yolov8_detect_result", Image, queue_size=10000)
        self.image_sub = rospy.Subscriber("/camera/color/image_raw", Image, self.camera_callback,
                                          queue_size=1,buff_size=52428800)  # "/camera_fr/image_raw"
        rospy.spin()

    def camera_callback(self, data):
        try:
            # self.img = ros_numpy.numpify(data)
            self.img = self.bridge.imgmsg_to_cv2(data, "rgb8")
            # print("image is read from subscriber and shape is :", np.shape(self.img)) #(1544, 2048) numpy
            # self.cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")

        except CvBridgeError as e:
            print("something is wrong with camera_callback function")

        img0 = self.img
        img0 = cv2.resize(img0, (640, 640))
        ctx.push()

        origin_img = self.pred.inference(img0)
        origin_img = cv2.resize(origin_img, (640, 480))
        ctx.pop()
        self.pub_detect_result_yolov8.publish(self.bridge.cv2_to_imgmsg(origin_img, "rgb8"))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--engine", default="/home/wyw/TensorRT-For-YOLO-Series/yolov8l.trt",help="TRT engine Path")
    parser.add_argument("-i", "--image",help="image path")
    parser.add_argument("-o", "--output", help="image output path")
    parser.add_argument("-v", "--video", default="src/video1.mp4", help="video path or camera index ")
    parser.add_argument("--end2end", default=True, action="store_true",
                        help="use end2end engine")
#python trt.py -e yolov8n.trt  -i src/1.jpg -o yolov8n-1.jpg --end2end,default="/home/wyw/yolov7/figure/horses_prediction.jpg",
    args = parser.parse_args()
    print(args)
    rospy.init_node('yolov8_rrt')

    detect()
    # pred.get_fps()
    img_path = args.image
    video = args.video
    # if img_path:
    #   origin_img = pred.inference(img_path)
    #
    #   cv2.imwrite("%s" %args.output , origin_img)
    # if video:
    #   pred.detect_video(video, conf=0.1, end2end=args.end2end) # set 0 use a webcam
