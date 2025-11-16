import os
from pathlib import Path

ASCII_ART = r"""
 _   _                 _   _               
| \ | | _____      __| \ | | _____      __
|  \| |/ _ \ \ /\ / /|  \| |/ _ \ \ /\ / /
| |\  |  __/\ V  V / | |\  |  __/\ V  V / 
|_| \_|\___| \_/\_/  |_| \_|\___| \_/\_/  

        N O V A   N E W S   S U I T E
"""

ENV_PATH = Path(__file__).resolve().parent.parent / ".env"


def print_ascii_art() -> None:
        print(ASCII_ART)


def prompt_gemini_key() -> str:
    key = input("Enter your Gemini API key: ").strip()
    return key


def prompt_portfolio() -> str:
    print("Enter your portfolio tickers as a comma-separated list, e.g. 'AAPL, MSFT, NVDA':")
    portfolio = input("Portfolio: ").strip()
    return portfolio


def write_env(gemini_key: str, portfolio: str) -> None:
    # This function updates (or creates) the .env file that lives at the
    # project root. That way we don't need to retype things every run.
    lines: list[str] = []
    if ENV_PATH.exists():
        with ENV_PATH.open("r") as f:
            lines = f.readlines()

    def upsert(key: str, value: str) -> None:
        # Either update an existing line with this key or append a new one.
        nonlocal lines
        key_prefix = f"{key}="
        for i, line in enumerate(lines):
            if line.startswith(key_prefix):
                lines[i] = f"{key}={value}\n"
                break
        else:
            lines.append(f"{key}={value}\n")

    upsert("GEMINI_API_KEY", gemini_key)
    upsert("PORTFOLIO_TICKERS", portfolio)

    with ENV_PATH.open("w") as f:
        f.writelines(lines)

    print(f"Configuration saved to {ENV_PATH}")


def first_time_setup() -> tuple[str, list[str]]:
    """Run the welcome wizard and return (api_key, portfolio_list)."""
    print_ascii_art()
    gemini_key = prompt_gemini_key()
    portfolio_raw = prompt_portfolio()
    write_env(gemini_key, portfolio_raw)

    portfolio_list = [t.strip().upper() for t in portfolio_raw.split(",") if t.strip()]
    return gemini_key, portfolio_list


def load_from_env() -> tuple[str | None, list[str]]:
    """Load API key and portfolio list from environment / .env if present."""
    if ENV_PATH.exists():
        with ENV_PATH.open("r") as f:
            for line in f:
                if line.startswith("GEMINI_API_KEY="):
                    os.environ.setdefault("GEMINI_API_KEY", line.strip().split("=", 1)[1])
                elif line.startswith("PORTFOLIO_TICKERS="):
                    os.environ.setdefault("PORTFOLIO_TICKERS", line.strip().split("=", 1)[1])

    api_key = os.getenv("GEMINI_API_KEY")
    portfolio_raw = os.getenv("PORTFOLIO_TICKERS", "")
    portfolio_list = [t.strip().upper() for t in portfolio_raw.split(",") if t.strip()]
    return api_key, portfolio_list
