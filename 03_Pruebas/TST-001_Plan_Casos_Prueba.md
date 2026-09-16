# TST-001 - Plan y Casos de Prueba SoftEdu

## Información del elemento de configuración

- Código del CI: TST-001
- Nombre: Plan y Casos de Prueba
- Proyecto: SoftEdu
- Versión: 1.0
- Estado: Aprobado para línea base inicial
- Fecha: 09/09/2026
- Responsable: Equipo SoftEdu

## Historial de versiones

| Versión | Fecha      | Descripción del cambio                        | Responsable    |
| ------- | ---------- | --------------------------------------------- | -------------- |
| 1.0     | 09/09/2026 | Creación del plan y casos de prueba iniciales | Equipo SoftEdu |

## 1. Propósito y Alcance

El presente documento establece el plan de pruebas y los casos de prueba iniciales para el sistema **SoftEdu**, garantizando la verificación y validación de los requisitos funcionales frente a los diseños y componentes de código fuente implementados (trazabilidad SCM).

## 2. Casos de Prueba Detallados

### CP-001 - Registrar estudiante

- Requisito asociado: RF-01
- Diseño asociado: DIS-001 - Entidad Estudiante

Precondiciones:
- El estudiante no debe existir previamente en el sistema.

Resultado esperado:
- Registrar correctamente identificación, nombre y correo.

Estado esperado: Aprobado.

### CP-002 - Consultar estudiante

- Requisito asociado: RF-02
- Diseño asociado: DIS-001 - Entidad Estudiante

Precondiciones:
- El estudiante debe estar previamente registrado.

Resultado esperado:
- Consultar un estudiante existente.

Estado esperado: Aprobado.

### CP-003 - Registrar curso

- Requisito asociado: RF-03
- Diseño asociado: DIS-001 - Entidad Curso

Precondiciones:
- El código del curso no debe estar registrado.

Resultado esperado:
- Registrar un curso.

Estado esperado: Aprobado.

### CP-004 - Matricular estudiante

- Requisito asociado: RF-04
- Diseño asociado: DIS-001 - Entidad Matrícula

Precondiciones:
- El estudiante debe existir.
- El curso debe existir.

Resultado esperado:
- Asociar estudiante y curso.

Estado esperado: Aprobado.

## 3. Trazabilidad de pruebas

| Caso de prueba | Requisito | Diseño  | Código                    |
| -------------- | --------- | ------- | ------------------------- |
| CP-001         | RF-01     | DIS-001 | SRC-001                   |
| CP-002         | RF-02     | DIS-001 | SRC-001                   |
| CP-003         | RF-03     | DIS-001 | No aplica en esta versión |
| CP-004         | RF-04     | DIS-001 | No aplica en esta versión |

## 4. Observaciones de configuración

Este documento constituye el Elemento de Configuración TST-001.

Los casos de prueba deberán actualizarse cuando una solicitud de cambio modifique los requisitos, el diseño o el código relacionado.
