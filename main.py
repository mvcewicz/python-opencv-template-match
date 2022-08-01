import cv2
import numpy as np

template = cv2.imread('template.jpeg', 0)
img = cv2.imread('img.png', 0)
img1 = cv2.imread('img1.png', 0)
img2 = cv2.imread('img2.png', 0)

match = cv2.matchTemplate(img, template, 5)  # element of template
match_1 = cv2.matchTemplate(img1, template, 5)  # element of template
not_match = cv2.matchTemplate(img2, template, 5)  # not element of template

print(img)
print(img1)
print(img2)

threshold = 0.5

is_matched = np.array(np.where(match > threshold)).shape[1] > 0
is_matched_1 = np.array(np.where(match_1 > threshold)).shape[1] > 0
is_matched_2 = np.array(np.where(not_match > threshold)).shape[1] > 0

print(f"Matched img: {is_matched}")
print(f"Matched img1: {is_matched_1}")
print(f"Not matched img2: {is_matched_2}")
