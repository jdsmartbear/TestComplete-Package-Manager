import os
import json
import shutil
import zipfile
import tempfile

from tcpm.download import downloadFile


REPO_ZIP_URL = (
    'https://github.com/jdsmartbear/'
    'TestComplete-Package-Manager/archive/refs/heads/main.zip'
)

PACKAGES_DIR = 'packages'
MANIFEST_FILE = 'manifest.json'


def run(args):
    if not args:
        print('Usage: tcpm install <package-name>')
        return

    packageName = args[0]
    projectRoot = os.getcwd()

    tmpDir = tempfile.mkdtemp()
    zipPath = os.path.join(tmpDir, f'{packageName}.zip')

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

    if not os.path.isdir(packageRoot):
        print(f'Package "{packageName}" not found.')
        return

    manifestPath = os.path.join(packageRoot, MANIFEST_FILE)

    if not os.path.isfile(manifestPath):
        print(f'Error: {MANIFEST_FILE} not found in package "{packageName}".')
        return

    with open(manifestPath, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    files = manifest.get('files', [])

    if not files:
        print(f'Warning: No files defined in {MANIFEST_FILE}.')
        return

    print(f'Installing "{packageName}" into:')
    print(f'  {projectRoot}')

    for entry in files:
        fileName = entry.get('fileName')
        location = entry.get('location', '').strip()

        if not fileName:
            print('Warning: Skipping manifest entry with no fileName.')
            continue

        srcPath = os.path.join(packageRoot, fileName)

        if not os.path.isfile(srcPath):
            print(f'Warning: Missing file "{fileName}" in package.')
            continue

        destDir = (
            os.path.join(projectRoot, location)
            if location
            else projectRoot
        )

        os.makedirs(destDir, exist_ok=True)

        destPath = os.path.join(destDir, fileName)

        shutil.copy2(srcPath, destPath)

    print('Install complete.')