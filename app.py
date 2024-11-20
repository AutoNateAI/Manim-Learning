from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, List, Optional
from pydantic import BaseModel
from ai_engine import generate_description_openai
from models import DescriptionResponse, DescriptionRequest, ScreenplayRequest, ScreenplayResponse
import uvicorn
import json


app = FastAPI(
    title="AutoNate AI - Video Generator",
    description="Generates Videos Using NLP",
    version="1.0.0"
)

# Add CORSMiddleware to the application
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins in dev mode
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

######### START OF REAL MODELS --- DELETE ABOVE MODELS AFTERWARDS ##########


######### START OF REAL ENDPOINTS --- DELETE ABOVE ENDPOINTS AFTERWARDS ##########
@app.post("/generate-description/", response_model=DescriptionResponse)
async def generate_description(request: DescriptionRequest):
    """Generate a description and title using OpenAI"""
    try:
        result = generate_description_openai(
            description=request.description,
            video_type=request.video_type
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@app.post("/generate-screenplay/", response_model=ScreenplayResponse)
async def generate_screenplay(request: ScreenplayRequest):
    """Generate a screenplay using the stored JSON file"""
    try:
        # Read the stored screenplay from JSON file
        with open('generated_screenplay.json', 'r') as f:
            screenplay_data = json.load(f)
        return screenplay_data
    except FileNotFoundError:
        raise HTTPException(
            status_code=404, 
            detail="Generated screenplay file not found"
        )
    except json.JSONDecodeError:
        raise HTTPException(
            status_code=500, 
            detail="Error decoding screenplay data"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=str(e)
        )



# Configuration and startup
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)