import urllib.request
from pathlib import Path


def downloadFile(url: str, destPath):
    destPath = Path(destPath)
    destPath.parent.mkdir(parents=True, exist_ok=True)

    urllib.request.urlretrieve(url, destPath)