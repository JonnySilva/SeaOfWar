import sys
from shared.MESSAGES import Messages as MESSAGE
from src.screens import Screens as screen

def main():
    screen.menu()
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        MESSAGE.MESSAGE_FORCE_EXIT()
        sys.exit()
    