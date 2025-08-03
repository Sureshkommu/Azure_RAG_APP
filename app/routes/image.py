 # Upload, search, and ask endpoints
from fastapi import APIRouter, Query
from app.services.image_service import generate_image


router = APIRouter()

@router.get("/generate-image/")
async def get_generated_image(prompt: str = Query(..., description="Prompt to generate image")):
    try:
        image_url = generate_image(prompt)
        return {
            "prompt": prompt,
            "image_url": image_url
        }
    except Exception as e:
        return {"error": str(e)}