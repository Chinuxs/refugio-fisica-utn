# Laboratorio 2 — resultados y conclusiones para completar

**Trabajo contra las fuerzas de rozamiento · revisión del 7/11/2026.**

Se revisaron `lab2.pdf`, los tres escaneos y las celdas/fórmulas del Excel
en `E:\UTN\Fisica I\Laboratorios\lab2`.

**Criterio adoptado:** interpretar 698,2; 39,8 y 20 como **gramos** y convertirlos
a kg antes de calcular energías. Es el criterio acordado tras contrastar el
Laboratorio 1 y la ficha del equipo; el encabezado impreso dice kg, pero los
números anotados son incompatibles con esa escala para este carrito.
La justificación y sus límites quedan documentados en la sección 6.

[Excel de revisión con fórmulas](datos-laboratorio-2/laboratorio-2-propuesta-masas-g.xlsx)
· [Tablas en CSV](datos-laboratorio-2/laboratorio-2-tablas-propuesta.csv).
El original se conserva sin modificar. El Excel nuevo tiene hojas **Datos**,
**Resultados** y **Lectura**, con la conversión adoptada explícita. Los nombres
de los archivos conservan «propuesta» para mantener los enlaces existentes.

## Respuestas finales del formulario

**Error en J:** `0,00016`

**Trabajo de la fuerza de rozamiento promedio ± error en J:**
`(−0,03426 ± 0,00016) J`

**Conclusiones:**

> La energía potencial gravitatoria disminuyó más de lo que aumentó la energía
> cinética. La diferencia corresponde al trabajo negativo del rozamiento, cuyo
> valor promedio fue (−0,03426 ± 0,00016) J. Por lo tanto, la energía mecánica
> disminuyó, transformándose parte de ella en energía interna por fricción.
> El error informado corresponde a la dispersión del promedio de las cinco
> mediciones.

El campo de error lleva el valor positivo; el ± ya aparece en la fórmula.
La interpretación corresponde al modelo de la guía: no se midió directamente
la energía interna ni se evaluaron incertidumbres instrumentales.

## 1. Datos para la Tabla I

| Magnitud | En el archivo original | Valor adoptado en SI |
| --- | --- | --- |
| Masa del carro M | 698,2 | **0,6982 kg** |
| Masa colgante m₁ | 39,8 | **0,0398 kg** |
| Masa colgante m₂ | 20 | **0,0200 kg** |
| Masa móvil total | 758 | **0,7580 kg** |
| Separación de sensores ΔX | 0,5 | **0,50 m** |
| Variación de altura en módulo Δh | 0,5 | **0,50 m** |

Se usa g = 9,8 m/s², como en las fórmulas originales. Se conservan todas
las velocidades del Excel:

| Medición | v₁ (m/s) | v₂ (m/s) |
| --- | --- | --- |
| 1 | 0,085 | 0,415 |
| 2 | 0,082 | 0,415 |
| 3 | 0,083 | 0,416 |
| 4 | 0,083 | 0,414 |
| 5 | 0,084 | 0,417 |

## 2. Respuestas para los incisos a), b) y c)

### a) ¿Cómo son las energías al pasar por los sensores?

Texto para completar:

> Al pasar del sensor 1 al sensor 2 aumenta la energía cinética del sistema,
> porque aumenta su rapidez. La masa m₁ desciende y la masa m₂ asciende;
> como m₁ > m₂, disminuye la energía potencial gravitatoria total. La ganancia
> de energía cinética es menor que la disminución de energía potencial, por
> lo que la energía mecánica final es menor que la inicial. Esta diferencia
> corresponde al trabajo negativo del rozamiento en el modelo del ensayo.

Sistema: **carro + dos masas colgantes**, considerando gravedad mediante U.
Las tres masas tienen el mismo módulo de velocidad, por cuerdas inextensibles
y sin deslizamiento. Se usa el modelo de la consigna, sin añadir energías
rotacionales de ruedas/poleas no caracterizadas en los datos.

### b) ¿Cuál es el valor de Δh?

> Cada masa colgante cambia su altura en el mismo módulo que el recorrido
> horizontal del carro: **Δh = ΔX = 0,50 m**. m₁ baja 0,50 m y m₂ sube 0,50 m.

El dato es un **módulo**: con altura positiva hacia arriba,
Δy₁ = −0,50 m y Δy₂ = +0,50 m.

### c) Expresión correspondiente al sistema

$$W_{fr}=\Delta E_m=\Delta K+\Delta U,$$
$$\boxed{W_{fr}=\frac12(M+m_1+m_2)(v_2^2-v_1^2)
+(m_2-m_1)g\,\Delta h}.$$

