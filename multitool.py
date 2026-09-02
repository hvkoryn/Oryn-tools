#!/usr/bin/env python3
"""
MultiTool v2.0
Un semplice multi-tool da terminale con boot sequence, ASCII art e menu.
Personalizza le funzioni in fondo al file per aggiungere ciò che ti serve.
"""

import os
import sys
import time
import random
import platform

from rich.console import Console
from rich.panel import Panel
from rich.align import Align
import pyfiglet

console = Console()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def boot_sequence():
    """Sequenza di avvio tipo 'launching...' — sostituisce l'apertura di un nuovo terminale."""
    clear()
    messages = [
        "[*] Launching Oryn Tools Connector v2.0...",
        "[*] Loading modules...",
        "[*] Initializing core services...",
        "[*] Checking system compatibility...",
        "[*] Establishing local environment...",
        "[+] All systems ready.",
    ]
    for msg in messages:
        console.print(msg, style="bold green")
        time.sleep(random.uniform(0.3, 0.6))
    time.sleep(0.8)


def show_banner():
    clear()
    ascii_banner = pyfiglet.figlet_format("Oryn Tools", font="slant")
    console.print(Align.center(f"[bold cyan]{ascii_banner}[/bold cyan]"))
    console.print(Align.center("[dim]v2.0 - Personal Toolkit[/dim]"))
    console.print(Align.center("[dim]by oryntech[/dim]\n"))


def show_menu():
    options = [
        "1. File Finder",
        "2. Network Ping",
        "3. Doxbin",
        "4. Esci",
    ]
    for opt in options:
        console.print(f"  {opt}", style="white")
    console.print()


# ---------------------------------------------------------------
# Funzioni del menu — personalizza/aggiungi qui le tue
# ---------------------------------------------------------------

def doxbin():
    import webbrowser
    webbrowser.open("https://doxbin.com")


def file_finder():
    query = console.input("[bold yellow]Nome file da cercare (o parte del nome): [/bold yellow]")
    start_path = console.input(
        "[bold yellow]Cartella di partenza (invio per home): [/bold yellow]"
    ) or os.path.expanduser("~")
    console.print(f"[dim]Ricerca in corso in {start_path}...[/dim]")

    found = []
    for root, _dirs, files in os.walk(start_path):
        for f in files:
            if query.lower() in f.lower():
                found.append(os.path.join(root, f))
                if len(found) >= 20:
                    break
        if len(found) >= 20:
            break

    if found:
        for f in found:
            console.print(f"  [green]{f}[/green]")
    else:
        console.print("[red]Nessun file trovato.[/red]")


def network_ping():
    host = console.input("[bold yellow]Host da pingare (es. google.com): [/bold yellow]")
    param = "-n" if os.name == "nt" else "-c"
    os.system(f"ping {param} 4 {host}")


# ---------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------

def main():
    boot_sequence()
    while True:
        show_banner()
        show_menu()
        choice = console.input("[bold magenta]Scegli un'opzione: [/bold magenta]")
        console.print()

        if choice == "1":
            file_finder()
        elif choice == "2":
            network_ping()
        elif choice == "3":
            doxbin()
        elif choice == "4":
            console.print("[bold cyan]Uscita in corso...[/bold cyan]")
            time.sleep(0.5)
            sys.exit(0)
        else:
            console.print("[red]Opzione non valida.[/red]")

        console.input("\n[dim]Premi INVIO per tornare al menu...[/dim]")


if __name__ == "__main__":
    main()
