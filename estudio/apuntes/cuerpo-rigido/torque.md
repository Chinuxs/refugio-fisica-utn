# Ficha — torque y equilibrio rotacional

## 🎯 Qué recordar

El **torque** (momento de una fuerza) describe cuánto tiende una fuerza a hacer girar un cuerpo **respecto de un eje**. Como al abrir una puerta, importa dónde y en qué dirección empujás. Una fuerza puede ser grande y tener torque nulo si su línea de acción pasa por el eje.

Dos torques de sentidos opuestos se restan **algebraicamente**. Que la suma sea cero significa que no hay aceleración angular en el modelo de eje fijo e inercia constante; para equilibrio estático también se necesita equilibrio de fuerzas y ausencia de movimiento.

## 🖼️ Esquema / dibujo

    Puerta vista desde arriba
    bisagra O ●────────────────● picaporte
                                     ↑ F
                brazo perpendicular ─┘

La fuerza representada es perpendicular a la puerta. Si empujás **hacia la bisagra** siguiendo la puerta, el brazo perpendicular es cero. [Esquema de torques y signos](assets/mapa-rotacion.svg).

## 📐 Fórmula

$
|\tau|=rF\sin\varphi=F\,d_\perp,\qquad
\sum\tau_z=I_z\alpha_z
$

- \(r\): distancia desde el eje al punto de aplicación; \(\varphi\): ángulo entre \(\vec r\) y \(\vec F\); \(d_\perp\): distancia **del eje a la línea de acción**.
- Elegir un sentido positivo (por ejemplo, antihorario visto desde un lado). El contrario tiene signo negativo.
- En equilibrio rotacional: \(\sum\tau_z=0\). La relación \(\sum\tau_z=I_z\alpha_z\) supone un eje fijo y \(I_z\) constante.
- Unidad: **N·m**; aunque dimensionalmente coincide con el joule, el torque no se etiqueta en J.

## ⚠️ Error frecuente

Confundir \(r\) con el brazo perpendicular, sumar sólo módulos sin signos o pensar que torque cero implica que no actúan fuerzas.

## 🔗 Ver también

- [Recorrido desde cero](desde-cero.md)
- [Momento de inercia](momento-de-inercia.md)
- [Dinámica y signos en teoría esencial](teoria-esencial.md#dinámica-por-qué-cambia-el-giro)
- [Errores frecuentes](../../errores-comunes/README.md)
