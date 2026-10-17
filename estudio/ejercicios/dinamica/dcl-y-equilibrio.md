# DCL y equilibrio: reconocer las fuerzas antes de calcular

[Índice de ejercicios](README.md) · [Teoría](../../apuntes/dinamica/teoria-completa.md) · [Fuentes y claves](../../apuntes/dinamica/fuentes.md)

## 1. Los doce casos del TP introductorio

**Fuente:** D-intro, casos I–XII. Se pide identificar sistema, entorno,
modelo, fuerzas, reacciones y marco. Usamos modelo de partícula para la
traslación; en los sistemas de dos bloques hacemos un DCL por bloque.

La tabla describe las fuerzas **sobre el cuerpo elegido**, no sus reacciones.
Salvo la órbita, el suelo se toma como marco inercial aproximado. En la
órbita usamos un marco aproximadamente inercial centrado en la Tierra.

| Caso | Agentes y fuerzas reales | Qué concluir y qué falta decidir |
| --- | --- | --- |
| I. Luna orbitando | Tierra: fuerza gravitatoria hacia su centro | La órbita requiere aceleración radial; no hay equilibrio inercial |
| II. Objeto lanzado hacia arriba | Tierra: peso, después de soltarlo y sin aire | El mismo DCL al subir, en la cima y al bajar; en la cima $v=0$, no $a=0$ |
| III. Bloque quieto sobre mesa rugosa | Tierra: peso; mesa: normal | Sin otra tendencia horizontal, $f_e=0$ y $N=mg$ |
| IV. Bloque tirado por cuerda horizontal | Peso, normal, tensión; roce si el contacto lo requiere | Calcular el roce estático requerido o usar cinético si desliza |
| V. Bloque sobre plano rugoso | Peso vertical, normal perpendicular, posible roce paralelo | El roce depende del régimen; en reposo sin otras fuerzas se requiere $mg\sin\beta$ cuesta arriba |
| VI. Cuerpo colgado | Peso y tensión | Si permanece quieto respecto del suelo, $T=mg$; si acelera, hay que plantear Newton |
| VII. Mano contra pared vertical | Peso; mano: fuerza horizontal; pared: normal y roce | Si está sostenido quieto, $N=F_{\mathrm{mano}}$, $f_e=mg\leq\mu_eN$ |
| VIII. Dos bloques apilados; se empuja el inferior | En el superior: peso, normal del inferior y roce; en el inferior: peso, normal del piso, normal y roce del superior, fuerza aplicada | Si acompañan sin deslizar, el roce acelera al superior; su reacción frena al inferior respecto de la fuerza aplicada |
| IX. Bloque deslizándose en mesa lisa | Peso y normal | $a=0$: puede seguir moviéndose sin fuerza horizontal |
| X. Bloque subiendo por plano liso | Peso y normal | Aceleración cuesta abajo; pierde rapidez |
| XI. Bloque bajando por plano liso | Las mismas fuerzas del caso X | La aceleración sigue cuesta abajo; gana rapidez |
| XII. Dos bloques juntos sobre mesa lisa, empuje sobre uno | En cada uno: peso, normal y fuerza del otro; el empujado recibe además la fuerza externa | Misma aceleración mientras mantengan contacto; la fuerza de contacto no es todo el empuje |

**Cómo agregar las reacciones:** para cada fuerza invertir agente y receptor.
La reacción al peso está en la Tierra; a la normal y al roce, en la
superficie; a la tensión, en la cuerda. Dibujarlas en el DCL del receptor
correspondiente, no en el del bloque.

**Verificación:** ninguna fuerza se introduce sólo porque el cuerpo se mueve.
**Error típico:** en X dibujar una fuerza cuesta arriba heredada del lanzamiento.
**Pregunta oral:** ¿por qué X y XI tienen el mismo DCL? Porque las
interacciones presentes son las mismas; el sentido de la velocidad no
crea una fuerza.

## 2. Bloque de 490 N sostenido por dos cuerdas

**Fuente:** D-2025, ejercicio 1; equivalente a D-I, ejercicio 4(a–c),
página PDF 3. Se buscan $T_2$ y $T_3$.

