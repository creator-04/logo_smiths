from fastapi import FastAPI, UploadFile, File 
from diffusers import StableDiffusionPipeline 
import torch
from PIL import Image
import io

app = FastAPI()

# Load Stable Diffusion Model
device = "cuda" if torch.cuda.is_available() else "cpu"
model = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4").to(device)

@app.post("/generate_logo/")
async def generate_logo(prompt: str):
    image = model(prompt).images[0]
    img_bytes = io.BytesIO()
    image.save(img_bytes, format="PNG")
    img_bytes.seek(0)
    return {"message": "Logo generated successfully!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
