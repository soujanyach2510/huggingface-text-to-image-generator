# Hugging Face Diffusers library
This project demonstrates how to run a **text-to-image generative AI model locally** and generate images from natural language prompts.

---

# Features

- Text-to-image generation
- Uses Stable Diffusion v1.4
- GPU acceleration with CUDA (if available)
- Automatic fallback to CPU
- Saves generated images locally
- Displays output using matplotlib

---

# How It Works

1. Load the Stable Diffusion model using Hugging Face Diffusers
2. Detect whether GPU is available
3. Generate an image from a text prompt
4. Save the generated image to disk
5. Display the image using matplotlib

---

# Example Prompt

```
A girl sitting on the beach side
```

---

# Example Output

The model generates an image based on the prompt and saves it as:

```
image_from_stable.png
```

---

# Project Structure

```
stable-diffusion-image-generator/
│
├── image_generator.py
└── README.md
```

---

# Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core language |
| PyTorch | Deep learning framework |
| Diffusers | Stable Diffusion pipeline |
| Hugging Face | Model hosting |
| Matplotlib | Image display |

---

# Installation

Clone the repository:

```
git clone https://github.com/yourusername/stable-diffusion-image-generator.git
cd stable-diffusion-image-generator
```

Install dependencies:

```
pip install torch diffusers transformers matplotlib
```

---

# Running the Application

Run the script:

```
python image_generator.py
```

The program will:

1. Load the Stable Diffusion model
2. Generate an image from the prompt
3. Save the image locally
4. Display the generated result

---

# Skills Demonstrated

This project demonstrates:

- Generative AI
- Text-to-image models
- Hugging Face Diffusers usage
- PyTorch deep learning workflows
- AI model inference pipelines

---

# Future Improvements

- Add Streamlit UI
- Allow dynamic user prompts
- Support multiple image generation
- Add style and resolution controls
- Save multiple variations
