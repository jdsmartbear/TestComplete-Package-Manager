import os
import json
import zipfile
import tempfile
import shutil

from tcpm.download import downloadFile


REPO_ZIP_URL = (
    'https://github.com/jdsmartbear/'
    'TestComplete-Package-Manager/archive/refs/heads/main.zip'
)

PACKAGES_DIR = 'packages'


def run(args):
    if not args:
        print('Usage: tcpm install <package-name>')
        return

    packageName = args[0]
    projectRoot = os.getcwd()

    tmpDir = tempfile.mkdtemp()
    zipPath = os.path.join(tmpDir, 'repo.zip')

    print('Downloading package repository...')
    downloadFile(REPO_ZIP_URL, zipPath)

    with zipfile.ZipFile(zipPath, 'r') as zipRef:
        zipRef.extractall(tmpDir)

    extractedRoot = os.path.join(
        tmpDir,
        'TestComplete-Package-Manager-main'
    )

    packageRoot = os.path.join(
        extractedRoot,
        PACKAGES_DIR,
        packageName
    )

    manifestPath = os.path.join(packageRoot, 'manifest.json')

    if not os.path.exists(manifestPath):
        print(f'Package "{packageName}" is missing manifest.json.')
        return

    with open(manifestPath, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    print(f'Installing "{manifest["name"]}" into:')
    print(f'  {projectRoot}')

    for entry in manifest.get('files', []):
        fileName = entry['fileName']
        location = entry.get('location', '').strip()

        srcPath = os.path.join(packageRoot, location, fileName) \
            if location else os.path.join(packageRoot, fileName)

        if not os.path.exists(srcPath):
            print(f'Warning: Missing file "{fileName}" in package.')
            continue

        destDir = (
            os.path.join(projectRoot, location)
            if location
            else projectRoot
        )

        os.makedirs(destDir, exist_ok=True)
        shutil.copy2(srcPath, os.path.join(destDir, fileName))

    print('Install complete.')