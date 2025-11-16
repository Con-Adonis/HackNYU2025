import os
from pathlib import Path

ASCII_ART = r"""
███╗   ██╗ ██████╗ ██╗   ██╗ █████╗
████╗  ██║██╔═══██╗██║   ██║██╔══██╗
██╔██╗ ██║██║   ██║██║   ██║███████║
██║╚██╗██║██║   ██║██║   ██║██╔══██║
██║ ╚████║╚██████╔╝╚██████╔╝██║  ██║
╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
        N   O   V   A
"""

ENV_PATH = Path(__file__).resolve().parent.parent / ".env"


def print_ascii_art():
        print(ASCII_ART)


def prompt_gemini_key() -> str:
    key = input("Enter your Gemini API key: ").strip()
    return key


def prompt_portfolio() -> str:
    print("Enter your portfolio tickers as a comma-separated list, e.g. 'AAPL, MSFT, NVDA':")
    portfolio = input("Portfolio: ").strip()
    return portfolio


def main():
    print_ascii_art()
    gem_key = prompt_gemini_key()
    portfolio = prompt_portfolio()
    with ENV_PATH.open("w") as f:
        f.write("GEMINI_API_KEY = '" + gem_key + "'\n" + "PORTFOLIO_TICKERS = '" + portfolio + "'")

    print(f"Configuration saved to {ENV_PATH}")