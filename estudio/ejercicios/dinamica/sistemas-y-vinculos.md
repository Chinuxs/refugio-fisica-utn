# Sistemas de cuerpos: contacto, roce y poleas

[Índice](README.md) · [Guía por casos](../../apuntes/dinamica/resolucion-por-casos.md) · [Fuentes](../../apuntes/dinamica/fuentes.md)

## 1. Dos bloques en contacto

**Fuente:** D-II, ejercicio 1, página PDF 1.
**Datos:** $m_1=2\ \mathrm{kg}$, $m_2=4\ \mathrm{kg}$, $F=3\ \mathrm N$;
mesa lisa. Se buscan aceleración, resultantes y fuerza de contacto.

**DCL y ejes:** $+x$ en el sentido del empuje. Cada bloque tiene peso y
normal equilibrados. El empujado recibe $F$ y una fuerza de contacto hacia
atrás; el otro recibe contacto hacia adelante.

Para el conjunto:

$$
F=(m_1+m_2)a\Rightarrow a=0{,}50\ \mathrm{m/s^2}.
$$

Las resultantes individuales son $m_1a=1\ \mathrm N$ y $m_2a=2\ \mathrm N$.

| Empuje aplicado sobre… | Aislar el bloque que sólo recibe contacto | Contacto |
| --- | --- | --- |
| $m_1$ | $C=m_2a$ | $2\ \mathrm N$ |
| $m_2$ | $C=m_1a$ | $1\ \mathrm N$ |

**Control:** en el bloque empujado, $F-C$ da su propia resultante.
**Error típico:** suponer que toda la fuerza externa se transmite al otro.
**Pregunta oral:** ¿cambia la aceleración al invertir el orden? No, pero
sí cambia la fuerza necesaria para acelerar al bloque que queda adelante.

<a id="bloques-apilados"></a>
## 2. Bloques apilados: adherencia y deslizamiento

**Fuente:** D-II, ejercicio 2; resolución R-II, páginas 1–6.
**Datos:** superior $m_1=2\ \mathrm{kg}$, inferior $m_2=4\ \mathrm{kg}$,
$\mu_e=0{,}20$, $\mu_d=0{,}17$; mesa lisa.
Se pide la fuerza máxima sin deslizamiento y las aceleraciones al duplicarla.

**Interpretación principal:** $F$ actúa sobre el bloque **inferior**, como
en R-II y en la foto de clase. La figura del TP PDF sugiere aplicación sobre
el superior; se resuelve esa alternativa al final.

**DCL:** el superior tiene peso, normal del inferior y roce en el sentido
de $F$. El inferior recibe $F$, el roce opuesto, su peso, la normal del
superior y la normal del piso. Tomamos $+x$ en el sentido de $F$.

### a. Se mueven juntos

$$
N_{12}=m_1g=19{,}6\ \mathrm N,\qquad
f_{e,\max}=0{,}20(19{,}6)=3{,}92\ \mathrm N.
$$

Para el superior, $f_e=m_1a$, de modo que
$a_{\max}=3{,}92/2=1{,}96\ \mathrm{m/s^2}$.
Para el conjunto:

$$
\boxed{F_{\max}=(m_1+m_2)a_{\max}=11{,}76\ \mathrm N}.
$$

### b. Se aplica el doble

Ahora $F=23{,}52\ \mathrm N$ y no alcanza el roce estático.
La superficie superior de $m_2$ desliza en el sentido de $F$ respecto de
$m_1$. El roce cinético sobre $m_1$ sigue en ese sentido:

$$
f_d=0{,}17(19{,}6)=3{,}332\ \mathrm N,
$$

$$
\boxed{a_1=f_d/m_1=1{,}666\ \mathrm{m/s^2}},
$$

$$
\boxed{a_2=(F-f_d)/m_2=5{,}047\ \mathrm{m/s^2}}.
$$

**Control:** $a_2>a_1$ confirma el deslizamiento relativo supuesto.
$m_1a_1+m_2a_2=F$; ya no corresponde usar una única aceleración común.

### Si la fuerza actúa sobre el superior

El inferior sólo acelera por roce: $f_e=m_2a$.
Entonces:

$$
a_{\max}=\frac{\mu_em_1g}{m_2}=0{,}98\ \mathrm{m/s^2},
\qquad F_{\max}=5{,}88\ \mathrm N.
$$

Al duplicar **este** máximo, $F=11{,}76\ \mathrm N$:

$$
a_1=\frac{11{,}76-3{,}332}{2}=4{,}214\ \mathrm{m/s^2},
\qquad a_2=\frac{3{,}332}{4}=0{,}833\ \mathrm{m/s^2}.
$$

