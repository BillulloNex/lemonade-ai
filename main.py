import random
import time

def init():
    """Initialize random values"""
    random.seed()
    return random.randint(1, 100)

def loop():
    """A loop function that performs random operations"""
    while True:
        value = random.random()
        print(f"Current value: {value}")
        time.sleep(1)
        if value > 0.9:
            break
    return value