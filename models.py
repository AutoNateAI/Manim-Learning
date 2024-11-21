from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class DescriptionRequest(BaseModel):
    description: str
    video_type: str

class DescriptionResponse(BaseModel):
    title: str
    description: str
    time_scraped: datetime

class ScreenplayRequest(BaseModel):
    title: str
    description: str

class SceneEntity(BaseModel):
    name: str
    description: str

class Scene(BaseModel):
    descriptive_background: str
    descriptive_scene_entities: List[SceneEntity]
    descriptive_scene_entities_interaction: str
    voiceover: str

class ScreenplayResponse(BaseModel):
    scenes: List[Scene]
    time_scraped: datetime

class SceneEntityForSVG(BaseModel):
    name: str
    description: str

class SceneForSVG(BaseModel):
    descriptive_background: str
    descriptive_scene_entities: List[SceneEntityForSVG]
    scene_number: int

class SVGGenerationRequest(BaseModel):
    scenes: List[SceneForSVG]

class SVGAsset(BaseModel):
    svg_code: str
    scene_number: int
    filename: str
    name: str  # Added name field
    type: str  # To distinguish between background and entity SVGs

class SVGGenerationResponse(BaseModel):
    assets: List[SVGAsset]
    time_generated: datetime

class ManimScriptRequest(BaseModel):
    title: str
    description: str
    screenplay: ScreenplayResponse
    svg_assets: SVGGenerationResponse

class ManimScriptResponse(BaseModel):
    manim_script: str
    time_generated: datetime

class VideoGenerationRequest(BaseModel):
    script: str
    title: str

class VideoGenerationResponse(BaseModel):
    video_url: str
    time_generated: datetime