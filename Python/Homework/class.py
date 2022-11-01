# class Car:
#     def drive(self, speed):
#         print(speed)
#
#
# car1 = Car()
# car1.drive("200")
import random
import shutil
columns = shutil.get_terminal_size().columns

class Solder:
    def __init__(self,name, weapons, points, nationality = "arm"):
        self.name = name
        self.weapons = weapons
        self.nationality = nationality
        self.points =points

    def results(self):
        print("-------Result {}-------".format(self.name).center(columns))
        print("{} has {} points.".format(self.name, self.points).center(columns))
        for weapon in self.weapons:
            print("The weapon is: {}. Bullet numbers is: {}".format(weapon.weapon_name, weapon.number_of_bullet).center(columns))


    def shoot(self, weapon_type, solder):
        print("**************** {} has shoot to {} with {} ****************".format(self.name, solder.name, weapon_type.weapon_name).center(columns))
        solder.points -= weapon_type.get_points
        for i in self.weapons:
            if i.weapon_name == weapon_type.weapon_name:
                i.number_of_bullet -= 1
        self.results()
        solder.results()


class Weapon:
    def __init__(self, weapon_name, get_points, number_of_bullet):
        self.weapon_name = weapon_name
        self.number_of_bullet = number_of_bullet
        self.get_points = get_points

def war(solder1, solder2):
    print("Beginning Results For The Soldiers".center(columns))
    solder1.results()
    solder2.results()
    while solder1.points > 0 or solder2.points > 0:
        if solder1.points > solder2.points:
            winner = solder1.name
        elif solder2.points > solder1.points:
            winner = solder2.name
        elif solder1.points == solder2.points:
            winner = None

        if solder1.points <= 0 or solder2.points <= 0:
            if winner == None:
                print("Game over!!! No winner".center(columns))
            else:
                print("Game Over!!! The winner is {}".format(winner).center(columns))
            break
        solder1.shoot(random.choice(solder1.weapons), solder2)
        solder2.shoot(random.choice(solder2.weapons), solder1)




def main():
    weapon1 = Weapon("tank", 10, 7)
    weapon11 = Weapon("gun", 3, 20)
    weapon2 = Weapon("tank", 10, 7)
    weapon22 = Weapon("gun", 3, 20)
    weapons1 = [weapon1, weapon11]
    weapons2 = [weapon2, weapon22]
    alex = Solder("Alex", weapons1, 27)
    sam = Solder("Sam", weapons2, 27)
    # alex.shoot(weapon11, sam)
    # sam.shoot(weapon2, alex)
    war(alex, sam)


if __name__ == "__main__":
    main()




