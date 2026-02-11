
from repo.repo import *
from service.service import *
from domain.domain import *
from teste.teste import rulare

repo = Examen_file_repo("examene.txt")
validator = Examen_validator()
service = Service(repo, validator)
alltime = 0
data2 = ""
#Rulam testele
rulare()
while True:
    if alltime == 1:
        service.Print_data(data2)
        print('\n')

    print("================= Examenele de maine =================")
    service.Print()
    print("================= Examenele de maine =================")
    print("1. Adauga un nou examen")
    print("2. Seteaza o data")
    print("3. Afisare in fisier")

    try:
        try:
            optiune = int(input("Optiunea aleasa este: "))
        except:
            raise ValueError("Optiunea nu este valida")
    except Exception as e:
        print("Eroare: ", e)
        continue

    if optiune == 1:
        data = input("Data este: ")
        try:
            try:
                data = datetime.datetime.strptime(data,"%d.%m")
            except:
                raise ValueError("Data nu este corecta")
            ora = input("Ora este: ")
            try:
                ora = datetime.datetime.strptime(ora, "%H:%M").time()
            except:
                raise ValueError("Ora nu este introdusa corect")

            materia = input ("Materia este: ")
            tip = input ("Tipul examenului este(normala/restanta): ")

            service.Create_examen(data,ora,materia,tip)
        except Exception as e:
            print ("Eroare: ", e)
            continue

    if optiune == 2:
        data = input("Data dorita de introdus este: ")
        try:
            data = datetime.datetime.strptime(data, "%d.%m")
        except:
            print("Data nu este corecta")
            continue
        try:
            service.Print_data(data)
            data2 = data
            alltime = 1
        except Exception as e:
            print("Eroare: ", e)
            continue

    if optiune == 3:
        numef = input("Numele fisierului este: ")
        sir = input("Sirul de caractere este: ")
        try:
            service.Afisare(numef,sir)
        except Exception as e:
            print("Eroare: ", e)
            continue