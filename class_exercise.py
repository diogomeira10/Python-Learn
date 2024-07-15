class Entity:

    def attack(self):
        print(f'Attacking for {self.damage} damage!')


class Monster(Entity):

    def __init__(self, health, damage):
        # super().Attack(damage)
        self.health = health
        self.damage = damage

    def __repr__(self):
        return f'A monster with {self.health} hp'


monster = Monster(200,100)

print(monster) # Output : A monster with 200 hp
monster.attack() # Attacking for 100 damage!