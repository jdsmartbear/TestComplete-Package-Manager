import sys
from tcpm import install, uninstall, list, version

def main():
    if len(sys.argv) < 2:
        print('Usage: tcpm <command> [args]')
        return

    cmd = sys.argv[1]

    if cmd in ('install', 'i'):
        install.run(sys.argv[2:])
    elif cmd == 'uninstall':
        uninstall.run(sys.argv[2:])
    elif cmd == 'list':
        list.run()
    elif cmd in ('-v', '--version'):
        version.run()
    else:
        print(f'Unknown command: {cmd}')

if __name__ == '__main__':
    main()