**Qué aprender:** el cuerpo que recibe la fuerza importa. No modificar los
datos para hacer coincidir una respuesta con una figura diferente.
**Pregunta oral:** ¿por qué el roce estático puede acelerar al superior?
Porque “estático” se refiere a que no desliza sobre el inferior.

## 3. Mesa y masa colgante: primero equilibrio, después movimiento

**Fuente:** D-II, ejercicio 6, página PDF 2.
**Datos:** $m_A=10\ \mathrm{kg}$ sobre mesa, $m_B=5\ \mathrm{kg}$ colgante,
coeficiente dado 0,20; bloque $C$ apoyado sobre $A$.
Se pide $m_C$ mínimo que impide el arranque y la aceleración al retirar $C$.

**Modelo:** cuerda inextensible, polea fija ideal; $C$ aumenta la normal
sobre la mesa. Para reproducir ambos incisos del TP se toma
$\mu_e=\mu_d=0{,}20$, pues el enunciado da un solo coeficiente.

**DCL:** sobre $A$, tensión hacia la polea, roce opuesto, peso, normal
de la mesa y contacto de $C$; sobre $B$, peso abajo y tensión arriba.

### a. Masa mínima para permanecer en reposo

$$
T=m_Bg,\qquad f_e=T,\qquad N=(m_A+m_C)g.
$$

En el umbral:

$$
m_Bg=\mu_e(m_A+m_C)g
\Rightarrow
\boxed{m_C=15\ \mathrm{kg}}.
$$

### b. Al retirar C

El máximo estático baja a $0{,}20(10g)=19{,}6\ \mathrm N$,
menor que los 49 N requeridos: arranca con $B$ descendiendo.

Elegimos $+x_A$ hacia la polea y $+y_B$ hacia abajo. La cuerda fija
impone el mismo módulo $a$:

$$
T-19{,}6=10a,\qquad 49-T=5a.
$$

Sumar elimina la tensión:

$$
\boxed{a=\frac{49-19{,}6}{15}=1{,}96\ \mathrm{m/s^2}},
\qquad T=39{,}2\ \mathrm N.
$$

**Control:** $T<49\ \mathrm N$ permite que $B$ acelere hacia abajo.
**Error típico:** quitar $C$ de la masa total y olvidar que también cambia
la normal y el roce.

## 4. Dos planos conectados por una polea fija

**Fuente:** D-II, ejercicio 12, figura 03-06(b), página PDF 4.
**Datos:** $m_1=20\ \mathrm{kg}$ sobre 30° y $m_2=18\ \mathrm{kg}$
sobre 60°. Se buscan $a$ y $T$, sin roce y con coeficiente 0,10.

**DCL:** cada bloque tiene peso, normal perpendicular y tensión cuesta
arriba. Con deslizamiento, el roce se opone a la velocidad sobre cada plano.
Cuerda tensa y polea fija ideales.

Sin roce, comparar $m_2g\sin60^\circ=152{,}77\ \mathrm N$ con
$m_1g\sin30^\circ=98\ \mathrm N$. Tomamos $m_2$ bajando y $m_1$
subiendo como sentidos positivos compatibles.

$$
T-m_1g\sin30^\circ=m_1a,
\qquad m_2g\sin60^\circ-T=m_2a.
$$

$$
\boxed{a=1{,}441\ \mathrm{m/s^2},\qquad T=126{,}82\ \mathrm N}.
$$

Con deslizamiento en esos sentidos y $\mu_d=0{,}10$:

$$
a=\frac{m_2g\sin60^\circ-m_1g\sin30^\circ
-\mu_dg(m_1\cos30^\circ+m_2\cos60^\circ)}{m_1+m_2}
=0{,}7624\ \mathrm{m/s^2}.
$$

$$
T=m_1a+m_1g\sin30^\circ+\mu_dm_1g\cos30^\circ
=130{,}22\ \mathrm N.
$$

Si el coeficiente 0,10 también se usa como estático al arrancar, la
diferencia de componentes de peso, 54,77 N, supera el máximo conjunto
25,79 N: el sentido supuesto es compatible con el arranque.

**Control:** el roce reduce la aceleración; las dos ecuaciones deben
producir la misma tensión. Pequeñas diferencias con las respuestas del TP
provienen de redondear aceleraciones antes de recuperar $T$.
**Error típico:** usar las masas para decidir el sentido sin proyectar
los pesos sobre sus planos.

<a id="polea-movil"></a>
## 5. Polea móvil: la cuerda fija la relación de aceleraciones

