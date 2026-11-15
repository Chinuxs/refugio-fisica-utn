# Estática y Rototraslación — teoría esencial

> **Alcance del tercer parcial informado:** estudiar aquí las secciones de
> **equilibrio y estabilidad** (TP 10, ejercicios 1–9). Las secciones de
> **rodadura y dinámica de la rototraslación** corresponden a los ejercicios
> 10–21 y **no entran en el parcial actual**. Se conservan para consulta.
> [Ver selección del TP 10](README.md).

## 🎯 Qué recordar

- **Equilibrio de un cuerpo rígido:** deben anularse tanto la fuerza externa
  neta como el torque externo neto. Cumplir una sola condición no alcanza.
- **Estática:** cuerpo en reposo en el marco elegido. También puede haber
  traslación uniforme sin giro con fuerzas y torques equilibrados.
- **Centro de gravedad (CG):** punto donde puede representarse la resultante
  del peso. En un campo gravitatorio uniforme coincide con el centro de masa.
- **Rototraslación:** traslación del CM + rotación alrededor del CM.
  Requiere estudiar ambas, vinculadas por la condición de rodadura si no patina.
- **Rozamiento estático:** se calcula de las ecuaciones y luego se verifica
  su límite. Su sentido se opone a la tendencia de deslizamiento del contacto;
  puede favorecer o frenar el movimiento del CM.

## 🖼️ Esquema / dibujo

![Escalera en equilibrio con fuerzas reales y rueda rodando sin deslizar: CM, contacto y velocidades.](assets/equilibrio-rodadura.svg)

## Antes de las fórmulas: elegir una herramienta (Estática, TP 10: 1–9)

1. **Interpretar** qué cuerpo o sistema permanece en reposo y qué solicita
   el problema: reacción, tensión o un límite de contacto.
2. **Dibujar un DCL** sólo con fuerzas reales: peso, tensiones, normales,
   rozamiento y reacciones de articulación según el apoyo.
3. **Comprobar el modelo de equilibrio:** para un cuerpo rígido en reposo
   deben anularse fuerzas y momentos externos.
4. **Elegir ejes y punto de momentos.** Un punto por el que pasan reacciones
   desconocidas suele evitar que aparezcan en la ecuación de momentos.
5. **Plantear y verificar.** Calcular primero las fuerzas necesarias;
   sólo imponer rozamiento máximo o normal nula al llegar al límite
   correspondiente. Revisar signos, unidades y si hay contacto.

Esta secuencia es **elaboración didáctica propia**, basada en los tipos de
problemas de los ejercicios 1–9. No adelanta el desarrollo de ninguno.

## 📐 Fórmula

### Equilibrio: fuerzas y momentos (TP 10: 1–9)

