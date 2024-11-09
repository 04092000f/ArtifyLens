# Enter your code here
import cv2
import numpy as np

points = []
frame = []
frameHSV = []
trackTolerance = 0
trackSoftness = 0
trackDefringe = 50
isColor = False
isBackground = False

def setColor(action, x, y, flags, userdata):
    global points, isColor, frameHSV, pixelColorHSV
    
    if action == cv2.EVENT_LBUTTONDOWN and not isColor:
        isColor = True
        points = (x,y)
        pixelColorHSV = tuple(frameHSV[y,x,:])
        newImage = removeBackground()
        newImage = addAnnotation(newImage)
        cv2.imshow(windowName, newImage)

def removeBackground():
    global trackTolerance, trackSoftness, trackDefringe, isBackground, frame, frameHSV, bg
    
    # Modify brightness of green channel (Defringe)
    B, G, R = cv2.split(frame)
    brightnessOffset = 2 * trackDefringe - 100
    
    # Apply defringing effect primarily to the green channel
    gModified = np.uint8(np.clip((np.int32(G) + np.ones_like(G, dtype="int32") * brightnessOffset), 0, 255))
    
    # Merge modified green channel with original blue and red channels
    frameModified = cv2.merge((B, gModified, R))
    frameModifiedHSV = cv2.cvtColor(frameModified, cv2.COLOR_BGR2HSV)
    
    # Remove color background in the Hue channel (Tolerance)
    hMod, sMod, vMod = cv2.split(frameModifiedHSV)
    colorValue = pixelColorHSV[0]
    upperH = np.array(np.clip(colorValue + trackTolerance, 0, 180), dtype="uint8")
    lowerH = np.array(np.clip(colorValue - trackTolerance, 0, 180), dtype="uint8")
    mask = cv2.inRange(hMod, lowerH, upperH)
    mask = 255 - mask
    
    # Apply Gaussian blur for softness
    if trackSoftness > 0:
        maskBlur = cv2.blur(mask, (10*trackSoftness, 10*trackSoftness), (-1,-1))
        maskBlur = np.uint8(np.round((maskBlur/255.0)*(mask/255.0)*255))
    else:
        maskBlur = mask
    
    # Apply mask to modify brightness of V channel
    newV = np.uint8(np.round((vMod/255.0 * maskBlur/255.0) * 255))
    imageWithoutBg = cv2.merge((hMod, sMod, newV))
    imageWithoutBg = cv2.cvtColor(imageWithoutBg, cv2.COLOR_HSV2BGR)
    
    # Resize background image
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    resized_bg = cv2.resize(bg, (frame_width, frame_height))
    
    # Add background
    if isBackground:
        maskInv = 255 - mask
        maskInv3Ch = np.ones_like(resized_bg)
        for i in range(3):
            maskInv3Ch[:,:,i] = maskInv
        bgCut = np.uint8(np.round((resized_bg/255.0) * (maskInv3Ch/255.0) * 255))
        imageWithNewBg = cv2.add(imageWithoutBg, bgCut)
        output = imageWithNewBg
    else:
        output = imageWithoutBg
    return output



def getParameter(*args):
    global trackTolerance, trackSoftness, trackDefringe
    
    trackTolerance = cv2.getTrackbarPos("Tolerance", windowName)
    trackSoftness = cv2.getTrackbarPos("Softness", windowName)
    trackDefringe = cv2.getTrackbarPos("Defringe", windowName)
    
    if isColor:
        newImage = removeBackground()
        newImage = addAnnotation(newImage)
        cv2.imshow(windowName, newImage)

def activateBackground(*args):
    global isBackground
    
    if isColor:
        isBackground = cv2.getTrackbarPos("Background", windowName)
        newImage = removeBackground()
        newImage = addAnnotation(newImage)
        cv2.imshow(windowName, newImage)

def addAnnotation(image):
    imageCopied = image.copy()
    cv2.putText(imageCopied, "Click to remove green scene", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,255,255), 4)
    cv2.putText(imageCopied, "esc: exit", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,255,255), 4)
    cv2.putText(imageCopied, "s: save video", (10, 130), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,255,255), 4)
    return imageCopied

def saveVideo(*args):
    global cap, frame, frameHSV
    
    if cap.isOpened():
        fps = round(cap.get(cv2.CAP_PROP_FPS))
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        numberFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        ret = cap.set(cv2.CAP_PROP_POS_FRAMES,0)
        out = cv2.VideoWriter("output.mp4", cv2.VideoWriter_fourcc('M','J','P','G'), fps, (frame_width,frame_height))
        print("VideoWriter started")
        
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret:
                frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                frameBg = removeBackground()
                out.write(frameBg)
                frameBg = addAnnotation(frameBg)  # Use addAnnotation here
                cv2.imshow(windowName, frameBg)
                k = cv2.waitKey(10)
                if k == ord('a'):
                    frameBg = removeBackground()
                    frameBg = addAnnotationAborted(frameBg)
                    cv2.imshow(windowName, frameBg)
                    print("VideoWriter aborted")
                    break
            else:
                break
        frameBg = removeBackground()
        frameBg = addAnnotationFinished(frameBg)
        cv2.imshow(windowName, frameBg)        
        print("VideoWriter finished")
        out.release()


# Read video and background
cap = cv2.VideoCapture("greenscreen-demo.mp4")
bg = cv2.imread("background.jpg", cv2.IMREAD_COLOR)

# Check for video and background
if not cap.isOpened():
    print("Error opening video!")
elif bg is None:
    print("Error opening background!")
else:
    print("Video and background loaded successfully!")

# Read frame
_, frame = cap.read()
frameCopied = addAnnotation(frame)

# Get frame height/width
frameHeight, frameWidth = frame.shape[:2]

# Create window
windowName = "Display Frame"
cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
cv2.imshow(windowName, frameCopied)
cv2.resizeWindow(windowName, frameWidth, frameHeight)

frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
cv2.setMouseCallback(windowName, setColor)

cv2.createTrackbar("Tolerance", windowName, 0, 100, getParameter)
cv2.createTrackbar("Softness", windowName, 0, 100, getParameter)
cv2.createTrackbar("Defringe", windowName, 50, 100, getParameter)
cv2.createTrackbar("Background", windowName, 0, 1, activateBackground)

# Main loop
k = 0
while k != 27:
    k = cv2.waitKey(20) & 0xFF
    if k == ord('s'):
        saveVideo()

cap.release()
cv2.destroyAllWindows()