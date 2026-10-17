# Cuando cambia la rapidez: MCUV y etapas

[Índice](README.md) · [Teoría](../../apuntes/movimiento-circular/teoria-completa.md#5-aceleración-tangencial-y-movimiento-no-uniforme) · [Fuentes](../../apuntes/movimiento-circular/fuentes.md)

Estos problemas pertenecen a Movimiento Circular, pero no son MCU durante
las etapas con aceleración angular. Son cinemáticos: no hace falta
inventar fuerzas si sólo se piden ángulos, velocidades y aceleraciones.

## 1. Volante que parte del reposo

**Fuente:** C-PDF, ejercicio 2; TP 05 Ej 02.pdf.
**Datos:** $R=0{,}30\ \mathrm m$, $\omega_0=0$,
$\alpha=0{,}50\ \mathrm{rad/s^2}$ constante.
Se buscan $a_t$, $a_r$ y $|\vec a|$ al comenzar, a 120° y a 240°.

**Esquema:** punto sobre el borde; $\vec v$ tangente, $\vec a_r$ hacia
el centro y $\vec a_t$ tangente en el sentido de giro creciente.

La componente tangencial es constante:

$$
a_t=\alpha R=0{,}15\ \mathrm{m/s^2}.
$$

Como se dan ángulos y no tiempos, conviene:

$$
\omega^2=2\alpha\Delta\theta,\qquad
a_r=\omega^2R,\qquad |\vec a|=\sqrt{a_t^2+a_r^2}.
$$

Convertimos $120^\circ=2\pi/3$ rad y $240^\circ=4\pi/3$ rad:

| Posición desde el arranque | $a_t$ (m/s²) | $a_r$ (m/s²) | $|\vec a|$ (m/s²) |
| --- | --- | --- | --- |
| Inicio | 0,150 | 0 | 0,150 |
| 120° | 0,150 | 0,6283 | 0,6460 |
| 240° | 0,150 | 1,2566 | 1,2656 |

**Control:** al comenzar, $\omega=0$ y por eso no hay componente radial,
aunque sí hay aceleración tangencial.
**Error típico:** sumar $a_t+a_r$ como números sobre el mismo eje.
**Pregunta oral:** ¿aceleración angular constante implica aceleración
total constante? No, porque $a_r$ aumenta con $\omega^2$.

## 2. Motor de 500 a 3000 rpm: resultado impreso que hay que corregir

**Fuente:** C-PDF, ejercicio 7, página PDF 1.
**Datos:** 500 → 3000 rpm en 5 s con $\alpha$ constante; volante
de diámetro 45 cm. Se piden velocidades angulares, aceleración angular,
vueltas, rapidez del borde y aceleraciones del borde.

Tomamos positivo el sentido de giro:

$$
\omega_0=\frac{500(2\pi)}{60}=52{,}3599\ \mathrm{rad/s},
\qquad \omega_f=100\pi=314{,}1593\ \mathrm{rad/s}.
$$

$$
\boxed{\alpha=\frac{\omega_f-\omega_0}{5}
=52{,}3599\ \mathrm{rad/s^2}}.
$$

Con aceleración angular constante, la velocidad angular media es
$(\omega_0+\omega_f)/2$:

$$
\Delta\theta=\frac{\omega_0+\omega_f}{2}(5)
=916{,}2979\ \mathrm{rad},
$$

$$
\boxed{n=\frac{\Delta\theta}{2\pi}=145{,}8333\text{ vueltas}}.
$$

**Comprobación independiente en rpm:** la media es
$(500+3000)/2=1750$ rpm y el tiempo es $5/60$ min;
$1750(5/60)=145{,}8333$ vueltas. Los 112,5 de la respuesta del TP
no corresponden a estos datos.

El radio es $R=0{,}45/2=0{,}225\ \mathrm m$:

$$
\boxed{v_f=\omega_fR=70{,}686\ \mathrm{m/s}},
$$

$$
\boxed{a_t=\alpha R=11{,}781\ \mathrm{m/s^2}},
\qquad
\boxed{a_{r,f}=\omega_f^2R=22206{,}61\ \mathrm{m/s^2}}.
$$

La aceleración radial grande es compatible con un borde que recorre
un radio pequeño a gran rapidez. Usar $\pi=3{,}14$ prematuramente explica
la diferencia menor con los 22184 m/s² impresos.

**Error típico:** usar diámetro como radio o usar sólo $\omega_f t$
para un intervalo en el que la velocidad angular cambia.
**Qué aprender:** verificar las vueltas también como área bajo
la gráfica $\omega(t)$.

## 3. Arranque, giro uniforme y frenado

**Fuente:** C-PDF, ejercicio 3, página PDF 1.
**Datos:** parte del reposo, llega a 200 rpm en 6 s, mantiene esa rapidez
durante un tiempo desconocido y se detiene en 5 min; total 3100 vueltas.

**Hipótesis de la resolución:** arranque y frenado uniformemente acelerados.
El primer tramo lo declara el enunciado; para el frenado se adopta la
misma idealización usada por la respuesta del TP.

Conviene trabajar inicialmente con vueltas y segundos:
$f=200/60=10/3$ vueltas/s.

El área bajo la gráfica de frecuencia contra tiempo cuenta vueltas:

| Tramo | Figura del área | Vueltas |
| --- | --- | --- |
| Arranque, 6 s | Triángulo | $\tfrac12(6)(10/3)=10$ |
| MCU, tiempo $t_u$ | Rectángulo | $(10/3)t_u$ |
| Frenado, 300 s | Triángulo | $\tfrac12(300)(10/3)=500$ |

$$
10+\frac{10}{3}t_u+500=3100
\Rightarrow t_u=777\ \mathrm s.
$$

$$
\boxed{t_{\mathrm{total}}=6+777+300=1083\ \mathrm s},
\qquad
\boxed{\Delta\theta_{\mathrm{total}}=6200\pi\ \mathrm{rad}}.
$$

**Control:** 3100 vueltas a la rapidez máxima llevarían 930 s; el total
debe ser mayor porque hubo arranque y frenado.
**Error típico:** convertir “5 min” en 5 s o usar una sola $\alpha$
para las tres etapas.
**Pregunta oral:** ¿cuál tramo es MCU? Sólo el de frecuencia constante.