**Origen del bloque:** condiciones de equilibrio registradas para la
presentación de cátedra, **diapositivas 8–9**; fuerzas, apoyos y elección de
pivote ilustrados por **TP 10, ejercicios 1–6 y 9**.
Las convenciones y el orden de resolución son una síntesis propia.
[Detalle de procedencia y cotejo pendiente](fuentes.md#mapa-de-trazabilidad-por-concepto).

$$\sum F_x=0,\qquad \sum F_y=0,\qquad \sum\tau_{O,z}=0.$$

En problemas planos hay tres ecuaciones independientes. Elegir O en un apoyo
o articulación suele eliminar torques de fuerzas desconocidas **porque su
línea de acción pasa por O**. Esto simplifica el cálculo; no significa que
esas fuerzas desaparezcan del DCL o de las ecuaciones de traslación.
Con fuerza neta nula, el torque neto es el mismo respecto de cualquier punto.

$$\tau_{O,z}=r_xF_y-r_yF_x,\qquad |\tau|=Fd_\perp.$$

Para dibujar un **DCL**, primero aislá el cuerpo: el peso actúa en el CG,
y cada contacto o vínculo se reemplaza por las fuerzas que ejerce sobre
él. No dibujes a la vez una fuerza y sus componentes como fuerzas extra.

**Apoyos ideales:** pared lisa → normal perpendicular a la pared;
suelo rugoso → normal y rozamiento; cable → tensión a lo largo del cable;
articulación plana ideal → dos componentes de reacción, sin par resistente.
Una barra uniforme tiene su peso aplicado en el punto medio; no suponer
uniformidad si el enunciado da otro CG.

| Condición física | Planteo |
| --- | --- |
| Contacto estático | $|f_s|\le\mu_sN$ |
| Deslizamiento inminente | $|f_s|=\mu_sN$ |
| Roce cinético | $|f_k|=\mu_kN$ |
| Contacto unilateral | $N\ge0$; al perder apoyo, $N=0$ |
| Vuelco inminente | La resultante normal llega al borde de la base |

### Estabilidad: mirar la altura del CG (TP 10: 7–9)

**Origen del bloque:** centro de gravedad en la presentación de cátedra,
**diapositiva 3**; estabilidad y energía potencial, **diapositivas 4–7**.
Condiciones de deslizamiento, desplazamiento de la normal y vuelco:
**TP 10, ejercicios 7–9**, con apoyo del límite de rozamiento en el
**ejercicio 2**. Los umbrales del bloque son deducciones para la
**geometría ideal indicada**, no fórmulas universales.
[Detalle y verificación pendiente](fuentes.md#mapa-de-trazabilidad-por-concepto).

$$U_g=Mgy_{cm},\qquad F_x=-\frac{\partial U}{\partial x}.$$

Para una coordenada permitida q, equilibrio requiere $dU/dq=0$.
Un mínimo local estricto de U da equilibrio estable; un máximo, inestable;
U constante en un entorno da equilibrio neutro. Si la segunda derivada
es cero, estudiar la forma de U: no basta ese dato para clasificar.
En un giro puede usarse $\tau=-dU/d\theta$.

Para un bloque rectangular homogéneo, base b y altura H, sobre una tabla
que se inclina lentamente:

$$\tan\beta_{deslizamiento}=\mu_s,\qquad
\tan\beta_{vuelco}=b/H.$$

Ocurre primero el límite de menor ángulo. La proyección vertical del CG
llega al borde al comenzar el vuelco; este criterio supone la gravedad
y los contactos del caso, sin fuerzas adicionales.

### Rodadura: separar movimiento del CM y giro — complemento excluido (TP 10: 10–21)

**Origen del bloque:** presentación de cátedra, diapositivas **12–16**,
y **Sears §10.3** como bibliografía complementaria. No usar este apartado
para ampliar el alcance informado del tercer parcial.
[Fuentes](fuentes.md).

$$\vec v_P=\vec v_{cm}+\vec\omega\times\vec r_{P/cm}.$$

Sobre suelo fijo, sin deslizamiento, $v_{contacto}=0$ y $v_{cm}=R|\omega|$.
R es el radio **exterior de contacto**. Para avanzar hacia +x, tomando
antihorario positivo: $v_{cm,x}=-R\omega_z$ y $a_{cm,x}=-R\alpha_z$
en rodadura rectilínea sobre un plano fijo.

El punto superior tiene rapidez $2v_{cm}$. El contacto es el **centro
instantáneo de rotación (CIR)**, pero no un pivote material fijo:
tener velocidad instantánea cero no implica aceleración cero.

$$K=\frac12Mv_{cm}^2+\frac12I_{cm}\omega^2
=\frac12I_{CIR}\omega^2,\qquad I_{CIR}=I_{cm}+MR^2.$$

La última igualdad es una alternativa: no sumar otra vez la energía de
traslación a $I_{CIR}\omega^2/2$.

### Dinámica y energía de la rototraslación — complemento excluido (TP 10: 10–21)

**Origen del bloque:** presentación de cátedra, diapositivas **12–16**,
TP 10 ejercicios **10–21** y **Sears §10.3**. Las hipótesis adicionales
de modelos concretos están registradas en [fuentes](fuentes.md).

$$\sum\vec F_{ext}=M\vec a_{cm},\qquad
\sum\tau_{ext,cm,z}=I_{cm}\alpha_z.$$

Se usa el caso de la presentación: eje de simetría por el CM que no cambia
de dirección. No trasladar automáticamente esta ecuación al CIR.

$$K_i+U_i+W_{nc}=K_f+U_f.$$

El roce estático ideal en contacto con una superficie **fija**, sin
deformaciones ni deslizamiento, no realiza trabajo neto sobre el cuerpo.
Puede producir torque y ser necesario para rodar. Si patina o hay resistencia
al rodamiento, revisar las pérdidas y la restricción $v_{cm}=R|\omega|$.

Para una pendiente uniforme de ángulo β y $I_{cm}=cMR^2$, sin otras fuerzas:

$$a_{cm}=\frac{g\sin\beta}{1+c},\quad
f_s=\frac{c}{1+c}Mg\sin\beta,\quad
\mu_s\ge\frac{c}{1+c}\tan\beta.$$

a se dirige cuesta abajo; fₛ, cuesta arriba, incluso si el cuerpo inicialmente
sube sin patinar. Con descenso vertical h desde reposo:
$v_{cm}=\sqrt{2gh/(1+c)}$.

**Unidades:** fuerzas en N, distancias en m, I en kg·m², energía en J,
ω en rad/s y α en rad/s². Usar g = 9,8 m/s² salvo indicación.

## ⚠️ Error frecuente

- Usar sólo $\sum F=0$ y olvidar los torques.
- Medir el brazo sobre la barra en vez de perpendicular a la fuerza.
- Imponer $f_s=\mu_sN$ fuera del límite de adherencia.
- Suponer que la normal siempre actúa en el centro de la base.
- Dibujar fuerzas y sus componentes como si fueran fuerzas adicionales.
- Conservar energía mecánica en el caso del TP donde las ruedas **deslizan**.
- Usar $a_{cm}=R\alpha$ para la aceleración total en una pista curva:
  la vinculación es tangencial, y el CM también tiene aceleración normal.

## 🔗 Ver también

- [Índice separado: Estática 1–9 / Rototraslación 10–21](README.md)
- [Mapa de trazabilidad por concepto y estado de verificación](fuentes.md#mapa-de-trazabilidad-por-concepto)
- [Casos del TP 10](resolucion-por-casos.md)
- [Inercias y Steiner](../cuerpo-rigido/teoria-esencial.md)
- [Trabajo y Energía](../trabajo-energia/README.md)
- [Fuentes y comprobaciones](fuentes.md)
- [Volver al tema](README.md)
