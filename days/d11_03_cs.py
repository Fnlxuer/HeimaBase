class Player:
    def __init__(self, role):
        self.role = role
        self.hp = 100
        self.gun = None

    def attack(self, enemy, count=10):
        if self.gun is None:
            print("%s have no gun!" % self.role)
        elif self.gun.bullet_count == 0:
            self.gun.add_bullet(count)
        else:
            self.gun.shoot(enemy)

    def hurt(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print("%s died!" % self.role)
        else:
            print("%s is injured! hp is %d" % (self.role, self.hp))

    def __str__(self):
        if self.hp <= 0:
            return "%s died!" % self.role
        else:
            if self.gun is None:
                return "you are %s, hp: %d, you have no gun" % (self.role, self.hp)
            else:
                return "you are %s, hp: %d, gun: %s" % (self.role, self.hp, self.gun)


class Gun:
    def __init__(self, modal, damage):
        self.type = modal
        self.damage = damage
        self.bullet_count = 30

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self, enemy):
        if self.bullet_count == 0:
            print("has no bullet")
        else:
            self.bullet_count -= 3
            enemy.hurt(self.damage)

    def __str__(self):
        return "type: %s, damage: %d, bullet_count: %d" % (self.type, self.damage, self.bullet_count)


ak47 = Gun("AK47", 30)
xm = Player("JC")
lw = Player("TF")
lw.gun = ak47
for i in range(4):
    lw.attack(xm)
print(lw)
print(xm)
