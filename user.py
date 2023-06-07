

class User:


    def __init__(self, first_name, last_name, email, age, is_reward_member = False, gold_card_points = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = is_reward_member
        self.gold_card_points = gold_card_points

    def display_info(self):
        print(f'{self.first_name}\n{self.last_name}\n{self.email}\n{self.age}\n{self.is_reward_member}\n{self.gold_card_points}')
        return self

    def enroll(self):
        self.is_reward_member= True
        self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - amount
        return self



user1 = User('Bruce', 'Banner', 'BruceB@dojo.com', 44)
user2 = User('Tony', 'Stark', 'TStark@dojo.com', 40)
user3 = User('Peter', 'Parker','PP@dojo.com', 17)





user1.enroll().spend_points(50).display_info()

user2.enroll().spend_points(80).display_info()

user3.display_info()









