from manim import *

class ClientServer(Scene):
    def construct(self):
        client = Circle(color=BLUE, fill_opacity=0.5).shift(LEFT * 3)
        server = Square(color=ORANGE, fill_opacity=0.5).shift(RIGHT * 3)
        data = Dot(color=RED) 

        self.play(FadeIn(client), FadeIn(server))
        self.play(data.animate.move_to(client.get_center()))
        self.play(data.animate.move_to(server.get_center()))
        self.wait(1)

# Add this code block to render the scene automatically
with tempconfig({"quality": "medium_quality", "preview": True}):
    scene = ClientServer()
    scene.render()