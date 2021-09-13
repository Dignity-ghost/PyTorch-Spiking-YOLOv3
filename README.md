# PyTorch-Spiking-YOLOv3
A modified repository based on PyTorch-Spiking-YOLOv3([cwq159/PyTorch-Spiking-YOLOv3](https://github.com/cwq159/PyTorch-Spiking-YOLOv3)) and YOLOv3([ultralytics/yolov3](https://github.com/ultralytics/yolov3)), which make it suitable for VOC-dataset. There is no extra contribution, and thanks for the two authors above.

## Introduction
For spiking implementation, some operators in YOLOv2-Tiny have been converted equivalently. Please refer to yolov3-tiny-ours(\*).cfg in /cfg for details.
### Conversion of some operators
+ 'maxpool(stride=2)'->'convolutional(stride=2)'
+ 'maxpool(stride=1)'->'none'
+ 'leaky_relu'->'relu'
+ 'batch_normalization'->'fuse_conv_and_bn'

## Usage
Please refer to [ultralytics/yolov3](https://github.com/ultralytics/yolov3) for the basic usage for training, evaluation and inference. The main advantage of PyTorch-Spiking-YOLOv3 is the transformation from ANN to SNN.
### Train
```
$ python3 train.py --batch-size 32 --cfg cfg/yolov3-tiny-ours.cfg --data data/coco.data --weights ''
```
### Test
```
$ python3 test.py --cfg cfg/yolov3-tiny-ours.cfg --data data/coco.data --weights weights/best.pt --batch-size 32 --img-size 640
```
### Detect
```
$ python3 detect.py --cfg cfg/yolov3-tiny-ours.cfg --weights weights/best.pt --img-size 640
```
### Transform
```
$ python3 ann_to_snn.py --cfg cfg/yolov3-tiny-ours.cfg --data data/coco.data --weights weights/best.pt --timesteps 128
```
For higher accuracy(mAP), you can try to adjust some hyperparameters.

*Trick: the larger timesteps, the higher accuracy.*
