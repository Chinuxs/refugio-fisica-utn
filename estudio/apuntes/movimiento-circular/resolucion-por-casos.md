# Movimiento circular y MCU: resolución por casos

[Teoría completa](teoria-completa.md) · [Ejercicios resueltos](../../ejercicios/movimiento-circular/README.md) · [Machete visual](Movimiento_Circular_UTN_FRLP.md)

## Diagnóstico inicial

Preguntá: ¿el radio es fijo?, ¿la rapidez es constante?, ¿qué fuerza apunta al
centro?, ¿el dato es angular o lineal? En cualquier punto, elegí `+r` hacia el
centro y usá `ΣFr = m v²/R`. La “centrípeta” no se agrega al DCL: es el nombre
de la resultante radial.

## Mapa de casos

| Si aparece… | Modelo | Receta | Fuente cátedra | Ejercicios |
| --- | --- | --- | --- |
| rpm, vueltas, período, frecuencia | MCU cinemático | `f=rpm/60`, `ω=2πf`, `T=1/f`, `v=ωR`, `aᵣ=v²/R` | C-actual ej. 1 y 5; C-PDF ej. 5 y 10 | [MCU: Tierra, nave y transmisiones](../../ejercicios/movimiento-circular/cinematica-mcu.md) |
| dos ruedas y correa sin patinar | Transmisión | igualá rapidez en el borde: `ω1R1=ω2R2`; no igualés `ω` salvo eje común | C-PDF ej. 5 | [MCU: Tierra, nave y transmisiones](../../ejercicios/movimiento-circular/cinematica-mcu.md) |
| curva plana | Giro horizontal | `N=mg`; el roce estático aporta `m v²/R`; imponé `f≤μeN` | C-actual ej. 6; C-PDF ej. 16 | [Giros horizontales](../../ejercicios/movimiento-circular/giros-horizontales.md) |
| peralte o avión inclinado | Fuerza inclinada | separá vertical (`a_y=0`) y radial (`a_r=v²/R`); dividí ecuaciones para eliminar la fuerza | C-actual ej. 3 y 6; C-PDF ej. 16 | [Giros horizontales](../../ejercicios/movimiento-circular/giros-horizontales.md) |
| cuerda que forma un cono | Péndulo cónico | `R=L sinθ`; tensión vertical equilibra peso; componente horizontal curva | C-PDF ej. 11 y 18 | [Giros horizontales](../../ejercicios/movimiento-circular/giros-horizontales.md) |
| satélite u órbita | Gravedad radial | `GMm/r²=mv²/r`; usá `r=Rastro+h`, no solo la altura | C-actual ej. 4 | [Órbitas y curvatura](../../ejercicios/movimiento-circular/orbitas-y-curvatura.md) |
| loop, cima o cuerda vertical | Círculo no uniforme | DCL local + `ΣFr=mv²/R`; si cambia la rapidez, conectá puntos con energía | C-PDF ej. 9 y 13 | [Círculo vertical](../../ejercicios/movimiento-circular/circulo-vertical.md) |
| acelera o frena mientras gira | MCUV | convertí rpm a rad/s; aplicá ecuaciones angulares por etapas; `a_t=Rα` y `aᵣ=ω²R` | C-actual ej. 2; C-PDF ej. 2, 3 y 7 | [Aceleración angular](../../ejercicios/movimiento-circular/aceleracion-angular.md) |

## Tips que evitan errores

- `ω` en rad/s no es `v`: falta multiplicar por el radio.
- En MCU la rapidez es constante, pero el vector velocidad cambia y por eso
  existe `aᵣ`.
- En un círculo vertical, el peso suele tener componente tangencial: no
  supongas la misma rapidez arriba y abajo sin una hipótesis adicional.
- En una cima convexa el límite de contacto es `v≤√(gR)`; en la parte alta de
  un loop interior con cuerda o carril, la condición mínima de contacto es
  `v≥√(gR)`.
- `T=0` o `N=0` es una condición límite del vínculo, no ausencia de
  aceleración.
- Para una trayectoria cualquiera reemplazá `R` por el radio de curvatura `ρ`.

## Orden sugerido de práctica

1. [Cinemática MCU](../../ejercicios/movimiento-circular/cinematica-mcu.md)
2. [Giros horizontales](../../ejercicios/movimiento-circular/giros-horizontales.md)
3. [Órbitas y curvatura](../../ejercicios/movimiento-circular/orbitas-y-curvatura.md)
4. [Círculo vertical](../../ejercicios/movimiento-circular/circulo-vertical.md)
5. [Aceleración angular](../../ejercicios/movimiento-circular/aceleracion-angular.md)
