import cv2
import numpy as np

def detect_reference_object(image=None, image_file='webcam.png', folder='./upload_data/', 
    shoulder_left=None, shoulder_right=None):
    
    if image is None:
        image = cv2.imread(folder+image_file)
        image = cv2.resize(image, (224, 224))
    image2 = image.copy()
    [r, c, pix] = image.shape
    for x in range(r):
        for y in range(c):
            image2[x][y][0] = 0
            image2[x][y][2] = 0
            image2[x][y][1] = 255 if image2[x][y][1] == 255 else 0
    ret, thresh_gray = cv2.threshold(cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY), 
        100, 255, cv2.THRESH_BINARY)
    # find contours in the edged image, keep only the largest
    ## Step #1 - Detect contours using both methods on the same image
    contours, _ = cv2.findContours(thresh_gray.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(image, [box], 0, (255, 0, 0),1)
    # Find the index of the largest contour
    areas = [cv2.contourArea(c) for c in contours]
    max_index = np.argmax(areas)
    cnt=contours[max_index]
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(image,(x,y),(x+w,y+h),(255, 0, 0),2)
    if shoulder_left is not None:
        [row, col] = shoulder_left
        cv2.circle(image,(row, col), 3, (255, 255, 0), -1)
    if shoulder_right is not None:
        [row, col] = shoulder_right
        cv2.circle(image,(row, col), 3, (255, 255, 0), -1)
    cv2.imwrite(folder + image_file.replace('.png','_box.png'), image)
    print([shoulder_left, shoulder_right])
    if shoulder_left is not None and shoulder_right is not None:
        [x1, y1] = shoulder_left
        [x2, y2] = shoulder_right
        dis = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
        print( ['distance', dis, w] )
        return dis*7.4/w
    else:
        return 60

if __name__ == "__main__":
    detect_reference_object(image_file='webcam2.png')
