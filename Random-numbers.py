# Source https://www.youtube.com/watch?v=KzqSDvzOFNA&ab_channel=CoreySchafer
import random

value = random.random()   #random float number between 0 and 1 (except 1)
print(value)
################################################################################################################
value = random.uniform(1,10)   #random float nuber between 0 and 10 (except 10)
print(value)
################################################################################################################
value = random.randint(1,10)
print(value)
################################################################################################################
greetings = ['Hello', 'Hi', 'Hey', 'Howdy', 'Hola']

value = random.choice(greetings)   #random choise from a list
print(value)
print(value + ", Dean!")
################################################################################################################
colours = ['Red', 'Black', 'Green']

results = random.choices(colours, k=10)  # 10 random results from a list
print(results)

results = random.choices(colours, weights=[18, 18, 2], k=10)
# 10 random results from a list + mix the chances to be selected 18/38, 18/38, 2/38 - casino
print(results)
################################################################################################################
deck = list(range(1, 53)) # make a list of numbers from 1 to 52
random.shuffle(deck)    # shuffle the numbers from 1 to 52
print(deck)
################################################################################################################
hand = random.sample(deck, k=5) # sample of 5 unique numbers from 'deck'
print(hand)

