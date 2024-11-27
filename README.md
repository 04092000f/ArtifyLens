# ArtifyLens

ArtifyLens is a project that has implemented some parts of a selfie app. Mainly three features have been implemented:

## Feature 1: Instagram Filters

For the first feature, we have designed 2 instagram-like filters.

### 1. **Pencil Sketch Filter** - This will generate a sketch of the given image as shown in the output below.
#### How it Works:
- **Grayscale Conversion**: The image is first converted to <code>grayscale</code>, which removes all color and simplifies the image.
- **Image Inversion**: The <code>grayscale</code> image is <code>inverted</code>, creating a negative image that contrasts strongly with the original.
- **Gaussian Blur**: <code>Gaussian blur</code> is applied to the inverted image to smooth out the details.
- **Sketch Creation**: Finally, the original <code>grayscale</code> image is divided by the <code>blurred negative</code> image to create a <code>pencil sketch</code> effect.

### 2. **Cartoon Filter** - This should produce a cartoonified output of the input image.
#### How it Works:
- **Grayscale Conversion**: The image is first converted to <code>grayscale</code> to focus on the structure.
- **Median Blur**: <code>Median blur</code> is applied to reduce noise and smooth the image.
- **Edge Detection**: <code>Adaptive thresholding</code> is used to detect the edges, which are then highlighted in black to form the cartoon outlines.
- **Bilateral Filtering**: <code>Bilateral filter</code> is used to reduce the color palette of the image while preserving edges, creating the smooth, flat colors seen in cartoons.
- **Combination**: The color-reduced image is combined with the detected edges to produce the <code>cartoonified</code> effect.

  #### The final output is given below

| **Original Image** | **Cartoonified Image** | **Pencil Sketch** |
|--------------------|------------------------|-------------------|
| ![Original Image](https://github.com/04092000f/Selfie-app/blob/main/trump.jpg) | ![Cartoonified Image](https://github.com/04092000f/Selfie-app/blob/main/cartoon.jpg) | ![Pencil Sketch](https://github.com/04092000f/Selfie-app/blob/main/sketch.png) |

### Feature 2: Blemish Removal

This feature involves the development of a <code>blemish removal</code> tool that processes images to remove <code>blemishes</code> or <code>imperfections</code> from facial or object surfaces.

#### How it Works:

- **Initial Setup:**
    - The image (e.g., <code>blemish.png</code>) is loaded into the program.

- **User Clicks on a Blemish:**
    - When the user clicks on a blemish in the image, the program automatically selects a patch from the surrounding area based on the smallest gradient and blends it onto the blemish location.

- **Viewing the Result:**
    - The user immediately sees the modified image with the blemish removed, and they can continue clicking on other blemishes to remove them.
 
- **Saving the Image:**
    - After editing, the user presses the <code>S</code> key to save the modified image as <code>blemish_removed.png</code>.
 

- **Resetting or Exiting:**
    - The user can press <code>R</code> to reset the image to its original form or <code>ESC</code> to exit the program.

#### The final output is given below

| **Original Image** | **After Blemish Removal** |
|--------------------|--------------------------|
| ![Original Image](https://github.com/04092000f/Selfie-app/blob/main/blemish.png) | ![Blemish Removal](https://github.com/04092000f/Selfie-app/blob/main/blemish_removed.png) |

### Feature 3: Chroma Keying

This feature involves the use of <code>chroma keying</code> (also known as <code>green screen</code> or <code>blue screen</code>) to remove a <code>solid-colored</code> background from images or videos and mask it with another background.

#### How it Works

- **Chroma Keying (Green Screen Removal):**
    - The program removes a <code>green</code> background from a video and mask it with a new background image.
 
      
- **Interactive Parameters:**
  - The user can adjust:
    - **Tolerance:** Controls the range of <code>green</code> hues to be removed.
    - **Softness:** Controls how <code>smooth</code> the edges of the removed green area will be.
    - **Defringe:** Adjusts the <code>brightness</code> of the green channel to remove <code>fringes</code> around the edges of the object.

- **Background Masking:**
    - Foreground image is masked behind the new background once the green background is removed.
 
- **Mouse Click Color Selection:**
  - Users can click on the green area of the video to select the exact color to be removed. The selected color is used as a reference for removing the green background.
 
- **Real-time Video Processing:**
  - The video is processed frame by frame, and the green background is removed with the selected parameters.
  
- **Video Saving:**
  - After applying the effect, the user can save the processed video as <code>output.mp4</code>.
    
- **Annotations:**
  - Text annotations are added to the video for user guidance in <code>submission_chroma.py</code>.

#### The final output is given below:
| **Original Video** | **After Chroma Keying** |
|--------------------|-------------------------|
| ![Original](https://github.com/04092000f/Selfie-app/blob/main/greenscreen-demo.gif) | ![Chroma](https://github.com/04092000f/Selfie-app/blob/main/output.gif) |
