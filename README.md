# Hide-and-Seek (HaS)
Code for the [Hide-and-Seek: Forcing a Network to be Meticulous for Weakly-supervised Object and Action Localization, ICCV 2017]
Krishna Kumar Singh, Yong Jae Lee
(http://krsingh.cs.ucdavis.edu/krishna_files/papers/hide_and_seek/hide_seek.html)

If you use our work, please cite:
```bibtex
@inproceedings{singh-iccv2017,
  title = {Hide-and-Seek: Forcing a Network to be Meticulous for Weakly-supervised Object and Action Localization},
  author = {Krishna Kumar Singh and Yong Jae Lee},
  booktitle = {International Conference on Computer Vision (ICCV)},
  year = {2017}
}
```

## Pre-requisites
1. Torch (http://torch.ch/docs/getting-started.html)
2. For training use the code https://github.com/soumith/imagenet-multiGPU.torch
3. For the visualization and generating Class Activation Maps(CAM) use the code https://github.com/metalbubble/CAM

## Training
1. Please download `train.lua` and `opts.lua` and replace it in  https://github.com/soumith/imagenet-multiGPU.torch
2. The new code has two additional arguments `patchSize` and `hideProb`. `patchSize` decides the size of the patch to be hidden. For example to hide the patches of size 32 give argument `-patchSize 32`. Multiple patch sizes can be provided seperated by comma, for example `-patchSize 0,16,32,44,56`. Here, `0` indicates no patch will be hidden. `hideProb` indicates by what probability patches will be hidden. For example to hide patches with `50%` probability give the argument `-hideProb 0.5`.

## Pre-trained Models
1. AlexNet-HaS-Mixed: https://drive.google.com/open?id=1QIrXJV5Sw0eYyXjauW6SlxkQXe3uDnmL
2. GoogLeNet-HaS-32: https://drive.google.com/open?id=1N3zgRmD0trCMfYOw1vo_DbesW4Ug7qx5
3. Please subtract mean and divide by standard deviation (`meanstdCache.t7`). For class ordering refer `classes.t7`.

## Hide-and-Seek (Data Augmentation)
If you need to hide the image patches for data augmentation, please refer the code `hide_patch.py`.


## Results

|            Method             | No HaS | HaS | Boost |
| :---------------------------: | :-----: | :-------: | :---------: |
|Weakly-supervised object localization| 54.90| 58.75| **+3.85** |
|Weakly-supervised semantic seg| 60.80 | 61.45 | **+0.65** |
|Weakly-supervised action localization| 34.23  |  36.44 | **+2.21**|
|Image classification|   76.15 | 77.20 | **+1.05** |
|Semantic segmentation|   48.00 |  49.31 | **+1.31** |
|Emotion recognition|  93.65 | 94.88 | **+1.23** |
|Person re-identification| 71.60 | 72.80 | **+1.20** |\\	
 
## Visualization of AlextNet-HaS for object localization:
[Click Here](http://vision3.idav.ucdavis.edu:8080/)
## Contact
Please contact krsingh@ucdavis.edu for any questions.     
