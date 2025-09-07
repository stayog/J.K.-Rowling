import hashlib
import time
import random

class Rune:
    def __init__(self, symbol):
        self.symbol = symbol
        self.energy = random.randint(50, 150)

    def charge(self, value):
        self.energy += value
        return f"{self.symbol} charged to {self.energy}"

    def drain(self):
        drained = self.energy // 2
        self.energy -= drained
        return drained


def secret_hash(message):
    return hashlib.sha256(message.encode()).hexdigest()


def shifting_pattern(n=10):
    pattern = []
    for i in range(n):
        row = "".join(random.choice("#*.-") for _ in range(n))
        pattern.append(row)
    return "\n".join(pattern)


if __name__ == "__main__":
    rune = Rune("⚡")
    print(rune.charge(20))
    print("Drained energy:", rune.drain())

    msg = "Whispers in the code..."
    print("Secret hash:", secret_hash(msg))

    print("\nRandom Pattern:")
    print(shifting_pattern(12))

    time.sleep(1)
    print("Done at:", time.strftime("%Y-%m-%d %H:%M:%S"))
