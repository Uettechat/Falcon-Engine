version = (0, 1, 0)  # major, minor, patch
print(f"Launching FalconEngine v{version[0]}.{version[1]}.{version[2]}...")

import os
import sys
import platform

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"
import pygame

pygame.init()

print(f"Using Python {platform.python_version()}, pygame {pygame.version.ver}, SDL {pygame.version.SDL}, {platform.system()} {platform.version()}")
