import os
import sys
from pathlib import Path

import requests

RELEASES_URL = "https://discord.com/api/v9/social-sdk/releases"
version_file = Path("version")


def main():
    authorization = os.getenv("AUTHORIZATION", None)
    response = requests.get(RELEASES_URL, headers={"Authorization": authorization})

    if response.status_code != 200:
        print("Failed to get versions", sys.stderr)
        print(response.status_code, sys.stderr)
        print(response.content, sys.stderr)
        print(response.headers, sys.stderr)
        return

    content = response.json()
    latest_version = content["latest_version"]

    if latest_version == version_file.read_text():
        print("No new version")
        return

    response = requests.get(
        f"{RELEASES_URL}/{latest_version}", headers={"Authorization": authorization}
    )

    if response.status_code != 200:
        print("Failed to get artifacts", sys.stderr)
        print(response.status_code, sys.stderr)
        print(response.content, sys.stderr)
        print(response.headers, sys.stderr)
        return

    content = response.json()
    download_url = content["artifacts"][0]["download_url"]
    filename = content["artifacts"][0]["filename"]
    response = requests.get(download_url, stream=True)

    with open(filename, "wb") as f:
        for chunk in response.iter_content(chunk_size=256):
            f.write(chunk)

    version_file.write_text(latest_version)


if __name__ == "__main__":
    main()
