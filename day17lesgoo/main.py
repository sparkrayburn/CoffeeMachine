class User:
    def __init__(self,user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0
        self.following = 0


    def follow(self, user):
        user.followers += 1
        user.following += 1


user_1 = User("001", "Abhinav")
print(user_1.id , user_1.name, user_1.followers)
user_2 = User("001", "King")
user_1.follow(user_2)
user_2.follow(user_1)
print(user_2.followers, user_2.following)
print(f"user 1 followers = {user_1.followers}\n","user 1 followoing =  {user_1.following}")