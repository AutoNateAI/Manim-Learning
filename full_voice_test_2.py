from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.openai import OpenAIService
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")

class WhatIsCodingLanguage(VoiceoverScene):
    def construct(self):
        # Set voice service
        self.set_speech_service(OpenAIService(voice="alloy", api_key=OPENAI_API_KEY))

        # Scene 1: Introduction with code rain effect
        intro_text = Text("What is a Coding Language?", font_size=64).to_edge(UP)
        code_rain = VGroup(*[
            Text("01", font="Monospace", font_size=24) 
            for _ in range(20)
        ]).arrange_in_grid(rows=4, cols=5)
        
        with self.voiceover(text="What is a coding language, you ask? Well, first... What even *is* a language?") as tracker:
            self.play(
                Write(intro_text),
                *[FadeIn(digit, shift=DOWN) for digit in code_rain],
                run_time=tracker.duration
            )

        self.wait(0.5)
        self.play(FadeOut(intro_text), FadeOut(code_rain))

        # Scene 2: Language as Communication Tool
        human1 = Circle(radius=0.5, color=BLUE).shift(LEFT*3)
        human2 = Circle(radius=0.5, color=RED).shift(RIGHT*3)
        
        message = Text("Hello!", font_size=36)
        message_path = ArcBetweenPoints(human1.get_center(), human2.get_center(), angle=PI/4)
        
        with self.voiceover(text="Language is a tool for communication! It's how we share what's going on in our heads with the outside world.") as tracker:
            self.play(Create(human1), Create(human2))
            self.play(
                MoveAlongPath(message, message_path),
                rate_func=linear,
                run_time=tracker.duration/2
            )
            self.play(FadeOut(message))

        self.play(FadeOut(human1), FadeOut(human2))

        # Scene 3: Brain to Computer Translation
        brain = SVGMobject("./static/svgs/brain2.svg").scale(1.5).to_edge(LEFT)
        arrow1 = Arrow(LEFT, RIGHT)
        code_block = Code(
            code='''
            def greet():
                print("Hi!")
            ''',
            language="python",
            font_size=24
        )
        arrow2 = Arrow(LEFT, RIGHT)
        computer = SVGMobject("./static/svgs/computer2.svg").scale(1.5).to_edge(RIGHT)
        
        translation_group = VGroup(brain, arrow1, code_block, arrow2, computer).arrange(RIGHT)
        
        with self.voiceover(text="Communication is all about sharing *information*. And what's inside that information? Experiences, details, instructions.") as tracker:
            self.play(
                FadeIn(brain),
                Create(arrow1),
                Write(code_block),
                Create(arrow2),
                FadeIn(computer),
                run_time=tracker.duration
            )

        self.play(FadeOut(translation_group))

        # Scene 4: Nature's Communication
        binary_tree = VGroup()
        def create_branch(pos, angle, length, depth):
            if depth == 0: return
            end_pos = pos + length * np.array([np.cos(angle), np.sin(angle), 0])
            line = Line(pos, end_pos)
            binary_tree.add(line)
            create_branch(end_pos, angle + PI/4, length*0.7, depth-1)
            create_branch(end_pos, angle - PI/4, length*0.7, depth-1)
            
        create_branch(ORIGIN, PI/2, 2, 5)
        binary_tree.set_color(GREEN)
        
        with self.voiceover(text="But why bother sharing all this info? Because sharing it lets us get work done *faster*! It's how everything in nature works, from insects to animals to—yes, computers.") as tracker:
            self.play(Create(binary_tree), run_time=tracker.duration/2)
            self.play(
                binary_tree.animate.set_color_by_gradient(BLUE, GREEN),
                run_time=tracker.duration/2
            )

        self.play(FadeOut(binary_tree))

        # Scene 5: Coding in Action
        code_editor = Rectangle(height=4, width=6, color=WHITE)
        code_lines = VGroup(*[
            Text(line, font="Monospace", font_size=24)
            for line in [
                "def calculate_sum(a, b):",
                "    return a + b",
                "",
                "result = calculate_sum(5, 3)",
                "print(result)  # 8"
            ]
        ]).arrange(DOWN, aligned_edge=LEFT).move_to(code_editor)
        
        with self.voiceover(text="Just like humans use human languages to share information for work—like building a house or solving a puzzle—we use coding languages to share instructions with computers so they can do the heavy lifting for us.") as tracker:
            self.play(Create(code_editor))
            self.play(Write(code_lines), run_time=tracker.duration)

        self.play(FadeOut(code_editor), FadeOut(code_lines))

        # Scene 6: Final Transformation
        wizard = Star(outer_radius=1.5, inner_radius=0.8, color=YELLOW)
        sparkles = VGroup(*[
            Dot(point=rotate_vector(RIGHT*2, angle), radius=0.05, color=YELLOW)
            for angle in np.linspace(0, TAU, 8)
        ])
        
        with self.voiceover(text="In short, coding languages let us talk to machines so they can do the *work* for us—super efficiently. And that's why learning a coding language is like unlocking a secret superpower! Pretty cool, right?") as tracker:
            self.play(Create(wizard))
            self.play(
                Rotate(sparkles, angle=2*PI, about_point=ORIGIN),
                rate_func=linear,
                run_time=tracker.duration
            )

        self.wait(1)
        self.play(FadeOut(wizard), FadeOut(sparkles))