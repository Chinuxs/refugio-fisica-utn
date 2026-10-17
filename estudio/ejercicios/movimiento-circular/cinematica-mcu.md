# MCU: Tierra, nave y transmisiones

[Índice](README.md) · [Teoría](../../apuntes/movimiento-circular/teoria-completa.md) · [Fuentes](../../apuntes/movimiento-circular/fuentes.md)

## 1. Rotación terrestre y latitud

**Fuente:** C-actual, ejercicio 1.
**Datos:** radio terrestre $R_{\mathrm T}=6380\ \mathrm{km}$, una vuelta
en 24 h; latitud de La Plata $34{,}92126^\circ$ sur.
Se buscan velocidad angular, rapideces en el ecuador y La Plata,
aceleración radial ecuatorial y período que daría $a_r=g$.

**Modelo:** Tierra esférica con rotación uniforme alrededor de eje fijo.
Es un cálculo cinemático; no hace falta DCL para los primeros incisos.

**Esquema:** una persona en el ecuador describe un círculo de radio
$R_{\mathrm T}$. A latitud $\lambda$, su círculo tiene radio
$R_{\mathrm T}\cos\lambda$, centrado sobre el eje de rotación.

### a. Velocidad angular

Convertimos antes de reemplazar:

$$
R_{\mathrm T}=6{,}380\times10^6\ \mathrm m,\qquad
T_{\mathrm{per}}=24(3600)=86400\ \mathrm s.
$$

$$
\boxed{|\omega|=\frac{2\pi}{86400}
=7{,}2722\times10^{-5}\ \mathrm{rad/s}}.
$$

### b y c. Rapidez en dos latitudes

$$
\boxed{v_{\mathrm{ecuador}}=|\omega|R_{\mathrm T}
=463{,}97\ \mathrm{m/s}},
$$

$$
\boxed{v_{\mathrm{La\ Plata}}
=|\omega|R_{\mathrm T}\cos34{,}92126^\circ
=380{,}42\ \mathrm{m/s}}.
$$

Son módulos. La velocidad vectorial es tangente al paralelo, en el sentido
de rotación. Ambas personas comparten período y velocidad angular.

### d. Aceleración radial en el ecuador

$$
a_r=\omega^2R_{\mathrm T}
=0{,}03374\ \mathrm{m/s^2},
\qquad
\boxed{\frac{a_r}{g}=0{,}003443}.
$$

Es aproximadamente $0{,}3443\%$ de $g$.
Apunta hacia el eje; en el ecuador ese sentido coincide con el centro
de la Tierra. En otras latitudes no son la misma dirección.

### e. Período para que a_r sea igual a g

Mantenemos el radio y el valor de $g$ dados en el modelo:

$$
\left(\frac{2\pi}{T_{\mathrm{per}}}\right)^2R_{\mathrm T}=g
\Rightarrow
\boxed{T_{\mathrm{per}}=2\pi\sqrt{\frac{R_{\mathrm T}}g}
=5069{,}64\ \mathrm s=84{,}49\ \mathrm{min}}.
$$

**Control:** el período debe ser mucho menor que 24 h para producir una
aceleración radial mucho mayor. Es una comparación ideal, sin modelar
deformaciones terrestres.
**Error típico:** usar el radio terrestre completo para La Plata.
**Pregunta oral:** ¿cambia $\omega$ con la latitud? No; cambia el radio
de la trayectoria y por eso cambia $v$.

## 2. Nave anular: de rpm a gravedad artificial

**Fuente:** C-actual, ejercicio 5.
**Datos:** nave en forma de anillo, $3\ \mathrm{rpm}$; se busca radio y
rapidez para una aceleración centrípeta de $9{,}8\ \mathrm{m/s^2}$.

**Esquema y DCL:** astronauta contra el borde interior. En el modelo sin
otras fuerzas radiales, el piso ejerce una normal hacia el eje:
$N=ma_r$. Observamos desde un marco inercial y elegimos $+r$ hacia el eje.

$$
|\omega|=\frac{3(2\pi)}{60}=\frac{\pi}{10}
=0{,}31416\ \mathrm{rad/s}.
$$

$$
\omega^2R=g
\Rightarrow
\boxed{R=\frac{g}{\omega^2}=99{,}29\ \mathrm m}.
$$

$$
\boxed{v=|\omega|R=31{,}19\ \mathrm{m/s}}.
$$

**Control:** $v^2/R=9{,}8\ \mathrm{m/s^2}$. Para girar más lentamente y
mantener el mismo efecto, haría falta un radio mayor.
**Error típico:** reemplazar 3 directamente como rad/s.
**Pregunta oral:** ¿qué fuerza real produce la aceleración? La normal del piso.
**Qué aprender:** la igualdad $a_r=g$ es la condición de diseño, no una
afirmación de que la nave generó gravedad terrestre.

## 3. Poleas y correa: cuándo igualar omega y cuándo igualar v

**Fuente:** C-PDF, ejercicio 5, página PDF 1; TP 05 Ej 05.pdf.
**Datos:** eje motor a 1800 rpm, poleas de diámetros 5, 10 y 15 cm.
Otro eje tiene el mismo conjunto. Se buscan rapideces de los bordes y
velocidades del segundo eje para las tres conexiones indicadas.

**Modelo:** poleas rígidas sobre cada eje, correa tensa sin deslizamiento.
Problema cinemático; las tensiones de la correa no se necesitan.

En el eje motor:

$$
\omega_1=\frac{1800(2\pi)}{60}=60\pi\ \mathrm{rad/s}.
$$

Convertir **diámetro a radio** antes de usar $v=\omega R$:

| Diámetro | Radio | Rapidez del borde |
| --- | --- | --- |
| 5 cm | 0,025 m | $1{,}5\pi=4{,}712\ \mathrm{m/s}$ |
| 10 cm | 0,050 m | $3\pi=9{,}425\ \mathrm{m/s}$ |
| 15 cm | 0,075 m | $4{,}5\pi=14{,}137\ \mathrm{m/s}$ |

La correa iguala la rapidez de los bordes que conecta:

$$
|\omega_1|R_1=|\omega_2|R_2
\Rightarrow n_2=n_1\frac{D_1}{D_2}.
$$

| Polea motriz → conducida | Rapidez angular del segundo eje |
| --- | --- |
| 5 cm → 15 cm | 600 rpm = $20\pi\ \mathrm{rad/s}$ |
| 10 cm → 10 cm | 1800 rpm = $60\pi\ \mathrm{rad/s}$ |
| 15 cm → 5 cm | 5400 rpm = $180\pi\ \mathrm{rad/s}$ |

**Control:** una polea conducida mayor gira menos veces por segundo.
Las otras poleas del mismo eje conducido comparten su velocidad angular.
**Error típico:** imponer la misma $\omega$ en ejes distintos unidos por correa.
**Pregunta oral:** ¿qué cambia si patina la correa? Deja de valer la
igualdad de rapideces en el contacto.
