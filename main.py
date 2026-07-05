from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))

from night_security_shift.app import GameApp  # noqa: E402


def main():
    app = GameApp()
    app.run()


if __name__ == "__main__":
    main()