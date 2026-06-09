from rich.console import Console
from rich.live import Live
from rich.spinner import Spinner
import time

console = Console()

# =========================================
# THINKING ANIMATION
# =========================================

def thinking():

    with Live(
        Spinner(
            "dots",
            text="[bold cyan]GHOST is thinking...[/bold cyan]"
        ),
        refresh_per_second=12,
    ):

        time.sleep(2)

# =========================================
# LOADING ANIMATION
# =========================================

def loading(text="Loading..."):

    with Live(
        Spinner(
            "dots",
            text=f"[bold bright_blue]{text}[/bold bright_blue]"
        ),
        refresh_per_second=12,
    ):

        time.sleep(1.5)

# =========================================
# TYPING EFFECT
# =========================================

def typing_effect(text):

    for char in text:

        print(char, end="", flush=True)

        time.sleep(0.02)

    print()