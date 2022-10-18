users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
print(users['Jonathan']['twitter'])

# 2. Get Erik's hometown
print(users['Erik']['home_town'])

# 3. Get the list of Erik's lottery numbers
print(users['Erik']['lottery_numbers'])

# 4. Get the species of Avril's pet Monty
species = users['Avril']['pets']
species1 = species[0]['species']
print(species1)

# 5. Get the smallest of Erik's lottery numbers
lotto_num = users['Erik']['lottery_numbers']
lotto_num1 = min(lotto_num)
print(lotto_num1)

# 6. Return a list of Avril's lottery numbers that are even
list = users['Avril']['lottery_numbers']
list1 = []
for num in list:
    if num % 2 == 0:
        list1.append(num)
print(list1)

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
lotto = users['Erik']['lottery_numbers']
lotto.append(7)
print(lotto)

# 8. Change Erik's hometown to Edinburgh
users['Erik']['home_town'] = 'Edinburgh'
print(users['Erik']['home_town'])

# 9. Add a pet dog to Erik called "fluffy"
dog = {
  "name": "fluffy",
  "species": "dog"
}
new_pet = users['Erik']['pets']
new_pet.append(dog)
print(users['Erik']['pets'])

# 10. Add another person to the users dictionary
another = {
  "David": {
    "twitter": "dvdjms74",
    "lottery_numbers": [1, 2, 3, 4, 5, 6],
    "home_town": "Derby",
    "pets": [
      {
        "name": "Scary Mary",
        "species": "t-rex"
      },
      {
        "name": "blue",
        "species": "whale"
      }
    ]
  }
}
users.update(another)
print(users)
