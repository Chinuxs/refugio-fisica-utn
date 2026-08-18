# Trabajo y Energía — machete visual

> Objetivo: reconocer la herramienta, plantear lo mínimo necesario y volver al
> ejercicio. Los flujos orientan; no reemplazan el análisis físico.

## 🧠 ¿Cuándo pensar en Trabajo y Energía?

Suele ser útil cuando aparecen fuerzas y desplazamientos, cambios de rapidez o
altura, resortes, o cuando conviene comparar un estado inicial con uno final
sin describir cada instante intermedio.

```text
¿Fuerza + desplazamiento?       → TRABAJO
¿Rapidez inicial y final?       → ENERGÍA CINÉTICA
¿Altura o resorte?              → ENERGÍA POTENCIAL
¿Comparar dos estados?          → TRABAJO–ENERGÍA
                                  o CONSERVACIÓN DE ENERGÍA
```

## 🧰 Trabajo de una fuerza constante

$$
W=F\,d\cos\theta
$$

$\theta$ es el ángulo **entre la fuerza y el desplazamiento**.

| Fuerza respecto del desplazamiento | $\theta$ | $\cos\theta$ | Trabajo |
| --- | ---: | ---: | ---: |
| mismo sentido | $0^\circ$ | $1$ | $W>0$ |
| perpendicular | $90^\circ$ | $0$ | $W=0$ |
| sentido opuesto | $180^\circ$ | $-1$ | $W<0$ |

```text
W > 0  → la fuerza aporta energía al movimiento
W < 0  → la fuerza extrae energía del movimiento
W = 0  → no aporta cambio de K durante ese desplazamiento
```

Una fuerza puede actuar y realizar trabajo nulo. No alcanza con preguntar si
la fuerza existe: hay que compararla con el desplazamiento.

### El signo del trabajo

```text
NO mirar solamente hacia dónde apunta F

        F y desplazamiento
                ↓
        ángulo entre ambos
                ↓
              cos θ
                ↓
        signo del trabajo
```

> ❌ No asignar el signo del trabajo automáticamente por el signo de un eje
> cartesiano. El signo sale del producto escalar $\vec F\cdot\vec d$.

## ➕ Trabajo neto

$$
W_{\text{neto}}=\sum_i W_i
$$

Cada fuerza real puede hacer su propio trabajo. Para organizarlas:

```text
DCL → identificar fuerzas reales
    → decidir cuáles hacen trabajo durante el desplazamiento
    → calcular cada Wᵢ
    → sumar
```

El armado del DCL y la identificación de fuerzas se repasan en
[Dinámica](../dinamica/README.md) y en la
[Segunda Ley de Newton](../dinamica/conceptos/segunda-ley-newton.md).

## 🏃 Energía cinética

$$
K=\frac12mv^2
$$

- Depende de la masa y del cuadrado de la **rapidez**.
- Es escalar: no depende de la dirección instantánea de $\vec v$.
- Para masa constante:

```text
v × 2
  ↓
K × 4
```

## 🎯 Teorema trabajo–energía

$$
\boxed{W_{\text{neto}}=\Delta K=K_f-K_i}
$$

El trabajo total realizado por las fuerzas sobre un cuerpo produce el cambio
de su energía cinética.

```text
1. Elegir cuerpo o sistema.
2. Marcar estado inicial y final.
3. Identificar las fuerzas que realizan trabajo.
4. Calcular W_neto.
5. Usar W_neto = ΔK.
6. Despejar la incógnita.
7. Verificar unidades y sentido físico.
```

## 🏔️ Energía potencial gravitatoria

Cerca de la superficie terrestre y con $g$ aproximadamente constante:

$$
U_g=mgh,
\qquad
\Delta U_g=mg(h_f-h_i)
$$

La referencia $U_g=0$ puede elegirse donde resulte conveniente. En general
importa la diferencia de alturas, no una altura absoluta obligatoria.

$$
W_g=-\Delta U_g
$$

> ❌ Cambiar la referencia modifica los valores de $U_g$, pero no
> $\Delta U_g$ ni el resultado físico.

## 🌀 Energía potencial elástica

Para un resorte ideal:

$$
U_e=\frac12kx^2
$$

$x$ mide la deformación respecto de la longitud natural. Tanto comprimir como
estirar almacena energía: como aparece $x^2$, cambiar el signo de $x$ no cambia
$U_e$.

Referencia mínima de la Ley de Hooke, en una dimensión:

$$
F_e=-kx
$$

El signo menos indica que la fuerza elástica se opone a la deformación.

## 🔄 Energía mecánica

La energía mecánica es una suma útil para resolver problemas, no una forma de
energía nueva e independiente:

$$
E_m=K+U
$$

Si intervienen varias energías potenciales:

$$
E_m=K+U_g+U_e+\dots
$$

### Si sólo hacen trabajo fuerzas conservativas

$$
\boxed{E_{m,i}=E_{m,f}}
\qquad\Longleftrightarrow\qquad
K_i+U_i=K_f+U_f
$$

