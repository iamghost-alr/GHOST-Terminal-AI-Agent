import traceback

from rich.console import Console
from rich.panel import Panel
from rich import box
from rich.align import Align
from rich.rule import Rule
from rich.table import Table
from rich.live import Live
from rich.spinner import Spinner
from rich.text import Text

import random
import time

console = Console()

GHOST_BANNER = r"""

 ▄████  ██░ ██  ▒█████    ██████ ▄▄▄█████▓
██▒ ▀█▒▓██░ ██▒▒██▒  ██▒▒██    ▒ ▓  ██▒ ▓▒
██░▄▄▄░▒██▀▀██░▒██░  ██▒░ ▓██▄   ▒ ▓██░ ▒░
▓█  ██▓░▓█ ░██ ▒██   ██░  ▒   ██▒░ ▓██▓ ░
▒▓███▀▒░▓█▒░██▓░ ████▓▒░▒██████▒▒  ▒██▒ ░
░▒   ▒  ▒ ░░▒░▒░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ▒ ░░
 ░   ░  ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░▒  ░ ░    ░
░ ░   ░  ░  ░░ ░░ ░ ░ ▒  ░  ░  ░    ░
      ░  ░  ░  ░    ░ ░        ░

"""

whispers = [
    "...connection secured...",
    "...Initializing...",
    "...Memory Stabilized...",
    "...Tools Loaded...",
    "...System Ready.",
]

def ghost_whisper():

    if random.randint(1, 5) == 1:

        console.print(
            f"\n[bright_black italic]{random.choice(whispers)}[/bright_black italic]"
        )

def show_banner():

    banner = Text(GHOST_BANNER)

    banner.stylize("bold bright_cyan")

    console.print("\n")

    console.print(
        Panel(
            Align.center(banner),
            border_style="dark_magenta",
            box=box.DOUBLE_EDGE,
            padding=(1, 4),
            subtitle="[bright_black]Terminal Agent[/bright_black]"
        )
    )

    ghost_whisper()

def startup():

    console.print("\n")

    startup_lines = [
        "Initializing Memory...",
        "Loading Tools...",
        "Connecting Deepseek API...",
        "Starting Neural Core...",
        "System Ready."
    ]

    for line in startup_lines:

        console.print(
            f"[bold bright_blue]{line}[/bold bright_blue]"
        )

        time.sleep(0.3)

    ghost_whisper()

def user_input():

    console.print(
        "\n[bold bright_green]You[/bold bright_green] ❯ ",
        end=""
    )

def typing_effect(text: str):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.015)
    print()

def ai_response(message):

    console.print("\n")

    console.print(
        Panel(
            message,
            title="[bold bright_cyan]GHOST[/bold bright_cyan]",
            border_style="bright_cyan",
            box=box.ROUNDED,
            padding=(1, 2)
        )
    )

    ghost_whisper()

def tool_used(tool_name):

    console.print(
        f"[bold yellow]◉[/bold yellow] "
        f"[bold bright_blue]{tool_name}[/bold bright_blue] activated"
    )

def memory_saved():

    console.print(
        "[bold magenta]◉ MEMORY[/bold magenta] "
        "[green]Stored successfully[/green]"
    )

def searching():

    console.print(
        "[bold blue]◉ SEARCH[/bold blue] "
        "Searching the web..."
    )

def thinking():

    with Live(
        Spinner(
            "dots",
            text="[bold bright_cyan]GHOST is thinking...[/bold bright_cyan]"
        ),
        refresh_per_second=12,
    ):

        time.sleep(2)

def loading(text="Loading..."):

    with Live(
        Spinner(
            "dots",
            text=f"[bold dark_magenta]{text}[/bold dark_magenta]"
        ),
        refresh_per_second=12,
    ):

        time.sleep(1.5)

def typing_effect(text):

    for char in text:

        print(char, end="", flush=True)

        time.sleep(0.018)

    print()

def success(message):

    console.print(
        f"[bold green]✔ SUCCESS[/bold green] "
        f"{message}"
    )

def warning(message):

    console.print(
        f"[bold yellow]⚠ WARNING[/bold yellow] "
        f"{message}"
    )

def show_error(message):

    console.print(
        f"[bold red]✖ ERROR[/bold red] "
        f"{message}"
    )

def info(message):

    console.print(
        f"[bold white]◆ INFO[/bold white] "
        f"{message}"
    )

def divider():

    console.print(
        Rule(
            "[bright_black]━━━━━━━━━━━━━━━ ◈ ━━━━━━━━━━━━━━━[/bright_black]"
        )
    )

def show_tools():

    table = Table(
        title="[bold bright_cyan]Loaded Modules[/bold bright_cyan]",
        border_style="dark_magenta",
        box=box.ROUNDED
    )

    table.add_column(
        "Module",
        style="bright_cyan"
    )

    table.add_column(
        "Status",
        style="green"
    )

    table.add_row(
        "Calculator",
        "ONLINE"
    )

    table.add_row(
        "Weather",
        "ONLINE"
    )

    table.add_row(
        "Notes Memory",
        "ONLINE"
    )

    table.add_row(
        "Web Search",
        "ONLINE"
    )

    console.print(table)

    ghost_whisper()