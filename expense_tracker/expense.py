class Expense:
    def __init__(self, amount,category,date, note=""):
        # instance variables
        self.amount = amount
        self.category = category
        self.date = date
        self.note = note

    def __str__(self):
        return f"{self.date} , {self.category} ,{self.amount} ,{self.note}"
    

# with this "__str__" while printing it shows the result else it shows <Expense object at 0x0834bf>
# exp1 = Expense(250, "Food", "2024-07-19", "Lunch")
# print(exp1)