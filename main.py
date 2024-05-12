# Dependencies
import cv2
import torch
import matplotlib.pyplot as plt
import numpy as np
import os

# Midas
midas = torch.hub.load('intel-isl/MiDaS','MiDaS_small')
midas.to('cpu')
midas.eval()

# Transform pipeline
transforms = torch.hub.load('intel-isl/MiDaS', 'transforms')
transform = transforms.small_transform
frames = []
# Images
folder_path = './images'
images = []
for filename in os.listdir(folder_path):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
        images.append(os.path.join(folder_path, filename))

for image in images:
    # Making Frames
    frame = cv2.imread(image)
    # Get the aspect ratio of the original frame
    aspect_ratio = frame.shape[1] / frame.shape[0]
    desired_height = 400
    desired_width = int(desired_height* aspect_ratio)  
    frame_resized = cv2.resize(frame, (desired_width, desired_height))

    # Transform input for midas
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    imgbatch = transform(img).to('cpu')

    # Prediction
    with torch.no_grad():
        prediction = midas(imgbatch)
        prediction = torch.nn.functional.interpolate(
            prediction.unsqueeze(1),
            size = img.shape[:2], 
            mode = 'bicubic',
            align_corners = False
        ).squeeze()

        output = prediction.cpu().numpy()

        print(output)

    output = output.max() - output
    # Normalize the depth values to a suitable range, e.g., 0 to 1
    min_depth = np.min(output)
    max_depth = np.max(output)
    depth_range = max_depth - min_depth
    output_normalized = (output - min_depth) / depth_range

    cv2.imshow('CV2Frame',frame_resized)
    plt.imshow(output_normalized, cmap='viridis')
    plt.colorbar(label='Depth in relative units')  
    plt.title('Depth Map')
    plt.axis('off')
    plt.show()