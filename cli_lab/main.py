# cli_lab/main.py
from cli_lab.levels import level1_intro

def main():
    print("=== CLI Linux Lab ===")
    print("1) Level 1 - Intro Challenge")
    print("0) Exit")
    choice = input("Select a level: ").strip()

    if choice == "1":
        level1_intro.main()
    else:
        print("Goodbye!")

if __name__ == "__main__":
    main()

