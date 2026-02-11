from domain.domain import *

class Examen_file_repo:
    def __init__(self, filename):
        self.filename = filename
        self.examene = {}
        self.key = 0
        self.__load()

    def __load(self):
        self.examene.clear()
        with open(self.filename, "r") as f:
            for line in f:
                line = line.strip()

                if not line:
                    continue

                parts = line.split(";")

                data = parts[0]
                ora = parts[1]
                materia = parts[2]
                tip = parts[3]

                self.examene[self.key] = Examen(data,ora,materia,tip)
                self.key += 1

    def __save(self):
        with open(self.filename, "w") as f:
            for examen in self.examene.values():
                data = examen.getData().strftime("%d.%m")
                ora = examen.getOra().strftime("%H:%M")
                f.write(F"{data};{ora};{examen.getMaterie()};{examen.getTip()} \n")

    def getAll(self):
        return self.examene

    def store(self, examen):
        for elem in self.examene.values():
            if examen.getMaterie() == elem.getMaterie():
                if examen.getTip() == elem.getTip():
                    raise ValueError("Acest examen exista deja")
        self.examene[self.key] = examen
        self.key +=1
        self.__save()