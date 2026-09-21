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
        # Atribut private untuk array data karyawan
        self.__employees = []

    def add_employee(self, employee: Employee):
        # Memvalidasi input object menggunakan isinstance
        if not isinstance(employee, Employee):
            raise TypeError("Objek yang ditambahkan harus berupa instance dari class Employee!")
        
        self.__employees.append(employee)
        print(f"Karyawan {employee.name} berhasil ditambahkan ke {self.name}.")

    # Private method untuk menghitung total penggajian
    def __calculate_payroll(self) -> float:
        return sum(emp.salary for emp in self.__employees)

    # Public method untuk memanggil private method internal secara aman
    def process_payroll(self):
        total = self.__calculate_payroll()
        print(f"--- Proses Penggajian {self.name} ---")
        print(f"Total Karyawan : {len(self.__employees)}")
        print(f"Total Payroll  : Rp {total:,.2f}")

# Uji Coba Program (Testing)

if __name__ == "__main__":
    # 1. Inisialisasi Perusahaan
    company = Company("Tech Corp")

    # 2. Buat Data Karyawan
    emp1 = Employee("sam", 5000000)
    emp2 = Employee("jovee", 7500000)

    # 3. Tambahkan Karyawan ke Perusahaan (Validasi isinstance)
    company.add_employee(emp1)
    company.add_employee(emp2)

    # Uji Coba 1: Mencoba menambahkan objek non-Employee (Akan Error)
    try:
        company.add_employee("Bukan Karyawan")
    except TypeError as e:
        print(f"\n[Error Handling] {e}")

    # Uji Coba 2: Menjalankan Proses Payroll (Memanggil Private Method secara Internal)
    print()
    company.process_payroll()

    # Uji Coba 3: Mencoba Mengakses Private Method Secara Langsung dari Luar (Akan AttributeError)
    try:
        company.__calculate_payroll()
    except AttributeError as e:
        print(f"\n[Akses Ilegal Diblokir] {e}")