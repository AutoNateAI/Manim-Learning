from openai import OpenAI
from dotenv import load_dotenv
import os, json
from datetime import datetime
from models import SceneForSVG, SVGAsset
from typing import List

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)


def generate_description_openai(description, video_type):

    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[
            {
                "role": "system",
                "content": f"""
                
                Generate an engaging description and title for a 30-45 second Instagram Reels video based on the video type and initial concept you provide.

                These descriptions should appeal directly to the target audience that has historically shown an interest in similar content. The targeted audience must be captivated both by the visuals, descriptive language, and the tone used. The aim is to craft an enticing, informative description that other AI or individuals can use to construct a visual screenplay, with specific attention to enhancing animation, voiceover, and SVG graphics.

                Please include any hooks that grab attention right from the start, transitions to keep the interest alive, and a strong conclusion that makes an audience want to understand more or share the information widely.

                # Steps

                1. **Identify Key Elements**: Pull out the main ideas and themes from the provided video description and type. Understand the desired tone for the video.
                2. **Define the Target Audience**: Focus on who this content is designed for and what aspects would appeal to them—whether humor, impactful facts, or visual entertainment.
                3. **Craft an Attention-Grabbing Hook**: Start with a hook to draw in the audience immediately, preferably something surprising, relatable, or question-based to prompt curiosity.
                4. **Develop the Flow**: Describe the narrative in a way that maintains high engagement throughout, keeping the tone in line with video type (voiceover explainer, educational, or entertaining + educational). Ensure smooth transitions.
                5. **Conclude with Impact**: Add a punchy ending that either ties back to the hook or leaves the audience with a memorable thought or call-to-action.
                6. **Provide Descriptive Language Suitable for Animation**: Include visuals and sounds that complement animation, while considering how voiceover may convey key elements. The language should give adequate detail for an animator to envision the flow of scenes.

                # Output Format

                Generate a single concise paragraph (approximately 3-4 sentences) that provides all the elements necessary for a screenplay to be developed with ease. If direct phrasing for visual elements can be helpful, add them with qualifying descriptors (e.g., "as we see..." or "the character hesitates while...").

                # Examples

                ### Example 1
                **Input:**
                - Type: Educational
                - Concept Description: How plants adapt to survive in harsh climates like deserts.

                **Output:**
                Hook your audience with this engaging visual journey into survival like no other! We're about to take a fascinating look at how smart desert plants have evolved ingenious ways to beat the heat and save water. From quirky cactus shapes to magical waxy coats, these intricate animations will unveil the secrets hidden deep beneath the desert sands, giving an eye-popping twist to adaptive survival. By the end, you'll see these rugged plants in a whole new light—hardy heroes of the natural world!

                ### Example 2
                **Input:**
                - Type: Entertaining + Educational
                - Concept Description: The surprising history of bubblegum.

                **Output:**
                Get ready to chew on some incredible history! Ever wondered how our favorite stretchy pink candy came to be? This visually fun short animation will take you on a bubbly ride, revealing unexpected twists in bubblegum's story—from early experiments by scientists to the iconic bubble-blowing we all know and love today. Stay with us till the end, and we'll see if you can guess a bubble-blowing fun fact!

                # Notes

                - Hooking the audience right at the beginning is critical for ensuring maximum engagement.
                - Descriptions should contain vivid imagery and be intended for a high-energy, animated storytelling style.
                - Avoid technical jargon; keep it conversational, upbeat, and resonant with youthful energy wherever possible.
                - Consider how the visuals (animations with a voiceover) and descriptions must align well for effective reel screenplay production.

                Return the information in the following JSON structure:
                
                {{
                    "description": "<description>",
                    "title": "<title>
                }}
                """
            },
            {
                "role": "user",
                "content": f"description: {description}\nVideo Type: 30 - 45 seconds reels like video with the {video_type} effect."
            }
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "generate_description_openai",
                "schema": {
                    "type": "object",
                    "properties": {
                        "description": {"type": "string"},
                        "title": {"type": "string"}
                    },
                    "additionalProperties": False
                }
            }
        }
    )

    # Get the json back from OpenAI in string format
    str_json = response.choices[0].message.content

    # Convert it to a Python object
    data_obj = json.loads(str_json)

    # Add the current time for when the data was scraped
    data_obj["time_scraped"] = datetime.now().isoformat()

    return data_obj


