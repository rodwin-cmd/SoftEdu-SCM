# REQ-001 - Especificación de Requisitos de SoftEdu

## Información del elemento de configuración

- Código del CI: REQ-001
- Nombre: Especificación de Requisitos Funcionales
- Proyecto: SoftEdu
- Versión: 1.1
- Estado: Aprobado
- Fecha: 2026-09-23
- Responsable: Hector Morales

## Historial de versiones

| Versión | Fecha      | Descripción del cambio                        | Responsable    |
| ------- | ---------- | --------------------------------------------- | -------------- |
| 1.1     | 2026-09-23 | Agregar RF-05: Registrar teléfono de estudiante | Hector Morales |
| 1.0     | 2026-09-09 | Creación inicial de requisitos funcionales     | Equipo SoftEdu |

---

## 1. Requisitos Funcionales

### RF-01: Registrar Estudiante
**Descripción:** El sistema debe permitir registrar un nuevo estudiante con su identificación, nombre completo y correo electrónico.
**Estado:** Completo - Implementado en v1.0

### RF-02: Consultar Estudiante
**Descripción:** El sistema debe permitir consultar la información de un estudiante registrado.
**Estado:** Completo - Implementado en v1.0

### RF-03: Registrar Curso
**Descripción:** El sistema debe permitir registrar nuevos cursos.
**Estado:** Parcial - Pendiente de implementación

### RF-04: Matricular Estudiante
**Descripción:** El sistema debe permitir matricular un estudiante en un curso.
**Estado:** Parcial - Pendiente de implementación

### RF-05: Registrar Teléfono del Estudiante
**Descripción:** El sistema debe permitir registrar y consultar el número de teléfono de contacto del estudiante.
**Justificación:** Se requiere un medio de contacto adicional para los estudiantes.
**Criterios de aceptación:**
- El teléfono debe ser un atributo opcional al registrar estudiantes
- Debe ser posible consultar el teléfono junto con otros datos del estudiante
- El sistema debe mantener compatibilidad con registros existentes sin teléfono
**Estado:** Completo - Implementado en CR-001 (v1.1)

---

## 2. Encabezado e Identificación del Elemento de Configuración (CI)
Esta sección inicial identifica de manera unívoca el elemento dentro del sistema de gestión de configuración:
* **Identificador del CI:** Código único asignado al elemento (ej. `CI-REQ-001`).
* **Proyecto:** Nombre o código del proyecto de software.
* **Versión:** Número de versión actual del documento o elemento (ej. `v1.0`).
* **Estado:** Situación actual en el ciclo de vida (ej. *En revisión*, *Aprobado*, *Línea Base*).
* **Fecha:** Fecha de la última actualización o emisión.
* **Responsable:** Nombre del autor, analista o responsable de la configuración del elemento.

---

## 2. Historial de Versiones
Registro cronológico de las modificaciones sufridas por el documento o el requisito para garantizar la trazabilidad:
* **Versión**
* **Fecha**
* **Autor / Responsable**
* **Descripción de los Cambios**

---

## 3. Propósito y Alcance
* **Propósito:** Explicación clara de la razón de ser del requerimiento y el valor que aporta al negocio o al usuario final.
* **Alcance:** Delimitación de los sistemas, módulos, procesos o perfiles de usuario afectados o cubiertos por este requisito.

---

## 4. Requisitos Funcionales y No Funcionales
Especificación detallada de lo que el sistema debe hacer y cómo debe comportarse:
* **Requisitos Funcionales:** Comportamientos, entradas, procesos y salidas esperadas del sistema.
* **Requisitos No Funcionales:** Atributos de calidad, restricciones técnicas, rendimiento, seguridad, usabilidad o disponibilidad.

---

## 5. Criterios de Aceptación
Condiciones específicas y comprobables que deben cumplirse para que el requerimiento sea considerado completo y válido por el cliente o el equipo de calidad:
* Verificaciones basadas en escenarios (casos de prueba esperados).
* Condiciones límite y restricciones comprobables.

---

## 6. Control de Cambios posteriores a la Línea Base
> **Nota de Control de Configuración:**  
> Cualquier modificación, adición o eliminación realizada sobre este requisito una vez que haya sido integrado en una **Línea Base** oficial, **debe ser estrictamente controlada** a través del proceso formal de Gestión de Cambios del proyecto (Solicitud de Cambio - RFC). Ningún cambio posterior podrá aplicarse sin la debida evaluación de impacto, aprobación del comité correspondiente y actualización de la documentación asociada.
