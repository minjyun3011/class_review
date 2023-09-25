class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.full_name = f"{first_name} {family_name}"
        self.age = age
        
    def __str__(self):
        return f"{self.full_name}"
        return f"{self.age}"
    
    def age_judge(self):
        if (self.age < 20):
            return f"{1000}"
        elif (20 <= self.age < 65):
            return f"{1500}"
        elif (65 <= self.age):
            return f"{1200}"
        elif (self.age <= 3):
            return f"{0}"
        elif (75 <= self.age):
            return f"{500}"
        
    def info_csv(self):
        return f"{self.full_name},{self.age},{self.age_judge()}"
    
    def info_tab(self):
        return f"{self.full_name}   {self.age}  {self.age_judge()}"
    
    def info_psv(self):
        return f"{self.full_name}|{self.age}|{self.age_judge()}"


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)


print(ken)
print(tom)

print(ken.age)
print(tom.age)
print(ieyasu.age)

print(ken.age_judge())
print(tom.age_judge())
print(ieyasu.age_judge())

print(ken.info_csv())
print(tom.info_csv())
print(ieyasu.info_csv())

print(ken.info_tab())
print(tom.info_tab())
print(ieyasu.info_tab())

print(ken.info_psv())
print(tom.info_psv())
print(ieyasu.info_psv())

