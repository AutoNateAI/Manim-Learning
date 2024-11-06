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

        # Scene 1: Introduction (0-5 seconds)
        intro_text = Text("What is a Coding Language?", font_size=64).to_edge(UP)
        with self.voiceover(text="What is a coding language, you ask? Well, first... What even *is* a language?") as tracker:
            self.play(Write(intro_text), run_time=tracker.duration)

        self.wait(0.5)
        self.play(FadeOut(intro_text))

        # Scene 2: Language as a Tool for Communication (5-12 seconds)
        speech_bubble = SVGMobject("./static/svgs/speech_bubble.svg").scale(2).to_edge(LEFT)
        info_bubble = SVGMobject("./static/svgs/info_icon.svg").scale(2).to_edge(RIGHT)

        with self.voiceover(text="Language is a tool for communication! It’s how we share what’s going on in our heads with the outside world.") as tracker:
            self.play(FadeIn(speech_bubble), FadeIn(info_bubble), run_time=tracker.duration)

        self.play(FadeOut(speech_bubble), FadeOut(info_bubble))

        # Scene 3: What is Communication? (12-19 seconds)
        brain = SVGMobject("./static/svgs/brain.svg").scale(2).to_edge(LEFT)
        waves = SVGMobject("./static/svgs/waves.svg").scale(2).to_edge(RIGHT)
        info_labels = VGroup(
            Text("Experiences").next_to(brain, DOWN).scale(0.7),
            Text("Details").next_to(waves, DOWN).scale(0.7),
            Text("Instructions").next_to(brain, RIGHT).scale(0.7)
        )

        with self.voiceover(text="Communication is all about sharing *information*. And what’s inside that information? Experiences, details, instructions.") as tracker:
            self.play(FadeIn(brain), FadeIn(waves), run_time=tracker.duration)
            self.play(FadeIn(info_labels), run_time=tracker.duration)

        self.play(FadeOut(brain), FadeOut(waves), FadeOut(info_labels))

        # Scene 4: Why Share Information? (19-26 seconds)
        bee = SVGMobject("./static/svgs/bee.svg").scale(2).to_edge(LEFT)
        wolf = SVGMobject("./static/svgs/wolf.svg").scale(2).to_edge(RIGHT)
        computer = SVGMobject("./static/svgs/computer.svg").scale(2).shift(DOWN)

        with self.voiceover(text="But why bother sharing all this info? Because sharing it lets us get work done *faster*! It’s how everything in nature works, from insects to animals to—yes, computers.") as tracker:
            self.play(FadeIn(bee), FadeIn(wolf), FadeIn(computer), run_time=tracker.duration)

        self.play(FadeOut(bee), FadeOut(wolf), FadeOut(computer))

        # Scene 5: Human and Computer Languages (26-36 seconds)
        construction_worker = SVGMobject("./static/svgs/construction_worker.svg").scale(2).to_edge(LEFT)
        human_typer = SVGMobject("./static/svgs/typer.svg").scale(2).to_edge(RIGHT)
        robot = SVGMobject("./static/svgs/robot.svg").scale(2).shift(DOWN)

        with self.voiceover(text="Just like humans use human languages to share information for work—like building a house or solving a puzzle—we use coding languages to share instructions with computers so they can do the heavy lifting for us.") as tracker:
            self.play(FadeIn(construction_worker), FadeIn(human_typer), FadeIn(robot), run_time=tracker.duration)

        self.play(FadeOut(construction_worker), FadeOut(human_typer), FadeOut(robot))

        # Scene 6: Why Coding Languages Matter (36-45 seconds)
        superhero = SVGMobject("./static/svgs/superhero.svg").scale(2).center()
        cape = SVGMobject("./static/svgs/cape.svg").scale(2).center()

        with self.voiceover(text="In short, coding languages let us talk to machines so they can do the *work* for us—super efficiently. And that’s why learning a coding language is like unlocking a secret superpower! Pretty cool, right?") as tracker:
            self.play(FadeIn(superhero), FadeIn(cape), run_time=tracker.duration)

        self.wait(1)
        self.play(FadeOut(superhero), FadeOut(cape))
