# object detection on certificates

1. Set up YOLO with this repository -> https://github.com/AlexeyAB/darknet
2. Put `objectDetector.py` and `ocr.py` inside `x64` folder
3. Make a folder named `validation` and put `sequenceMatcher.py` inside


about each file

### objectDetector.py
  - for object detection
  - asks used to input the path of the image to test
  - you can change the `command` value depending on your need
    - `darknet_no_gput.exe` for windows with no gpu
    - `darknet.exe` for windows with gpu

### ocr.py
  - for text recognition
  - asks user to input the path of the image to test (the same path you used for object detection)
  - change `PATH` and `IMAGES_PATH` values
    - `PATH` = whole path for the `x64` folder
    - `IMAGES_PATH` = you can make another folder inside `x64` to put all preprocessed images and final results`
    - line 64 is where you save the final result, please change the path in accordance to what you have
  - if you want to save denoised and grayscaled images, uncomment lines no. 17 and 21

### sequenceMatcher.py
 - this code was used to test the 30 text recognition results (results are in text file  for each image) in bulk
 - sample test filenames are `TEST_1.txt`, `TEST_2.txt`, TEST_30.txt`
 - depending on how many text files you want to test, you can change the 
  - `i` value in line 7 = which file to start
  - `while (i <= __):` in line 9 = in the blank, change the number to until which file you want to stop testing
 - inside a test file are the class name (in number), original text, and actual result separated by the character `|`, a newline for each class

    
---
- `yolo-obj.cfg` and `data` folder were used for training the detector
- YOLO weights are available in https://bit.ly/2XA0fnW
