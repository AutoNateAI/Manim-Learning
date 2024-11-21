from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, List, Optional
from pydantic import BaseModel
from ai_engine import generate_description_openai, generate_manim_script_openai
from manim_video_gen import generate_video_with_voiceover_9x16
from models import DescriptionResponse, DescriptionRequest, ManimScriptRequest, ManimScriptResponse, ScreenplayRequest, ScreenplayResponse, SVGGenerationRequest, SVGGenerationResponse, VideoGenerationRequest, VideoGenerationResponse
from ai_engine import generate_svgs
import uvicorn
import json, random, datetime


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


EDUCATIONAL_TEMPLATES = [
    {
        "title": "The Science Behind Deep Learning",
        "description": "Dive into the fascinating world of neural networks as we unravel how machines learn! Through vibrant animations, we'll explore how artificial neurons process information, make decisions, and evolve through training. Watch as complex patterns emerge from simple mathematical principles, revealing the magic behind AI's problem-solving abilities."
    },
    {
        "title": "Ocean Mysteries Revealed",
        "description": "Journey into the depths of our planet's most enigmatic ecosystem! Discover mind-blowing facts about deep-sea creatures, their bioluminescent abilities, and survival strategies. Through captivating visuals, we'll explore how life thrives in the most extreme conditions, revealing nature's incredible adaptability."
    }
]

ENTERTAINMENT_TEMPLATES = [
    {
        "title": "Evolution of Dance: A Digital Story",
        "description": "Get ready for a high-energy journey through time as we animate the evolution of dance! Watch as moves transform from classical to contemporary, showcasing how rhythm and expression have shaped cultural movements. This vibrant visual feast will have you grooving through decades of dance revolution!"
    },
    {
        "title": "The Secret Life of Household Items",
        "description": "Ever wondered what your everyday objects do when you're not looking? Join us on this whimsical adventure as we imagine the secret lives of your household items! Through playful animations, we'll bring to life the hidden stories of your favorite objects in ways you've never imagined."
    }
]

EXPLAINER_TEMPLATES = [
    {
        "title": "Crypto Explained: Beyond the Buzz",
        "description": "Demystify the world of cryptocurrency in this engaging explainer! Watch as we break down blockchain technology, digital currencies, and mining through clear, concise animations. By the end, you'll understand the fundamentals that power this digital revolution."
    },
    {
        "title": "The Psychology of Procrastination",
        "description": "Uncover the science behind why we procrastinate and how to overcome it! Through compelling visuals, we'll explore the psychological triggers that lead to postponing tasks and discover practical strategies for better time management. Learn why your brain resists certain tasks and how to hack your productivity!"
    }
]


######### START OF REAL MODELS --- DELETE ABOVE MODELS AFTERWARDS ##########


######### START OF REAL ENDPOINTS --- DELETE ABOVE ENDPOINTS AFTERWARDS ##########
@app.post("/generate-description/", response_model=DescriptionResponse)
async def generate_description(request: DescriptionRequest):
    """Generate a description and title using OpenAI"""
    # try:
    #     result = generate_description_openai(
    #         description=request.description,
    #         video_type=request.video_type
    #     )
    #     return result



    try:
        video_type = request.video_type.lower()
        print(request.description)
        
        # Select template based on video type
        if "educational" in video_type:
            template = random.choice(EDUCATIONAL_TEMPLATES)
        elif "entertainment" in video_type:
            template = random.choice(ENTERTAINMENT_TEMPLATES)
        else:  # default to explainer
            template = random.choice(EXPLAINER_TEMPLATES)
        # Add timestamp for consistency with real API
        response = {
            "title": template["title"],
            "description": template["description"],
            "time_scraped":"2024-11-17T00:51:31.450198"
        }

        print(response)
        
        return response
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
    

@app.post("/generate-svgs/", response_model=SVGGenerationResponse)
async def generate_svg_assets(request: SVGGenerationRequest):
    """Generate SVG assets for all scenes"""
    try:
        # Generate SVGs for all scenes
        svg_assets = generate_svgs(request.scenes)
        
        # Return the response with generated assets
        return SVGGenerationResponse(
            assets=svg_assets,
            time_generated="2024-11-17T00:51:31.450198"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/generate-manim-script/", response_model=ManimScriptResponse)
async def generate_manim_script(request: ManimScriptRequest):
    """Generate a Manim script based on the video content"""
    try:
        manim_script = generate_manim_script_openai(
            title=request.title,
            description=request.description,
            screenplay=request.screenplay.dict(),
            svg_assets=request.svg_assets.dict()
        )
        
        return ManimScriptResponse(
            manim_script=manim_script,
            time_generated="2024-11-17T00:51:31.450198"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Add this new endpoint
@app.post("/generate-video-9x16/", response_model=VideoGenerationResponse)
async def generate_video(request: VideoGenerationRequest):
    """Generate a 9:16 video using manim script"""
    print(request)
    try:
        video_url = generate_video_with_voiceover_9x16(
            script=request.script,
            title=request.title
        )
        
        return VideoGenerationResponse(
            video_url=video_url,
            time_generated="2024-11-17T00:51:31.450198"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating video: {str(e)}"
        )


# Configuration and startup
if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)