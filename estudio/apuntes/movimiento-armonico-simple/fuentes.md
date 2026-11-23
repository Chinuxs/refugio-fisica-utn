# MAS — fuentes

Síntesis propia a partir de `7. MAS/07 Movimiento oscilatorio-20260919/`.

| Material consultado | Uso |
| --- | --- |
| `07 Movimiento Oscilatorio.pptx` | Diap. 3–17: conceptos, energía, función seno y dinámica; 18–19: péndulo; 20–21: amortiguado y forzado |
| `tp7.pdf` | Págs. PDF 1–5 (impresas 35–39): selección de casos; ej. 13 como comprobación numérica |
| Sears, Zemansky, Young y Freedman, Física Universitaria, vol. 1, 14.ª ed.; archivo terminado en `461-495.pdf` | Consulta de resorte vertical (§14.4), péndulo (§14.5), amortiguamiento y resonancia (§14.7–14.8) |

Los números del nombre del recorte no coinciden con las páginas impresas:
el capítulo 14 comienza en la página impresa 433. La numeración de ejercicios
usada en la guía es la del TP 7.

## Criterios y comprobaciones

- Se conserva la convención **seno** de la presentación; si el TP da coseno,
  se deriva esa expresión directamente.
- En el **ej. 1**, con $x=8\cos(2t+\pi/3)$ cm, el primer máximo de **rapidez**
  ocurre en $\pi/12\simeq0{,}262$ s, con $v=-16$ cm/s. El primer máximo
  positivo de velocidad ocurre en $7\pi/12\simeq1{,}833$ s. La respuesta
  impresa usa el primer criterio aunque escribe “velocidad máxima”.
- En el **ej. 5**, si se elige como $t=0$ el cruce del equilibrio hacia $+x$,
  resulta $x=0{,}1\sin(20t)$ m. La fase $\pi/2$ impresa ubica el instante
  inicial en un extremo; sólo sirve si se elige otro origen de tiempos.
- En el péndulo, los 15° son un criterio aproximado de la presentación, no
  una frontera exacta de validez. Para rapidez y tensión se ofrece el balance
  energético sin aproximación angular.
- La respuesta forzada se escribe con $(k-m\Omega^2)^2$ en el denominador,
  diferenciando la frecuencia aplicada $\Omega$ de la natural $\sqrt{k/m}$.

## Revisión directa del 15 de noviembre de 2026

Se releyeron las **21 diapositivas** actuales y los **26 ejercicios del TP 7**.
Se pudieron abrir los dos `.ppt` antiguos mediante PowerPoint en modo de
lectura y exportarlos temporalmente para inspeccionar texto, fórmulas y
gráficos. El `.doc` de cinemática circular también permitió extraer su texto;
no se usa como teoría de MAS ni se da por validada una figura no contrastada.

## Trazabilidad por concepto

| Apartado | Cátedra contrastada | Complemento / elaboración propia |
| --- | --- | --- |
| Periódico, oscilatorio y condición de MAS | Presentación, diap. 3–5 y 17 | Sears §14.1–14.2; preguntas y distinciones propias |
| Energía y funciones de posición | Diap. 6–16; TP 7.1–2, 5–9, 12–14, 16, 18 | Sears §14.2–14.3, pp. 435–445; tabla propia de fases y energía temporal |
| Elección de fase con posición y velocidad | Diap. 10–16; apoyo `Ejercicios de MAS.ppt`, diap. 14–17 y 22–24 | La ficha propia mantiene la convención seno; Sears usa coseno y otra fase |
| Resorte vertical y nuevo equilibrio | TP 7.10–11, 15–16; `Resumen clase 12.ppt`, diap. 21–22 | Sears §14.4, p. 446; distinción propia entre deformación y elongación |
| Péndulo simple y validez angular | Diap. 18–19; TP 7.19–25 | Sears §14.5, pp. 450–451; geometría exacta y advertencias propias |
| Roce que permite acompañar la plataforma | TP 7.17–18 | Deducción propia por Newton y máximo de $|a|$ |
| Amortiguado y forzado | Diap. 20–21 | Sears §14.7–14.8, pp. 453–457; corrección de la respuesta estacionaria |
| Choque seguido de MAS | S1.2 y S3.2; enlace con TP 8.22–25 | Sears ejemplo 14.5, p. 445: cambia la masa oscilante; no confundir con enunciado de cátedra |

El recorte `…461-495.pdf` contiene páginas **impresas 433–467**. Incluye
MAS angular y péndulo físico, pero su presencia en el libro no confirma
que formen parte del alcance informado para este segundo parcial.

## Material antiguo y equivalencias

