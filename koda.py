from manim import *

class KodaCharacter(SVGMobject):
    def __init__(self, **kwargs):
        super().__init__("./static/svgs/koda.svg", **kwargs)
        # Get references to moveable parts
        self.parts = {}
        for submob in self.submobjects:
            if isinstance(submob, VMobject) and hasattr(submob, 'id'):
                self.parts[submob.id] = submob
        
        # Store main body parts
        self.head = self.submobjects[1]  # Head group
        self.left_arm = self.submobjects[2]  # Left arm group
        self.right_arm = self.submobjects[3]  # Right arm group
        self.left_leg = self.submobjects[4]  # Left leg group
        self.right_leg = self.submobjects[5]  # Right leg group
        
    def wave(self):
        # Create a waving animation using just the right arm
        return Succession(
            Rotate(self.right_arm, angle=PI/4, about_point=self.right_arm.get_start()),
            Rotate(self.right_arm, angle=-PI/4, about_point=self.right_arm.get_start())
        )
    
    def type(self):
        # Create typing animation using just the arms
        return AnimationGroup(
            self.left_arm.animate.shift(DOWN * 0.1),
            self.right_arm.animate.shift(DOWN * 0.1),
            rate_func=there_and_back,
            run_time=0.2
        )

class KodaIntroScene(Scene):
    def construct(self):
        # Create and position Koda
        koda = KodaCharacter()
        koda.scale(2)  # Make Koda bigger
        koda.move_to(ORIGIN)  # Center Koda
        
        # Intro sequence
        self.play(FadeIn(koda))
        self.wait(0.5)
        
        # Wave animation
        self.play(koda.wave())
        self.wait(0.5)
        
        # Typing animation
        for _ in range(3):  # Type three times
            self.play(koda.type())
        
        self.wait()