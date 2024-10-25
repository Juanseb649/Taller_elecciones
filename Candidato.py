__author__ = "Juan Sebastian Ibarra Salas"
__License__ = "GPL"
__Version__ = "1.0.0"
__Email__ = "juan.ibarrasalas@campusucc.edu.co"

from Medio import Medio

class Candidato:
    def __init__(self, nombre, edad, partidoPolitico, costoCampania, cantidadVotos, porcentajeCandidato):
        self.__nombre = nombre
        self.__edad = edad
        self.__partidoPolitico = partidoPolitico
        self.__costoCampania = costoCampania
        self.__cantidadVotos = cantidadVotos
        self.__porcentajeCandidato = porcentajeCandidato
        self.__rango1 = VotosRangoEdad()
        self.__rango2 = VotosRangoEdad()
        self.__rango3 = VotosRangoEdad()

    # Metodos, Getters & Setters
    def getNombre(self):
        return self.__nombre
    
    def getEdad(self):
        return self.__edad
    
    def getPartidoPolitico(self):
        return self.__partidoPolitico
    
    def getCostoCampania(self):
        return self.__costoCampania
    
    def getRango1(self):
        return self.__rango1
    
    def getRango2(self):
        return self.__rango2
    
    def getRango3(self):
        return self.__rango3
    
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def setEdad(self, edad):
        self.__edad = edad
    
    def setPartidoPolitico(self, partidoPolitico):
        self.__partidoPolitico = partidoPolitico
    
    def setRangoEdad1(self, rangoEdad):
        self.__rango1 = rangoEdad

    def setRangoEdad2(self, rangoEdad):
        self.__rango2 = rangoEdad
    
    def setRangoEdad3(self, rangoEdad):
        self.__rango3 = rangoEdad

    # Da el total de los votos para este candidato del genero Masculino
    def darTotalVotosGeneroMasculino(self):
        return (self.getRango1().getVotosMasculinos() +
                self.getRango2().getVotosMasculinos() +
                self.getRango3().getVotosMasculinos())
    
    # Da el total de los votos para este candidato del genero Femenino
    def darTotalVotosGeneroFemenino(self):
        return (self.getRango1().getVotosFemeninos() +
                self.getRango2().getVotosFemeninos() +
                self.getRango3().getVotosFemeninos())
    
    # Da el total de votos para este candidato dentro del rango de edad 1
    def darVotosRango1(self):
        return (self.getRango1().getVotosMasculinos() +
                self.getRango1().getVotosFemeninos())
    
    # Da el total de votos para este candidato dentro del rango de edad 2
    def darVotosRango2(self):
        return (self.getRango2().getVotosMasculinos() +
                self.getRango2().getVotosFemeninos())
    
    # Da el total de votos para este candidato dentro del rango de edad 3
    def darVotosRango3(self):
        return (self.getRango3().getVotosMasculinos() +
                self.getRango3().getVotosFemeninos())
    
    # Registra un voto para este candidato en base a su genero, edad ademas suma el al costo de campania
    def registrarVoto(self, genero, edad, medio):
        if (edad >= self.getRango1().getEdadMinima() and
            edad <= self.getRango1().getEdadMaxima()):
            self.getRango1().registrarVoto(genero)
            if medio == Medio.TELEVISION:
                self.__costoCampania += 1000
            elif medio == Medio.RADIO:
                self.__costoCampania += 500
            elif medio == Medio.INTERNET:
                self.__costoCampania += 100
            else:
                print("Medio no reconocido")
        elif (edad >= self.getRango2().getEdadMinima() and
    edad <= self.getRango2().getEdadMaxima()):
            self.getRango2().registrarVoto(genero)
            if medio == Medio.TELEVISION:
                self.__costoCampania += 1000
            elif medio == Medio.RADIO:
                self.__costoCampania += 500
            elif medio == Medio.INTERNET:
                self.__costoCampania += 100
            else:
                print("Medio no reconocido")
        elif (edad >= self.getRango3().getEdadMinima() and
    edad <= self.getRango3().getEdadMaxima()):
            self.getRango3().registrarVoto(genero)
            if medio == Medio.TELEVISION:
                self.__costoCampania += 1000
            elif medio == Medio.RADIO:
                self.__costoCampania += 500
            elif medio == Medio.INTERNET:
                self.__costoCampania += 100
            else:
                print("Medio no reconocido")
        else:
            print("Edad no reconocida")
    
    # Reinicia el numero de votos para el candidato
    def reiniciar(self):
        self.getRango1().reiniciar()
        self.getRango2().reiniciar()
        self.getRango3().reiniciar()