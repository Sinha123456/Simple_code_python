#tutorial from Telusko(https://www.youtube.com/watch?v=b7JzgybKvys&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=58)
class Hospital:

    def __init__(self, reception, doctor, nurse):
        self.reception = reception
        self.doctor = doctor
        self.nurse = nurse
        self.dent = self.Dentist()
    def staff(self):
        print("Our receptionist is", self.reception, "\n", "Our doctor is: ", self.doctor, "\n", "and our nurse is : " +self.nurse)

    class Dentist:
        def __init__(self):
            self.patients = 20
            self.dentist = 5
        def staff(self):
            print("number of patients in the hospital:", self.dentist, "\n", "Number of dentist:",  self.dentist)

            self.dent.staff()
s1 = Hospital('Johanna', 'Dr. Hamid', 'Johny')


s1.dent.staff()
#duck typing
class Birds:
    def fly(self):
        print("Fly with wings")
class Airplane:
    def fly(self):
#         print("fly with fuel.")
# class Fish:
#     print("Fish swim in sea.")
# br = Birds()
# ar = Airplane()
# print(br.fly())
# print(ar.fly())
# for obj in Birds(), Airplane():
#     obj.fly()
def product(a,b):
    p = a*b
    print(p)
def product(a,b,c):
    p = a * b*c
product(3,4)
product(2,6,4)