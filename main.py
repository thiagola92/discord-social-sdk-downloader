import json
import re
from pathlib import Path

import requests

RSS_URL = "https://docs.discord.com/developers/change-log/rss.xml"
RSS_CACHE = "rss.xml"
VERSION_FILE = "version.json"


def get_rss() -> str:
    rss_file = Path(RSS_CACHE)

    if rss_file.exists():
        return rss_file.read_text()

    response = requests.get(RSS_URL)

    if response.status_code != 200:
        return ""

    rss_file.write_text(response.text)

    return rss_file.read_text()


def get_version(rss: str) -> dict:
    version_file = Path(VERSION_FILE)

    # Delete file at any moment so we can test again.
    if version_file.exists():
        biggest = json.loads(version_file.read_text())
    else:
        biggest = {"major": 0, "minor": 0, "patch": 0, "collected": False}

    for result in re.findall(r"\n +<title><!\[CDATA\[(.+)\]\]>", rss):
        if result.startswith("Discord Social SDK"):
            for version in re.findall(r"(\d+).(\d+).(\d+)", result):
                major = int(version[0])
                minor = int(version[1])
                patch = int(version[2])

                if major < biggest["major"]:
                    continue
                elif major > biggest["major"]:
                    biggest["major"] = major
                    biggest["minor"] = minor
                    biggest["patch"] = patch
                    continue

                if minor < biggest["minor"]:
                    continue
                elif minor > biggest["minor"]:
                    biggest["major"] = major
                    biggest["minor"] = minor
                    biggest["patch"] = patch
                    continue

                if patch < biggest["patch"]:
                    continue
                elif patch > biggest["patch"]:
                    biggest["major"] = major
                    biggest["minor"] = minor
                    biggest["patch"] = patch
                    continue

    version_file.write_text(json.dumps(biggest))

    return biggest


def main():
    rss = get_rss()
    print(get_version(rss))


if __name__ == "__main__":
    main()
