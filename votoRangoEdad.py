__author__ = "Juan Sebastian Ibarra Salas"
__License__ = "GPL"
__Version__ = "1.0.0"
__Email__ = "juan.ibarrasalas@campusucc.edu.co"

class votosRangoEdad:
    
    def __init__(self, edadMinima,edadMaxima):
        self.__votosMasculinos = 0
        self.__votosfemeninos = 0
        self.__edadMinima = edadMinima
        self.__edadMaxima = edadMaxima
    
    #Metodos
    
    # Getters & setters
    
    def getcvotosMasculinos(self):
        return self.__votosMasculinos
    
    def getvotosFemeninos (self):
        return self .__votosfemeninos
    
    def getedadMinima(self):
        return self.__edadMinima
    
    def getEdadMaxima(self):
        return self.__EdadMaxima
    
    #Registra un voto y evalua el sexo, sea masculino o femenino
    
    def registrarVoto(self,genero):
        if genero == "Masculino":
            self.__votosMasculinos += 1
        elif genero == "femenino":
            self.__votosfemeninos += 1
        else:
            print ("Genero no Reconocido")
    
    #Reiniciar el numero de votos
    
    def reiniciar (self):
        self.__votosMasculinos = 0
        self.__votosfemeninos = 0