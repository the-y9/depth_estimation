# Depth Estimation with MiDaS

This project performs depth estimation on a set of images using the MiDaS (Mixed Data Sampling) model.

## Dependencies

- OpenCV (`cv2`)
- PyTorch (`torch`)
- Matplotlib (`matplotlib.pyplot`)
- NumPy (`numpy`)
- OS (`os`)

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/the-y9/depth_estimation.git
   ```

2. Install dependencies:
   ```bash
   pip install torch torchvision matplotlib numpy
   ```
   or
   ```bash
   pip install -r requirements.txt
   ```

4. Run the script:
   ```bash
   python main.py
   ```

## Description

The script loads a set of images from a specified folder and performs depth estimation using the MiDaS model. It then displays the original image along with its corresponding depth map.

### Steps:

1. Load the MiDaS model.
2. Load images from the specified folder.
3. Resize each image to a desired height while maintaining the aspect ratio.
4. Transform the input image for MiDaS.
5. Perform depth prediction using MiDaS.
6. Normalize the depth values.
7. Display the original image and its depth map.

## Note 

The quality of the image and the complexity of the background can affect the accuracy of the depth estimation. For best results, use high-quality images with clear and distinct foreground objects, as these factors can impact the accuracy of depth estimation.

## Credits

- MiDaS: [GitHub Repository](https://github.com/intel-isl/MiDaS)