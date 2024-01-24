class Unit:
    def __init__(self, name, hp, damage): # 생성자
        self.name = name # 객체가 만들어질때 자동호출
        self.hp = hp
        self.damage = damage
        print(f"{self.name} 유닛이 생성되었습니다.")
        print(f"체력 {self.hp}, 공격력 {self.damage}")

class AttackUnit:
    def __init__(self, name, hp, damage): 
        self.name = name 
        self.hp = hp
        self.damage = damage
        print(f"{self.name} 유닛이 생성되었습니다.")
        print(f"체력 {self.hp}, 공격력 {self.damage}")    

    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격 합니다.\
              공격력 : {self.damage}")
        
    def damaged(self, damage):
        print(f"{self.name} : {self.damage} 데미지를 입었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")

marine1 = AttackUnit("마린", 100, 5)
tank1 = AttackUnit("탱크", 200, 10)
marine1.attack(2)
marine1.damaged(60)
marine1.damaged(40)