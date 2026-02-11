from domain.domain import *
from datetime import *

class Service:
    def __init__(self, repo, validator):
        self.repo = repo
        self.validator = validator

    def Create_examen(self, data, ora, materie, tip):
        examen = Examen(data,ora,materie,tip)

        if self.validator != None:
            self.validator.validate(examen)
        self.repo.store(examen)

    def Print(self):
        list = self.repo.getAll()
        afisare = []
        for examen in list.values():
            maine = date.today() + timedelta(days=1)
            maine = maine.strftime("%d.%m")
            azi = examen.getData()
            azi = azi.strftime("%d.%m")
            if azi == maine:
                afisare.append(examen)

        sort_afisare = sorted(afisare, key = lambda x: x.getOra())

        if len(sort_afisare) != 0:
            for examen in sort_afisare:
                data = examen.getData().strftime("%d.%m")
                print(F"Data:{data} Ora:{examen.getOra()} Materia:{examen.getMaterie()} Tipul:{examen.getTip()} \n")

    def Print_data(self, data):
        list = self.repo.getAll()
        data_inaintata = data + timedelta(days=3)
        data_inaintata = data_inaintata.strftime("%d.%m")
        afisare = []

        for examen in list.values():
            data = examen.getData()
            data = data.strftime("%d.%m")
            if data <= data_inaintata:
                afisare.append(examen)

        sort_afisare = sorted (afisare, key = lambda x: x.getData())

        ultima_data = None
        for examen in sort_afisare:
            data_curenta = examen.getData().strftime("%d.%m")

            if data_curenta != ultima_data:
                print(f"\nData: {data_curenta}")
                print("-" * 40)
                print(f"{'Ora':<8}{'Materie':<20}{'Tip':<10}")
                print("-" * 40)
                ultima_data = data_curenta

            ora = examen.getOra().strftime("%H:%M")
            print(f"{ora:<8}{examen.getMaterie():<20}{examen.getTip():<10}")

    def Afisare(self, numef, sir):
        list = self.repo.getAll()
        afisare = []

        for examen in list.values():
            if sir in examen.getMaterie():
                afisare.append(examen)

        sort_afisare = sorted(afisare, key = lambda x: (x.getData(), x.getOra()))

        with open(numef, "w") as f:
            for examen in sort_afisare:
                data = examen.getData().strftime("%d.%m")
                ora = examen.getOra().strftime("%H:%M")
                f.write(F"{data};{ora};{examen.getMaterie()};{examen.getTip()} \n")