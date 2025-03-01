class employee:
    # special method/magic-method/dunder-ethod-constructor
    def __init__(self):
        print("Strating executing attribute/data")
        self.id = 123
        self.salary = 50000
        self.designation = 'SDE'
        print("Attribute and data have been initiated")
    
    def travel(self,destination):
        print("This travel method was called maually")
        print(f"Employee is now travelling {destination}")

sam = employee()

# print(sam.salary)
sam.travel('Dubai')