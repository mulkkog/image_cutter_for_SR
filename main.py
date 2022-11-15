import argparse
from argparse import ArgumentParser
import numpy as np
from cv2 import cv2
import os

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-resource', type=str, default='resource')
    parser.add_argument('-result', type=str, default='result')

    args = parser.parse_args()
    image_list = os.listdir(args.resource)
    # print(image_list)

    sample_image = cv2.imread(args.resource + '/' + image_list[0], cv2.IMREAD_COLOR)
    while True:
        roi = cv2.selectROI(sample_image)
        print('roi =', roi)

        image_roi = sample_image[roi[1]:roi[1] + roi[3], roi[0]:roi[0] + roi[2]]
        cv2.imshow('selected', image_roi)
        key = cv2.waitKey(0)

        if key == 114:  # r: retry
            cv2.destroyWindow("selected")
        if key == 103:  # g: go!,,.
            cv2.destroyAllWindows()
            break

    for image in image_list:
        current_img = cv2.imread(args.resource + '/' + image, cv2.IMREAD_COLOR)
        current_img_roi = current_img[roi[1]:roi[1] + roi[3], roi[0]:roi[0] + roi[2]]
        cv2.imwrite(args.result + '/cropped_' + image, current_img_roi)


