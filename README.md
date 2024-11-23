# Selfie App

In this Project, some parts of a selfie app have been implemented. particularly implemented three features have been implemented:

## Feature 1: Instagram Filters

For the first feature, we have designed 2 instagram-like filters.

### 1. **Pencil Sketch Filter** - This will generate a sketch of the given image as shown in the output below.
#### How it Works:
- **Grayscale Conversion**: The image is first converted to grayscale, which removes all color and simplifies the image.
- **Image Inversion**: The grayscale image is inverted, creating a negative image that contrasts strongly with the original.
- **Gaussian Blur**: A Gaussian blur is applied to the inverted image to smooth out the details.
- **Sketch Creation**: Finally, the original grayscale image is divided by the blurred negative image to create a pencil sketch effect.

### 2. **Cartoon Filter** - This should produce a cartoonified output of the input image.
#### How it Works:
- **Grayscale Conversion**: The image is first converted to grayscale to focus on the structure.
- **Median Blur**: A median blur is applied to reduce noise and smooth the image.
- **Edge Detection**: Adaptive thresholding is used to detect the edges, which are then highlighted in black to form the cartoon outlines.
- **Bilateral Filtering**: A bilateral filter is used to reduce the color palette of the image while preserving edges, creating the smooth, flat colors seen in cartoons.
- **Combination**: The color-reduced image is combined with the detected edges to produce the cartoonified effect.

| **Original Image** | **Cartoonified Image** | **Pencil Sketch** |
|--------------------|------------------------|-------------------|
| ![Original Image](https://github.com/04092000f/Selfie-app/blob/main/trump.jpg) | ![Cartoonified Image](https://github.com/04092000f/Selfie-app/blob/main/cartoon.jpg) | ![Pencil Sketch](https://github.com/04092000f/Selfie-app/blob/main/sketch.png) |

### Feature 2: Blemish Removal

This feature involves the development of a blemish removal tool that processes images to remove blemishes or imperfections from facial or object surfaces.

#### How it Works:

- **Initial Setup:**
    - The image (e.g., blemish.png) is loaded into the program.

- **User Clicks on a Blemish:**
    - When the user clicks on a blemish in the image, the program automatically selects a patch from the surrounding area based on the smallest gradient and blends it onto the blemish location.

- **Viewing the Result:**
    - The user immediately sees the modified image with the blemish removed, and they can continue clicking on other blemishes to remove them.
 
- **Saving the Image:**
    - After editing, the user presses the S key to save the modified image as blemish_removed.png.
 

- **Resetting or Exiting:**
    - The user can press R to reset the image to its original form or ESC to exit the program.


| **Original Image** | **After Blemish Removal** |
|--------------------|--------------------------|
| ![Original Image](https://github.com/04092000f/Selfie-app/blob/main/blemish.png) | ![Blemish Removal](https://github.com/04092000f/Selfie-app/blob/main/blemish_removed.png) |

### Feature 3: Chroma Keying

This feature involves the use of chroma keying (also known as "green screen" or "blue screen") to remove a solid-colored background from images or videos and replace it with another background.

#### How it Works

- **Chroma Keying (Green Screen Removal):**
    - The program removes a green background from a video and replaces it with a new background image.
 
      
- **Interactive Parameters:**
  - The user can adjust:
    - **Tolerance:** Controls the range of green hues to be removed.
    - **Softness:** Controls how smooth the edges of the removed green area will be.
    - **Defringe:** Adjusts the brightness of the green channel to remove fringes around the edges of the object.

- **Background Replacement:**
    - A new background image is added behind the foreground once the green background is removed.
 
- **Mouse Click Color Selection:**
  - Users can click on the green area of the video to select the exact color to be removed. The selected color is used as a reference for removing the green background.
 
- **Real-time Video Processing:**
  - The video is processed frame by frame, and the green background is removed with the selected parameters.
  
- **Video Saving:**
  - After applying the effect, the user can save the processed video as output.mp4.
    
- **Annotations:**
  - Text annotations are added to the video for user guidance.

| **Original Video** | **After Chroma Keying** |
|--------------------|-------------------------|
| ![Original](https://github.com/04092000f/Selfie-app/blob/main/greenscreen-demo.gif) | ![Chroma](https://github.com/04092000f/Selfie-app/blob/main/output.gif) |