**Fuente:** D-II, ejercicio 15, figuras 03-08(a–b), página PDF 4.
**Datos:** $m_1=4\ \mathrm{kg}$, $m_2=6\ \mathrm{kg}$, mesa lisa;
poleas y cuerdas ideales. Se piden las aceleraciones y tensiones.

![Comparación de las dos geometrías de polea móvil del TP](../../apuntes/dinamica/assets/poleas-moviles.svg)

### a. La polea móvil sostiene a m2

$T_1$ es la tensión de la cuerda que viene desde $m_1$, pasa por la polea
fija, rodea la móvil y termina en el techo. $T_2$ es la del conector entre
la polea móvil y $m_2$.

Tomamos $x_1$ hacia la polea fija y $y_2$ hacia abajo. La longitud
de la cuerda larga contiene $-x_1+2y_2$:

$$
a_1=2a_2.
$$

La polea móvil sin masa tiene dos tirones $T_1$ hacia arriba y uno $T_2$
hacia abajo: $T_2=2T_1$.

$$
T_1=m_1a_1,\qquad m_2g-T_2=m_2a_2.
$$

Sustituyendo ambos vínculos:

$$
a_2=\frac{m_2g}{4m_1+m_2}
=2{,}673\ \mathrm{m/s^2},\qquad
a_1=5{,}345\ \mathrm{m/s^2},
$$

$$
T_1=21{,}38\ \mathrm N,\qquad T_2=42{,}76\ \mathrm N.
$$

### b. La cuerda de m1 sostiene el eje de la polea móvil

En esta figura, la cuerda de tensión $T_1$ pasa por la polea fija y se une
al **eje** de la móvil. Una segunda cuerda, de tensión $T_2$, tiene un
extremo fijo abajo, rodea la móvil por arriba y termina en $m_2$.

Si $y_p$ crece al bajar la polea, la primera cuerda da
$a_p=a_1$. La segunda tiene longitud
$\ell=\text{cte}+y_2-2y_p$, por lo que:

$$
a_2=2a_p=2a_1.
$$

La polea recibe $T_1$ hacia arriba y dos $T_2$ hacia abajo:
$T_1=2T_2$.

$$
T_1=m_1a_1,\qquad m_2g-T_2=m_2a_2.
$$

$$
m_2g-\frac{m_1a_1}{2}=2m_2a_1
\Rightarrow
a_1=\frac{2m_2g}{m_1+4m_2}=4{,}20\ \mathrm{m/s^2},
$$

$$
\boxed{a_2=8{,}40\ \mathrm{m/s^2},\quad
T_1=16{,}80\ \mathrm N,\quad T_2=8{,}40\ \mathrm N}.
$$

**Corrección comprobada:** el TP imprime $T_1=4{,}20\ \mathrm N$,
que no cumple $T_1=m_1a_1$. Su $T_2=8{,}40\ \mathrm N$ sí coincide.

**Control:** en b, $58{,}8-8{,}4=6(8{,}4)$ y $16{,}8=2(8{,}4)$.
**Error típico:** trasladar $a_1=2a_2$ de la figura a a la b.
**Pregunta oral:** ¿de dónde sale el factor 2? De contar los tramos
cuya longitud cambia, no de una propiedad universal de “las poleas”.

## 6. Tres masas y dos cuerdas

**Fuente:** D-II, ejercicio 17, página PDF 5.
**Datos:** 4 kg cuelgan a la izquierda, 2 kg sobre mesa y 1 kg a la
derecha; $\mu_d=0{,}35$. Se buscan aceleración y tensiones.

**Hipótesis:** sistema deslizándose hacia el lado de 4 kg. La guía sólo
da rozamiento cinético; no permite determinar el arranque desde reposo
si el coeficiente estático fuera desconocido.

**DCL:** cada colgante tiene peso y su propia tensión. El bloque central
tiene peso, normal, las dos tensiones y roce hacia la derecha.
Ejes positivos: izquierda para el central, abajo para 4 kg y arriba
para 1 kg. Las cuerdas fijas imponen módulos de aceleración iguales.

$$
4g-T_L=4a,\qquad
T_L-T_R-0{,}35(2g)=2a,\qquad
T_R-1g=1a.
$$

Sumando:

$$
a=\frac{(4-1)g-0{,}35(2g)}{4+2+1}
=3{,}22\ \mathrm{m/s^2}.
$$

Volviendo a los colgantes:

$$
\boxed{T_L=26{,}32\ \mathrm N,\qquad T_R=13{,}02\ \mathrm N}.
$$

**Control:** $T_L\ne T_R$: son cuerdas distintas.
La aceleración positiva es compatible con el deslizamiento supuesto.
**Qué aprender:** sumar las tres ecuaciones para $a$ y volver a los DCL
individuales para cada tensión.
