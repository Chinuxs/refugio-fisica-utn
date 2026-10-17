# Órbitas y radio de curvatura

[Índice](README.md) · [Guía por casos](../../apuntes/movimiento-circular/resolucion-por-casos.md) · [Fuentes](../../apuntes/movimiento-circular/fuentes.md)

## 1. Satélite a 350 km de altura

**Fuente:** C-actual, ejercicio 4.
**Datos:** $h=350\ \mathrm{km}$, $m=220\ \mathrm{kg}$,
$M_{\mathrm T}=5{,}98\times10^{24}\ \mathrm{kg}$,
$R_{\mathrm T}=6{,}371\times10^6\ \mathrm m$,
$G=6{,}674\times10^{-11}\ \mathrm{N\,m^2/kg^2}$.
Se piden rapidez orbital, aceleración centrípeta y período.

**Modelo:** órbita circular, Tierra esférica y masa central mucho mayor
que la del satélite; se desprecia arrastre. Marco aproximadamente
inercial centrado en la Tierra.

**DCL:** sólo gravedad hacia el centro. Eje radial positivo hacia adentro.
La velocidad es tangente y se dibuja separada del DCL.

Primero, el radio orbital:

$$
r=R_{\mathrm T}+h=6{,}721\times10^6\ \mathrm m.
$$

Newton radial:

$$
\frac{GM_{\mathrm T}m}{r^2}=m\frac{v^2}{r}.
$$

La masa del satélite se cancela:

$$
\boxed{v=\sqrt{\frac{GM_{\mathrm T}}r}
=7705{,}96\ \mathrm{m/s}\approx7{,}706\ \mathrm{km/s}}.
$$

$$
\boxed{a_r=\frac{GM_{\mathrm T}}{r^2}
=8{,}8353\ \mathrm{m/s^2}},
$$

$$
\boxed{T_{\mathrm{per}}=\frac{2\pi r}{v}
=5480{,}08\ \mathrm s=91{,}33\ \mathrm{min}}.
$$

**Verificación:** $v^2/r$ reproduce la aceleración gravitatoria a esa
altura. La fuerza radial sería $ma_r\approx1943{,}76\ \mathrm N$.
No se usó $g=9{,}8$ constante para una altura que el ejercicio permite
incorporar mediante gravitación.

**Error típico:** usar 350 km como radio o agregar una fuerza centrípeta
opuesta al peso.
**Pregunta oral:** ¿el satélite está sin gravedad? No: la gravedad es
justamente la que lo mantiene en órbita.
**Qué aprender:** la órbita circular surge de igualar Newton radial con
la fuerza gravitatoria, no de equilibrar fuerzas.

## 2. Descenso del piloto: aceleración y fuerza de apoyo

**Fuente:** C-actual, ejercicio 2, con figura del descenso.
**Datos:** radio de curvatura inferior $\rho=280\ \mathrm m$ y aceleración
de referencia $5{,}5g$. Se pide la rapidez correspondiente.

Es un **modelo del ejercicio**, no una predicción fisiológica individual.
En la parte baja la normal a la trayectoria apunta hacia arriba.
Interpretamos los $5{,}5g$ como aceleración normal de ese tramo:

$$
a_r=\frac{v^2}{\rho}=5{,}5g
\Rightarrow
\boxed{v=\sqrt{5{,}5g\rho}=122{,}85\ \mathrm{m/s}}.
$$

Si se tratara de la magnitud de la aceleración total y hubiese aceleración
tangencial no nula, faltaría ese dato; se supone despreciable en el
instante analizado para usar directamente $v^2/\rho$.

### Qué cambiaría si el dato fuera una lectura de apoyo

En el DCL del piloto, en la parte baja: peso abajo y fuerza del asiento
$N$ arriba. Desde un marco inercial:

$$
N-mg=m\frac{v^2}{\rho}.
$$

Para el resultado anterior, $N=6{,}5mg$, no $5{,}5mg$.
Si otro enunciado fijara **$N=5{,}5mg$**, entonces
$a_r=4{,}5g$ y la rapidez sería $111{,}12\ \mathrm{m/s}$.
Esa segunda cifra responde a otra condición.

**Control:** aceleración se mide en m/s²; fuerza de apoyo, en N.
**Error típico:** confundir $N/m$ con $a_r$ sin descontar el peso.
**Pregunta oral:** ¿por qué aparece un $g$ adicional en $N/m$? Porque
el asiento debe compensar el peso y además producir la aceleración
ascendente necesaria.
