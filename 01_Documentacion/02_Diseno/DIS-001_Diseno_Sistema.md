# DIS-001 - Diseño del Sistema SoftEdu

## Información del elemento de configuración

- Código del CI: DIS-001
- Nombre: Diseño del Sistema
- Proyecto: SoftEdu
- Versión: 1.0
- Estado: Aprobado para línea base inicial
- Fecha: 09/09/2026
- Responsable: Equipo SoftEdu

## Historial de versiones

| Versión | Fecha      | Descripción del cambio                    | Responsable    |
| ------- | ---------- | ------------------------------------------ | -------------- |
| 1.1     | 2026-09-23 | Agregar atributo telefono a entidad Estudiante | Hector Morales |
| 1.0     | 09/09/2026 | Diseño inicial del sistema                | Equipo SoftEdu |

## 1. Descripción general

SoftEdu se organiza en tres componentes principales:

1. Gestión de estudiantes.
2. Gestión de cursos.
3. Gestión de matrículas.

## 2. Entidades principales

### Estudiante

La entidad Estudiante contiene los siguientes atributos:

#### Atributos v1.0
- **identificacion** (string): Número único de identificación del estudiante
- **nombre_completo** (string): Nombre completo del estudiante
- **correo_electronico** (string): Correo electrónico de contacto

#### Atributos v1.1 (CR-001)
- **telefono** (string, opcional): Número de teléfono de contacto del estudiante

**Estructura de clase Estudiante (v1.1):**
```python
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
```

**Notas de diseño:**
- El atributo telefono es opcional para mantener compatibilidad hacia atrás
- Se implementa como parámetro por defecto con valor None
- El método mostrar_informacion() incluye el teléfono en la salida