| Archivo | Lectura y uso |
| --- | --- |
| `2022/tp7.pdf` | Idéntico por SHA-256 al TP vigente |
| `2022/07 Movimiento Oscilatorio R1.ppsx` | 21 diapositivas; el texto extraído coincide con la presentación actual. No son copias binarias idénticas |
| `2022/Trabajo práctico 7.pdf` y `N°7 MAS/Ejerc.pdf` | 19 páginas cada uno; bytes distintos pero **texto extraído por página idéntico**. Es un mismo apoyo textual, no dos fuentes independientes |
| `N°7 MAS/Presentación.pdf` | 21 páginas, con fórmulas/gráficos incorporados como imágenes; apoyo del mismo tema, no un examen |
| `Ejercicios de MAS.ppt` | 36 diapositivas; seis problemas con planteos y gráficos. Usar especialmente las comprobaciones simultáneas de $x_0$ y $v_0$ |
| `Resumen clase 12.ppt` | 32 diapositivas; dinámica, energía, proyección circular, péndulo, resorte vertical y ejercicios. Numeración independiente del TP vigente |
| `Ejercitación de cinemática circular.doc` | Dos problemas: giro de rapidez variable y centrifugadora. Herramienta auxiliar; no se incluye como ejercicio de MAS |

## Erratas y ambigüedades adicionales

| Fuente / ubicación | Qué corregir o comprobar |
| --- | --- |
| Presentación, diap. 16 | $v(x)$ requiere los dos signos; la raíz positiva sola representa rapidez o una rama |
| Presentación, diap. 19 | Para la analogía restauradora, $k_{ef}=-F_t/s=mg/L>0$; la igualdad escrita con $F/x$ pierde un signo. Además $L\theta$ es arco; la proyección horizontal es $L\sin\theta$ |
| Presentación, diap. 21 | La respuesta correcta es $A=F_0/\sqrt{(k-m\Omega^2)^2+(b\Omega)^2}$. La expresión mostrada mezcla potencias de frecuencia y no es dimensionalmente consistente |
| Misma diap. 21, curva C | $b=\sqrt2m\omega_0$ marca la desaparición del pico de amplitud a frecuencia positiva en el modelo forzado. **No** es el umbral de sobreamortiguamiento libre: el crítico es $b=2m\omega_0$ |
| `Ejercicios de MAS.ppt`, diap. 6–9 | Hay inconsistencias entre el período escrito y la frecuencia angular usada. Si se adopta $T=0,75$ s, debe resultar $\omega=8\pi/3$ rad/s, no $3\pi/2$. Releer el gráfico antes de fijar el dato; no reutilizar los tiempos derivados |
| Mismo `.ppt`, diap. 26 | Con $A$ redondeada a 0,29 m y $\omega=4$ rad/s, el coeficiente de aceleración debe ser 4,64 m/s², no 4,56. Con los datos exactos conviene conservar $A=\sqrt{0,085}$ m hasta el final |
| Mismo `.ppt`, diap. 32 y 34 | Aparecen 62,83 y 63,83 dentro de argumentos del mismo movimiento. Todas las derivadas deben conservar la misma $\omega$ |
| `Resumen clase 12.ppt`, diap. 11 | Para $x=+0,10$ m y $\omega=3$ rad/s, $a=-0,90$ m/s²; el signo positivo sólo corresponde al módulo |
| TP 7.24 / apoyo PDF pp. 16–17 | $\theta_{max}=\arccos(0,96)=0,283794$ rad. Proyección horizontal: 0,280000 m; arco: 0,283794 m. No son exactamente la misma amplitud lineal |

Los errores del apoyo de 19 páginas, incluidas fase del diapasón, datos
copiados y períodos del péndulo, se conservan en la
[auditoría anterior](../../parciales/auditoria-material.md#advertencias-de-los-apuntes-de-apoyo).
Estas comprobaciones propias revelan resultados; para intentar ejercicios,
usar primero la [práctica sin controles](../../parciales/Segundo_Parcial/practica.md).

[Inventario y límites de lectura](../../parciales/Segundo_Parcial/auditoria-fuentes.md).

[Volver al tema](README.md)

## Comparaciones didácticas

[Cuadros de osciladores y parámetros](comparar-osciladores.md), el esquema
de los tres sistemas, las curvas y
[el método de cocientes](../dinamica/herramientas-matematicas/comparar-por-cocientes.md)
son **elaboración propia**. Referencias del contraste registrado el 15/11:
diap. 3–17 (MAS y energía), 18–19 (péndulo), TP 7.10–11, 15–16
(vertical), 19–25 (péndulo), y `Resumen clase 12.ppt` diap. 21–22.
Sears §14.2–14.5 es bibliografía complementaria. No se reabrieron los
originales locales en esta modificación.