**Modelo:** cuerdas ideales; nudo de masa despreciable en equilibrio.
Los ángulos $\theta_2,\theta_3$ se miden **desde la horizontal**, como en
la figura del TP. El cable vertical transmite $T_1=490\ \mathrm N$.

**Esquema:** dos cuerdas salen del nudo hacia arriba, una a la izquierda
($T_2$) y otra a la derecha ($T_3$); la cuerda del bloque tira del nudo hacia
abajo ($T_1$). Ejes: $+x$ a la derecha, $+y$ arriba.

La idea es aislar el nudo: tres tensiones actúan sobre él. No se agrega el
peso del bloque también, porque su efecto ya llega mediante $T_1$.

$$
-T_2\cos\theta_2+T_3\cos\theta_3=0,
$$

$$
T_2\sin\theta_2+T_3\sin\theta_3-490=0.
$$

### a y b. Cuerdas simétricas

La ecuación horizontal da $T_2=T_3=T$. La vertical:

$$
2T\sin\theta=490
\quad\Longrightarrow\quad T=\frac{490}{2\sin\theta}.
$$

| Ángulo de cada cuerda | $T_2=T_3$ |
| --- | --- |
| $60^\circ$ | $282{,}90\ \mathrm N$ |
| $10^\circ$ | $1410{,}90\ \mathrm N$ |

**Lectura física:** las cuerdas casi horizontales necesitan tensiones
grandes porque cada una aporta poca componente vertical. En el límite
$\theta\to0$, no hay solución con tensión finita para sostener ese peso.

### c. Una cuerda a 60° y otra horizontal

Como $\theta_3=0$, la cuerda derecha no sostiene verticalmente:

$$
T_2\sin60^\circ=490
\quad\Rightarrow\quad T_2=565{,}80\ \mathrm N,
$$

$$
T_3=T_2\cos60^\circ=282{,}90\ \mathrm N.
$$

**Comprobación:** las componentes horizontales se anulan; la suma vertical
de las tensiones superiores vale 490 N en los tres casos.

**Construcción gráfica pedida en a:** dibujar los tres vectores punta con
cola, respetando sus direcciones. El polígono de fuerzas debe cerrar porque
la resultante es cero. La escala se elige explícitamente, por ejemplo
1 cm por 100 N; no se confunde este dibujo con el DCL.

**Error típico:** dividir el peso por dos sin considerar la inclinación.
**Pregunta oral:** ¿puede cada tensión superar el peso total? Sí, si sus
componentes verticales son pequeñas.
**Qué aprender:** usar primero equilibrio por componentes y leer desde dónde
se mide el ángulo.

## 3. Semáforo: cuerdas con ángulos distintos

**Fuente:** D-I, ejercicio 5, página PDF 3; R-I, páginas 3–10.
También aparece en el video GeoGebra TP 02 Ejercicio 5.

**Datos y pedido:** peso 125 N, cuerda izquierda a 37° y derecha a 53°
de la horizontal; calcular las tres tensiones. Hipótesis y ejes iguales
al caso anterior.

El semáforo está en equilibrio, por lo que su cuerda vertical tiene
$T_1=125\ \mathrm N$. Sobre el nudo:

$$
T_3\cos53^\circ=T_2\cos37^\circ,\qquad
T_2\sin37^\circ+T_3\sin53^\circ=125.
$$

Despejar $T_3$ de la primera y sustituir en la segunda evita adivinar una
repartición del peso. Equivalentemente:

$$
T_2=\frac{125\cos53^\circ}{\sin(37^\circ+53^\circ)}
=75{,}23\ \mathrm N,
$$

$$
T_3=\frac{125\cos37^\circ}{\sin(37^\circ+53^\circ)}
=99{,}83\ \mathrm N.
$$

**Control:** cada componente horizontal vale aproximadamente 60,08 N;
las verticales suman 125 N. La cuerda más vertical tiene mayor tensión.

**Error típico:** usar 37° para ambas cuerdas por simetría visual.
**Pregunta oral:** ¿las dos tensiones superiores son acción y reacción?
No: son fuerzas sobre el mismo nudo, ejercidas por cuerdas distintas.
**Qué aprender:** los videos muestran el cierre vectorial; las ecuaciones
permiten obtener los módulos sin depender de la escala del dibujo.