def generate_screenplay_openai(title, description):

    system_prompt = """

    Create a screenplay for a 30-45 second Instagram reel video based on the title and context provided. Focus on making it an engaging SVG animated voiceover scene, with detailed visual descriptions.

    The animation should use the math animation library Manim to create smooth and creative interactions between entities. Graphically illustrate the scenes with descriptive language, focusing on vibrant interactions that bring out the main idea of the reel. Describe both the entities and the background details vividly to make them come alive.

    # Steps

    1. Read the provided title and context, and identify the main message and theme of the screenplay.
    2. Write a detailed screenplay with a clear narrative arc that fits into a 30-45 second timeline.
    3. Detail every key scene and moment in the animation:
    - Describe what entities are in the scene and how they move, interact, and change.
    - Include clear visual imagery to show how objects are animated and how they should appear.
    - Write the voiceover script along with cues for which part of the animation the lines correspond to.
    4. Make the experience engaging—describe each piece of the action with vivid vocabulary, capturing the essence of interaction, movement, and emotion.

    # Output Format

    The output should be a screenplay with three major sections for each segment within the 30-45 second reel:

    - **Scene Description**: Describe the main entities, the background, and how the visual elements are animated.
    - **Entity Interactions**: Explain how the entities interact with each other at this point in time, including any animations or transformations.
    - **Voiceover**: Write the dialogue or narration that corresponds to the current scene.

    Ensure the total screenplay length fits comfortably within the 30-45 second runtime, with concise yet vivid visualization and engaging storytelling along each step.

    # Example 

    ### Input
    - **Title**: "The Power of Consistency"
    - **Context**: The video is about the idea that small actions repeated consistently lead to big results over time.

    ### Output
    #### Scene 1 - Starting Small
    - **Scene Description**: The screen opens with a soft panoramic view of a blank graph, starting from zero. Small dots begin appearing on the graph, each one glowing faintly as it lands—these dots represent "small consistent actions." The background is a gradient from dark blue to light blue, giving a calm, early morning atmosphere.
    - **Entity Interactions**: One dot slowly bounces onto the graph, leaving an expanding ripple effect that highlights its importance. Several more dots start bouncing in next to the first, generating ripples that overlap with each other.
    - **Voiceover**: "All big changes start small. Just one small action, consistently done over time..."

    #### Scene 2 - Consistency Builds Trajectory
    - **Scene Description**: The camera zooms out, and we see rows of small arrows pointing up, representing an increasing trend. The graph’s background shifts to warmer hues—orange and yellow—indicating growth. The dots now begin connecting to each other, creating a linear path that points steadily upwards.
    - **Entity Interactions**: An arrow sweeps across, connecting the dots with smooth, curving animations that light up as it travels. The line grows larger while moving forward, emphasizing the theme of progression.
    - **Voiceover**: "...connect them together, and suddenly you see your trajectory changing for the better."

    #### Scene 3 - Compounding Effects
    - **Scene Description**: The screen pulls back again, revealing a larger graph where the line shoots upward more dramatically. Animated sparkles surround the line, adding an energetic sense of achievement. The colors shift to bright gold, signifying success.
    - **Entity Interactions**: The growing line transforms into a rising curve—its motion becomes rapid and bold as it continues upward, emphasizing momentum from the compounding effect. The dots begin to accelerate and merge into a unified glow at the peak of the curve.
    - **Voiceover**: "Over time, consistency takes you on a journey that delivers impact far beyond what was imaginable."

    Final Ending: The graph transforms into a golden shining arrow pointing at the words "Consistency is Key," which emerge in a bright cursive font.

    # Notes

    - This screenplay should be delivered with enough description for an animator to clearly visualize the scenes, including details about how color, shape, pacing, and interaction all play a role in delivery.
    - Utilize energetic vocabulary to make the video exciting and memorable, capturing the feeling of progress, growth, and success.
    - Ensure animations feel human-like in fluidity, and focus on highlighting growth, change, and moments of culmination.

    """

    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[
            {
                "role": "system",
                "content": f"""
                {system_prompt}

                Return the information in the following JSON structure:
                
                {{
                    "scenes": "List<Screenplay Scenes>",
                }}
                """
            },
            {
                "role": "user",
                "content": f"description: {description}\nTitle: {title} effect."
            }
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "generate_screenplay_openai",
                "schema": {
                    "type": "object",
                    "properties": {
                        "scenes": {"type": "array",
                                    "description": "The list of scenes covered in the generated screenplay.",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                        "descriptive_background": {
                                            "type": "string",
                                            "description": "Very graphic language describing the background for the scene, knowing that the background will be generated as an svg."
                                        },
                                        "descriptive_scene_entities": {
                                            "type": "array",
                                            "description": "Very graphic language describing the entities in the scene",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "name": {
                                                        "type": "string",
                                                        "description": "the name of the entity"
                                                    },
                                                    "description": {
                                                        "type": "string",
                                                        "description": "Very graphic language describing the entity in the scene, knowing that the entity will be generated as an svg."
                                                    }
                                                }
                                            }
                                        },
                                        "descriptive_scene_entities_interaction": {
                                            "type": "string",
                                            "description": "Very graphic language describing the interactions between entities in the scene."
                                        },
                                        "voiceover": {
                                            "type": "string",
                                            "description": "The voice over for the scene. It should go hand and hand with the animation and the entities."
                                        }
                                    },
                                },
                        },
                    },
                    "additionalProperties": False
                }
            }
        }
    )

    # Get the json back from OpenAI in string format
    str_json = response.choices[0].message.content

    # Convert it to a Python object
    data_obj = json.loads(str_json)

    # Add the current time for when the data was scraped
    data_obj["time_scraped"] = datetime.now().isoformat()

    return data_obj


