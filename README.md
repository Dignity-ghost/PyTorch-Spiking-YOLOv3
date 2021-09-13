# PyTorch-Spiking-YOLOv3
A modified repository based on PyTorch-Spiking-YOLOv3([cwq159/PyTorch-Spiking-YOLOv3](https://github.com/cwq159/PyTorch-Spiking-YOLOv3)) and YOLOv3([ultralytics/yolov3](https://github.com/ultralytics/yolov3)), which makes it suitable for VOC-dataset and YOLOv2. There is no extra contribution, and thanks for the two authors above. It is feasible for CNN training and testing and SNN testing.

## Dataset
VOC dataset should be the same state as PyTorch-Spiking-YOLOv3, such as:
/parent
  /dataset/VOC
  /PyTorch-Spiking-YOLOv3
Please get VOC.tar in dataset and upzip them.
Use voc_label.py in dataset (from https://pjreddie.com/media/files/voc_label.py) to generate labels.
Use rebuild_voc.py in VOC to make a new collection of VOCdatset in folder VOC.

## Introduction
For spiking implementation, some operators in YOLOv2-Tiny have been converted equivalently. Please refer to yolov3-tiny-ours(\*).cfg in /cfg for details.
### Conversion of some operators
+ 'maxpool(stride=2)'->'convolutional(stride=2)'
+ 'maxpool(stride=1)'->'none'
+ 'leaky_relu'->'relu'
+ 'batch_normalization'->'fuse_conv_and_bn'

## Usage
Please refer to [ultralytics/yolov3](https://github.com/ultralytics/yolov3) for the basic usage for training, evaluation and inference. 
### Train
```
$ python3 train.py
```
### Test
```
$ python3 test.py
```
### Detect
```
$ python3 detect.py
```
### Transform
```
$ python3 ann_to_snn.py
```
For higher accuracy(mAP), you can try to adjust some hyperparameters.

*Trick: the larger timesteps, the higher accuracy.*
