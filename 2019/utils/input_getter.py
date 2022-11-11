from typing import Dict, List
from dotenv import load_dotenv
import os
import requests


def get_url_for_day(day: int) -> str:
    return f"https://adventofcode.com/2019/day/{day}/input"


def get_cookie() -> Dict[str, str]:
    load_dotenv()
    return {"session": os.getenv("aoc_session")}


def get_input_for_day(day: int) -> List[str]:
    r = requests.get(url=get_url_for_day(day), cookies=get_cookie())
    lines = r.text.split("\n")
    return lines
