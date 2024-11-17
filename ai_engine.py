from openai import OpenAI
from dotenv import load_dotenv
import os, json
from datetime import datetime
from models import DescriptionResponse

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def generate_description_openai(description, video_type):
    client = OpenAI(api_key=OPENAI_API_KEY)

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
                "name": "post_extraction_schema",
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

if __name__ == "__main__":
    import pprint
    # Example Usage
    video_type = "Entertainment + Education"
    description = "A young black boy learning to code in the hood and uses the knowledge to program his mind for success."
    print("Starting AI Description and Title Generator🚀/n")
    json_output = generate_description_openai(description, video_type)
    pprint.pprint(json_output)
