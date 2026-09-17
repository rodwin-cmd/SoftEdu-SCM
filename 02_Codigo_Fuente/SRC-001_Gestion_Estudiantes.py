# SRC-001 - Gestion de Estudiantes
# Proyecto: SoftEdu
# Version: 1.0
# Estado: Aprobado para linea base inicial
# Fecha: 09/09/2026
# Responsable: Equipo SoftEdu

class Estudiante:
    def __init__(self, identificacion, nombre_completo, correo_electronico, telefono=None):
        self.identificacion = identificacion
        self.nombre_completo = nombre_completo
        self.correo_electronico = correo_electronico
        self.telefono = telefono

    def mostrar_informacion(self):
        return {
            "identificacion": self.identificacion,
            "nombre_completo": self.nombre_completo,
            "correo_electronico": self.correo_electronico,
            "telefono": self.telefono
        }

def registrar_estudiante(identificacion, nombre_completo, correo_electronico, telefono=None):
    estudiante = Estudiante(
        identificacion,
        nombre_completo,
        correo_electronico,
        telefono
    )
    return estudiante
