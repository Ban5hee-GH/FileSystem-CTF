import os
import time

# Global variables for game state
CURRENT_DIR = "C:\\Users\\User"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(level_title):
    clear_screen()
    width = 70
    print("*" * width)
    print(f"** {level_title} **".center(width))
    print("*" * width)
    print("| SYSTEM:   Windows 10 (Simulated) - RESTRICTED SHELL")
    print("| USER:     user\\desktop-pc234")
    print("+" + "-" * width + "+")
    print()

def print_objectives(objectives, hint):
    print(":: CURRENT MISSION OBJECTIVES ::")
    for obj in objectives:
        print(f" [!] {obj}")
    print(f"\n >> HINT: {hint}")
    print("-" * 50)
    print()

def print_success(message):
    print("\n" + "="*60)
    print(f" SUCCESS: {message}")
    print("="*60)
    input(" Press ENTER to proceed to the next level...")

def generic_cmd_handler(cmd, args):
    """Handles standard commands like help, exit, whoami"""
    if cmd in ["cls", "clear"]:
        clear_screen()
        return True
    elif cmd == "help":
        print("\n AVAILABLE COMMANDS: DIR, TYPE, IPCONFIG, PING, CLS, EXIT")
        return True
    elif cmd == "whoami":
        print("user\\desktop-pc234")
        return True
    elif cmd == "exit":
        print("Exiting...")
        return "EXIT"
    return False