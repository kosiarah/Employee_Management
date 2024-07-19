class Staff:
    def __init__(self, name, date_of_birth, gender, email, salary, address, start_date, position):
        self.name = name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.email = email
        self.salary = salary
        self.address = address
        self.start_date = start_date
        self.position = position


    def __str__(self):
        return f"Name: {self.name}, Date of Birth: {self.date_of_birth}, Gender: {self.gender}, Email: {self.email}, Salary: {self.salary}, Address: {self.address}, Start Date: {self.start_date}, Position: {self.position}"


    def update_name(self, new_name):
        self.name = new_name

    def update_date_of_birth(self, new_date_of_birth):
        self.date_of_birth = new_date_of_birth

    def update_gender(self, new_gender):
        self.gender = new_gender

    def update_email(self, new_email):
        self.email = new_email

    def update_salary(self, new_salary):
        self.salary = new_salary

    def update_address(self, new_address):
        self.address = new_address  

    def update_start_date(self, new_start_date):
        self.start_date = new_start_date

    def update_position(self, new_position):
        self.position = new_position
        


class Department:
    def __init__ (self, name, staff_size, head_of_department, location):
        self.name = name
        self.staff_size = staff_size
        self.head_of_department = head_of_department
        self.location = location

        self.staffs = []

    def add_staff(self, staff):
        self.staffs.append(staff)
        print(f"Staff {staff} added")

    def get_size(self):
        print(len(self.staffs))

    def remove_staff(self, staff):
        self.staffs.remove(staff)
        print(f"Staff removed")

    def get_info(self, email):
        for staff in self.staffs:
            if staff.email == email:
                return f"Staff found: {staff}"
            else:
                return f"No staff found"
            
    def update_head_of_department(self, new_head_of_department):
        self.head_of_department = new_head_of_department
        
    def __str__(self):
        return f"Department Name: {self.name}, Staff Size: {self.staff_size}, Head of Department: {self.head_of_department}, Location: {self.location}"
        


kosi = Staff("Kosi", "14/02/05", "Male", "email", 10, "address", "13/07/24", "intern")
temi = Staff("Temi", "12/12/12", "Male", "email", 12, "address", "12/12/12", "clerk")
ict = Department("ICT", 5, "Mr. Dozie", "Online")

ict.add_staff(kosi)
ict.add_staff(temi)
ict.remove_staff(temi)
# print(ict.get_info(kosi.email))
# kosi.update_name("David")
print(f"Name: {kosi.name}")

ict.update_head_of_department("chigo")
print(ict.head_of_department)

print(ict.get_info(kosi.email))


"""
    
remove employee()
Update employee()
Get_info(email)
total staff count()
Change HOD()
"""