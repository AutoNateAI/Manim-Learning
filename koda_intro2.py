from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.openai import OpenAIService
from dotenv import load_dotenv
import os

load_dotenv()

# Define custom config for 9:16 ratio
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080

PYTHON_BLUE = rgb_to_color([0.19, 0.42, 0.60])  # #306998
PYTHON_YELLOW = rgb_to_color([1.0, 0.83, 0.23])  # #FFD43B
CODE_BLUE = rgb_to_color([0.29, 0.55, 0.75])  # #4B8BBE
TURQUOISE = rgb_to_color([0.25, 0.88, 0.82])  # #40e0d0
DARK_BG = rgb_to_color([0.12, 0.12, 0.12])  # #1E1E1E

class MeetKoda(VoiceoverScene):
    def create_subtitle(self, text):
        """Helper function to create consistent subtitles"""
        return Text(
            text,
            font="Arial",
            font_size=32,
            color=WHITE,
            stroke_width=0.5,
            stroke_color=BLACK
        ).to_edge(DOWN, buff=1.0)

    def construct(self):
        # Set voice service
        self.set_speech_service(OpenAIService(voice="nova", api_key=os.getenv("OPENAI_API_KEY")))

        # Create background
        background = Rectangle(height=config.frame_height, width=config.frame_width, 
                             fill_color=DARK_BG, fill_opacity=1)
        
        # Load Koda SVG
        koda = SVGMobject("./static/svgs/koda4.svg")
        koda.scale(3).shift(DOWN * 2)  # Adjusted scale and position for 9:16
        
        # Function to compare colors with tolerance
        def color_matches(mob_color, target_color, tolerance=0.1):
            return np.allclose(color_to_rgb(mob_color), 
                             color_to_rgb(target_color), 
                             atol=tolerance)

        # Extract SVG elements (same as before)
        cape = VGroup(*[mob for mob in koda 
                       if isinstance(mob, VMobject) and 
                       color_matches(mob.get_color(), CODE_BLUE)])
        
        python_logo = VGroup(*[mob for mob in koda 
                             if isinstance(mob, VMobject) and 
                             color_matches(mob.get_color(), PYTHON_YELLOW)])
        
        code_lines = VGroup(*[mob for mob in koda 
                            if isinstance(mob, VMobject) and 
                            (color_matches(mob.get_color(), PYTHON_YELLOW) or 
                             color_matches(mob.get_color(), CODE_BLUE)) and 
                            mob.get_width() < 1])
        
        power_bands = VGroup(*[mob for mob in koda 
                             if isinstance(mob, Circle) and 
                             color_matches(mob.get_color(), PYTHON_YELLOW)])
        
        laptop = VGroup(*[mob for mob in koda.submobjects 
                         if isinstance(mob, VMobject) and 
                         mob.get_center()[0] < -1 and 
                         mob.get_height() < 1])
        
        glasses = VGroup(*[mob for mob in koda.submobjects 
                          if isinstance(mob, VMobject) and 
                          mob.get_center()[1] > 1 and 
                          mob.get_stroke_width() > 0])

        # Initial scene setup
        subtitle1 = self.create_subtitle("Welcome to Python Programming!")
        with self.voiceover(text="Hey there, future coders! Ready to embark on an epic programming adventure?") as tracker:
            self.play(
                FadeIn(background),
                run_time=1
            )
            self.play(
                DrawBorderThenFill(koda),
                Write(subtitle1),
                run_time=tracker.duration - 1
            )

        # Introduction with binary effect
        subtitle2 = self.create_subtitle("Meet Your Coding Mentor")
        with self.voiceover(text="I'm Koda, your coding companion and digital guide through the wonderful world of Python programming!") as tracker:
            self.play(
                ReplacementTransform(subtitle1, subtitle2),
                run_time=1
            )
            
            binary_text = VGroup(*[
                Text(num, font="Monospace", font_size=24, color=CODE_BLUE)
                for num in ["01", "10", "11", "00"]
            ]).arrange_in_grid(rows=2, cols=2, buff=1).shift(UP * 4 + LEFT)  # Adjusted position for 9:16
            
            self.play(
                FadeIn(binary_text),
                binary_text.animate.shift(UP * 0.3),
                run_time=tracker.duration - 1
            )

        # Python power animation
        subtitle3 = self.create_subtitle("Unlock the Power of Code")
        with self.voiceover(text="With the power of Python at our fingertips, we'll unlock the secrets of coding and create amazing things together!") as tracker:
            self.play(
                ReplacementTransform(subtitle2, subtitle3),
                python_logo.animate.scale(1.2),
                power_bands.animate.set_color(YELLOW),
                rate_func=there_and_back,
                run_time=tracker.duration/2
            )
            
            for line in code_lines:
                self.play(
                    Create(line),
                    run_time=tracker.duration/8
                )

        # Teaching tools highlight
        subtitle4 = self.create_subtitle("Learn at Your Own Pace")
        with self.voiceover(text="Whether you're a complete beginner or already know some coding, I'll be right here to help you learn, explore, and have fun while doing it!") as tracker:
            self.play(
                ReplacementTransform(subtitle3, subtitle4),
                run_time=1
            )
            
            glow_color = BLUE
            self.play(
                *[
                    AnimationGroup(
                        mob.animate.set_color(glow_color),
                        mob.animate.set_stroke(color=glow_color, width=3),
                        lag_ratio=0.2
                    )
                    for mob in [laptop, glasses]
                ],
                run_time=tracker.duration/2
            )
            
            self.play(
                laptop.animate.set_color(WHITE),
                glasses.animate.set_color(WHITE),
                run_time=tracker.duration/2
            )

        # Final flourish
        subtitle5 = self.create_subtitle("Let's Start Coding!")
        with self.voiceover(text="So, are you ready to start our coding journey? Let's dive in and see what awesome projects we can create together!") as tracker:
            self.play(
                ReplacementTransform(subtitle4, subtitle5),
                run_time=1
            )
            
            self.play(
                Rotate(power_bands, angle=TAU),
                koda.animate.scale(1.1),
                binary_text.animate.shift(UP * 0.5),
                rate_func=there_and_back,
                run_time=tracker.duration - 1
            )
            
            self.play(
                FadeOut(binary_text),
                FadeOut(subtitle5),
                run_time=0.5
            )

        # Hold final pose
        self.wait(1)