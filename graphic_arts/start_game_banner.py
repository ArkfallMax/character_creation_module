from asciimatics.renderers import FigletText, Fire  # type: ignore
from asciimatics.renderers import SpeechBubble  # type: ignore

from asciimatics.scene import Scene  # type: ignore
from asciimatics.screen import Screen  # type: ignore
from asciimatics.effects import Print  # type: ignore
from asciimatics.exceptions import ResizeScreenError  # type: ignore
from pyfiglet import Figlet  # type: ignore
import sys


def animation(screen):
    scenes = []

    text = Figlet(font="banner", width=200).renderText("START GAME")
    print(text)
    effects = [
        Print(screen,
              Fire(screen.height, 80, text, 0.4, 40, screen.colours),
              0,
              speed=1,
              transparent=False,
              ),
        Print(screen,
              FigletText("Real Practic Game", "banner"),
              screen.height - 15,
              colour=Screen.COLOUR_WHITE,
              bg=Screen.COLOUR_WHITE,
              speed=1),
        Print(screen,
              SpeechBubble("Please press X - start game"),
              screen.height-5,
              speed=1, transparent=False)

    ]
    scenes.append(Scene(effects, -1))

    screen.play(scenes, stop_on_resize=True)


def run_screensaver():
    Screen.wrapper(animation)


if __name__ == "__main__":
    run_screensaver()
    sys.exit(0)
