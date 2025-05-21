"""
Custom Research Assistant with cool animations
"""
import time
import random
import sys
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.style import Style
from rich.color import Color

# Console setup
console = Console()

class ResearchAssistant:
    def __init__(self):
        self.history = []
        self.current_status = "Ready"
        self.thinking_animation_active = False

    def start_thinking_animation(self):
        """Start the thinking animation with neon effects"""
        self.thinking_animation_active = True

        # More interesting spinner frames
        thinking_frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]

        thinking_messages = [
            "Searching knowledge base...",
            "Analyzing information...",
            "Consulting sources...",
            "Processing data...",
            "Synthesizing findings...",
            "Formulating response...",
            "Verifying facts...",
            "Organizing content...",
            "Finalizing research...",
        ]

        # Neon colors for the animation
        neon_colors = [
            "#FF00FF",  # Magenta
            "#FF3366",  # Hot Pink
            "#FF0066",  # Neon Pink
            "#FF3300",  # Neon Orange
            "#FF6600",  # Bright Orange
            "#FF0000",  # Bright Red
        ]

        i = 0
        message_change_counter = 0
        current_message_idx = 0
        color_idx = 0

        # Show thinking animation for a random amount of time (3-6 seconds)
        end_time = time.time() + random.uniform(4, 7)

        while time.time() < end_time:
            frame = thinking_frames[i % len(thinking_frames)]
            message = thinking_messages[current_message_idx]
            color = neon_colors[color_idx % len(neon_colors)]

            # Display with neon color
            console.print(f"\r[bold {color}]{frame} {message}[/bold {color}]", end="")

            time.sleep(0.1)
            i += 1
            message_change_counter += 1

            # Change the message occasionally
            if message_change_counter >= 15:
                current_message_idx = (current_message_idx + 1) % len(thinking_messages)
                message_change_counter = 0
                color_idx += 1  # Change color with each message change

        # Clear the animation line when done
        console.print("\r" + " " * 80 + "\r", end="")
        self.thinking_animation_active = False

    def generate_research(self, query):
        """Generate a research response for the given query"""
        self.current_status = "Researching"
        self.start_thinking_animation()

        # Generate a simple response based on the query
        topic = query

        # Create a summary based on the topic
        summary = f"Based on my research about '{topic}', I've found several interesting points. " \
                 f"This is a fascinating subject with many aspects to explore. " \
                 f"The information available suggests that {topic} has significant implications " \
                 f"in various fields and continues to be an area of active interest and development."

        # Generate some key points
        key_points = [
            f"The concept of {topic} has evolved significantly over time",
            f"Recent developments in {topic} show promising results",
            f"Experts in the field have different perspectives on {topic}",
            f"There are several practical applications of {topic} in everyday life",
            f"Further research on {topic} could lead to important breakthroughs"
        ]

        # Generate some sources
        sources = [
            f"Research Journal of {topic.title()} Studies (2023)",
            f"International {topic.title()} Association",
            f"The {topic.title()} Handbook (2022 Edition)",
            f"Expert interviews and analysis"
        ]

        # Generate follow-up questions
        follow_up_questions = [
            f"What are the historical origins of {topic}?",
            f"How does {topic} impact different industries?",
            f"What are the future trends in {topic}?",
            f"Who are the leading experts in {topic}?"
        ]

        # Create a response object
        response = {
            "topic": topic,
            "summary": summary,
            "key_points": key_points,
            "sources": sources,
            "tools_used": ["search", "wikipedia"],
            "follow_up_questions": follow_up_questions
        }

        self.history.append((query, response))
        self.current_status = "Ready"
        return response

def display_splash_screen():
    """Display an animated splash screen with neon effects"""
    console.clear()

    # Define logo - SPICYNICK CUSTOM LOGO
    logo = r"""
   _____       _            _   _ _      _
  / ____|     (_)          | \ | (_)    | |
 | (___  _ __  _  ___ _   _|  \| |_  ___| | __
  \___ \| '_ \| |/ __| | | | . ` | |/ __| |/ /
  ____) | |_) | | (__| |_| | |\  | | (__|   <
 |_____/| .__/|_|\___|\__, |_| \_|_|\___|_|\_\
        | |            __/ |
        |_|           |___/
    """

    tagline = ">> PREMIUM RESEARCH EXPERIENCE <<"

    # Create neon color animation effect
    neon_colors = [
        "#FF00FF",  # Magenta
        "#FF3366",  # Hot Pink
        "#FF0066",  # Neon Pink
        "#FF3300",  # Neon Orange
        "#FF6600",  # Bright Orange
        "#FF0000",  # Bright Red
        "#FF3300",  # Neon Orange
        "#FF6600",  # Bright Orange
        "#FF00FF",  # Back to Magenta
    ]

    # Display pulsing neon logo animation
    for _ in range(3):  # Pulse 3 times
        for color in neon_colors:
            # Clear previous logo
            console.clear()

            # Print logo with current neon color
            console.print(f"[bold {color}]{logo}[/bold {color}]")

            # Add a glow effect with a lighter shade
            lighter_color = color
            console.print(f"[bold {lighter_color}]          {tagline}[/bold {lighter_color}]")

            # Short delay for animation effect
            time.sleep(0.1)

    # Final static display with neon glow
    console.clear()
    console.print(f"[bold #FF00FF]{logo}[/bold #FF00FF]")

    # Type out the tagline with a typing effect
    typed_tagline = ""
    for char in tagline:
        typed_tagline += char
        console.print(f"\r[bold #FF00FF]          {typed_tagline}[/bold #FF00FF]", end="")
        time.sleep(0.05)

    console.print("\n")
    console.print("\n[bold #FF8C00]Initializing SpicyNick Research System...[/bold #FF8C00]")

    # Animated loading bar with SpicyNick colors
    with Progress(
        SpinnerColumn(),
        TextColumn("[bold #FF8C00]Loading components...[/bold #FF8C00]"),
        console=console
    ) as progress:
        task = progress.add_task("", total=100)

        while not progress.finished:
            progress.update(task, advance=1.5)
            time.sleep(0.02)

    time.sleep(0.5)
    console.clear()

