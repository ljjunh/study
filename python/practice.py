import random

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed): # 생성자
        self.name = name # 객체가 만들어질때 자동호출
        self.hp = hp
        self.speed = speed
        print(f"{self.name} 유닛이 생성되었습니다.")

    def move(self, location):
        print(f"{self.name} : {location} 방향으로 이동합니다. [속도 {self.speed}]")

    def damaged(self, damage):
        print(f"{self.name} : {self.damage} 데미지를 입었습니다.")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
        if self.hp <= 0:
            print(f"{self.name} : 파괴되었습니다.")


# 공격 유닛(일반 유닛 클래스를 상속받아서 만듬)
class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed): 
        Unit.__init__(self, name, hp, speed) # Unit에서 name과 hp상속
        self.damage = damage

    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격 합니다. 공격력 : {self.damage}")
        

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 5, 1)
    
    #스팀팩
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print(f"{self.name} : 스팀팩을 사용합니다. (HP 10 감소)")
        else:
            print(f"{self.name} : 체력이 부족하여 스팀팩을 사용하지 않습니다.")

# 탱크
class Tank(AttackUnit):
    size_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 35, 1)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        if self.seize_mode == False:
            print(f"{self.name} : 시즈모드로 전환합니다.")
            self.damage *= 2
            self.seize_mode = True
        else:
            print(f"{self.name} : 시즈모드를 해제합니다.")
            self.damage /= 2
            self.seize_mode = False


# 날 수 있는 기능을 가진 클래스
class Flyable(Unit):
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
        
    def fly(self, name, location):
        print(f"{self.name} : {location} 방향으로 날라갑니다. [속도 {self.flying_speed}]")

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed = 0
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):
        self.fly(self.name, location)

# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False
    
    def clocking(self):
        if self.clocked == True:
            print(f"{self.name} : 클로킹 모드를 해제합니다.")
            self.clocked = False
        else:
            print(f"{self.name} : 클로킹 모드로 전환합니다.") 
            self.clocked = True

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

# 게임 시작
game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()

# 유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 부대 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# 공격 모드 준비(마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()
# 공격
for unit in attack_units:
    unit.attack("1시")

# 피해
for unit in attack_units:
    unit.damaged(random.randint(5, 21)) # 데미지 랜덤으로 받음 (5 ~ 20)

# 게임 종료
game_over()