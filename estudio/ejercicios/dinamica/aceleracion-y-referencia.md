# Aceleración, referencia y peso aparente

[Índice](README.md) · [Teoría](../../apuntes/dinamica/teoria-completa.md) · [Fuentes](../../apuntes/dinamica/fuentes.md)

## 1. Bloque elevado: tensión, velocidad constante y cuerda floja

**Fuente:** D-II, ejercicio 3, página PDF 1.
**Datos:** $m=5\ \mathrm{kg}$, primero $a_y=+2\ \mathrm{m/s^2}$;
luego tensión 49 N; finalmente la cuerda se afloja y el bloque sube
2 m antes de detenerse.

**DCL:** peso abajo y tensión arriba mientras la cuerda está tensa.
Marco del suelo y $+y$ hacia arriba.

### a. Aceleración hacia arriba

$$
T-mg=ma_y\Rightarrow
\boxed{T=5(9{,}8+2)=59\ \mathrm N}.
$$

### b. Tensión de 49 N

$$
49-5(9{,}8)=5a_y\Rightarrow a_y=0.
$$

La velocidad adquirida se conserva: el bloque continúa subiendo
uniformemente si todavía tenía velocidad ascendente. No se detiene
por quedar equilibradas las fuerzas.

### c. Cuerda floja

Ahora $T=0$ y $a_y=-g$. Entre el instante de aflojarse y la altura máxima:

$$
v_f^2=v_i^2+2a_y\Delta y,\qquad
0=v_i^2-2(9{,}8)(2),
$$

$$
\boxed{v_i=6{,}26\ \mathrm{m/s}\text{ hacia arriba}}.
$$

**Control:** la resultante sigue hacia abajo en la cima aunque $v_f=0$.
**Error típico:** mantener la tensión en el DCL después de aflojarse.
**Qué aprender:** cada etapa puede tener un DCL distinto.

## 2. Balanza dentro de un ascensor

**Fuente:** D-II, ejercicio 7, página PDF 2.
**Datos:** la balanza indica 220 N al acelerar hacia arriba a
$1{,}20\ \mathrm{m/s^2}$. Se pide el peso real, cuándo marcará 175 N
y la lectura si el ascensor cae libremente.

**Modelo:** el cuerpo acompaña al ascensor, balanza ideal; se desprecia
el aire. El suelo es marco inercial aproximado.
En el DCL del cuerpo: tensión $T$ arriba y peso abajo; $+y$ arriba.

### a. Hallar masa y peso

$$
T-mg=ma_y
\Rightarrow m=\frac{220}{9{,}8+1{,}20}=20\ \mathrm{kg}.
$$

$$
\boxed{P=196\ \mathrm N}.
$$

### b. Lectura de 175 N

$$
a_y=\frac{175-196}{20}=-1{,}05\ \mathrm{m/s^2}.
$$

La aceleración es hacia abajo. Puede ocurrir al bajar ganando rapidez,
o al subir frenando; la lectura no determina por sí sola la velocidad.

### c. Caída libre

$$
a_y=-g\Rightarrow T=m(g-g)=0.
$$

**Control:** el peso no desaparece; desaparece la fuerza de sostén ideal.
**Error típico:** sumar o restar $ma$ según “sube” o “baja” sin conocer
la aceleración.
**Pregunta oral:** ¿qué mide la balanza? La tensión; no directamente el
campo gravitatorio ni la masa.

## 3. Caja en un camión: el roce puede acelerar o frenar

**Fuente:** D-II, ejercicio 11, páginas PDF 3–4.
**Datos:** $m=40\ \mathrm{kg}$, $\mu_e=0{,}30$, $\mu_d=0{,}20$.
Camión sobre camino horizontal; inicialmente la caja lo acompaña.
Se pide el roce al acelerar a $1{,}80\ \mathrm{m/s^2}$ y al frenar
con aceleración $-3\ \mathrm{m/s^2}$.

**Marco y DCL:** observamos desde el suelo; $+x$ hacia adelante.
Peso y normal se equilibran verticalmente:

$$
N=392\ \mathrm N,\qquad f_{e,\max}=117{,}6\ \mathrm N.
$$

La única fuerza horizontal sobre la caja es el roce.

### a. El camión acelera

Suponer que la caja acompaña requiere:

$$
f_{\mathrm{req}}=ma=40(1{,}80)=72\ \mathrm N.
$$

Como $72<117{,}6$, la hipótesis es posible:
$f_e=72\ \mathrm N$ **hacia adelante**. El roce estático acelera la caja.

### b. El camión frena

Para acompañar se necesitarían $40(3)=120\ \mathrm N$ hacia atrás.
No alcanza el máximo estático, así que la caja desliza hacia adelante
**respecto del camión**.

$$
\boxed{f_d=0{,}20(392)=78{,}4\ \mathrm N\text{ hacia atrás}}.
$$

La caja adquiere aceleración $a_{\mathrm{caja}}=-78{,}4/40
=-1{,}96\ \mathrm{m/s^2}$, distinta de la del camión.

**Control:** la aceleración relativa es
$a_{\mathrm{caja}}-a_{\mathrm{camión}}=+1{,}04\ \mathrm{m/s^2}$,
compatible con deslizar hacia adelante sobre la plataforma.
**Error típico:** imponer que la caja tenga la aceleración del camión
incluso después de que falla la adherencia.
**Pregunta oral:** ¿por qué en a no se usa $a=0$ si el roce es estático?
Porque la caja está quieta respecto del camión, no del suelo.

## 4. Una fuerza variable elegida por el experimentador

**Fuente:** video “Ejemplo ejercicio de dinámica.mp4”, versión 2025.
La escritura visible muestra una masa colgante $m_1=2\ \mathrm{kg}$
y otra $m_2=8\ \mathrm{kg}$ sobre mesa lisa, unidas por polea fija;
una fuerza horizontal $F$ tira del bloque de la mesa alejándolo de la polea.
Se reconstruye el planteo visible; no se atribuyen consignas no transcritas.

**Ejes compatibles:** para $m_2$, positivo alejándose de la polea;
para $m_1$, positivo arriba. La cuerda ideal tensa da el mismo $a$.
DCL: peso y tensión en $m_1$; peso, normal, tensión y $F$ en $m_2$.

$$
T-m_1g=m_1a,\qquad F-T=m_2a.
$$

Al sumar:

$$
\boxed{a(F)=\frac{F-m_1g}{m_1+m_2}},
\qquad
\boxed{T(F)=\frac{m_1(F+m_2g)}{m_1+m_2}}.
$$

Con $F$ expresada en N:

$$
a=\frac{F-19{,}6\ \mathrm N}{10\ \mathrm{kg}}.
$$

| Valor de F | Aceleración | Interpretación |
| --- | --- | --- |
| $F<19{,}6\ \mathrm N$, con $F\geq0$ | Negativa | La aceleración de la masa colgante apunta hacia abajo |
| $F=19{,}6\ \mathrm N$ | Cero | Equilibrio o velocidad constante, según el estado inicial |
| $F>19{,}6\ \mathrm N$ | Positiva | La aceleración de la masa colgante apunta hacia arriba |

**Control:** en $F=19{,}6\ \mathrm N$, $T=19{,}6\ \mathrm N$.
En $F=0$, $a=-1{,}96\ \mathrm{m/s^2}$ y $T=15{,}68\ \mathrm N$.
**Error típico:** cambiar de signo una tensión porque cambió el sentido
de la aceleración. La cuerda sigue tirando en la misma dirección geométrica.
**Qué aprender:** obtener primero una expresión simbólica permite estudiar
varios casos sin resolver desde cero.
