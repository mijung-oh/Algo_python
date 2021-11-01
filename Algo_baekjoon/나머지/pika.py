from random import randint

class Pokemon:
    
    def __init__(self, name):
        self.name = name
        self.level = 5
        self.hp = self.level * 20
        self.exp = 0
    
    @staticmethod
    def bark():
        print('pikachu')
        
#     @classmethod
#     def game_start(cls, pika1, pika2):
        
#         while pika1.hp > 0 and pika2.hp > 0: ## 둘 다 살아있으면 
            
#             ## 먼저 공격할 대상 정하기
#             target = cls.random_order(pika1, pika2)
#             not_target = pika1 if target != pika1 else pika2
            
#             ## 어떤 공격할지 정하기
#             if cls.random_attack() == 1:
#                 target.body_attack(not_target)
#             else:
#                 target.thousond_volt(not_target)
    
    @staticmethod
    def game_start(self,pika2):
        
        while self.hp > 0 and pika2.hp > 0: ## 둘 다 살아있으면 
            
            ## 먼저 공격할 대상 정하기
            target = self.random_order(self, pika2)
            not_target = self if target != self else pika2
            
            ## 어떤 공격할지 정하기
            if self.random_attack() == 1:
                target.body_attack(not_target)
            else:
                target.thousond_volt(not_target)
                
    
    def random_order(self, pika1, pika2):
        if randint(1,2) == 1:
            return pika1
        else: 
            return pika2
        
    @staticmethod
    def random_attack():
        if randint(1,2) == 1:
            return 1
        else:
            return 2
        
    def body_attack(self, pika):
        pika.hp -= self.level * 5
        print(f'{self.name} 🤜🤜🤜 {pika.name} 🩸🩸🩸 몸통박치기 🩸🩸🩸')
        if pika.hp <= 0:## 상대방 쓰러뜨리면
            print('GAMEOVER')
            print(f'{self.name} 승! 👏🙌')
            self.exp += pika.level * 15
            if self.exp == self.level * 100:
                print(f'{self.name} 레벨업')
                self.level += 1
                self.exp = 0
    
    def thousond_volt(self, pika):
        pika.hp -= self.level * 7
        print(f'{self.name} 🤜🤜🤜 {pika.name} 🌟🌟🌟 십만볼트 🌟🌟🌟')
        if pika.hp <= 0:## 상대방 쓰러뜨리면
            print('GAMEOVER')
            print(f'{self.name} 승! 👏🙌')
            self.exp += pika.level * 15
            if self.exp == self.level * 100:
                print(f'{self.name} 레벨업')
                self.level += 1
                self.exp = 0

p1 = Pokemon('미정카츄')
p2 = Pokemon('용재카츄')
Pokemon.game_start(p1,p2)