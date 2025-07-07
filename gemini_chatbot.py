"""
Modern Gemini Chatbot using LangChain and Rich
"""
import os
from rich.console import Console
from rich.panel import Panel
from rich.live import Live
from rich.align import Align
from rich.text import Text
from rich.prompt import Prompt
from rich.spinner import Spinner
from rich.layout import Layout
from rich.progress import Progress, SpinnerColumn, TextColumn
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

console = Console()

# LangChain Gemini LLM setup
gemini = ChatGoogleGenerativeAI(
    google_api_key=GEMINI_API_KEY,
    model="models/gemini-2.0-flash"
)

def animated_typing(text, color="cyan"):
    """Animated typing effect for chatbot responses."""
    for char in text:
        console.print(f"[bold {color}]{char}[/bold {color}]", end="", soft_wrap=True, highlight=False)
        console.file.flush()
        import time; time.sleep(0.01)
    console.print()

def main():
    console.clear()
    console.print(Panel(Align.center("[bold magenta]Gemini AI Chatbot[/bold magenta]", vertical="middle"), style="bold cyan", width=60))
    console.print("[bold green]Type your message and press Enter. Type 'exit' to quit.[/bold green]\n")
    chat_history = []
    while True:
        user_input = Prompt.ask("[bold yellow]You[/bold yellow]", default="", show_default=False)
        if user_input.lower() in ["exit", "quit"]:
            console.print("[bold red]Goodbye![/bold red]")
            break
        if not user_input.strip():
            continue
        chat_history.append(("user", user_input))
        with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
            progress.add_task(description="Gemini is thinking...", total=None)
            response = gemini.invoke([HumanMessage(content=user_input)])
        answer = response.content if hasattr(response, "content") else str(response)
        chat_history.append(("gemini", answer))
        animated_typing(answer, color="cyan")

if __name__ == "__main__":
    main()
