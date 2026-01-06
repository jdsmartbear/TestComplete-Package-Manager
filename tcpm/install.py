import os
import shutil
import zipfile
import tempfile

from tcpm.download import downloadFile

REPO_ZIP_URL = 'https://github.com/jdsmartbear/TestComplete-Package-Manager/archive/refs/heads/main.zip'
PACKAGES_DIR = 'packages'


def run(args):
    if not args:
        print('Usage: tcpm install <package-name>')
        return

    packageName = args[0]
    cwd = os.getcwd()

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

    packagePath = os.path.join(
        extractedRoot,
        PACKAGES_DIR,
        packageName
    )

    if not os.path.exists(packagePath):
        print(f'Package "{packageName}" not found.')
        return

    print(f'Installing "{packageName}" into:')
    print(f'  {cwd}')

    for item in os.listdir(packagePath):
        src = os.path.join(packagePath, item)
        dst = os.path.join(cwd, item)

        if os.path.isdir(src):
            shutil.copytree(src, dst, dirs_exist_ok=True)
        else:
            shutil.copy2(src, dst)

    print('Install complete.')