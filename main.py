import os
import sys
from pathlib import Path

import requests

RELEASES_URL = "https://discord.com/api/v9/social-sdk/releases"
AUTHORIZATION = os.environ["AUTHORIZATION"]
version_file = Path("version")


def discover_latest() -> str:
    response = requests.get(RELEASES_URL, headers={"Authorization": AUTHORIZATION})

    if response.status_code != 200:
        print("Failed to get versions", sys.stderr)
        sys.exit(1)

    content = response.json()
    return content["latest_version"]


def download_latest(latest_version: str) -> str:
    response = requests.get(
        f"{RELEASES_URL}/{latest_version}", headers={"Authorization": AUTHORIZATION}
    )

    if response.status_code != 200:
        print("Failed to get artifacts", sys.stderr)
        sys.exit(1)

    content = response.json()
    download_url = content["artifacts"][0]["download_url"]
    filename = content["artifacts"][0]["filename"]
    response = requests.get(download_url, stream=True)

    with open(filename, "wb") as f:
        for chunk in response.iter_content(chunk_size=256):
            f.write(chunk)

    return filename


def main():
    latest_version = discover_latest()
    filename = download_latest(latest_version)

    print(filename)

    version_file.write_text(latest_version)


if __name__ == "__main__":
    main()
