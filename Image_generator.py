import torch
from diffusers import StableDiffusionPipeline
import matplotlib.pyplot as plt

device = 'cuda' if torch.cuda.is_available() else "cpu"

pipeline = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
pipeline = pipeline.to(device)

with torch.no_grad():
    image = pipeline("A girl sitting on the beach side").images[0]

image.save("image_from_stable.png")
plt.imshow(image)
plt.show()