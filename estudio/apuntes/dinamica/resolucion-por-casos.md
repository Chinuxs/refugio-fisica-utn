# Dinámica: resolución por casos

[Teoría completa](teoria-completa.md) · [Ejercicios resueltos](../../ejercicios/dinamica/README.md) · [Errores frecuentes](../../errores-comunes/README.md)

Esta guía sirve para reconocer el modelo antes de escribir ecuaciones. La receta común es:

1. Definí el sistema y dibujá un DCL por cada cuerpo relevante.
2. Elegí ejes que simplifiquen las fuerzas y fijá los signos.
3. Marcá vínculos: cuerda inextensible, contacto, polea, apoyo o aceleración impuesta.
4. Planteá `ΣF = m a` por componentes.
5. Recién después aplicá rozamiento, límites y relaciones geométricas.
6. Resolvé, recuperá las magnitudes auxiliares y verificá unidades y sentido.

## Mapa rápido

| Si el enunciado habla de… | Caso | Receta | Fuente cátedra | Ejercicios |
| --- | --- | --- | --- |
| cuerpo quieto, cuerdas, nudo | Equilibrio | `ΣFx=0`, `ΣFy=0`; no agregues fuerzas de acción-reacción al mismo DCL | D-intro; D-2025 ej. 1 y 4; D-I ej. 4–5 | [DCL y equilibrio](../../ejercicios/dinamica/dcl-y-equilibrio.md) |
| bloque en plano inclinado | Plano | ejes paralelo/perpendicular; `mg sin θ` y `mg cos θ`; normal primero | D-I ej. 7–10; D-II ej. 12 | [Rozamiento y planos](../../ejercicios/dinamica/rozamiento-y-planos.md) |
| “no desliza”, “a punto de moverse” | Rozamiento estático | suponé el sentido de tendencia; calculá `f`; verificá `|f|≤μeN`; solo en el límite `f=μeN` | D-2025 ej. 2 y 5; D-I ej. 7, 9 y 11 | [Rozamiento y planos](../../ejercicios/dinamica/rozamiento-y-planos.md) |
| velocidad constante | Equilibrio dinámico | `a=0`, pero puede haber muchas fuerzas; no confundas rapidez constante en curva con `a=0` | D-II ej. 3, 5 y 11 | [Aceleración y referencia](../../ejercicios/dinamica/aceleracion-y-referencia.md) |
| varios bloques unidos | Sistema de cuerpos | escribí una ecuación por cuerpo; usá el vínculo para igualar aceleraciones; sumá para eliminar tensiones internas | D-II ej. 1, 2, 6, 15 y 17 | [Sistemas y vínculos](../../ejercicios/dinamica/sistemas-y-vinculos.md) |
| polea móvil o dos cuerdas | Vínculo geométrico | dibujá los tramos; derivá la longitud constante para obtener la relación de aceleraciones | D-II ej. 12, 15 y 17 | [Sistemas y vínculos](../../ejercicios/dinamica/sistemas-y-vinculos.md) |
| ascensor, balanza, peso aparente | Marco acelerado | en marco del suelo: `N-mg=ma`; una lectura es la normal, no el peso real | D-II ej. 3 y 7 | [Aceleración y referencia](../../ejercicios/dinamica/aceleracion-y-referencia.md) |
| camión que acelera o frena | Roce que acelera | el rozamiento puede ser la fuerza horizontal que produce `ma`; su sentido se opone al deslizamiento relativo | D-II ej. 11 | [Aceleración y referencia](../../ejercicios/dinamica/aceleracion-y-referencia.md) |

## Recetas de examen

### DCL y equilibrio

Incluí únicamente fuerzas reales que actúan sobre el cuerpo: peso, normal,
tensión, fuerzas aplicadas y rozamiento. Si hay varias cuerdas, cada una tiene
su propia tensión salvo que el modelo permita justificar que son iguales.

### Plano inclinado con roce

Tomá `+x` paralelo al plano. Si el bloque acelera hacia arriba, el roce va
hacia abajo; si acelera hacia abajo, el roce va hacia arriba. Para decidir si
permanece quieto, no impongas automáticamente `f=μeN`: primero calculá el roce
necesario y comparalo con el máximo disponible.

### Sistemas y poleas

No supongas que todas las aceleraciones son iguales: obtené esa relación de la
cuerda. La tensión se cancela al sumar ecuaciones solo cuando es interna al
sistema elegido. Si hay poleas o cuerdas distintas, mantené `T1`, `T2`, etc.

### Control final

- ¿Cada término de `ΣF` tiene unidades de N?
- ¿La normal es compatible con el contacto?
- ¿El signo de `a` coincide con el sentido supuesto?
- ¿Una tensión o una normal negativa indica que el modelo dejó de ser válido?
- ¿El resultado límite tiene sentido: `μ→0`, masa muy grande o fuerza nula?

## Ejercicios recomendados en orden

1. [DCL y equilibrio](../../ejercicios/dinamica/dcl-y-equilibrio.md)
2. [Rozamiento y planos](../../ejercicios/dinamica/rozamiento-y-planos.md)
3. [Aceleración, referencia y peso aparente](../../ejercicios/dinamica/aceleracion-y-referencia.md)
4. [Sistemas de cuerpos y vínculos](../../ejercicios/dinamica/sistemas-y-vinculos.md)
