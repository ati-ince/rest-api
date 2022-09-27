import cv2 
import pytesseract

img = cv2.imread('images\\fish-chips-1_en-US.PNG')

# Adding custom options
custom_config = r'--oem 3 --psm 6'
txt = pytesseract.image_to_string(img, config=custom_config)
print(f'out: {txt}')