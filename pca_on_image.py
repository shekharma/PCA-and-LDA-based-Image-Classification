import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from PIL import Image

# Load the image
image_path =  "C:/Users/Administrator/Downloads/cat.png"  # Replace with your image file path
image = Image.open(image_path)

# Convert the image to a numpy array
image_array = np.array(image)

# Reshape the image array to have each row represent a sample
# and each column represent a feature
height, width, num_channels = image_array.shape
flattened_image = image_array.reshape(-1, num_channels)

# Apply PCA
n_components = min(height, width, num_channels) - 1  
pca = PCA(n_components=n_components)
pca.fit(flattened_image)

# Reconstruct the image using the principal components
reconstructed_image = pca.inverse_transform(pca.transform(flattened_image))
reconstructed_image = reconstructed_image.reshape(height, width, num_channels)

# Plot the original and reconstructed images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image_array.astype(np.uint8))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Reconstructed Image')
plt.imshow(reconstructed_image.astype(np.uint8))
plt.axis('off')

plt.show()
