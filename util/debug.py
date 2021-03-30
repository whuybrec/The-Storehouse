import io
from inspect import getframeinfo, stack
import time
import os
import aiohttp


BLACK = '\033[0;30m'
RED = '\033[0;31m'
GREEN = '\033[0;32m'
BROWN = '\033[0;33m'
BLUE = '\033[0;34m'
PURPLE = '\033[0;35m'
CYAN = '\033[0;36m'
GREY = '\033[0;37m'
YELLOW = '\033[1;33m'

DARK_GREY = '\033[1;30m'
LIGHT_RED = '\033[1;31m'
LIGHT_GREEN = '\033[1;32m'
LIGHT_BLUE = '\033[1;34m'
LIGHT_PURPLE = '\033[1;35m'
LIGHT_CYAN = '\033[1;36m'
WHITE = '\033[1;37m'

RESET = "\033[0m"
UNDERLINE = '\033[4m'
BOLD = "\x1b[1m"


def debug(message):
    caller = getframeinfo(stack()[1][0])
    print(f"{PURPLE}[{time.strftime('%d/%m %H:%M:%S')}] {RESET}"
          f"{CYAN}{BOLD}DEBUG{RESET} "
          f"{LIGHT_RED}{caller.filename[len(os.getcwd())+1:]} {caller.lineno}: {RESET}"
          f"{message}")


def info(message):
    caller = getframeinfo(stack()[1][0])
    print(f"{PURPLE}[{time.strftime('%d/%m %H:%M:%S')}] {RESET}"
          f"{CYAN}{BOLD}INFO{RESET} "
          f"{LIGHT_RED}{caller.filename[len(os.getcwd())+1:]} {caller.lineno}: {RESET}"
          f"{message}")


async def get_image_from_code(code):
    url = "https://carbonara.now.sh/api/cook/"
    json = {
        "code": code,
        "language": "python",
        "theme": "material",
        "fontFamily": "JetBrains Mono",
        "windowControls": False,
        "paddingHorizontal": "28px",
        "paddingVertical": "28px",
        "backgroundColor": "#28BBB2",
        "watermark": False,
        "squaredImage": False
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=json) as r:
            if r.status != 200:
                print(r.status)
                raise ConnectionError("Unable to get carbon.now image")
            f = io.BytesIO(await r.read())
    return f

