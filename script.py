import random
import time

print("Lets go gambling!")
money = int(input("How much do you want to gamble? "))
bet = int(input("Set your bet! "))

gamble = input("Do you want to start gambling? (yes/no) ").lower()
while money > 0:
  r1 = random.randint(1, 10)
  r2 = random.randint(1, 10)
  r3 = random.randint(1, 10)
  money -= bet

  time.sleep(0.5)
  print(f"[{r1}]", end="", flush=True)
  time.sleep(0.5)
  print(f"[{r2}]", end="", flush=True)
  time.sleep(0.5)
  print(f"[{r3}]", end="", flush=True)
  time.sleep(1)
  print()
  if r1 == r2 == r3:
    print("DING DING DING, You just hit the jackpot!")
    money += 10 * bet
  elif r1 == r2 or r1 == r3 or r2 == r3:
    print("You win!")
    money += 2 * bet
  else:
    print("You lose!")
  print()
  time.sleep(0.75)
  print(f"You new balance is: {money}$ ")
  print("-"* 40)
  time.sleep(0.5)

print("You lost all your money!")
  


  

  
