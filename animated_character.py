from manim import *

class SimpleCharacter(VGroup):
    def __init__(self, color=BLUE, **kwargs):
        super().__init__(**kwargs)
        
        # Create basic character parts
        self.body = Circle(radius=1, fill_opacity=1, color=color)
        self.eyes = VGroup(
            Dot(point=np.array([-0.3, 0.2, 0])),
            Dot(point=np.array([0.3, 0.2, 0]))
        )
        self.mouth = ArcBetweenPoints(
            start=np.array([-0.3, -0.2, 0]),
            end=np.array([0.3, -0.2, 0]),
            angle=-TAU/8
        )
        
        # Add all parts to the character
        self.add(self.body, self.eyes, self.mouth)

class CharacterScene(Scene):
    def construct(self):
        # Create character
        character = SimpleCharacter()
        
        # Initial animation - character appears
        self.play(FadeIn(character))
        
        # Jumping animation
        self.play(
            character.animate.shift(UP),
            rate_func=there_and_back,
            run_time=1
        )
        
        # Spinning animation
        self.play(Rotate(character, angle=TAU, run_time=2))
        
        # Happy expression - mouth curve adjustment
        happy_mouth = ArcBetweenPoints(
            start=np.array([-0.3, -0.2, 0]),
            end=np.array([0.3, -0.2, 0]),
            angle=-TAU/4
        )
        self.play(
            Transform(character.mouth, happy_mouth)
        )
        
        # Bouncing animation
        self.play(
            character.animate.shift(UP * 2),
            rate_func=there_and_back_with_pause,
            run_time=2
        )
        
        # Fade out
        self.play(FadeOut(character))

# Extended character with more expressions
class ExpressiveCharacter(SimpleCharacter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.expressions = {
            'happy': self._create_happy_mouth(),
            'sad': self._create_sad_mouth(),
            'surprised': self._create_surprised_mouth()
        }
    
    def _create_happy_mouth(self):
        return ArcBetweenPoints(
            start=np.array([-0.3, -0.2, 0]),
            end=np.array([0.3, -0.2, 0]),
            angle=-TAU/4
        )
    
    def _create_sad_mouth(self):
        return ArcBetweenPoints(
            start=np.array([-0.3, -0.3, 0]),
            end=np.array([0.3, -0.3, 0]),
            angle=TAU/4
        )
    
    def _create_surprised_mouth(self):
        return Circle(radius=0.2).shift(DOWN * 0.2)
    
    def change_expression(self, expression):
        if expression in self.expressions:
            return Transform(self.mouth, self.expressions[expression])
        raise ValueError(f"Expression '{expression}' not found")

class EmotionalScene(Scene):
    def construct(self):
        character = ExpressiveCharacter()
        
        # Sequence of emotional changes
        self.play(FadeIn(character))
        self.wait()
        
        # Happy expression
        self.play(character.change_expression('happy'))
        self.wait()
        
        # Jump while happy
        self.play(
            character.animate.shift(UP * 1.5),
            rate_func=there_and_back_with_pause,
            run_time=1.5
        )
        
        # Surprised expression
        self.play(character.change_expression('surprised'))
        self.play(
            character.animate.scale(1.2),
            rate_func=there_and_back,
            run_time=0.5
        )
        
        # Sad expression
        self.play(character.change_expression('sad'))
        self.play(
            character.animate.shift(DOWN * 0.5),
            run_time=1
        )
        
        # Return to happy
        self.play(
            character.change_expression('happy'),
            character.animate.shift(UP * 0.5)
        )
        
        self.wait()
        self.play(FadeOut(character))