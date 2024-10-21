from manim import *

class WhatIsLanguageScene(Scene):
    def construct(self):
        # Set the green background
        self.camera.background_color = GREEN
        
        # Set aspect ratio for 9x16
        self.camera.frame_shape = (9, 16)

        # Title text: "What is a Coding Language?"
        title = Text("What is a Coding Language?", font_size=60, color=YELLOW).to_edge(UP)
        self.play(FadeIn(title))
        self.wait(1)

        # 1. What is language? (Visuals with animation)
        question_1 = Text("What is Language?", font_size=40, color=BLUE).shift(UP*2)
        self.play(Write(question_1))
        self.wait(0.5)

        # Create two human characters
        human_left = SVGMobject("human_icon.svg").scale(1).shift(LEFT*3 + DOWN)
        human_right = SVGMobject("human_icon.svg").scale(1).shift(RIGHT*3 + DOWN)

        # Speech bubbles for each human
        speech_bubble_left = SVGMobject("speech_bubble.svg").scale(0.5).shift(LEFT*3 + UP*2)
        speech_bubble_right = SVGMobject("speech_bubble.svg").scale(0.5).shift(RIGHT*3 + UP*2)

        # Create some symbols inside speech bubbles (letters or emojis)
        left_symbols = Text("A B C", font_size=36, color=WHITE).move_to(speech_bubble_left.get_center())
        right_symbols = Text("1 2 3", font_size=36, color=WHITE).move_to(speech_bubble_right.get_center())

        # Add humans and speech bubbles to the scene
        self.play(FadeIn(human_left), FadeIn(human_right))
        self.play(FadeIn(speech_bubble_left), FadeIn(speech_bubble_right))
        self.wait(0.5)

        # Add text inside speech bubbles
        self.play(Write(left_symbols), Write(right_symbols))
        self.wait(0.5)

        # Arrows between the humans to represent communication
        arrow = Arrow(human_left.get_right(), human_right.get_left(), buff=0.1, color=YELLOW)
        self.play(Create(arrow))
        self.wait(1)

        # Fade out visuals and bring in the explanation text
        answer_1 = Text("A tool for communication", font_size=36, color=WHITE).next_to(question_1, DOWN)
        self.play(FadeOut(human_left, human_right, speech_bubble_left, speech_bubble_right, left_symbols, right_symbols, arrow))
        self.play(FadeIn(answer_1))
        self.wait(1.5)