Para reproducir las columnas U de la planilla, se toma como altura cero el
nivel inferior de referencia del esquema: en el estado 1, m₁ está a Δh y
m₂ a cero; en el estado 2 se intercambian esas alturas. La energía potencial
constante del carro se omite, porque no cambia:

$$U_1=m_1g\Delta h,\quad U_2=m_2g\Delta h,\quad
\Delta U=(m_2-m_1)g\Delta h.$$

Cambiar el cero de potencial cambia U₁ y U₂, pero no ΔU ni Wfr.
Si se supone rozamiento equivalente constante:

$$W_{fr}=-F_{fr,eq}\Delta X.$$

## 3. Tabla II — energías en J, con masas convertidas de g a kg

El segundo encabezado «U₁» de la tabla impresa debe interpretarse como **U₂**,
de acuerdo con la columna ΔU = U₂ − U₁ y el Excel.

| n | K₁ | K₂ | ΔK | U₁ | U₂ | ΔU |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 0,002738275 | 0,065273275 | 0,062535000 | 0,195020 | 0,098000 | −0,097020 |
| 2 | 0,002548396 | 0,065273275 | 0,062724879 | 0,195020 | 0,098000 | −0,097020 |
| 3 | 0,002610931 | 0,065588224 | 0,062977293 | 0,195020 | 0,098000 | −0,097020 |
| 4 | 0,002610931 | 0,064959084 | 0,062348153 | 0,195020 | 0,098000 | −0,097020 |
| 5 | 0,002674224 | 0,065903931 | 0,063229707 | 0,195020 | 0,098000 | −0,097020 |

Se muestran cifras adicionales para trasladar/verificar las cuentas; **no
representan precisión instrumental demostrada**. Redondear el resultado final.

Comprobación de la primera fila:

$$W_{fr,1}=0{,}062535-0{,}097020=-0{,}034485\ \mathrm J.$$

## 4. Tabla III — trabajo y error del valor medio

Se sigue exactamente la convención de la consigna:
$e_i=\overline W_{fr}-W_{fr,i}$; el error cuadrático se expresa en **J²**.

| n | Wfr,i (J) | eᵢ (J) | eᵢ² (J²) |
| --- | --- | --- | --- |
| 1 | −0,034485000 | +0,0002280064 | 5,1986918441 × 10⁻⁸ |
| 2 | −0,034295121 | +0,0000381274 | 1,4536986308 × 10⁻⁹ |
| 3 | −0,034042707 | −0,0002142866 | 4,5918746940 × 10⁻⁸ |
| 4 | −0,034671847 | +0,0004148534 | 1,7210334349 × 10⁻⁷ |
| 5 | −0,033790293 | −0,0004667006 | 2,1780945004 × 10⁻⁷ |

$$\overline W_{fr}=-0{,}0342569936\ \mathrm J,$$
$$\sum e_i^2=4{,}8927215754\times10^{-7}\ \mathrm{J^2},$$
$$E=\sqrt{\frac{\sum e_i^2}{n(n-1)}}
=\sqrt{\frac{4{,}8927215754\times10^{-7}}{5\cdot4}}
=0{,}0001564085\ \mathrm J.$$

**Resultado para el recuadro, con la conversión adoptada:**

$$\boxed{W_{fr}=(-0{,}03426\pm0{,}00016)\ \mathrm J}$$

Equivalente: **Wfr = (−34,26 ± 0,16) mJ**.
E es el **error estadístico del valor medio** pedido por la guía. No incluye
incertidumbres de balanza, posiciones, velocidades ni efectos sistemáticos;
no se informaron esas incertidumbres. Tampoco se le asigna un nivel de
confianza específico, porque la consigna no lo establece.

Como dato adicional, tomando ΔX sin incertidumbre:

$$F_{fr,eq}=-\frac{\overline W_{fr}}{\Delta X}
=0{,}068514\ \mathrm N,$$
$$F_{fr,eq}=(0{,}06851\pm0{,}00031)\ \mathrm N
\quad\text{(sólo dispersión estadística)}.$$

Es una fuerza resistente **equivalente del conjunto**, no una medición aislada
del roce carro–riel ni un coeficiente de rozamiento de deslizamiento.

## 5. Conclusión breve para completar el laboratorio

Versión ampliada de la conclusión, para un informe con más espacio:

> Entre los sensores, la energía potencial gravitatoria disminuyó 0,09702 J,
> mientras que la energía cinética aumentó, en promedio, 0,06276 J. La
> diferencia corresponde a una disminución de energía mecánica de 0,03426 J.
> Por el balance energético se obtuvo un trabajo de rozamiento de
> (−0,03426 ± 0,00016) J, donde el error informado corresponde a la dispersión
> del valor medio de cinco mediciones. El signo negativo indica que las
> fuerzas resistentes extraen energía mecánica del sistema. El resultado es
> compatible con su transformación en energía interna por rozamiento: no
> se conserva la energía mecánica, pero el balance no implica una pérdida
> de energía total. No se midió directamente esa energía interna y faltan
> las incertidumbres instrumentales para una evaluación completa del error.

