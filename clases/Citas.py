# Citas

class Citas():
    lista_citas = []
    def __init__(self,cliente_nombre: str,fotografo_elegido: str ,fecha: str,hora: str):
       self.cliente_nombre = cliente_nombre
       self.fecha = fecha
       self.hora = hora
       self.fotografo_elegido = fotografo_elegido
       Citas.lista_citas.append(self)

    def info_cita(self):
        return (f"\nEl dia {self.fecha}, a las {self.hora} tendra una cita con el fotografo: {self.fotografo_elegido}. ")

    def __str__(self):
        return self.info_cita()

    @classmethod
    def todas_citas(cls):
        return cls.lista_citas
    

        
        