import sys

from tcpm.guardrails import (
    ensureProjectDirectory,
    killTestCompleteProcesses,
    storesCheck,
    storesFilesCheck
)

from tcpm import install, uninstall, list, version


def main():
    if len(sys.argv) < 2:
        print('Usage: tcpm <command> [args]')
        sys.exit(1)

    cmd = sys.argv[1]
    args = sys.argv[2:]

    if cmd in ('install', 'i'):
        ensureProjectDirectory('install')
        killTestCompleteProcesses()
        storesCheck()
        storesFilesCheck()
        install.run(args)

    elif cmd == 'list':
        ensureProjectDirectory('list')
        storesCheck()
        storesFilesCheck()
        list.run(args)

    elif cmd == 'uninstall':
        ensureProjectDirectory('uninstall')
        killTestCompleteProcesses()
        storesCheck()
        storesFilesCheck()
        uninstall.run(args)

    elif cmd in ('-v', '--version'):
        version.run()

    else:
        print(f'Unknown command: {cmd}')
        sys.exit(1)


if __name__ == '__main__':
    main()
