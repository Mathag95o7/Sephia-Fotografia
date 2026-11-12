# Clases fotografo
import re 
class Fotografo:
    Verificar_CURP = r"^[A-Z]{4}\d{6}[HM][A-Z]{5}[A-Z\d]\d$"
    listado_fotografo = []
    def __init__(self,CURP: str, nombre: str,telefono: str,email: str,contra: str,especial: str):
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
        self.especial = especial

    def informacion_fotografo(self):
        return f"Fotografo: {self.nombre} | Especialidad: {self.especial} | Tel: {self.telefono} | Email: {self.email} | CURP: {self.CURP}"

    def __str__(self):
        return self.informacion_fotografo()

    def memoria_fotografo(self):
        for i, F in enumerate(Fotografo.listado_fotografo):
            if F.CURP == self.CURP:
                F.listado_fotografo[i] = self
                return True
        Fotografo.listado_fotografo.append(self)
        return True

    @classmethod
    def comprobacion_fotografo(cls, CURP: str, contra: str):
        CURP_crudo = CURP.strip().upper()
        for f in cls.listado_fotografo:
            if f.CURP == CURP_crudo and f.contra == contra.strip():
                return f
            return None

    @classmethod
    def todos_fotografo(cls):
        return cls.listado_fotografo


    



