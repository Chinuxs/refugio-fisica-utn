# Rozamiento y planos: cómo cambia el planteo

[Índice](README.md) · [Guía por casos](../../apuntes/dinamica/resolucion-por-casos.md) · [Fuentes](../../apuntes/dinamica/fuentes.md)

## 1. Bloque de 196 N: los cinco regímenes del ejercicio

**Fuente:** D-2025, ejercicio 2; D-I, ejercicio 7, página PDF 3.

**Datos:** $P=196\ \mathrm N$, $\mu_e=0{,}40$, $\mu_d=0{,}20$.
Bloque sobre mesa horizontal fija; fuerza aplicada horizontal.
Se pide el rozamiento y los valores de fuerza que inician o mantienen
el movimiento.

**DCL:** peso abajo, normal arriba, fuerza aplicada a la derecha y roce
opuesto al deslizamiento o a su tendencia. $+x$ a la derecha.

$$
N-P=0\Rightarrow N=196\ \mathrm N,\qquad
m=P/g=20\ \mathrm{kg}.
$$

$$
f_{e,\max}=0{,}40(196)=78{,}4\ \mathrm N,\qquad
f_d=0{,}20(196)=39{,}2\ \mathrm N.
$$

| Inciso | Razonamiento | Resultado |
| --- | --- | --- |
| a. Sin fuerza horizontal | No hay tendencia a deslizar | $f=0$ |
| b. Se aplican 49 N desde el reposo | Para equilibrar se necesitan 49 N, menores que 78,4 N | $f_e=49\ \mathrm N$ hacia la izquierda, $a=0$ |
| c. Umbral de inicio | Se alcanza el máximo estático | $F_{\mathrm{umbral}}=78{,}4\ \mathrm N$ |
| d. Movimiento a velocidad constante ya iniciado | El roce es cinético y $F-f_d=0$ | $F=39{,}2\ \mathrm N$ |
| e. Se aplican 98 N | Superan el máximo estático; desliza | $f_d=39{,}2\ \mathrm N$ hacia la izquierda |

En e, además:

$$
a=\frac{98-39{,}2}{20}=2{,}94\ \mathrm{m/s^2}.
$$

En c, la igualdad describe el estado de deslizamiento inminente; para
garantizar el arranque en el modelo ideal hay que superar ese umbral.
En d, si “mantener movimiento” significa mantener **rapidez constante**,
la respuesta es la indicada; una fuerza menor permite movimiento transitorio
mientras el bloque se frena.

**Control:** los 49 N del inciso b no se reemplazan por 78,4 N: ese es el
máximo disponible, no lo requerido.
**Error típico:** usar roce dinámico sólo porque existe una fuerza aplicada.
**Pregunta oral:** ¿por qué cuesta más arrancarlo que mantener rapidez?
Porque los coeficientes dados tienen $\mu_e>\mu_d$.

## 2. Plano y masa colgante: invertir el movimiento invierte el roce

**Fuente:** D-2025, ejercicio 3; D-I, ejercicio 8, página PDF 3.

**Datos:** bloque $A$ de 12 kg en plano de 30°, unido por cuerda ideal y
polea fija ideal a $B$. Cuando $m_B=2\ \mathrm{kg}$, $A$ baja con
velocidad constante. Se pide el peso de $B$ para que $A$ suba también
con velocidad constante.

**Esquema:** $A$ sobre el plano, cuerda paralela a él; $B$ cuelga del otro
lado. Sobre $A$: peso, normal, tensión cuesta arriba y roce contrario
al deslizamiento. Sobre $B$: peso y tensión.

### Primera situación: A baja

Tomamos $+x_A$ cuesta abajo. Como la velocidad es constante, $a=0$.
Para $B$, el equilibrio da $T=m_Bg=19{,}6\ \mathrm N$.

$$
N=12g\cos30^\circ=101{,}84\ \mathrm N,
$$

$$
12g\sin30^\circ-T-f_d=0
\Rightarrow f_d=58{,}8-19{,}6=39{,}2\ \mathrm N.
$$

Podemos recuperar el coeficiente:

$$
\mu_d=\frac{39{,}2}{101{,}84}=0{,}3849.
$$

### Segunda situación: A sube

La normal no cambia. Suponemos las mismas superficies y el mismo modelo
de roce cinético, de modo que su módulo sigue siendo 39,2 N, pero ahora
apunta cuesta abajo.

Con $+x_A$ cuesta arriba:

$$
T'-12g\sin30^\circ-f_d=0
\Rightarrow T'=58{,}8+39{,}2=98\ \mathrm N.
$$

Como $B$ también va a velocidad constante:

