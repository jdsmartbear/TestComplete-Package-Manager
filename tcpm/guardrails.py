import sys
import subprocess
from pathlib import Path

from tcpm.download import downloadFile


# ============================================================
# Constants
# ============================================================

STORES_CHILD_LINE = (
    '\t\t<child name="Stores" '
    'key="{5209DD15-2605-40DF-A046-0A90EFB0A928}" '
    'type="Stores" '
    'typeId="{5238AF17-5FE2-48FF-8BCC-9803A975A4F4}" '
    'pluginName="Stores" '
    'path="Stores\\Stores.tcStores" />\n'
)

FILES_TCFILES_URL = (
    'https://raw.githubusercontent.com/'
    'jdsmartbear/TestComplete-Package-Manager/main/'
    'mds-core/Files.tcFiles'
)

STORES_TCSTORES_URL = (
    'https://raw.githubusercontent.com/'
    'jdsmartbear/TestComplete-Package-Manager/main/'
    'mds-core/Stores.tcStores'
)


# ============================================================
# Guardrail A: Verify TestComplete Project directory
# ============================================================

def _hasValidMds(path: Path) -> bool:
    for p in path.iterdir():
        if p.is_file() and p.name.lower().endswith('.mds'):
            return True
    return False


def ensureProjectDirectory(commandName: str):
    cwd = Path.cwd()

    if _hasValidMds(cwd):
        return

    print(
        f'The {commandName} command can only be run in a TestComplete Project Folder, '
        'but no .mds file was found at the current directory.\n'
    )
    print('Please change the current directory to one that contains an .mds file and try again.\n')
    print('Example:\n')
    print('  cd "C:\\Users\\John.Smith\\TC Projects\\ABC Project Suite\\ABC Project"')
    print(f'  tcpm {commandName} <package-name>\n')

    sys.exit(1)


# ============================================================
# Guardrail B: Kill TestComplete / TestExecute processes
# ============================================================

def killTestCompleteProcesses():
    targets = ('testcomplete', 'testexecute')
    maxPasses = 10
    passes = 0

    while passes < maxPasses:
        passes += 1

        result = subprocess.run(
            ['tasklist'],
            capture_output=True,
            text=True
        )

        lines = result.stdout.lower().splitlines()
        pids = []

        for line in lines:
            for t in targets:
                if t in line:
                    parts = line.split()
                    if len(parts) >= 2 and parts[1].isdigit():
                        pids.append(parts[1])

        if not pids:
            return

        for pid in pids:
            subprocess.run(
                ['taskkill', '/F', '/PID', pid, '/T'],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

    print('Warning: Some TestComplete/TestExecute processes could not be terminated.')


# ============================================================
# Guardrail C: Ensure Stores child exists in .mds
# ============================================================

def storesCheck():
    mdsFiles = list(Path.cwd().glob('*.mds'))
    if not mdsFiles:
        return

    mdsPath = mdsFiles[0]
    text = mdsPath.read_text(encoding='utf-8')

    start = text.find('<children>')
    if start == -1:
        return

    end = text.find('</children>', start)
    if end == -1:
        return

    childrenBlock = text[start:end]

    if 'name="Stores"' in childrenBlock:
        return

    updatedText = (
        text[:end]
        + STORES_CHILD_LINE
        + '\t'
        + text[end:]
    )

    mdsPath.write_text(updatedText, encoding='utf-8')


# ============================================================
# Guardrail D: Ensure Stores filesystem exists & is valid
# ============================================================

def storesFilesCheck():
    projectRoot = Path.cwd()

    storesDir = projectRoot / 'Stores'
    filesDir = storesDir / 'Files'
    tcpmDir = filesDir / 'TCPM'

    filesTcFilesPath = storesDir / 'Files.tcFiles'
    storesTcStoresPath = storesDir / 'Stores.tcStores'
    activityJsonPath = tcpmDir / 'activity.json'

    tcpmDir.mkdir(parents=True, exist_ok=True)

    if not storesDir.exists():
        storesDir.mkdir(parents=True, exist_ok=True)

        downloadFile(FILES_TCFILES_URL, filesTcFilesPath)
        downloadFile(STORES_TCSTORES_URL, storesTcStoresPath)

    else:
        if not filesTcFilesPath.exists():
            downloadFile(FILES_TCFILES_URL, filesTcFilesPath)

        if not storesTcStoresPath.exists():
            downloadFile(STORES_TCSTORES_URL, storesTcStoresPath)

    if not activityJsonPath.exists():
        activityJsonPath.write_text('[]', encoding='utf-8')