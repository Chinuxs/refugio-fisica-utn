# Métodos de resolución en Dinámica

Estas herramientas aparecen con frecuencia al aplicar la Segunda Ley de Newton.
No son fórmulas nuevas de Física: son procedimientos algebraicos que permiten
trabajar mejor con las ecuaciones obtenidas.

## Método 1: dividir ecuaciones para eliminar una incógnita común

### Cuándo conviene usarlo

Se puede considerar cuando:

- se aplicó la Segunda Ley de Newton en dos direcciones;
- aparecen dos ecuaciones simultáneamente válidas;
- ambas contienen una misma incógnita como factor;
- el cociente permite simplificar esa incógnita.

Algunos factores comunes posibles son la tensión, la masa, la normal, una
longitud, una carga o una constante común.

### Ejemplo: masa suspendida dentro de un automóvil acelerado

Al aplicar la Segunda Ley de Newton por componentes puede obtenerse:

$$
T\sin\theta = ma
$$

$$
T\cos\theta = mg
$$

En estas ecuaciones aparecen las incógnitas \(T\) y \(\theta\). La tensión
\(T\) es un factor común. En vez de despejarla por separado, se puede dividir
la primera ecuación por la segunda:

$$
\frac{T\sin\theta}{T\cos\theta}
=
\frac{ma}{mg}
$$

Como \(T\) y \(m\) son factores comunes no nulos, se simplifican:

$$
\frac{\sin\theta}{\cos\theta}
=
\frac{a}{g}
$$

Usando

$$
\tan\theta = \frac{\sin\theta}{\cos\theta},
$$

queda:

$$
\tan\theta = \frac{a}{g}
$$

y, por lo tanto:

$$
\theta = \arctan\left(\frac{a}{g}\right)
$$

No hace falta calcular un resultado numérico: este ejemplo muestra el método
general.

### Por qué es válido

No se trata de sumar o restar polinomios. Se usa la propiedad de división de
igualdades. Si:

$$
A=B
$$

y:

$$
C=D,
$$

con \(C\) y \(D\) distintos de cero, entonces:

$$
\frac{A}{C} = \frac{B}{D}
$$

En el problema, las dos ecuaciones son verdaderas simultáneamente. Por eso se
pueden dividir miembro a miembro.

La simplificación ocurre porque:

$$
\frac{TX}{TY} = \frac{X}{Y},
$$

si \(T\) es distinto de cero.

### Ejemplo numérico sencillo

Consideremos:

$$
8 = 2\cdot 4
$$

$$
12 = 3\cdot 4
$$

Entonces:

$$
\frac{8}{12}
=
\frac{2\cdot 4}{3\cdot 4}
=
\frac{2}{3}
$$

El factor común \(4\) se elimina.

### Error frecuente

Este procedimiento no es lo mismo que sumar ecuaciones, restar polinomios o
tachar cantidades sin comprobar cómo aparecen. Solo se pueden simplificar
factores comunes del numerador y del denominador.

Ejemplo válido:

$$
\frac{T\sin\theta}{T\cos\theta}
$$

Ejemplo no válido:

$$
\frac{T+\sin\theta}{T+\cos\theta}
$$

En el segundo caso no se puede cancelar \(T\), porque está sumando y no
multiplicando.

### Regla práctica para el parcial

> Cuando dos ecuaciones contienen la misma incógnita como factor, preguntarse:
> “¿Puedo dividir una ecuación por la otra para eliminarla?”

> Antes de simplificar, comprobar que las cantidades canceladas sean factores y
> que no sean cero.

### Forma recomendada de escribirlo en un examen

> Dividiendo miembro a miembro la ecuación (1) por la ecuación (2):

Luego se muestra el cociente entre ambas ecuaciones y se indican explícitamente
los factores que se simplifican.
