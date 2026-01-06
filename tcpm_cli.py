import sys
import ctypes

from tcpm.main import main as tcpmMain

def ensureAdmin():
    try:
        if not ctypes.windll.shell32.IsUserAnAdmin():
            print(
                'This command must be run from an elevated (Administrator) command prompt.\n'
                'Please right-click Command Prompt and choose "Run as administrator", '
                'then try again.'
            )
            sys.exit(1)
    except Exception:
        sys.exit(1)

if __name__ == '__main__':
    ensureAdmin()
    tcpmMain()