import time

# === ANSI Escape Codes ===
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
RED = "\033[31m"
CLS = "\033[2J\033[H"  # Clear screen

# Print the initial banner once
print(CLS)
print(f"""{BOLD}{YELLOW}
                           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                           @_________ _______  _______  _______ _________ _       _______  _       @
                           @\__   __/(  ____ \(  ____ )(        )\__   __/( (     /|(  ___  )( \      @
                           @   ) (   | (    \/| (    )|| () () |   ) (   |  \   ( || (   ) || (      @
                           @   | |   | (__    | (____)|| || || |   | |   |   \ | || (___) || |      @
                           @   | |   |  __)   |     __)| |(_)| |   | |   | (\ \) ||   ___  || |      @
                           @   | |   | (      | (\ (   | |   | |   | |   | | \  || (   ) || |      @
                           @   | |   | (____/\| ) \ \__| )   ( |___) (___| )   \ || )   ( || (____/\@
                           @   )_(   (_______/|/   \__/|/     \|_______/|/     )_)|/     \|(_______/@
                           @ _______           _         _______  _______  _       _______        @
                           @(  ____ \|\     /|( (     /| / ___   )(  ___  )( (     /|(  ____ \       @
                           @| (    \/| )   ( ||  \   ( | \/   )  || (   ) ||  \   ( || (    \/       @  
                           @| (__    | |   | ||   \ | |      /   )| |   | ||   \ | || (__            @
                           @|  __)   | |   | || (\ \) |     /   / | |   | || (\ \) ||  __)           @
                           @| (      | |   | || | \   |    /   /  | |   | || | \   || (              @
                           @| )      | (___) || )   \ |   /   (_/\| (___) || )   \ || (____/\       @
                           @|/       (_______)|/     )_) (_______/(_______)|/     )_)(_______/       @
                           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
{RESET}""")

print(f"{YELLOW}Welcome to PyTerminal Fun Zone!{RESET}")
print(f"{GREEN}---------------------------------{RESET}\n")

# Use a while loop to keep the program running until the user exits
while True:
    # Menu
    print(f"{BOLD}Main Menu:{RESET}")
    print("[1] Quiz Game")
    print("[2] Secret Encoder/Decoder")
    print("[3] Pattern Printer")
    print("[0] Exit\n")

    choice = input("Enter your choice: ").strip()

    # === QUIZ GAME ===
    if choice == "1":
        score = 0
        questions = [
            ("Which operator is used for membership in Python?\n(a) is\n(b) in\n(c) ==\n> ", "b"),
            ("What is ASCII value of 'A'?\n(a) 65\n(b) 97\n(c) 66\n> ", "a"),
            ("Which loop runs at least once?\n(a) for\n(b) while\n(c) do-while (conceptual)\n> ", "c")
        ]

        print(f"{CYAN}\nStarting Quiz...{RESET}\n")
        for q, correct in questions:
            answer = input(q).strip().lower()

            # membership check
            if answer not in ["a", "b", "c"]:
                print(f"{RED}Invalid option!{RESET}\n")
                continue

            # identity operator
            if answer is None:
                print(f"{RED}You gave no answer!{RESET}\n")
                continue

            if answer == correct:
                print(f"{GREEN}Correct!{RESET}\n")
                score += 1
            else:
                print(f"{RED}Wrong!{RESET}\n")

        print(f"Your Score: {score}/{len(questions)}")
        print(f"{YELLOW}{'Great Job!' if score == len(questions) else 'Keep Practicing!'}{RESET}\n")
        time.sleep(2)  # Pause before returning to menu

    # === ENCODER / DECODER ===
    elif choice == "2":
        print(f"{CYAN}\nSecret Encoder/Decoder{RESET}\n")
        text = input("Enter text: ")
        mode = input("Encode (e) or Decode (d)? ").lower()

        result = ""
        for ch in text:
            if mode == "e":
                result += chr(ord(ch) + 2)
            elif mode == "d":
                result += chr(ord(ch) - 2)
            else:
                result = "Invalid mode!"
                break

        print(f"\n{GREEN}Result: {result}{RESET}\n")
        time.sleep(2)  # Pause before returning to menu

    # === PATTERN PRINTER ===
    elif choice == "3":
        print(f"{CYAN}\nPattern Printer{RESET}\n")
        try:
            n = int(input("Enter number of rows: "))
        except ValueError:
            print(f"{RED}Invalid input. Please enter a number.{RESET}")
            time.sleep(2)
            continue

        print(f"\n{YELLOW}Triangle Pattern:{RESET}")
        for i in range(1, n+1):
            print("*" * i)

        print(f"\n{YELLOW}Pyramid Pattern:{RESET}")
        for i in range(1, n+1):
            print(" "*(n-i) + "*"*(2*i-1))

        print(f"\n{YELLOW}Hollow Box:{RESET}")
        for i in range(n):
            for j in range(n):
                if i==0 or i==n-1 or j==0 or j==n-1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print("\n")
        time.sleep(2)  # Pause before returning to menu

    # === EXIT ===
    elif choice == "0":
        print(f"{RED}\nGoodbye!{RESET}")
        time.sleep(1)
        break  # Exit the while loop

    # === INVALID CHOICE ===
    else:
        print(f"{RED}Invalid choice! Please enter a number from the menu.{RESET}")
        time.sleep(2) # Pause before returning to menu
        
    print(CLS) # Clear the screen before showing the menu again

