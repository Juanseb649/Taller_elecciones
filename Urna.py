__author__ = "Juan Sebastian Ibarra Salas"
__License__ = "GPL"
__Version__ = "1.0.0"
__Email__ = "juan.ibarrasalas@campusucc.edu.co"

from Candidato import Candidato


class Urna:
    def __init__(self):
        self.__Candidato = [None] * 3
        self.__Candidato1 = Candidato()
        self.__Candidato2 = Candidato()
        self.__Candidato3 = Candidato()
        self.__rangoEdad1 = VotosRangoEdad()
        self.__rangoEdad2 = VotosRangoEdad()
        self.__rangoEdad3 = VotosRangoEdad()

        # Rangos para el  candidato 1
        self.__Candidato1.setRangoEdad1(self.__rangoEdad1)
        self.__Candidato1.setRangoEdad2(self.__rangoEdad2)
        self.__Candidato1.setRangoEdad3(self.__rangoEdad3)

        # Rangos para el candidato 2
        self.__Candidato2.setRangoEdad1(self.__rangoEdad1)
        self.__Candidato2.setRangoEdad2(self.__rangoEdad2)
        self.__Candidato2.setRangoEdad3(self.__rangoEdad3)

        # Rangos para el candidato 3
        self.__Candidato3.setRangoEdad1(self.__rangoEdad1)
        self.__Candidato3.setRangoEdad2(self.__rangoEdad2)
        self.__Candidato3.setRangoEdad3(self.__rangoEdad3)

    # Getters & setters
    def __get__candidato1(self):
        return self.__Candidato1
    
    def __get__candidato2(self):
        return self.__Candidato2
    
    def __get__candidato3(self):
        return self.__Candidato3
    
    def __set__candidato1(self, candidato):
        self.__Candidato1 = candidato

    def __set__candidato2(self, candidato):
        self.__Candidato2 = candidato

    def __set__candidato3(self, candidato):
        self.__Candidato3 = candidato

    def buscarCandidato(self, numero):
        if numero == 1:
            return self.__Candidato1
        elif numero == 2:
            return self.__Candidato2
        elif numero == 3:
            return self.__Candidato3
        else:
            return None

    def agregarCandidatos(self, Nombre, Edad, PartidoPolitico, Posicion):
        if Posicion < 3:
            self.__Candidato[Posicion] = Candidato()
            return True
        return False

    def darTotalVotosGeneroFemenino(self):
        votosFemeninos__candidato1 = (self.__Candidato1.getRango1().getVotosFemeninos() +
    self.__Candidato1.getRango2().getVotosFemeninos() +
    self.__Candidato1.getRango3().getVotosFemeninos())
        votosFemeninos__candidato2 = (self.__Candidato2.getRango1().getVotosFemeninos() +
    self.__Candidato2.getRango2().getVotosFemeninos() +
    self.__Candidato2.getRango3().getVotosFemeninos())
        votosFemeninos__candidato3 = (self.__Candidato3.getRango1().getVotosFemeninos() +
        self.__Candidato3.getRango2().getVotosFemeninos() +
    self.__Candidato3.getRango3().getVotosFemeninos())
        return votosFemeninos__candidato1 + votosFemeninos__candidato2 + votosFemeninos__candidato3

    def darTotalVotosMasculinio(self):
        votosMasculinos__candidato1 = (self.__Candidato1.getRango1().getVotosMasculinos() +
    self.__Candidato1.getRango2().getVotosMasculinos() +
    self.__Candidato1.getRango3().getVotosMasculinos())
        votosMasculinos__candidato2 = (self.__Candidato2.getRango1().getVotosMasculinos() +
    self.__Candidato2.getRango2().getVotosMasculinos() +
    self.__Candidato2.getRango3().getVotosMasculinos())
        votosMasculinos__candidato3 = (self.__Candidato3.getRango1().getVotosMasculinos() +
        self.__Candidato3.getRango2().getVotosMasculinos() +
        self.__Candidato3.getRango3().getVotosMasculinos())
        return votosMasculinos__candidato1 + votosMasculinos__candidato2 + votosMasculinos__candidato3

    def darTotalVotosRangoEdad(self, edad):
        if edad is None:
            return "No se define la edad"
        elif (edad >= self.__rangoEdad1.getEdadMinima() and
        edad <= self.__rangoEdad1.getEdadMaxima()):
            votosCandidato1 = (self.__Candidato1.getRango1().getVotosFemeninos() + 
    self.__Candidato1.getRango1().getVotosMasculinos())
            votosCandidato2 = (self.__Candidato2.getRango1().getVotosFemeninos() +
    self.__Candidato2.getRango1().getVotosMasculinos())
            votosCandidato3 = (self.__Candidato3.getRango1().getVotosFemeninos() +
    self.__Candidato3.getRango1().getVotosMasculinos())
            return votosCandidato1 + votosCandidato2 + votosCandidato3
        elif (edad >= self.__rangoEdad2.getEdadMinima() and
    edad <= self.__rangoEdad2.getEdadMaxima()):
            votosCandidato1 = (self.__Candidato1.getRango2().getVotosFemeninos() +
    self.__Candidato1.getRango2().getVotosMasculinos())
            votosCandidato2 = (self.__Candidato2.getRango2().getVotosFemeninos() +
    self.__Candidato2.getRango2().getVotosMasculinos())
            votosCandidato3 = (self.__Candidato3.getRango2().getVotosFemeninos() +
    self.__Candidato3.getRango2().getVotosMasculinos())
            return votosCandidato1 + votosCandidato2 + votosCandidato3
        elif (edad >= self.__rangoEdad3.getEdadMinima() and
        edad <= self.__rangoEdad3.getEdadMaxima()):
            votosCandidato1 = (self.__Candidato1.getRango3().getVotosFemeninos() +
    self.__Candidato1.getRango3().getVotosMasculinos())
            votosCandidato2 = (self.__Candidato2.getRango3().getVotosFemeninos() +
    self.__Candidato2.getRango3().getVotosMasculinos())
            votosCandidato3 = (self.__Candidato3.getRango3().getVotosFemeninos() +
    self.__Candidato3.getRango3().getVotosMasculinos())
            return votosCandidato1 + votosCandidato2 + votosCandidato3
        else:
            return "La edad no es un valor valido"