def generate_background_svg(description: str, scene_number: int) -> SVGAsset:
    """Generate an SVG for a scene background based on the description."""
    # TODO: Implement actual SVG generation logic
    svg_code = f'''
    <svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
        <rect width="800" height="600" fill="#f0f0f0"/>
        <text x="400" y="300" text-anchor="middle">Background Scene {scene_number}</text>
    </svg>
    '''
    
    return SVGAsset(
        svg_code=svg_code,
        scene_number=scene_number,
        filename=f'background_scene_{scene_number}.svg',
        name=f'Scene {scene_number} Background',
        type='background'
    )

def generate_entity_svg(entity_description: dict, scene_number: int, entity_number: int) -> SVGAsset:
    """Generate an SVG for a scene entity based on its description."""
    # TODO: Implement actual SVG generation logic
    svg_code = f'''
    <svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
        <circle cx="200" cy="200" r="150" fill="#e0e0e0"/>
        <text x="200" y="200" text-anchor="middle">{entity_description['name']}</text>
    </svg>
    '''
    
    return SVGAsset(
        svg_code=svg_code,
        scene_number=scene_number,
        filename=f'entity_{scene_number}_{entity_number}.svg',
        name=entity_description['name'],
        type='entity'
    )

def generate_svgs(scenes: List[SceneForSVG]) -> List[SVGAsset]:
    """
    Generate all SVGs for the video scenes.
    This includes backgrounds and entities for each scene.
    """
    all_assets = []
    
    for scene in scenes:
        # Generate background SVG
        background_svg = generate_background_svg(
            scene.descriptive_background,
            scene.scene_number
        )
        all_assets.append(background_svg)
        
        # Generate SVGs for each entity in the scene
        for idx, entity in enumerate(scene.descriptive_scene_entities):
            entity_svg = generate_entity_svg(
                {"name": entity.name, "description": entity.description},
                scene.scene_number,
                idx + 1
            )
            all_assets.append(entity_svg)
    
    return all_assets


import json

def write_pretty_json(json_data, output_file):
    """
    Write Python dictionary to a file as pretty JSON.
    
    Args:
        json_data (dict): Python dictionary to be written as JSON
        output_file (str): Path to the output file
    """
    # Write to file with pretty formatting
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)

    

if __name__ == "__main__":
    import pprint
    # Example Usage
    video_type = "Entertainment + Education"
    description = "A young black boy learning to code in the hood and uses the knowledge to program his mind for success."
    # print("Starting AI Description and Title Generator🚀/n")
    # json_output = generate_description_openai(description, video_type)

    description = "Ever wonder how determination can code its way to success? Dive into the vibrant story of a young black boy in the hood who discovered the keyboard to his dreams! Watch as animations showcase his journey—starting from humble lines of code to building the software of his future—against an energetic backdrop full of grit and creativity. By the end, you'll be inspired to program your mind for success, championing innovation in the most unexpected places!"
    title = "Coding Dreams: Transforming Hood Hustle Into Tech Triumph"
    print("Starting AI Screenplay Generator🚀/n")
    json_output = generate_screenplay_openai(title, description)
    write_pretty_json(json_output, 'output.json')
    print("Done!\n")
