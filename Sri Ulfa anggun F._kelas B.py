class Employee:
    def __init__(self, name: str, salary: float):
        self.name = name
        self.__salary = salary

    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, value: float):
        if value < 0:
            raise ValueError("Gaji tidak boleh negatif!")
        self.__salary = value


class Company:
    def __init__(self, name: str):
        self.name = name
        self.__employees = []

    def add_employee(self, employee: Employee):
        if not isinstance(employee, Employee):
            raise TypeError("Objek yang ditambahkan harus berupa instance dari class Employee!")
        
        self.__employees.append(employee)
        print(f"Karyawan {employee.name} berhasil ditambahkan ke {self.name}.")

    def __calculate_payroll(self) -> float:
        return sum(emp.salary for emp in self.__employees)

    def process_payroll(self):
        total = self.__calculate_payroll()
        print(f"--- Proses Penggajian {self.name} ---")
        print(f"Total Karyawan : {len(self.__employees)}")
        print(f"Total Payroll  : Rp {total:,.2f}")


if __name__ == "__main__":
    company = Company("Tech Corp")

    emp1 = Employee("sam", 5000000)
    emp2 = Employee("jovee", 7500000)

    company.add_employee(emp1)
    company.add_employee(emp2)

    try:
        company.add_employee("Bukan Karyawan")
    except TypeError as e:
        print(f"\n[Error Handling] {e}")

    print()
    company.process_payroll()

    try:
        company.__calculate_payroll()
    except AttributeError as e:
        print(f"\n[Akses Ilegal Diblokir] {e}")