def run_app():
    """Run the main application"""
    # Show splash screen
    display_splash_screen()

    # Initialize AI assistant
    assistant = ResearchAssistant()

    # Create a stylish neon interface
    console.clear()

    # Create a neon border
    border_color = "#FF00FF"  # Neon magenta
    border_width = 60

    console.print(f"[bold {border_color}]{'═' * border_width}[/bold {border_color}]")
    console.print(f"[bold {border_color}]║[/bold {border_color}] [bold #FF4500]SpicyNick Research System[/bold #FF4500]" + " " * (border_width - 29) + f"[bold {border_color}]║[/bold {border_color}]")
    console.print(f"[bold {border_color}]{'═' * border_width}[/bold {border_color}]")

    console.print(f"[bold #FF8C00]Type your research query below or 'exit' to quit[/bold #FF8C00]\n")

    while True:
        # Clear previous output for cleaner display
        console.print("[bold green]Enter your research query:[/bold green]")
        query = input("> ")

        if query.lower() in ['exit', 'quit']:
            break

        if query.strip():
            console.print(f"\n[bold cyan]Researching:[/bold cyan] {query}")

            # Generate research
            results = assistant.generate_research(query)

            # Display results with neon styling
            console.print(f"\n[bold #FF00FF]{'═' * 60}[/bold #FF00FF]")
            console.print("[bold #FF00FF]Research Results[/bold #FF00FF]")
            console.print(f"[bold #FF00FF]{'═' * 60}[/bold #FF00FF]")

            # Create a panel for the summary with neon border
            summary_panel = Panel(
                results["summary"],
                title=f"[bold #FF3366]Topic: {results['topic']}[/bold #FF3366]",
                border_style="magenta",
                padding=(1, 2)
            )
            console.print(summary_panel)

            # Display key points with neon styling
            if results["key_points"]:
                console.print(f"\n[bold #FF6600]{'─' * 40}[/bold #FF6600]")
                console.print("[bold #FF6600]Key Findings[/bold #FF6600]")
                console.print(f"[bold #FF6600]{'─' * 40}[/bold #FF6600]")

                for i, point in enumerate(results["key_points"], 1):
                    console.print(f"  [bold #FF3366]{i}.[/bold #FF3366] {point}")

            # Display sources with neon styling
            if results["sources"]:
                console.print(f"\n[bold #00FFFF]{'─' * 40}[/bold #00FFFF]")
                console.print("[bold #00FFFF]References & Sources[/bold #00FFFF]")
                console.print(f"[bold #00FFFF]{'─' * 40}[/bold #00FFFF]")

                for i, source in enumerate(results["sources"], 1):
                    console.print(f"  [bold #00FFFF]{i}.[/bold #00FFFF] {source}")

            # Display follow-up questions with neon styling
            if results["follow_up_questions"]:
                console.print(f"\n[bold #00FF00]{'─' * 40}[/bold #00FF00]")
                console.print("[bold #00FF00]Suggested Follow-up Research[/bold #00FF00]")
                console.print(f"[bold #00FF00]{'─' * 40}[/bold #00FF00]")

                for i, question in enumerate(results["follow_up_questions"], 1):
                    console.print(f"  [bold #00FF00]{i}.[/bold #00FF00] {question}")

            # Wait for user to continue with neon prompt
            console.print(f"\n[bold #FF00FF]{'═' * 60}[/bold #FF00FF]")
            console.print("[bold #FF00FF]Press Enter to continue...[/bold #FF00FF]", end="")
            input()

            # Recreate the stylish neon interface
            console.clear()

            # Create a neon border
            border_color = "#FF00FF"  # Neon magenta
            border_width = 60

            console.print(f"[bold {border_color}]{'═' * border_width}[/bold {border_color}]")
            console.print(f"[bold {border_color}]║[/bold {border_color}] [bold #FF4500]SpicyNick Research System[/bold #FF4500]" + " " * (border_width - 29) + f"[bold {border_color}]║[/bold {border_color}]")
            console.print(f"[bold {border_color}]{'═' * border_width}[/bold {border_color}]")

            console.print(f"[bold #FF8C00]Type your research query below or 'exit' to quit[/bold #FF8C00]\n")

if __name__ == "__main__":
    print("Starting SpicyNick Research System...")
    try:
        print("Attempting to run the application...")
        run_app()
    except KeyboardInterrupt:
        print("\nApplication terminated by user")
        console.print("\n[bold yellow]Application terminated by user[/bold yellow]")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        import traceback
        print(f"Traceback: {traceback.format_exc()}")
        console.print(f"\n[bold red]An error occurred: {e}[/bold red]")
