# Trabajo y Energía — balances, tramos y pérdidas

## 🎯 Qué recordar

Elegir **dos estados y un sistema** antes de escribir el balance. Un estado
se describe por su rapidez, altura y deformación del resorte. Un tramo se
describe por las fuerzas que actúan durante el recorrido.

La energía permite relacionar estados sin conocer cuánto tarda el cuerpo.
Para una normal, una tensión o un tiempo, puede hacer falta otra herramienta.
Fuentes: [presentación de cátedra, diap. 7–17 y 20–27](fuentes.md#trazabilidad-por-concepto).

## 🖼️ Esquema / dibujo

![Altura inicial, zona de roce y compresión: la energía mecánica cambia sólo en el tramo rugoso de esta pista ideal](assets/balance-energia.svg)

| Estado | Anotar antes de calcular |
| --- | --- |
| Inicio | ¿Parte del reposo? ¿Qué altura y deformación tiene? |
| Cambio de tramo | ¿Termina el roce? ¿Empieza el contacto con el resorte? |
| Final | ¿Se detiene un instante, alcanza una altura o debe mantener contacto? |

Esta tabla es una herramienta didáctica propia, aplicable a distintos enunciados.

## 📐 Fórmula

### Dos formas del mismo balance

Para una partícula de masa constante en un marco inercial:

$$
W_{\mathrm{neto}}=\Delta K,
\qquad
K_i+U_i+W_{nc}=K_f+U_f.
$$

En la segunda forma, el trabajo del peso y del resorte ya está representado
por sus potenciales: **no volver a sumarlo como trabajo**.

Si el sistema incluye bloque, Tierra, resorte y superficie, y no intercambia
energía con el entorno, también puede escribirse:

$$
\Delta K+\Delta U+\Delta E_{\mathrm{int}}=0.
$$

Aquí el calentamiento es interno. No agregar además el mismo roce como una
segunda pérdida externa. Un sistema cerrado no intercambia materia; eso no
implica por sí solo que esté aislado ni que conserve energía mecánica.

### Estado no es proceso

Un **estado** tiene valores de $v$, altura $h$ y deformación $x$
en un instante. Entre dos estados ocurre un **proceso** con desplazamiento
y trabajos. Conviene escribir ambos por separado:

| Foto del sistema (estado) | Qué evaluar durante el tramo siguiente |
| --- | --- |
| Antes de entrar en una zona rugosa | Trabajo de rozamiento **sobre la distancia rugosa recorrida** |
| Al salir de la zona rugosa | Fuerzas que actúan desde ese punto, que pueden ser distintas |
| En la máxima compresión de un resorte | Es un instante de retorno: el **proceso de compresión ya ocurrió** |

Estos son ejemplos **genéricos**. No se identifican con las letras A–D
del parcial relatado porque aquí no está su figura original.

Si $v=0$ en una compresión máxima, $K=0$ **en ese estado**.
Eso no significa $\sum\vec F=0$: la fuerza del resorte puede empujar
al bloque hacia el equilibrio y hacer que invierta su velocidad.

### Un resorte puede realizar trabajo y ser conservativo

La fuerza elástica ideal **cambia con la posición**: $F_e=-kx$,
donde $x$ se mide desde la longitud natural. Por eso no se usa
$W=Fd\cos\theta$ con una **única fuerza constante** durante toda la
compresión. En un modelo unidimensional ideal:

$$
W_e=\int_{x_i}^{x_f}(-kx)\,dx
=-\frac12k(x_f^2-x_i^2)
=-\Delta U_e,\qquad U_e=\frac12kx^2.
$$

Desde $x_i=0$ hasta una compresión $|x_f|>0$, $W_e<0$ sobre el
bloque y aumenta $U_e$. Eso es **almacenamiento reversible**,
no disipación. Un resorte puede hacer trabajo distinto de cero
sin dejar de ser conservativo. El sistema bloque–resorte (y Tierra,
si se usa potencial gravitatorio) puede conservar energía mecánica
aunque las energías cinética y potencial cambien.

Si el peso y el resorte ya están representados mediante $U_g$ y
$U_e$, no sumar de nuevo sus trabajos. Si hay rozamiento localizado,
contarlo **sólo** en los tramos en que actúa; no imponer la misma
conservación o pérdida a todo el camino.

El [método transversal](../metodo-del-fenomeno-al-planteo.md)
explica cómo elegir el teorema antes de escribir el balance.

### Conservación: de dónde sale y cuándo usarla

$$
\begin{aligned}
W_{\rm neto}&=\Delta K\\
W_c+W_{nc}&=\Delta K\\
-\Delta U+W_{nc}&=\Delta K\\
W_{nc}&=\Delta(K+U)=\Delta E
\end{aligned}
$$

| Condición del intervalo | Balance | Qué significa |
| --- | --- | --- |
| $W_{nc}=0$ | $K_i+U_i=K_f+U_f$ | Energía mecánica igual en ambos estados |
| $W_{nc}\ne0$ | $K_i+U_i+W_{nc}=K_f+U_f$ | Energía mecánica cambia |
| $W_{\rm neto}=0$ | $K_i=K_f$ | No garantiza conservación de $E$ |

Pueden existir fuerzas no conservativas sin trabajo, por ejemplo la normal
en una pista fija lisa. Los trabajos no conservativos también pueden
cancelarse entre sí. Para conservar $E$ durante todo el recorrido,
la condición debe cumplirse en cada intervalo, no sólo entre los extremos.

| Fuerza | Clasificación | ¿Cuándo realiza trabajo? |
| --- | --- | --- |
| Peso (campo uniforme) | Conservativa | Si cambia altura: $W_g=mg(h_i-h_f)$ |
| Resorte ideal fijo | Conservativa | Si cambia deformación: $W_e=k(z_i^2-z_f^2)/2$ |
| Normal o tensión ideal | No necesariamente asociada a un potencial | Cero si perpendicular al desplazamiento de aplicación; puede no serlo con soporte móvil |
| Roce cinético en superficie fija | No conservativa | Negativo si desliza; $-\mu_kNd$ para $N$ constante |
| Fuerza aplicada / motor | Depende del modelo | Evaluar producto escalar a lo largo del recorrido |

### Referencias y justificación de ceros

| Término | Cuándo vale cero |
| --- | --- |
| $K$ | Reposo instantáneo en el marco elegido |
| $U_g$ | Altura en el nivel cero elegido |
| $U_e$ | Resorte sin deformar, con su longitud natural como referencia |
| $W$ de una fuerza | Sin desplazamiento de aplicación, perpendicular a él o contribuciones que se cancelan |

El cero de $U_g$ no significa ausencia de gravedad. Usar la misma referencia
en estado inicial, intermedio y final. En una rampa recta con ángulo $\alpha$
respecto de la horizontal y recorrido $d$, $|\Delta h|=d\sin\alpha$.
El peso usa la diferencia de altura con signo; el roce usa el recorrido.

~~~text
          ● inicial
          |\
   |Δh|   | \ d = recorrido
          | α \
          +----● final
~~~

El ángulo se mide entre la horizontal y el plano. Estas tablas y deducción
son elaboración propia. Reutilizar los diagramas de
[transformación de energía](assets/balance-energia.svg) y
[proyección del trabajo](assets/trabajo-proyeccion-area.svg).

### Qué significa cada signo

| Magnitud pedida | Cómo informarla |
| --- | --- |
| Variación de energía mecánica | $\Delta E=E_f-E_i$; negativa si disminuye |
| Trabajo del roce cinético en superficie fija | $W_r<0$ mientras hay deslizamiento |
| Energía mecánica disipada por ese roce | $D=-W_r\geq0$ |
| Trabajo neto | Puede ser positivo, negativo o cero; cambia $K$, no necesariamente $E$ |

Para un tramo horizontal rugoso de longitud $L$, con $N=mg$:
$W_r=-\mu_kmgL$. En un plano inclinado cambia $N$; si sólo hay peso y normal
en la dirección perpendicular, $N=mg\cos\alpha$.

### Porcentajes: mirar qué magnitud cambia

Con la misma masa en ambos estados:

| Dato | Consecuencia |
| --- | --- |
| Se conserva una fracción $q$ de la rapidez | $v_f=qv_i$; $K_f=q^2K_i$ |
| Se pierde una fracción $p$ de $K$ | $K_f=(1-p)K_i$; $v_f=\sqrt{1-p}\,v_i$ |
| Se duplica la compresión inicial de un resorte ideal | Su energía inicial se multiplica por cuatro |

Aplicación para reconocer variantes: S3 habla de **rapidez** y S4 de
**energía cinética**. Ver [el catálogo del parcial](../../parciales/Segundo_Parcial/patrones.md).

### Una pista recorrida varias veces

Marcar cada entrada y salida de la zona rugosa. Cada cruce completo cuesta
$D=\mu_kmgL$ bajo las hipótesis anteriores. En un retorno por una rampa lisa
se intercambian $K$ y $U_g$; no se agrega otra pérdida.

Si la energía cinética al entrar al tramo es menor que $D$, el cuerpo se
detiene **dentro** de él: ese intento no cuenta como cruce completo. Para
encontrar la posición final, usar la distancia realmente recorrida. La fuerza
de roce seco no produce un MAS ideal durante toda la ida y vuelta.

## ⚠️ Error frecuente

- Confundir el final de la zona rugosa con la máxima compresión del resorte.
- Usar toda la distancia de la pista para el trabajo de un roce localizado.
- Suponer que $v=0$ significa equilibrio: en una compresión máxima suele haber
  fuerza restauradora y el cuerpo vuelve a moverse.
- Elegir «llegar arriba con rapidez cero» cuando también se exige contacto
  con la cara interior de una pista abierta. Hay que revisar Newton radial.
- Usar $\sum\vec F_{ext}\cdot\Delta\vec r_{CM}$ como trabajo externo real de
  cualquier sistema deformable; el patinador de la diap. 17 muestra ese límite.

## 🔗 Ver también

- [Teoría esencial](teoria-esencial.md) · [Casos del TP 6](resolucion-por-casos.md)
- [Fuentes y erratas](fuentes.md)
- [Práctica del segundo parcial sin resultados](../../parciales/Segundo_Parcial/practica.md)
