import random

def main():
  print('You rolled a die')
  rolls = 3
  sum = 0
  for i range(0, rolls):
	roll = random.randint(1,6)
	dice_sum += roll
	print(f'You rolled a {roll}')
	print(f'You have rolled a total of {dice_sum}')

if __name__== "__main__":
  main()
