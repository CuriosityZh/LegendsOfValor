
#### main.py

```python
#!/usr/bin/env python3
import random

knight_orders = [
    "Order of the Silver Wolf – 'Honor in the Shadows' – Masters of silent warfare.",
    "Brotherhood of the Eternal Sun – 'Light Prevails' – Seekers of lost knowledge and justice.",
    "The Crimson Gauntlet – 'By Steel and Blood' – Ruthless knights known for their martial prowess.",
    "Wardens of the Obsidian Tower – 'Wisdom is Our Shield' – Protectors of forgotten relics.",
    "The Golden Stag – 'Strength Through Unity' – Defenders of the weak and protectors of sacred lands."
]

def get_random_order():
    return random.choice(knight_orders)

def main():
    print("Welcome to Legends of Valor!")
    print("Here's a randomly generated knight order:")
    print(get_random_order())

if __name__ == "__main__":
    main()
