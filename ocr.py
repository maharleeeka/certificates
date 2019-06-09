from PIL import Image
import time, cv2, pytesseract, re
    
def extractObjects():
    with open('coordinates.txt') as f:
        lines = f.readlines()
        return lines
        
def preprocessInputImage(filename, ctr):
    print("preprocessing ", ctr, " ...")
    c = str(ctr)
    
    input_image = cv2.imread(filename)

    # denoised
    input_image = cv2.fastNlMeansDenoisingColored(input_image,None,5,5,7,21)
    # cv2.imwrite(IMAGES_PATH + "remove_noise_"+ c + ".png", input_image)

    # change image to grayscale
    input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    # cv2.imwrite(IMAGES_PATH + "grayscaled_"+ c + ".png", input_image)

    # adaptive thresholding with otsu binarization
    ret, input_image = cv2.threshold(input_image,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imwrite(IMAGES_PATH + "thres_" + c + ".png", input_image)

def crop_new_object_images(path):
    print("cropping new images...")
    objects_detected = extractObjects()

    img = Image.open(path)

    i = 0
    
    file = open("OCR/final-result-text.txt","w", encoding='utf8')
    file.write('')
    file.close()

    
    while i < len(objects_detected):
        object_info = objects_detected[i].split("-")
        x1 = (int(float(object_info[1])))
        y1 = (int(float(object_info[2])))
        x2 = x1 +  int(float(object_info[3]))
        y2 = y1 +  int(float(object_info[4]))

        cropped_img = img.crop((x1,y1,x2,y2))

        new_img_path = PATH + "new/obj_detected_" + str(i) + ".jpg"

        cropped_img.save(new_img_path)

        width, height = cropped_img.size
        if (width < 500 or height < 500):
                width = width * 3
                height = height * 3
                
                cropped_img = cropped_img.resize((width, height), Image.ANTIALIAS)
                cropped_img.save(new_img_path)

        preprocessInputImage(new_img_path,i)
        
        result = characterRecognition(object_info[0], i)
        file = open(PATH + "OCR/final-result-text.txt", "a", encoding='utf8')
        file.write(result)
        file.write("\n")
        file.close()

        i += 1
    
    print("- DONE READING -")

def characterRecognition(type, ctr):
    print("tesseract...")
    result = pytesseract.image_to_string(Image.open(IMAGES_PATH + "thres_" + str(ctr) + ".png"), config='--psm 6')
    
    result = re.sub('[^0-9a-zA-Z]+', ' ', result)
    
    print(type.upper() + " - " + result)
    print('\n')
    return (type.upper() + " - " + result)


PATH = "C:/Users/Acer/Documents/Thesis/YOLO/windows-darknet/darknet/build/darknet/x64/"
IMAGES_PATH = PATH + "OCR/prep-images/"

test_image = input("test image path: ")

start_time = time.time()
crop_new_object_images(test_image)
end_time = time.time()
print("wall time: ", end_time - start_time)