$$
\boxed{P_B'=T'=98\ \mathrm N,\qquad m_B'=10\ \mathrm{kg}}.
$$

**Control:** para invertir el deslizamiento a rapidez constante, la tensión
aumentó en $2f_d=78{,}4\ \mathrm N$.
**Error típico:** conservar el signo del roce al invertir la velocidad.
**Pregunta oral:** ¿por qué no cambia $N$? Porque la cuerda es paralela
al plano y no cambia el balance perpendicular.

## 3. Mismo plano, pero ahora se pide permanecer en reposo

**Fuente:** D-I, ejercicio 9, páginas PDF 3–4. Los coeficientes de este
ejercicio son $\mu_e=0{,}40$ y $\mu_d=0{,}20$; **no** se usa el $\mu_d$
deducido en el ejercicio anterior.

**Datos:** $m_A=12\ \mathrm{kg}$, $\beta=30^\circ$. Se busca el intervalo
de pesos de $B$ que admite reposo.

Elegimos positivo cuesta arriba para $A$ y permitimos que $f_e$ tenga signo:

$$
T+f_e-m_Ag\sin\beta=0,\qquad T=P_B,
$$

$$
|m_Ag\sin\beta-P_B|\leq\mu_em_Ag\cos\beta.
$$

Por lo tanto:

$$
58{,}8-40{,}74\leq P_B\leq58{,}8+40{,}74,
$$

$$
\boxed{18{,}06\ \mathrm N\leq P_B\leq99{,}54\ \mathrm N}.
$$

En el límite inferior, $A$ tendería a bajar y el roce apunta cuesta arriba.
En el superior, tendería a subir y el roce apunta cuesta abajo.

**Qué aprender:** un intervalo de equilibrio puede tener dos límites
distintos; no se asigna al roce un único sentido para todos los pesos.

## 4. Bloque de 980 N, nudo y peso suspendido

**Fuente:** D-2025, ejercicio 4; D-I, ejercicio 10, página PDF 4.

**Datos:** $P_A=980\ \mathrm N$, $\mu_e=0{,}30$, peso colgante
$W=196\ \mathrm N$, cuerda del soporte a 45°. Se pide el roce en $A$
y el máximo $W$ compatible con reposo.

**Esquema de la fuente:** una cuerda horizontal une $A$ con un nudo;
desde el nudo salen otra cuerda vertical hacia el peso y otra inclinada
hacia el soporte. La cuerda inclinada **no tira directamente del bloque A**.

En el nudo, si $T_o$ es la tensión oblicua:

$$
T_o\sin45^\circ=W,\qquad T_A=T_o\cos45^\circ
\Rightarrow T_A=W.
$$

En $A$, con $+x$ hacia el nudo:

$$
N=P_A=980\ \mathrm N,\qquad T_A-f_e=0.
$$

Entonces $f_e=196\ \mathrm N$; es posible porque
$196<0{,}30(980)=294\ \mathrm N$.

En el límite:

$$
\boxed{W_{\max}=294\ \mathrm N}.
$$

**Control:** cambiar el peso modifica la tensión, no la normal de $A$,
porque la cuerda que llega a $A$ es horizontal.
**Error típico:** usar una componente oblicua sobre $A$ que pertenece
al DCL del nudo.
**Pregunta oral:** ¿qué pasaría con otro ángulo $\theta$? En esa geometría
$T_A=W\cot\theta$ y habría que rehacer la relación de fuerzas.

## 5. Bloques superpuestos arrastrados a velocidad constante

**Fuente:** D-2025, ejercicio 5; D-I, ejercicio 11, página PDF 4.

**Datos:** $P_A=39{,}2\ \mathrm N$ sobre $B$, $P_B=78{,}4\ \mathrm N$;
$\mu_d=0{,}25$ entre superficies que deslizan. Se tira de $B$ a la
izquierda con rapidez constante.

**DCL comunes:** en $A$ actúan su peso y la normal de $B$; en $B$, su peso,
la normal de $A$, la normal del piso y la fuerza aplicada. Hay que agregar
rozamiento y tensión según el caso.

$$
N_{AB}=P_A=39{,}2\ \mathrm N,\qquad
N_{\mathrm{piso}}=P_A+P_B=117{,}6\ \mathrm N,
$$

$$
f_{\mathrm{piso}}=29{,}4\ \mathrm N,\qquad
f_{AB,d}=9{,}8\ \mathrm N.
$$

Tomamos positivo hacia la izquierda para $B$:

| Caso | Ecuación de B, con $a_B=0$ | Fuerza aplicada |
| --- | --- | --- |
| a. A acompaña a B sin deslizar | $F-f_{\mathrm{piso}}=0$ | $29{,}4\ \mathrm N$ |
| b. A queda atado al soporte | $F-f_{\mathrm{piso}}-f_{AB,d}=0$ | $39{,}2\ \mathrm N$ |
| c. Cuerda une A y B pasando por polea fija | $F-f_{\mathrm{piso}}-f_{AB,d}-T=0$ | $49{,}0\ \mathrm N$ |

En a, el roce entre $A$ y $B$ vale cero en el movimiento uniforme indicado:
$A$ no necesita fuerza horizontal neta. No se aplica $\mu_dN$ a ese contacto.

En b, la cuerda mantiene $A$ quieto y equilibra su roce.
En c, la cuerda obliga a $A$ a moverse a la derecha mientras $B$ va a la
izquierda. En el DCL de $A$, $T=f_{AB,d}=9{,}8\ \mathrm N$.
Esa tensión también tira de $B$ a la derecha y debe sumarse a las
resistencias que equilibra $F$.

**Control:** cada contacto usa su propia normal; el piso sostiene el peso
de ambos bloques.
**Error típico:** creer que “hay rozamiento entre todas las superficies”
obliga a usar roce cinético en un contacto que no desliza.
**Qué aprender:** hacer un DCL por bloque y comprobar el movimiento relativo
en cada interfaz.