```text
más altura                         menos altura
    ↓                                   ↓
más U_g          ← intercambio →    menos U_g
menos K                              más K
```

Conservar $E_m$ **no** significa que $K$ o $U$ sean constantes: pueden
transformarse entre sí.

### Si hacen trabajo fuerzas no conservativas

Si $U$ incluye todas las energías potenciales de las fuerzas conservativas
elegidas:

$$
\boxed{W_{nc}=\Delta E_m=E_{m,f}-E_{m,i}}
$$

Con rozamiento, normalmente la energía mecánica no se conserva. La energía no
desaparece: parte se transforma, por ejemplo, en energía interna o térmica.

## 🧱 Trabajo del rozamiento cinético

Si el rozamiento cinético tiene módulo constante y se opone al desplazamiento:

$$
W_f=-f_kd
$$

En el modelo usual:

$$
f_k=\mu_kN
$$

Primero hay que calcular correctamente $N$: **no siempre vale $N=mg$**. Para
plantear fuerzas y componentes, ver [Dinámica](../dinamica/README.md). No
confundir este caso con el
[rozamiento estático](../dinamica/referencias-rapidas/rozamiento-estatico.md),
que se adapta hasta un máximo.

## ⟂ Normal, peso, tensión y trabajo nulo

Una fuerza no realiza trabajo cuando es perpendicular al desplazamiento.

```text
bloque sobre piso horizontal

        N
        ↑
        ● ─────→ d
        ↓
       mg
```

Si no hay desplazamiento vertical:

$$
W_N=0,
\qquad
W_g=0
$$

Esto no permite afirmar que “la normal nunca hace trabajo” o que “la tensión
nunca hace trabajo”. Siempre hay que mirar la fuerza y el desplazamiento del
punto sobre el que actúa.

## ⚡ Potencia

La potencia mide qué tan rápido se transfiere o transforma energía.

$$
P_{\text{media}}=\frac{W}{\Delta t},
\qquad
P=\vec F\cdot\vec v
$$

La segunda expresión es la potencia instantánea entregada por una fuerza.

## 📏 Unidades

```text
Trabajo / energía:  joule (J)    1 J = 1 N·m
Potencia:           watt (W)     1 W = 1 J/s
```

Trabajo y energía comparten unidades, pero representan conceptos diferentes.

## 🧭 Método rápido para elegir herramienta

| Quiero hallar o relacionar... | Primera herramienta a considerar |
| --- | --- |
| cambio de rapidez | $W_{\text{neto}}=\Delta K$ |
| rapidez y alturas | energía mecánica |
| problema con rozamiento | $W_{nc}=\Delta E_m$ |
| trabajo de una fuerza constante | $W=Fd\cos\theta$ |
| energía almacenada por altura | $U_g=mgh$ |
| energía almacenada en un resorte | $U_e=\frac12kx^2$ |

Es un selector inicial: antes de usar una ecuación, definir el cuerpo o
sistema, los estados y las hipótesis.

## 🔗 Relación con Dinámica

```text
DINÁMICA                         TRABAJO Y ENERGÍA
fuerzas → aceleración            trabajo → cambio de energía
ΣF = ma                          W_neto = ΔK
```

Si se buscan aceleraciones, fuerzas instantáneas, tensiones o normales,
Newton puede ser necesario. Si se quieren relacionar estados mediante
rapideces, alturas o desplazamientos, energía puede simplificar el problema.
Muchos ejercicios usan ambos métodos.

En Movimiento Circular, por ejemplo, energía relaciona velocidades entre
alturas y el DCL con Newton determina fuerzas en un punto: ver
[Movimiento circular vertical](../movimiento-circular/Movimiento_Circular_UTN_FRLP.md#10--movimiento-circular-vertical).

## ⚠️ Errores frecuentes

- ❌ Confundir fuerza con trabajo, o energía con fuerza.
- ❌ Suponer que toda fuerza presente realiza trabajo.
- ❌ Usar el ángulo de $\vec F$ respecto de un eje y no respecto de $\vec d$.
- ❌ Olvidar que el trabajo puede ser negativo.
- ❌ Creer que conservar energía implica rapidez constante.
- ❌ Conservar $E_m$ con rozamiento sin incluir su trabajo o transformación.
- ❌ Suponer automáticamente $N=mg$.
- ❌ Olvidar que $K$ depende de $v^2$.
- ❌ Mezclar joules, newtons, metros y watts.
- ❌ Resolver álgebra sin identificar primero estados inicial y final.

## ✅ Checklist para volver al ejercicio

- [ ] Elegí el cuerpo o sistema.
- [ ] Marqué estados inicial y final.
- [ ] Dibujé el desplazamiento y las fuerzas reales.
- [ ] Decidí qué fuerzas realizan trabajo y con qué signo.
- [ ] Declaré la referencia de energía potencial si hacía falta.
- [ ] Incluí el efecto de las fuerzas no conservativas.
- [ ] Revisé unidades y sentido físico del resultado.
