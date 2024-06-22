import random
import time

user_wins = 0
cpu_wins = 0

# r < p, p < s, s < r

def main():
    rpss = ["Rock...", "Paper...", "Scissors...", "Shoot!"]
    intro(rpss)
    battle()

def intro(intro_words):
    for item in intro_words:
        print(item)
        time.sleep(1)

rps = ["Rock", "Paper", "Scissors"]

def battle():
    global user_wins, cpu_wins
    while True:
        cpu_pick = random.choice(rps)
        pick = input("Enter Rock, Paper, or Scissors: ").capitalize()
        if pick == "Paper":
            if cpu_pick == "Rock":
                print(f"You win! CPU picked {cpu_pick}")
                user_wins += 1
            elif cpu_pick == "Scissors":
                print(f"You lose! CPU picked {cpu_pick}")
                cpu_wins += 1
            else:
                print(f"Draw! CPU also picked {cpu_pick}")
        elif pick == "Scissors":
            if cpu_pick == "Paper":
                print(f"You win! CPU picked {cpu_pick}")
                user_wins += 1
            elif cpu_pick == "Rock":
                print(f"You lose! CPU picked {cpu_pick}")
                cpu_wins += 1
            else:
                print(f"Draw! CPU also picked {cpu_pick}")
        elif pick == "Rock":
            if cpu_pick == "Scissors":
                print(f"You win! CPU picked {cpu_pick}")
                user_wins += 1
            elif cpu_pick == "Paper":
                print(f"You lose! CPU picked {cpu_pick}")
                cpu_wins += 1
            else:
                print(f"Draw! CPU also picked {cpu_pick}")
        else:
            print("Invalid input, please try again.")

        print(f"Score: You {user_wins} - CPU {cpu_wins}")

if __name__ == "__main__":
    main()
