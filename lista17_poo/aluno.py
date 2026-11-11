class Aluno:
    def __init__(self, nome, curso, tempoSemDormir):
        self.nome = nome
        self.curso = curso
        self.tempoSemDormir = tempoSemDormir

    def estudar(self, horasEstudo):
        self.tempoSemDormir += horasEstudo

    def dormir(self, horasDeSono):
        self.tempoSemDormir -= horasDeSono

    def get_tempoSemDormir(self):
        return self.tempoSemDormir

aluno1 = Aluno('abc', 'cco', 16)

print(aluno1.get_tempoSemDormir())

aluno1.estudar(6)

print(aluno1.get_tempoSemDormir())

aluno1.dormir(2)

print(aluno1.get_tempoSemDormir())
