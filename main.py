import tkinter as tk

class Car:
    def __init__(self, make, model, price):
        self.make = make
        self.model = model
        self.price = price

class Company:
    def __init__(self, name, commission_rate):
        self.name = name
        self.commission_rate = commission_rate

class Employee:
    def __init__(self, name, title, salary, company):
        self.name = name
        self.title = title
        self.salary = salary
        self.company = company

    def calculate_paycheck(self):
        return self.salary / 26  # assume bi-weekly paychecks

class Manager(Employee):
    def __init__(self, name, title, salary, company, bonus_percentage):
        super().__init__(name, title, salary, company)
        self.bonus_percentage = bonus_percentage

    def calculate_paycheck(self):
        base_paycheck = super().calculate_paycheck()
        bonus_amount = self.salary * (self.bonus_percentage / 100)
        return base_paycheck + bonus_amount

class Salesperson(Employee):
    def __init__(self, name, title, salary, company, commission_rate, cars_sold):
        super().__init__(name, title, salary, company)
        self.commission_rate = commission_rate
        self.cars_sold = cars_sold

    def calculate_paycheck(self):
        base_paycheck = super().calculate_paycheck()
        commission_earned = sum(car.price * self.commission_rate for car in self.cars_sold)
        return base_paycheck + commission_earned

    def get_commission(self):
        return sum(car.price * self.commission_rate for car in self.cars_sold)

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.name_label = tk.Label(self, text="Employee Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        self.title_label = tk.Label(self, text="Employee Title:")
        self.title_label.pack()
        self.title_entry = tk.Entry(self)
        self.title_entry.pack()

        self.salary_label = tk.Label(self, text="Employee Salary:")
        self.salary_label.pack()
        self.salary_entry = tk.Entry(self)
        self.salary_entry.pack()

        self.company_label = tk.Label(self, text="Company Name:")
        self.company_label.pack()
        self.company_entry = tk.Entry(self)
        self.company_entry.pack()

        self.commission_label = tk.Label(self, text="Commission Rate:")
        self.commission_label.pack()
        self.commission_entry = tk.Entry(self)
        self.commission_entry.pack()

        self.car_label = tk.Label(self, text="Car Price:")
        self.car_label.pack()
        self.car_entry = tk.Entry(self)
        self.car_entry.pack()

        self.cars_sold_label = tk.Label(self, text="Number of Cars Sold:")
        self.cars_sold_label.pack()
        self.cars_sold_entry = tk.Entry(self)
        self.cars_sold_entry.pack()

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack()

        self.calculate_paycheck_button = tk.Button(self, text="Calculate Paycheck",
                                                   command=self.calculate_paycheck)
        self.calculate_paycheck_button.pack()

        self.commission_button = tk.Button(self, text="Get Commission",
                                            command=self.get_commission)
        self.commission_button.pack()

    def calculate_paycheck(self):
        try:
            salary = float(self.salary_entry.get())
            commission_rate = float(self.commission_entry.get())
            company_name = self.company_entry.get()
            car_price = float(self.car_entry.get())
            cars_sold = int(self.cars_sold_entry.get())

            company = Company(company_name, commission_rate)
            salesperson = Salesperson(self.name_entry.get(), self.title_entry.get(), salary, company, commission_rate, [])
            car = Car("Brand", "Model", car_price)
            salesperson.cars_sold = [car] * cars_sold
            paycheck = salesperson.calculate_paycheck()
            messagebox.showinfo("Paycheck Information", f"Employee Name: {salesperson.name}\nPaycheck Amount: ${paycheck:.2f}")

        except ValueError:
            messagebox.showerror("Error", "Invalid input, please enter a valid number")

    def get_commission(self):
        try:
            commission_rate = float(self.commission_entry.get())
            car_price = float(self.car_entry.get())
            cars_sold = int(self.cars_sold_entry.get())

            company = Company(self.company_entry.get(), commission_rate)
            salesperson = Salesperson(self.name_entry.get(), self.title_entry.get(), 0, company, commission_rate, [])
            car = Car("Brand", "Model", car_price)
            salesperson.cars_sold = [car] * cars_sold
            commission = salesperson.get_commission()
            messagebox.showinfo("Commission Information", f"Employee Name: {salesperson.name}\nCommission Earned: ${commission:.2f}")

        except ValueError:
            messagebox.showerror("Error", "Invalid input, please enter a valid number")

root = tk.Tk()
app = Application(master=root)
app.mainloop()