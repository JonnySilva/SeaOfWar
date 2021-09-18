import sys
from utils.MESSAGES import Messages as MESSAGE
from console.screens import Screens as screen

def main():
    screen.menu()
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        MESSAGE.MESSAGE_FORCE_EXIT()
        sys.exit()
    