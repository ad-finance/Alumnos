class Alumno:
    nombre = "Juan"
    nota = 8

    def Name(self):
        return self.nombre

    def Mark(self):
        return self.nota

    def Result(self):
        if self.nota < 7:
            print("Resultado: Desaprobado")
        else:
            print("Resultado: Aprobado")

Juan = Alumno()
print("Nombre del alumno:", Juan.Name())
print("Nota:", Juan.Mark())
Juan.Result()