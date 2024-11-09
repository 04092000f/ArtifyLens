# Enter your code here
"""
Keybindings:

S: Save the Image
R: Reset the Image
ESC: Exit the App

"""
import cv2
import numpy as np

def blemish_removal(image_path, blemish_radius):
    # Load the image
    image = cv2.imread(image_path)
    clone = image.copy()
    dummy = image.copy()

    def mouse_callback(event, x, y, flags, param):
        nonlocal clone

        if event == cv2.EVENT_LBUTTONDOWN:
            blemish_center = (x, y)
            new_patch_center = select_best_patch(x, y, blemish_radius)
            if new_patch_center:
                new_patch = clone[new_patch_center[1]-blemish_radius:new_patch_center[1]+blemish_radius,
                                  new_patch_center[0]-blemish_radius:new_patch_center[0]+blemish_radius]
                mask = 255 * np.ones(new_patch.shape, new_patch.dtype)
                clone = cv2.seamlessClone(new_patch, clone, mask, blemish_center, cv2.NORMAL_CLONE)
                cv2.imshow('Blemish Removal', clone)

    def select_best_patch(x, y, radius):
        patches = []
        for i in range(-radius, radius+1):
            for j in range(-radius, radius+1):
                if i == 0 and j == 0:
                    continue
                new_x, new_y = x + i, y + j
                if new_x < radius or new_x >= image.shape[1]-radius or new_y < radius or new_y >= image.shape[0]-radius:
                    continue
                patch = clone[new_y-radius:new_y+radius, new_x-radius:new_x+radius]
                gradient = np.mean(cv2.Sobel(patch, cv2.CV_64F, 1, 1))
                patches.append(((new_x, new_y), gradient))

        patches.sort(key=lambda x: x[1])
        if patches:
            return patches[0][0]
        return None

    cv2.namedWindow('Blemish Removal')
    cv2.setMouseCallback('Blemish Removal', mouse_callback)

    cv2.imshow('Blemish Removal', image)
    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):  # Save image
            cv2.imwrite('blemish_removed.png', clone)
            print('Image saved as blemish_removed.png')
        elif key == ord('r'):  # Reset blemishes
            clone = dummy.copy()
            cv2.imshow('Blemish Removal', clone)
        elif key == 27:  # Exit on ESC
            break

    cv2.destroyAllWindows()

# Function Call
blemish_removal('blemish.png', 15)
