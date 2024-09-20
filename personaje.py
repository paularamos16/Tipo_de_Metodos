



class Personaje():
    
    
    def __init__(self,nombre:str):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0
        
    @property    
    def estado(self):
        return f"""
    nombre:{self.nombre}
    nivel:{self.nivel}
    experiencia:{self.experiencia}
        """
    
    @estado.setter
    def estado(self,exp:int):
        temp_exp = self.experiencia + exp
        while temp_exp >= 100:
            self.nivel += 1
            temp_exp -=1
        
        while temp_exp < 0:
            if self.nivel > 1:
                temp_exp = 100 + temp_exp
                self.nivel -=1
            else:
                temp_exp=0
        
        self.experiencia = temp_exp  
    
    #c
    def __lt__(self,other):
        return self.nivel < other.nivel
    #d
    def __gt__(self,other):
        return self.nivel > other.nivel
    #f
    def __eq__(self,other):
        return self.nivel == other.nivel
    
        
    def mostrar_probabilidad(self,other):
        if self < other:  #estamos llamando a la sobrecarga
            return 0.33
        elif self > other:
            return 0.66
        else:
            return 0.50
        
    @staticmethod
    def mostrar_dialogo_opcion(probabilidad_de_ganar):
        return int(input(f"""
                    Con tu nivel actual, tienes {probabilidad_de_ganar*100} de probabilidades de ganarle al Orco.
Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.
Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.

¿Qué deseas hacer?
1. Atacar
2. Huir
                    """))
            
        
        
        
        
        
        
        
        
        
        
        
        
        