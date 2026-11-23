# Del fenómeno físico al planteo matemático

## 🎯 Qué recordar

**No se elige una ecuación porque aparece una fuerza: se elige un principio
después de definir sistema, intervalo y condiciones físicas.**
Esta ficha es una guía didáctica transversal, no un ejercicio ni una regla de
cátedra para aplicar mecánicamente.

### Secuencia para un problema nuevo

1. Leer el **enunciado completo** y observar su figura original; si falta,
   declararlo antes de interpretar.
2. Separar **datos dados**, preguntas, hipótesis e interpretaciones propias.
3. Elegir el **sistema físico** (qué cuerpos incluye) y los **estados o
   intervalos** (antes, durante y después).
4. Dibujar el esquema o DCL, con ejes y fuerzas **reales**, si corresponde.
5. Preguntar qué sucede durante cada intervalo: desplazamiento, trabajo,
   interacción breve, cambio de masa que oscila.
6. Comprobar las **condiciones del principio** antes de usarlo.
7. Escribir el teorema general; sólo después, imponer una conservación si
   está justificada.
8. Especificar qué términos se anulan, y **por qué**, según ese intervalo.
9. Relacionar las ecuaciones, despejar y mantener las expresiones sin
   redondeos prematuros.
10. Verificar unidades, signos, límites, dirección y coherencia física.

Esta secuencia orienta la revisión del propio planteo: el estudiante sigue
tomando las decisiones y las soluciones quedan en documentos separados.

## 🖼️ Esquema / dibujo

~~~text
¿QUÉ CAMBIA?                  ¿QUÉ EVALUAR?
Estado i ── recorrido ──> f   trabajos, K, U y referencia
Estado i ── impacto ────> f   impulso externo, P por ejes
Después  ── oscilación ─> f   equilibrio, masa, x(0), v(0)

En cada flecha: sistema + fuerzas externas + intervalo + hipótesis.
~~~

Un **estado** es una foto de magnitudes en un instante (rapidez, altura,
deformación). Un **proceso** es la transformación entre dos fotos, durante
la que pueden actuar trabajos o impulsos. El estado de máxima compresión
no es «todo el proceso de comprimir»: es el punto de retorno de ese tramo
si allí el bloque se detiene instantáneamente.

## 📐 Fórmula

| Pregunta antes de plantear | Teorema general | ¿Cuándo aparece una conservación? |
| --- | --- | --- |
| ¿Qué trabajo realiza **cada fuerza** durante un recorrido? | $W_{\rm neto}=\Delta K$ | Si $W_{\rm neto}=0$, se conserva **$K$**, no necesariamente $K+U$ |
| ¿Qué parte del trabajo está representada por potenciales? | $\Delta(K+U)=W_{nc}$ | Si $W_{nc}=0$ en el intervalo, se conserva la **energía mecánica** |
| ¿Qué impulso actúa sobre el **sistema** durante el impacto? | $\Delta\vec P=\vec J_{\rm ext}$ | Si $\vec J_{\rm ext}=0$ o es despreciable, se conserva **$\vec P$**; también puede ser por componentes |
| ¿Es elástico el choque? | Calcular $K_i$ y $K_f$ con masas y velocidades | Sólo justificar $K_i=K_f$ si hay una condición física que lo autorice |

**Fuerzas internas:** para un sistema fijo de partículas, sus impulsos
se cancelan por pares por la tercera ley; eso **no anula** el impulso
externo. **Fuerzas no conservativas presentes:** pueden realizar trabajo
cero; no alcanza con identificarlas por nombre para decidir si $E$ cambia.

**Ejemplo sin datos de examen:** si un bloque baja por pista lisa, cruza
un tramo rugoso y comprime un resorte ideal, marcá los límites de los
tramos y el estado de compresión máxima. El trabajo de roce corresponde
**al recorrido rugoso**, no a una «pérdida» adicional durante la
compresión ideal. El resorte almacena energía potencial; su fuerza puede
hacer trabajo no nulo y seguir siendo conservativa.

Para la manipulación de dos ecuaciones, no hace falta otra ley física:
ver [sustitución, factorización y porcentajes](dinamica/herramientas-matematicas/relacionar-ecuaciones.md).

## ⚠️ Error frecuente

- Conservar energía mecánica sólo porque existe peso; o conservar momento
  sólo porque «las fuerzas internas se cancelan».
- Mezclar inicio y fin de distintos intervalos, o llamar estado a un tramo.
- Tratar $v=0$ en un punto de retorno como $\sum\vec F=0$.
- Elegir una ecuación extra, como conservación de $K$ en un choque, sin
  que el enunciado o el modelo lo autoricen.
- Redondear antes de cerrar el sistema o aceptar signos incompatibles con
  el dibujo.

## 🔗 Ver también

- [Trabajo y Energía: balances y tramos](trabajo-energia/balances-y-tramos.md)
- [Impulso: sistema e intervalo](impulso-cantidad-movimiento/conservacion-y-choques.md)
- [Choques oblicuos: ejes y signos](impulso-cantidad-movimiento/choques-oblicuos.md)
- [MAS: fase y equilibrio](movimiento-armonico-simple/fase-y-equilibrio.md)
- [Práctica del segundo parcial sin resultados](../parciales/Segundo_Parcial/practica.md)

**Procedencia:** síntesis de elaboración propia a partir de dificultades
relatadas después del segundo parcial; usa los principios respaldados en
las [fuentes de TP 6](trabajo-energia/fuentes.md),
[TP 7](movimiento-armonico-simple/fuentes.md) y
[TP 8](impulso-cantidad-movimiento/fuentes.md).
No reproduce un enunciado oficial ni amplía el temario.
