import datetime
from idlelib.configdialog import is_int


class Examen:
    """
    Clasa care se ocupa de gestiunea unui examen
    """
    def __init__(self, data, ora, materia, tip):
        if isinstance(data, str):
            data = datetime.datetime.strptime(data, "%d.%m").date()

        if isinstance(ora, str):
            ora = datetime.datetime.strptime(ora, "%H:%M").time()

        self.__data = data
        self.__ora = ora
        self.__materia = materia
        self.__tip = tip

    def getData(self):
        return self.__data

    def getOra(self):
        return self.__ora

    def getMaterie(self):
        return self.__materia

    def getTip(self):
        return self.__tip

class Examen_validator:
    def validate(self, examen):
        errors = ""

        if examen.getData() == "":
            errors += "Data nu poate fi goala"

        if examen.getOra() == "":
            errors += "Ora nu poate fi goala"

        if examen.getMaterie() == "":
            errors += "Materia nu poate fi goala"

        if examen.getTip() == "":
            errors += "Examenul nu poate fi gol"

        if examen.getTip() != "normala" and examen.getTip() != "restanta":
            raise ValueError("Examenul nu este de tipul corect")

