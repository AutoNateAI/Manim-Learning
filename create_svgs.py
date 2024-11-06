import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np

# Function to create an SVG file for each asset
def create_svg(filename, draw_function):
    fig, ax = plt.subplots()
    canvas = FigureCanvas(fig)
    ax.set_aspect('equal')
    ax.set_axis_off()
    
    draw_function(ax)  # Drawing the specific SVG element

    # Save as SVG file
    fig.savefig(f"./static/svgs/{filename}.svg", format="svg", bbox_inches='tight', pad_inches=0)
    plt.close(fig)

# Draw functions for specific assets
def draw_speech_bubble(ax):
    bubble = patches.FancyBboxPatch((0.2, 0.2), 0.6, 0.4, boxstyle="round,pad=0.1", edgecolor="none", facecolor="lightblue")
    tail = patches.Polygon([[0.35, 0.2], [0.45, 0], [0.55, 0.2]], closed=True, facecolor="lightblue")
    ax.add_patch(bubble)
    ax.add_patch(tail)

def draw_info_icon(ax):
    circle = patches.Circle((0.5, 0.5), 0.4, edgecolor="none", facecolor="yellow")
    ax.text(0.5, 0.5, "i", fontsize=80, va='center', ha='center', color='blue')
    ax.add_patch(circle)

def draw_brain(ax):
    brain = patches.Ellipse((0.5, 0.5), 0.8, 0.5, edgecolor="none", facecolor="pink")
    ax.add_patch(brain)
    # Simulate 'folds' with small curves
    for i in range(5):
        curve = patches.Arc((0.5 + i*0.05, 0.5), 0.6-i*0.1, 0.3, angle=0, theta1=0, theta2=180, edgecolor="purple")
        ax.add_patch(curve)

def draw_waves(ax):
    for i in range(5):
        wave = patches.Arc((0.5, 0.5), 1-i*0.2, 1-i*0.2, angle=0, theta1=0, theta2=360, edgecolor="lightgreen")
        ax.add_patch(wave)

def draw_bee(ax):
    body = patches.Ellipse((0.5, 0.5), 0.6, 0.3, edgecolor="none", facecolor="yellow")
    stripes = [patches.Rectangle((0.38 + i * 0.05, 0.35), 0.1, 0.3, edgecolor="none", facecolor="black") for i in range(3)]
    ax.add_patch(body)
    for stripe in stripes:
        ax.add_patch(stripe)
    wings = [patches.Ellipse((0.35, 0.65), 0.2, 0.4, edgecolor="none", facecolor="lightblue"),
             patches.Ellipse((0.65, 0.65), 0.2, 0.4, edgecolor="none", facecolor="lightblue")]
    for wing in wings:
        ax.add_patch(wing)

def draw_wolf(ax):
    body = patches.Ellipse((0.5, 0.5), 0.6, 0.4, edgecolor="none", facecolor="gray")
    ax.add_patch(body)
    # Ears
    ears = [patches.Polygon([[0.3, 0.7], [0.4, 0.9], [0.5, 0.7]], facecolor="gray"),
            patches.Polygon([[0.6, 0.7], [0.7, 0.9], [0.8, 0.7]], facecolor="gray")]
    for ear in ears:
        ax.add_patch(ear)
    # Tail
    tail = patches.Polygon([[0.8, 0.5], [1, 0.5], [0.9, 0.3]], facecolor="gray")
    ax.add_patch(tail)

def draw_computer(ax):
    screen = patches.Rectangle((0.2, 0.4), 0.6, 0.4, edgecolor="none", facecolor="lightgray")
    base = patches.Rectangle((0.3, 0.1), 0.4, 0.1, edgecolor="none", facecolor="gray")
    ax.add_patch(screen)
    ax.add_patch(base)

def draw_construction_worker(ax):
    body = patches.Rectangle((0.3, 0.2), 0.4, 0.6, edgecolor="none", facecolor="orange")
    helmet = patches.Ellipse((0.5, 0.85), 0.5, 0.2, edgecolor="none", facecolor="yellow")
    ax.add_patch(body)
    ax.add_patch(helmet)

def draw_typer(ax):
    body = patches.Rectangle((0.3, 0.2), 0.4, 0.6, edgecolor="none", facecolor="blue")
    computer = patches.Rectangle((0.35, 0.6), 0.3, 0.2, edgecolor="none", facecolor="gray")
    ax.add_patch(body)
    ax.add_patch(computer)

def draw_robot(ax):
    body = patches.Rectangle((0.3, 0.3), 0.4, 0.4, edgecolor="none", facecolor="silver")
    head = patches.Rectangle((0.4, 0.6), 0.2, 0.2, edgecolor="none", facecolor="silver")
    ax.add_patch(body)
    ax.add_patch(head)

def draw_superhero(ax):
    body = patches.Rectangle((0.3, 0.3), 0.4, 0.5, edgecolor="none", facecolor="red")
    cape = patches.Polygon([[0.3, 0.5], [0.5, 0.8], [0.7, 0.5]], facecolor="blue")
    ax.add_patch(body)
    ax.add_patch(cape)

def draw_cape(ax):
    cape = patches.Polygon([[0.3, 0.5], [0.5, 0.8], [0.7, 0.5]], facecolor="red")
    ax.add_patch(cape)


if __name__ == "__main__":
    # Create SVG assets
    create_svg("speech_bubble", draw_speech_bubble)
    create_svg("info_icon", draw_info_icon)
    create_svg("brain", draw_brain)
    create_svg("waves", draw_waves)
    create_svg("bee", draw_bee)
    create_svg("wolf", draw_wolf)
    create_svg("computer", draw_computer)
    create_svg("construction_worker", draw_construction_worker)
    create_svg("typer", draw_typer)
    create_svg("robot", draw_robot)
    create_svg("superhero", draw_superhero)
    create_svg("cape", draw_cape)

