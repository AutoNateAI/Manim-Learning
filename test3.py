from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.openai import OpenAIService
from dotenv import load_dotenv
import os

load_dotenv()

# Define custom config for 9:16 ratio (vertical video format)
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080

# Custom colors
ALGORITHM_BLUE = rgb_to_color([0.19, 0.42, 0.60])
HIGHLIGHT_YELLOW = rgb_to_color([1.0, 0.83, 0.23])
SEARCH_GREEN = rgb_to_color([0.25, 0.88, 0.82])
DARK_BG = rgb_to_color([0.12, 0.12, 0.12])

class BinarySearchExplanation(VoiceoverScene):
    def create_subtitle(self, text):
        """Helper function to create consistent subtitles"""
        return Text(
            text,
            font="Arial",
            font_size=36,
            color=WHITE,
            stroke_width=0.5,
            stroke_color=BLACK,
            line_spacing=1.2
        ).to_edge(UP, buff=2.0)

    def smooth_subtitle_transition(self, old_subtitle, new_subtitle, duration=1.75):
        """Helper function for smooth subtitle transitions"""
        self.play(
            FadeOut(old_subtitle, shift=UP * 0.5),
            FadeIn(new_subtitle, shift=UP * 0.5),
            run_time=duration
        )

    def create_array_squares(self, numbers):
        """Create squares with numbers for array visualization"""
        squares = VGroup()
        for i, num in enumerate(numbers):
            square = Square(side_length=0.8)
            number = Text(str(num), font_size=24)
            index = Text(str(i), font_size=20, color=GRAY).next_to(square, DOWN, buff=0.1)
            combined = VGroup(square, number, index)
            squares.add(combined)
        squares.arrange(RIGHT, buff=0.2)
        return squares

    def construct(self):
        # Set voice service
        self.set_speech_service(OpenAIService(
            voice="nova", 
            api_key=os.getenv("OPENAI_API_KEY")
        ))

        # Create background
        background = Rectangle(
            height=config.frame_height,
            width=config.frame_width,
            fill_color=DARK_BG,
            fill_opacity=1
        )

        # Initial array setup
        sorted_array = [2, 4, 6, 8, 10, 12, 14, 16]
        array_squares = self.create_array_squares(sorted_array)
        array_squares.shift(DOWN * 2)

        # Scene 1: Introduction
        subtitle1 = self.create_subtitle("Binary Search Algorithm")
        with self.voiceover(text="Welcome to the fascinating world of algorithms! Today, we're exploring Binary Search.") as tracker:
            self.play(
                FadeIn(background),
                Write(subtitle1),
                run_time=1
            )
            self.play(
                Create(array_squares),
                run_time=max(tracker.duration - 1, 2)
            )

        # Scene 2: Concept Introduction
        subtitle2 = self.create_subtitle("Divide and Conquer")
        with self.voiceover(text="Binary Search is like a smart guessing game. Instead of checking every number, we split our search in half each time!") as tracker:
            self.smooth_subtitle_transition(subtitle1, subtitle2)
            
            # Create divider line
            divider = Line(
                start=array_squares.get_center() + UP * 1.5,
                end=array_squares.get_center() + DOWN * 1.5,
                color=HIGHLIGHT_YELLOW
            )
            
            self.play(
                Create(divider),
                run_time=max(tracker.duration - 1.75, 1)
            )

        # Scene 3: Search Process
        subtitle3 = self.create_subtitle("Finding Number 12")
        target_number = 12
        with self.voiceover(text=f"Let's try to find the number {target_number}. We'll start by looking at the middle element.") as tracker:
            self.smooth_subtitle_transition(subtitle2, subtitle3)
            
            # Highlight middle element
            middle_idx = len(sorted_array) // 2
            middle_square = array_squares[middle_idx]
            
            self.play(
                middle_square[0].animate.set_fill(SEARCH_GREEN, opacity=0.5),
                run_time=max(tracker.duration - 1.75, 1)
            )

        # Scene 4: Comparison
        subtitle4 = self.create_subtitle("Compare and Navigate")
        with self.voiceover(text=f"The middle number is {sorted_array[middle_idx]}. Since {target_number} is greater, we only need to search the right half!") as tracker:
            self.smooth_subtitle_transition(subtitle3, subtitle4)
            
            # Fade out left half
            left_half = VGroup(*[array_squares[i] for i in range(middle_idx + 1)])
            
            self.play(
                left_half.animate.set_opacity(0.3),
                divider.animate.shift(RIGHT * 2),
                run_time=max(tracker.duration - 1.75, 1)
            )

        # Scene 5: Final Search
        subtitle5 = self.create_subtitle("Found It!")
        with self.voiceover(text="And there it is! We found twelve in just a few steps, much faster than checking every number!") as tracker:
            self.smooth_subtitle_transition(subtitle4, subtitle5)
            
            # Highlight found number
            target_idx = sorted_array.index(target_number)
            target_square = array_squares[target_idx]
            
            self.play(
                target_square[0].animate.set_fill(HIGHLIGHT_YELLOW, opacity=0.8),
                target_square.animate.scale(1.2),
                rate_func=there_and_back,
                run_time=max(tracker.duration - 1.75, 1)
            )

        # Final flourish
        with self.voiceover(text="Binary Search is a powerful tool that helps us find what we're looking for in the most efficient way possible!") as tracker:
            # Create celebration effect
            rays = VGroup(*[
                Line(
                    target_square.get_center(),
                    target_square.get_center() + RIGHT * 2 + UP * random.uniform(-1, 1),
                    stroke_width=2,
                    color=HIGHLIGHT_YELLOW
                )
                for _ in range(8)
            ])
            
            self.play(
                Create(rays),
                array_squares.animate.set_opacity(1),
                run_time=max(tracker.duration - 1, 1)
            )
            
            self.play(
                FadeOut(rays),
                FadeOut(subtitle5),
                run_time=1
            )

        # Hold final pose
        self.wait(1)