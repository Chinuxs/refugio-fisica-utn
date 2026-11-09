# El Refugio de Física

## Objetivo

Construir una base de conocimiento personal y colaborativa para estudiar
Física I en UTN FRLP.

El repositorio no debe ser solamente una colección de archivos o resultados
numéricos. Cada material debe ayudar a:

- comprender el concepto físico;
- reconocer el tipo de problema;
- elegir una estrategia;
- detectar errores frecuentes;
- preparar evaluaciones escritas y orales.

## Filosofía de trabajo

1. Interpretar el problema.
2. Representarlo mediante dibujos, esquemas o diagramas.
3. Identificar los principios físicos aplicables.
4. Elegir un sistema de referencia y ejes convenientes.
5. Plantear las ecuaciones.
6. Resolver y verificar unidades.
7. Explicar qué se aprendió.

Priorizar la comprensión sobre la memorización de fórmulas.

## Aprendizaje activo: el estudiante conduce la resolución

**Regla fundamental:** el estudiante debe intentar resolver cada ejercicio por su cuenta.
El asistente actúa como acompañante y revisor, no como solucionador automático.
No adelantar fórmulas, planteos, ecuaciones desarrolladas ni resultados de un
**ejercicio particular**, salvo petición explícita o una dificultad concreta
que requiera una ayuda gradual.

Secuencia de trabajo:

1. El estudiante interpreta el enunciado.
2. Identifica el sistema físico y, si corresponde, dibuja el esquema.
3. Decide qué principios físicos aplicar, sin que el asistente los anticipe.
4. Construye sus ecuaciones y fija ejes y signos.
5. Realiza los cálculos y controla unidades.
6. El asistente revisa lo hecho, pregunta o da pistas **de menor a mayor**
   sólo cuando sean necesarias; evita reemplazar el razonamiento.

**Separar niveles de ayuda:** el enunciado original va primero; las pistas
opcionales en un documento distinto; las soluciones y comprobaciones en otro,
marcado como material que revela resultados. No mostrar la resolución completa
para “ayudar” sin que el estudiante la haya solicitado. Las fichas conceptuales
sí pueden explicar fórmulas generales, sin resolver el ejercicio en curso.

Para Cuerpo Rígido, usar [el recorrido desde cero](estudio/apuntes/cuerpo-rigido/desde-cero.md)
y las fichas antes de [pistas del TP 9](estudio/apuntes/cuerpo-rigido/pistas-tp9.md).
La [guía por casos](estudio/apuntes/cuerpo-rigido/resolucion-por-casos.md)
queda como referencia de comprobación **posterior al intento**.

## Base de conocimiento de consulta rápida

El Refugio no busca parecer un libro. Cada concepto, herramienta matemática,
método o error detectado al resolver un ejercicio debe poder consultarse sin
volver a leer toda la resolución.

La prioridad es:

1. Encontrar rápido.
2. Recordar rápido.
3. Volver al ejercicio.

Evitar teoría innecesaria y no copiar capítulos completos de libros.

## Estructura principal

- `exposicion/`: materiales de la exposición de Cinemática y simulador de tiro
  oblicuo.
- `estudio/parciales/`: parciales, finales, recuperatorios y simulacros.
- `estudio/apuntes/`: conceptos, herramientas matemáticas, métodos y referencias
  rápidas.
- `estudio/ejercicios/`: ejercicios analizados y resueltos.

## Temas prioritarios actuales

- Dinámica.
- Movimiento Circular.
- Relación entre Dinámica y Movimiento Circular.
- Trabajo y Energía.
- Movimiento Armónico Simple.
- Impulso y cantidad de movimiento, centro de masa y choques.
- Cuerpo Rígido y Rotación: momento de inercia, torque, poleas, energía,
  rodadura y conservación del momento angular. Mantener teoría esencial,
  resolución por casos del TP 9 y fuentes con hipótesis y erratas explícitas.
- Estática y Rototraslación: equilibrio, estabilidad, vuelco, rodadura y CIR.
  Mantener teoría esencial, casos del TP 10 y fuentes; enlazar las inercias
  del tema Cuerpo Rígido para evitar duplicados.
- Modelo de cuerpo deformable, Elasticidad y Estática de los fluidos:
  `estudio/apuntes/elasticidad-hidrostatica/`. Se dispone de `tp11.pdf` con
  21 ejercicios y una presentación práctica con ocho casos. Usar numeración
  del PDF: PPTX práctico 13/18/21 equivalen a PDF 11/17/20. Desde el 7/11/2026
  hay teoría de cátedra `11 Hidrostática.pptx` (27 diapositivas): Elasticidad
  (Young, corte, módulo volumétrico, curva de tracción) e Hidrostática.
  El nuevo TP es copia binaria del anterior. Sears cap. 12, páginas impresas
  369–397, aporta Hidrostática y tensión superficial cualitativa (p. 378);
  su Hidrodinámica no amplía el parcial. No hay ejercicios de Elasticidad
  ni tensión superficial en TP 11: E1–E4 son procedimientos de teoría.
  Registrar erratas de la teoría (signos diap. 26, resta diap. 23, Δp en B)
  separadas de las correcciones de la presentación práctica anterior.

