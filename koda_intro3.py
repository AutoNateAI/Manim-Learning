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

PYTHON_BLUE = rgb_to_color([0.19, 0.42, 0.60])
PYTHON_YELLOW = rgb_to_color([1.0, 0.83, 0.23])
CODE_BLUE = rgb_to_color([0.29, 0.55, 0.75])
TURQUOISE = rgb_to_color([0.25, 0.88, 0.82])
DARK_BG = rgb_to_color([0.12, 0.12, 0.12])

class MeetKoda(VoiceoverScene):
    def create_subtitle(self, text):
        """Helper function to create consistent subtitles"""
        return Text(
            text,
            font="Arial",
            font_size=36,  # Slightly larger font
            color=WHITE,
            stroke_width=0.5,
            stroke_color=BLACK,
            line_spacing=1.2  # Add some line spacing
        ).to_edge(UP, buff=2.0)  # Position at top with more padding

    def smooth_subtitle_transition(self, old_subtitle, new_subtitle, duration=1.75):
        """Helper function for smooth subtitle transitions with minimum duration"""
        self.play(
            FadeOut(old_subtitle, shift=UP * 0.5),
            FadeIn(new_subtitle, shift=UP * 0.5),
            run_time=duration
        )

    def construct(self):
        # Set voice service
        self.set_speech_service(OpenAIService(voice="nova", api_key=os.getenv("OPENAI_API_KEY")))

        # Create background
        background = Rectangle(height=config.frame_height, width=config.frame_width, 
                             fill_color=DARK_BG, fill_opacity=1)
        
        # Load Koda SVG and position lower to make room for subtitles
        koda = SVGMobject("./static/svgs/koda4.svg")
        koda.scale(3).shift(DOWN * 1.5)  # Adjusted position to make room for top subtitles
        
        # Color matching function (same as before)
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
                Write(subtitle1, run_time=1.75),  # Slower text appearance
                run_time=max(tracker.duration - 1, 1.75)  # Ensure minimum duration
            )

        # Introduction with binary effect
        subtitle2 = self.create_subtitle("Meet Your Coding Mentor")
        with self.voiceover(text="I'm Koda, your coding companion and digital guide through the wonderful world of Python programming!") as tracker:
            self.smooth_subtitle_transition(subtitle1, subtitle2)
            
            # Position binary numbers to avoid subtitle
            binary_text = VGroup(*[
                Text(num, font="Monospace", font_size=24, color=CODE_BLUE)
                for num in ["01", "10", "11", "00"]
            ]).arrange_in_grid(rows=2, cols=2, buff=1).shift(UP * 2 + LEFT)
            
            self.play(
                FadeIn(binary_text),
                binary_text.animate.shift(UP * 0.3),
                run_time=max(tracker.duration - 1.75, 1)
            )

        # Python power animation
        subtitle3 = self.create_subtitle("Unlock the Power of Code")
        with self.voiceover(text="With the power of Python at our fingertips, we'll unlock the secrets of coding and create amazing things together!") as tracker:
            self.smooth_subtitle_transition(subtitle2, subtitle3)
            
            animation_time = max((tracker.duration - 1.75) / 2, 1)
            self.play(
                python_logo.animate.scale(1.2),
                power_bands.animate.set_color(YELLOW),
                rate_func=there_and_back,
                run_time=animation_time
            )
            
            for line in code_lines:
                self.play(
                    Create(line),
                    run_time=animation_time / len(code_lines)
                )

        # Teaching tools highlight
        subtitle4 = self.create_subtitle("Learn at Your Own Pace")
        with self.voiceover(text="Whether you're a complete beginner or already know some coding, I'll be right here to help you learn, explore, and have fun while doing it!") as tracker:
            self.smooth_subtitle_transition(subtitle3, subtitle4)
            
            animation_time = max((tracker.duration - 1.75) / 2, 1)
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
                run_time=animation_time
            )
            
            self.play(
                laptop.animate.set_color(WHITE),
                glasses.animate.set_color(WHITE),
                run_time=animation_time
            )

        # Final flourish
        subtitle5 = self.create_subtitle("Let's Start Coding!")
        with self.voiceover(text="So, are you ready to start our coding journey? Let's dive in and see what awesome projects we can create together!") as tracker:
            self.smooth_subtitle_transition(subtitle4, subtitle5)
            
            self.play(
                Rotate(power_bands, angle=TAU),
                koda.animate.scale(1.1),
                binary_text.animate.shift(UP * 0.5),
                rate_func=there_and_back,
                run_time=max(tracker.duration - 1.75, 1)
            )
            
            # Keep subtitle visible longer before fading
            self.wait(0.5)
            self.play(
                FadeOut(binary_text),
                FadeOut(subtitle5),
                run_time=1
            )

        # Hold final pose
        self.wait(1)