Si falta espacio, conservar las tres primeras oraciones y la aclaración del
tipo de error. Evitar escribir que «se destruyó energía» o que el ensayo
demuestra por sí solo un balance completo de todas las formas de energía.

## 6. Qué cambia respecto del Excel y de las anotaciones

- Las fórmulas de energía y del error medio son consistentes con la guía;
  la principal dificultad es **la unidad de las masas**.
- Al interpretar los números originales como g, los valores calculados con ellos y
  velocidades en m/s son numéricamente **mJ**, no J. Al pasar masas a kg,
  todas las energías y eᵢ se dividen por 1000; eᵢ², por 10⁶.
- El promedio −34,2569936 y el error 0,1564085 del Excel no deben copiarse
  como J con el criterio adoptado. Equivalen a −0,0342569936 J y
  0,0001564085 J.
- Los escaneos copian valores del Excel sin aclarar esa conversión; no son
  evidencia independiente de que las masas estén en kg.

| Unidad real de 698,2; 39,8; 20 | Resultado final |
| --- | --- |
| **g**, interpretación coherente con un carrito de laboratorio | **(−0,03426 ± 0,00016) J** |
| **kg**, interpretación literal de las celdas sin conversión | **(−34,26 ± 0,16) J**; implicaría un carro de 698,2 kg |

La segunda fila muestra qué implicaría leer literalmente el encabezado;
**no es el resultado adoptado para entregar**. La precisión estadística
relativa es ≈ 0,46 % en ambos casos y, por sí sola, no decide la unidad.

### Contraste con el Laboratorio 1 y el equipo

Se revisaron `lab1.pdf` y sus cinco escaneos en
`E:\UTN\Fisica I\Laboratorios\lab1`. Repiten las masas y las velocidades del
Laboratorio 2, con el mismo encabezado en kg. Las fuerzas manuscritas calculadas
a partir de esas masas no constituyen otra medición independiente de su unidad.

La aceleración ideal tampoco resuelve la duda: en
`a = (m₁ − m₂)g / (M + m₁ + m₂)`, multiplicar todas las masas por 1000 no
cambia el resultado. En cambio, sí multiplica energías y trabajos por 1000.

Ambas guías identifican el carro como **Leybold 337110**. La
[ficha oficial del fabricante](https://www.leybold-shop.com/physics/physics-equipment/mechanics/dynamics-and-kinematics/fletcher-s-trolley/trolley-337110.html)
indica un peso de 495 g y una masa dinámica de 500 g. Esto respalda el **orden
de magnitud en gramos**, no un carro de 698,2 kg. No certifica que el conjunto
utilizado pesara exactamente 698,2 g ni explica por sí solo la diferencia con
el carro de catálogo: faltan el registro de balanza y el detalle de accesorios.

Por estas razones se adoptó la conversión a kg, sin alterar las anotaciones
originales ni presentar la unidad inferida como una lectura verificada de balanza.

## Fuentes y reproducción

- `lab2.pdf`, edición 2019, páginas impresas 2–4 (PDF 4–6): modelo, incisos,
  tablas y fórmula del error. Se revisaron visualmente las páginas PDF 4 y 5.
- `Laboratorio_TP2_2022.xlsx`, hoja `Sheet1`: E3:G3 (masas), H3:I3
  (distancias), B4:C8 (velocidades), B12:L17 y C20 (cálculos originales).
  Se leyeron tanto fórmulas como resultados guardados, incluidas fórmulas compartidas.
- `Escáner_20261107 (6).png`, `(7).png`, `(8).png`: hojas de trabajo y anotaciones.
- `Tutorial TPN°2-2022.mp4` está disponible, pero **no se reprodujo ni
  transcribió**; no se le atribuyen datos o instrucciones no verificados.

Generador sin dependencias externas:

```powershell
py herramientas/resolver_laboratorio_2.py 'E:\UTN\Fisica I\Laboratorios\lab2\Laboratorio_TP2_2022.xlsx' 'estudio/laboratorios/datos-laboratorio-2' --unidad-masas g
```

La salida identifica la unidad **adoptada**, conserva las velocidades, guarda
fórmulas y valores calculados, y comprueba que el SHA-256 del original no cambió.

[Trabajo y Energía](../apuntes/trabajo-energia/README.md) ·
[Laboratorio 3](laboratorio-3.md) · [Volver a la portada](../../README.md)
