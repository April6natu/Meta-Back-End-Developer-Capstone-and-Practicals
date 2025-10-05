class Employees:
    def __init__(self, name, lastname) -> None:
        self.name = name
        self.lastname = lastname
        
class Supervisors(Employees):
    def __init__(self, name, lastname, password) -> None:
        super().__init__(name, lastname)
        self.password = password
        
class Chefs(Employees):
    def leave_request(self, days):
        return "May I take a leave for " + str(days) + " days"
    
faith = Supervisors("Faith", "Tamba", "password123")

vickey = Chefs("Vickey", "E")
courage = Chefs("Courage", "F")

print(vickey.leave_request(5))
print(faith.password)
print(vickey.name)
print(courage.lastname)