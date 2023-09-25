class Customer:
    def __init__(self, first_name, family_name):
        self.first_name = first_name
        self.family_name = family_name
        self.full_name = f"{first_name} {family_name}"

    def __str__(self):
        return f"{self.full_name}"


ken = Customer(first_name="Ken", family_name="Tanaka")
tom = Customer(first_name="Tom", family_name="Ford")

print(ken)
print(tom)


