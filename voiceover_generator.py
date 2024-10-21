import sys, os
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") 

def create_speech(input_text, output_file_path):
    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=input_text
    )
    response.stream_to_file(output_file_path)

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py output.mp3 '<input_text>'")
        sys.exit(1)
    input_text = sys.argv[2]
    output_file_path = sys.argv[1]
    create_speech(input_text, output_file_path)

if __name__ == "__main__":
    main()
