class Estudante:
    escola = "alabasta"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


aluno_1 = Estudante("Nami", 154970)
aluno_2 = Estudante("sanji", 768542)
mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "going merry"
aluno_3 = Estudante("Chopper", 985420)
mostrar_valores(aluno_1, aluno_2, aluno_3)