import random, json
with open('words.json', 'r') as file:
    data = json.load(file)
word = random.choice(data['words'])
print(word)