Para Trabajo y Energía, MAS, Impulso, Cuerpo Rígido y Estática y
Rototraslación y Elasticidad e Hidrostática, mantener dos guías breves por tema:
`teoria-esencial.md` (conceptos, fórmulas y condiciones) y
`resolucion-por-casos.md` (cómo reconocer el caso y qué plantear).
Basar los casos en los TP de la cátedra, indicar sus números de ejercicio y
registrar las fuentes en `fuentes.md`. Priorizar la consulta rápida; conservar
el material ampliado como referencia adicional.

## Formato para documentar ejercicios

### Preparación de parciales

- Segundo parcial: Trabajo y Energía, MAS e Impulso/Cantidad de Movimiento.
- Tercero: TP 9–11, excluyendo Rototraslación (TP 10: practicar sólo 1–9)
  e Hidrodinámica; el estudiante confirmó que entra sólo Hidrostática.
- Los índices en `estudio/parciales/` tienen enunciados, patrones y práctica.
  No inferir alcance actual de exámenes antiguos ni contar RAR/copias o
  soluciones como exámenes independientes. Auditoría en `auditoria-material.md`.

### Resoluciones

Cada ejercicio resuelto debería incluir, cuando corresponda:

1. Fuente o examen.
2. Tema.
3. Enunciado.
4. Datos.
5. Qué pide.
6. Diagrama o descripción del esquema.
7. Sistema de referencia y ejes.
8. Fuerzas o magnitudes involucradas.
9. Idea física principal.
10. Estrategia.
11. Desarrollo matemático.
12. Resultado con unidades.
13. Verificación física del resultado.
14. Error típico.
15. Pregunta oral relacionada.
16. Qué aprender de este ejercicio.

## Reglas conceptuales

- No presentar la fuerza centrípeta como una fuerza adicional.
- La fuerza centrípeta es la resultante radial de las fuerzas reales.
- Diferenciar rapidez de velocidad.
- Diferenciar trayectoria, posición y desplazamiento.
- Diferenciar Cinemática de Dinámica.
- En los diagramas de cuerpo libre, dibujar solamente fuerzas reales.
- Explicar siempre el significado físico de las ecuaciones.

## Estilo de escritura

- Español claro y accesible.
- Markdown simple.
- Explicaciones breves pero razonadas.
- Evitar lenguaje innecesariamente técnico.
- No copiar teoría sin explicarla.
- No dejar resultados sin unidades.
- No inventar datos ausentes en los enunciados.
- Marcar explícitamente cualquier hipótesis.
- Mantener los documentos útiles para estudiantes que no sean programadores.

## Diseño visual

Cuando un concepto pueda explicarse mediante un dibujo, esquema o diagrama,
debe preferirse el recurso visual antes que un bloque largo de texto.

- Un DCL vale más que un párrafo.
- Un triángulo vale más que una explicación extensa de seno y coseno.
- Un esquema de fuerzas vale más que una descripción textual.
- Usar diagramas ASCII sencillos o imágenes existentes siempre que ayuden.
- Para esquemas físicos nuevos, seguir el estilo SVG de Dinámica y Movimiento
  Circular: ejes, flechas, cuerpos y etiquetas legibles directamente en GitHub.
  En TyE, MAS e Impulso, los SVG se regeneran con
  `py herramientas/generar_diagramas_estudio.py` (sin dependencias externas).
  Revisar el resultado visual después de cambiar el generador.
- Mantener el texto breve y orientado a retomar el ejercicio.

### Convención visual para fichas

Toda ficha nueva debe seguir este orden:

1. `## 🎯 Qué recordar`
2. `## 🖼️ Esquema / dibujo`
3. `## 📐 Fórmula`
4. `## ⚠️ Error frecuente`
5. `## 🔗 Ver también`

Usar siempre esos íconos y títulos para que la ubicación de la información sea
predecible. La plantilla está en
[`estudio/apuntes/PLANTILLA.md`](estudio/apuntes/PLANTILLA.md).

Para recursos SVG:

- usar una tipografía sans serif legible, como `Inter`, `Segoe UI` o `Arial`;
- usar `Cambria Math`, `STIX Two Math` o una serif para fórmulas;
- mantener contraste alto y no depender únicamente del color;
- incluir texto alternativo al insertar la imagen en Markdown;
- priorizar diagramas que aporten información, no decoración.

## Reglas para asistentes de IA

Antes de cambiar el repositorio:

1. Leer este archivo.
2. Revisar la estructura y los README relacionados.
3. No eliminar material sin autorización explícita.
4. Mantener enlaces relativos funcionando.
5. Evitar duplicar contenido.
6. Proponer cambios pequeños y revisables.
7. Respetar la terminología usada por la cátedra.
8. Indicar cuando un ejercicio o fuente no aporta información suficiente.
9. No reemplazar razonamientos por respuestas automáticas.
10. Mantener actualizado `PROJECT_STATUS.md` cuando se complete trabajo
    relevante.
