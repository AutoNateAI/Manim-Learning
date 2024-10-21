from manim import *

class RedditAggregatorVisualization(Scene):
    def construct(self):
        # Title for the scene
        title = Text("The Benefits of Using a Reddit Aggregator", font_size=48)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        # Step 1: Subreddits as data sources
        subreddit1 = Text("r/Marketing", font_size=36)
        subreddit2 = Text("r/Entrepreneur", font_size=36)
        subreddit3 = Text("r/Startups", font_size=36)

        subreddits = VGroup(subreddit1, subreddit2, subreddit3).arrange(DOWN, buff=1)

        # Animate subreddits appearing
        self.play(FadeIn(subreddits))
        self.wait(1)

        # Step 2: Data aggregation visualization
        aggregator_box = Rectangle(width=4, height=2, color=BLUE)
        aggregator_label = Text("Reddit Aggregator", font_size=24).next_to(aggregator_box, UP)

        self.play(subreddits.animate.next_to(aggregator_box, LEFT))
        self.play(FadeIn(aggregator_box), Write(aggregator_label))

        # Animate data flow into the aggregator
        for subreddit in subreddits:
            arrow = Arrow(subreddit.get_right(), aggregator_box.get_left(), buff=0.1)
            self.play(GrowArrow(arrow))
            self.wait(0.5)

        # Step 3: Data processing
        data_label = Text("Aggregated Data", font_size=24).next_to(aggregator_box, RIGHT)
        self.play(Write(data_label))

        # Show trend insights
        trends_box = Rectangle(width=5, height=3, color=GREEN).next_to(aggregator_box, RIGHT, buff=1)
        trends_label = Text("Trending Topics & Insights", font_size=24).move_to(trends_box.get_center())
        self.play(FadeIn(trends_box), Write(trends_label))

        # Step 4: Conclusion
        conclusion_text = Text("Use Reddit Aggregator to Spot Trends and Optimize Campaigns!", font_size=30)
        self.play(FadeIn(conclusion_text))
        self.wait(2)

        self.play(FadeOut(conclusion_text), FadeOut(trends_box), FadeOut(data_label), FadeOut(aggregator_box), FadeOut(aggregator_label), FadeOut(subreddits), FadeOut(title))


# Add this code block to render the scene automatically
if __name__ == "__main__":
    from manim import tempconfig
    with tempconfig({"quality": "medium_quality", "preview": True}):
        scene = RedditAggregatorVisualization()
        scene.render()
