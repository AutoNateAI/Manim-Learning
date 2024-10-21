from manim import *

class WhatIsACodingLanguage(Scene):
    def construct(self):
        # Set the green background
        self.camera.background_color = GREEN
        
        # Set aspect ratio for 9x16
        self.camera.frame_shape = (9, 16)

        # Title text: "What is a Coding Language?"
        title = Text("What is a Coding Language?", font_size=60, color=YELLOW).to_edge(UP)
        self.play(FadeIn(title))
        self.wait(1)

        # 1. What is language?
        question_1 = Text("What is Language?", font_size=40, color=BLACK).shift(UP*2)
        answer_1 = Text("A tool for communication", font_size=36, color=WHITE).next_to(question_1, DOWN)
        self.play(Write(question_1))
        self.play(FadeIn(answer_1, shift=UP))
        self.wait(1.5)

        # 2. What is communication?
        question_2 = Text("What is Communication?", font_size=40, color=BLACK).shift(UP*2)
        answer_2 = Text("Sharing information", font_size=36, color=WHITE).next_to(question_2, DOWN)
        self.play(ReplacementTransform(question_1, question_2), FadeOut(answer_1))
        self.play(FadeIn(answer_2, shift=UP))
        self.wait(1.5)

        # 3. What is inside the information?
        info_box = Rectangle(color=WHITE, height=4, width=6)
        info_text = Text("Information", font_size=36, color=YELLOW).move_to(info_box.get_center())

        details = Text("Details", font_size=30, color=WHITE).move_to([2, 1, 0])
        experiences = Text("Experiences", font_size=30, color=WHITE).move_to([0, 0, 0])
        instructions = Text("Instructions", font_size=30, color=WHITE).move_to([-2, -1, 0])
        
        self.play(FadeOut(question_2), FadeOut(answer_2))
        self.play(Create(info_box), Write(info_text))
        self.wait(1.5)

        # Move "Information" upwards to make space for the other words
        self.play(info_text.animate.shift(UP*1.5))
        self.wait(0.5)

        # Bring in the other words (Details, Experiences, Instructions)
        self.play(FadeIn(details, shift=LEFT), FadeIn(experiences, shift=UP), FadeIn(instructions, shift=RIGHT))
        self.wait(2)

        # 4. Why is sharing info important?
        question_3 = Text("Why is Sharing Important?", font_size=40, color=BLACK).shift(UP*2)
        answer_3 = Text("It enables work to be done efficiently", font_size=36, color=WHITE).next_to(question_3, DOWN)
        self.play(FadeOut(info_box, info_text, details, experiences, instructions))
        self.play(FadeIn(question_3, shift=UP), FadeIn(answer_3, shift=UP))
        self.wait(2)

        # 5. Universal communication examples (Insects, animals, computers)
        insect = SVGMobject("insect_icon.svg").scale(0.7).shift(LEFT*4)
        animal = SVGMobject("animal_icon.svg").scale(0.7)
        computer = SVGMobject("computer_icon.svg").scale(0.7).shift(RIGHT*4)

        self.play(FadeOut(question_3, answer_3))
        self.play(FadeIn(insect, shift=DOWN), FadeIn(animal, shift=DOWN), FadeIn(computer, shift=DOWN))
        self.wait(1.5)

        spectrum_label = Text("Electromagnetic Spectrum", font_size=36, color=YELLOW).to_edge(DOWN)
        self.play(Write(spectrum_label))
        self.wait(1.5)

        # 6. Conclusion: Human language vs. Coding language
        question_4 = Text("Human Language vs. Coding Language", font_size=40, color=YELLOW).shift(UP*2)
        answer_4a = Text("Human Language: To communicate with humans", font_size=36, color=WHITE).next_to(question_4, DOWN)
        answer_4b = Text("Coding Language: To communicate with computers", font_size=36, color=WHITE).next_to(answer_4a, DOWN)

        self.play(FadeOut(spectrum_label, insect, animal, computer))
        self.play(FadeIn(question_4, shift=UP), FadeIn(answer_4a, shift=UP), FadeIn(answer_4b, shift=UP))
        self.wait(3)

        # End scene
        self.play(FadeOut(question_4, answer_4a, answer_4b, title))


