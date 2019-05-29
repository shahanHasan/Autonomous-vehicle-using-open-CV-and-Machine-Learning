import cv2
import numpy as np
import matplotlib.pyplot as plt

class lanes:

    def __init__(self,img):
        self.img=img

    def _getimg(self):
        image = self.img
        lane_image = np.copy(image)
        return lane_image

    def _lane_image_load(self):
        #read and write image
        #img = 'test_image.jpg'
        image = self.img
        lane_image = np.copy(image)
        return image

    def _canny(self):
        #edge detection
        #step 1 : gray scale
        lane_image = lanes._lane_image_load(self)
        gray = cv2.cvtColor(lane_image,cv2.COLOR_RGB2GRAY)
        #step 2 : reduce image noise (false edges) and smoothen lane_image
        # gaussian filter
        blur = cv2.GaussianBlur(gray, (5,5),0)
        #step 3 Canny method
        canny = cv2.Canny(blur,50,150)
        return canny

    def _region_of_interest(self):
        image = lanes._canny(self)
        height = image.shape[0]
        polygons = np.array([
        [(200,height),(1100,height),(550,250)]
        ])
        mask = np.zeros_like(image)
        cv2.fillPoly(mask, polygons , 255)
        masked_image = cv2.bitwise_and(image,mask)
        return masked_image

    def identifying_polygon():
        lane = lanes('test_image.jpg')
        plt.imshow(lane._canny())
        plt.show()

    def _make_coordinates(image,line):
        slope , intercept = line
        y1 = int(image.shape[0]) #bottom of the image
        y2 = int(y1*3/5) # slightly lower than the middle
        x1 = int((y1 - intercept)/slope)
        x2 = int((y2 - intercept)/slope)
        return [[x1,y1,x2,y2]]

    def _houghlines(self):
        #hough  transform method to detect lanes
        image = lanes._region_of_interest(self)
        lines = cv2.HoughLinesP(image, 2,np.pi/180,100,np.array([]),minLineLength=40,maxLineGap=5)
        return lines

    def _average_slope_intercept(self):
        image = lanes._getimg(self)
        lines = lanes._houghlines(self)
        left_fit = []
        right_fit = []
        for line in lines:
            x1,y1,x2,y2 = line.reshape(4)
            parameters = np.polyfit((x1,x2),(y1,y2),1)
            slope = parameters[0]
            intercept = parameters[1]
            if slope < 0:
                left_fit.append((slope,intercept))
            else:
                right_fit.append((slope,intercept))
        # add more weight to longer lines
        left_fit_average = np.average(left_fit, axis = 0)
        right_fit_average= np.average(right_fit, axis = 0)
        left_line  = lanes._make_coordinates(image, left_fit_average)
        right_line = lanes._make_coordinates(image, right_fit_average)
        averaged_lines = [left_line, right_line]
        return averaged_lines


    def _display_lines(self):
        lines = lanes._average_slope_intercept(self)
        line_image = np.zeros_like(lanes._getimg(self))
        if lines is not None:
            for line in lines:
                for x1,y1,x2,y2 in line:
                    cv2.line(line_image, (x1,y1),(x2,y2),(255,0,0),10)
        return line_image

    def _combinedImage(self):
        image = lanes._getimg(self)
        line_image = lanes._display_lines(self)
        combo_image = cv2.addWeighted(image,0.8,line_image,1, 1)
        return combo_image

    def main(frame):

        lane = lanes(frame)
        image = lane._combinedImage()
        cv2.imshow('result',image)


if __name__ == '__main__':
    #lanes.identifying_polygon()
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Our operations on the frame come here
        #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # Display the resulting frame
        lanes.main(frame)
        if cv.waitKey(1) == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()

    


    # lane = lanes('test_image.jpg')
    # image1 = lane._getimg()
    # cv2.imshow('result',image1)
    # cv2.waitKey(0)
