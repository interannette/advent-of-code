from typing import Dict, List, Optional
from dotenv import load_dotenv
import os
import requests
import sys
import re


def get_url_for_day(day: int, year: int = 2022) -> str:
    return f"https://adventofcode.com/{year}/day/{day}/input"


def get_cookie() -> Dict[str, str]:
    load_dotenv()
    return {"session": os.getenv("aoc_session")}


def attempt_day_int() -> Optional[int]:
    m = re.search(".*day(\d\d)\.py", sys.argv[0])
    if m:
        return int(m.group(1))
    else:
        return None


def get_input_for_day(day: Optional[int] = None) -> List[str]:

    if not day:
        day = attempt_day_int()
        if not day:
            raise Exception("Unable to determine day.")

    r = requests.get(url=get_url_for_day(day), cookies=get_cookie())
    lines = r.text.split("\n")
    if lines[-1] == "":
        lines = lines[:-1]
    return lines
