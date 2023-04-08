class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Are they a rewards member? {self.is_rewards_member}")
        print(f"Gold Card points: {self.gold_card_points}")
        print("-" * 20)
        return self
    
    def enroll(self):
        if self.is_rewards_member == True:
            print(f"User: {self.first_name} {self.last_name} is already a member.")
            print("-" * 20)
            return self
        else:
            self.is_rewards_member = True
            self.gold_card_points += 200
            return self
    
    def spend_points(self, amount):
        if amount < self.gold_card_points:
            self.gold_card_points -= amount
            return self
        else:
            print(f"User: {self.first_name} {self.last_name} does not have enough points.")
            print("-" * 20)
            return self


v_mars = User("Veronica", "Mars", "vmars@marsinvestigations.com", 32)
v_mars.display_info().enroll()

k_mars = User("Keith", "Mars", "kmars@marsinvestigations.com", 63)
mac = User("Cindy", "Mackenzie", "mac@marsinvestigations.com", 31)

v_mars.spend_points(50).display_info().enroll()
k_mars.enroll().spend_points(80).display_info()
mac.display_info().spend_points(40)