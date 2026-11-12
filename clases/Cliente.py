# Clases
import re 
class Cliente:
    Verificar_CURP = r"^[A-Z]{4}\d{6}[HM][A-Z]{5}[A-Z\d]\d$"
    listado = []
    def __init__(self,CURP: str, nombre: str,telefono: str,email: str,contra: str):
        curp_normal = CURP.strip().upper()
        if not re.match(self.Verificar_CURP, curp_normal):
            raise ValueError(
                f"El CURP '{CURP}' es incorrecto/invalido."
            )
        if len(contra.strip()) < 4:
            raise ValueError("La contraseña debe tener al menos 4 caracteres. ")
        
        self.CURP = curp_normal
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.contra = contra.strip()

    def informacion(self):
        return f"\nCliente: {self.nombre} | Tel: {self.telefono} | Email: {self.email} | CURP: {self.CURP}"

    def __str__(self):
        return self.informacion()

    def memoria(self):
        for i, C in enumerate(Cliente.listado):
            if C.CURP == self.CURP:
                C.listado[i] = self
                return True
        Cliente.listado.append(self)
        return True

    @classmethod
    def comprobacion(cls, CURP: str, contra: str):
        CURP_crudo = CURP.strip().upper()
        for c in cls.listado:
            if c.CURP == CURP_crudo and c.contra == contra.strip():
                return c
            return None

    @classmethod
    def todos(cls):
        return cls.listado


    



