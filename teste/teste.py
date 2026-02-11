from repo.repo import Examen_file_repo
from service.service import *
from datetime import date, timedelta


def test_create_examen():
    # Cream fisierul gol inainte de test
    open("test.txt", 'w').close()

    data = "10.02"
    ora = "15:30"
    materia = "informatica"
    tip = "normala"
    repo = Examen_file_repo("test.txt")
    validator = Examen_validator()
    service = Service(repo, validator)

    service.Create_examen(data, ora, materia, tip)

    with open("test.txt", 'r') as f:
        linie = f.readlines()

    assert linie[0] == "10.02;15:30;informatica;normala \n"

    open("test.txt", 'w').close()


def test_print():
    # Cream fisierul cu date de test
    with open("test2.txt", 'w') as f:
        f.write("12.02;12:00;engleza;restanta \n")
        f.write("12.02;12:00;engleza;restanta \n")
        f.write("12.02;16:30;matematica;normala \n")

    repo = Examen_file_repo("test2.txt")
    validator = Examen_validator()

    list = repo.getAll()
    afisare = []
    for examen in list.values():
        maine = date.today() + timedelta(days=1)
        maine = maine.strftime("%d.%m")
        azi = examen.getData()
        azi = azi.strftime("%d.%m")
        if azi == maine:
            afisare.append(examen)

    sort_afisare = sorted(afisare, key=lambda x: x.getOra())

    assert len(sort_afisare) >= 3
    assert sort_afisare[0].getData().strftime("%d.%m") == "12.02"
    assert sort_afisare[0].getOra().strftime("%H:%M") == "12:00"
    assert sort_afisare[0].getMaterie() == "engleza"
    assert sort_afisare[0].getTip() == "restanta"

    assert sort_afisare[1].getData().strftime("%d.%m") == "12.02"
    assert sort_afisare[1].getOra().strftime("%H:%M") == "12:00"
    assert sort_afisare[1].getMaterie() == "engleza"
    assert sort_afisare[1].getTip() == "restanta"

    assert sort_afisare[2].getData().strftime("%d.%m") == "12.02"
    assert sort_afisare[2].getOra().strftime("%H:%M") == "16:30"
    assert sort_afisare[2].getMaterie() == "matematica"
    assert sort_afisare[2].getTip() == "normala"


def rulare():
    test_create_examen()
    test_print()
    print("Testele au rulat cu succes!")


rulare()