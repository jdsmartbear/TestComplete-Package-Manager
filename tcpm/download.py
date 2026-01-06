from urllib.request import urlopen
from pathlib import Path

def downloadFile(url, targetPath):
    targetPath = Path(targetPath)
    with urlopen(url) as resp:
        targetPath.write_bytes(resp.read())