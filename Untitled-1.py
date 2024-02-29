class pasajero :
    def __init__(self, nombre, apellido, edad, pasaporte):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.__pasaporte=pasaporte

    def mostrarinformacion(self) :
        print("El pasajaero :"{self.nombre} {self.apellido} "de edad" {self.edad} ", con pasaporte :"{self.pasaporte})
    
