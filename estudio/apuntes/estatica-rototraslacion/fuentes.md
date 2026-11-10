# Estática y Rototraslación — fuentes

Síntesis propia a partir de la carpeta local de cátedra
`10. Estatica - Rototranslacion/10 Equilibrio del cuerpo rígido-20261103/`.
Los originales no se modifican ni se duplican en el repositorio.

| Material consultado | Uso |
| --- | --- |
| `10 Equilibrio y rototraslación.pptx` (18 diapositivas) | 3: CG; 4–7: potencial y estabilidad; 8–9: condiciones de equilibrio; 12: energía; 13–14: rodadura y CIR; 15–16: dinámica y campo de validez |
| `tp10.pdf` (7 páginas PDF, impresas 57–63) | Ej. 1–9: equilibrio y límites; 10–16: energía y rampa; 17–19: fuerza aplicada y ruedas; 20: loop; 21: cilindro y masa colgante |
| Sears, Zemansky, Young y Freedman, *Física Universitaria*, vol. 1, 14.ª ed., `…331-366.pdf` | Cap. 10, páginas impresas 303–338; §10.3, impresas 309–315, para rototraslación, CIR, rodadura, dinámica y roce |

El recorte de Sears es idéntico al de la carpeta del tema anterior (comparado
por SHA-256). **No contiene el capítulo específico de equilibrio y elasticidad**:
para estática se usan la presentación y el TP provistos. El nombre del recorte
no coincide con sus páginas impresas.

Se revisaron los 21 enunciados y sus respuestas, y las figuras de las páginas
PDF 1, 3, 4, 6 y 7 para fijar geometría, radios, puntos de aplicación y vínculos.
Las guías cubren estrategias por casos; no son las resoluciones completas de
todos los ejercicios.

## Mapa de trazabilidad por concepto

**Cómo leer este mapa:** las ubicaciones de diapositivas y la correspondencia
de ejercicios provienen de la **revisión documental ya asentada** en este
repositorio. Los originales están en una carpeta local fuera de GitHub,
por lo que **no se realizó un nuevo cotejo directo** para este cambio.
La referencia es útil para localizar el contenido, pero no debe presentarse
como una cita textual verificada en esta revisión.

| Concepto | Fuente de cátedra registrada | Bibliografía complementaria / elaboración propia |
| --- | --- | --- |
| Equilibrio de traslación y rotación | Presentación, diap. **8–9**; TP 10 **1–9** | Orden de resolución en DCL → fuerzas → momentos: **elaboración propia** |
| Reacciones de apoyo y DCL | TP 10 **1–6 y 9** (apoyos, tensiones, bisagras y contactos) | Idealizaciones de apoyos y elección de ejes explicadas como **síntesis propia**; asignación exacta a una diapositiva: **pendiente** |
| Momento de fuerza y elección del punto O | TP 10 **1–6 y 9** (planteos de momentos); presentación, diap. **8–9** (equilibrio) | Explicación de por qué conviene tomar momentos en un apoyo: **elaboración propia** |
| Centro de gravedad y estabilidad | Presentación, diap. **3** (CG), **4–7** (potencial y estabilidad); TP 10 **7–8** | Lectura de la altura del CG como ayuda conceptual: **síntesis propia** |
| Deslizamiento, vuelco y pérdida de apoyo | TP 10 **2 y 7–9** | Límites deducidos bajo geometría y contactos ideales de los casos: **elaboración propia**; no extrapolar como fórmulas universales |
| Rodadura, CIR, dinámica y energía (excluidos del parcial actual) | Presentación, diap. **12–16**; TP 10 **10–21** | **Sears §10.3**, complemento bibliográfico; hipótesis y comprobaciones propias debajo |

**Pendiente de contraste con los originales:** confirmar la numeración y
el contenido exacto de las diapositivas 3–9 y 12–16; repasar las figuras
y condiciones de apoyo, dirección de fuerzas, puntos de aplicación y
enunciados de los ejercicios 1–9. No atribuir a la presentación una
idealización o deducción que aquí se marque como propia.

## Alcance de evaluación (no es una fuente de cátedra)

Según el alcance **informado por el estudiante**, el tercer parcial incluye
**Estática del TP 10, ejercicios 1–9**, y excluye la **Rototraslación del
TP 10, ejercicios 10–21**. Se conserva toda la bibliografía para estudio
posterior. Esta selección **no procede de las diapositivas ni de Sears**
y debe reconfirmarse si se publica un temario oficial diferente.
[Índice separado](README.md).

## Criterios y comprobaciones

- Se mantienen las convenciones y el campo de validez de la presentación:
  eje de simetría por el CM y dirección del eje fija para la dinámica escalar.
- La tabla de inercias se enlaza desde Cuerpo Rígido para evitar duplicados.
- Se distingue el módulo de aceleración tangencial de la aceleración total
  del CM en trayectorias curvas, y la velocidad nula del CIR de su aceleración.

| Ejercicio | Comprobación / hipótesis |
| --- | --- |
| 1 | β = 53°, Ppersona = 98 N: T(s = ℓ/3) ≈ 69,84 N y smáx ≈ 4,386 m, compatibles con el redondeo impreso |
| 2 | fₛ,max = 470,4 N; fₛ(3 m) = 441 N; smáx = 3,30 m |
| 3a | El planteo impreso es consistente; sus valores intermedios presentan pequeñas diferencias aritméticas. Mantener las expresiones trigonométricas sin redondear hasta el final |
| 4 | R = 0,15 m, no 0,30 m: Pbarra = 58,8 N; posición final 53,13° desde la horizontal |
| 5 | Las respuestas corresponden al dibujo: ancho 2,4 m y altura 1,2 m. T = 214,36 N; HB = 185,64 N; VA + VB = 292,82 N. No asignar la mitad vertical a cada bisagra sin otra condición |
| 7 | F = 98 N; normal a 0,09 m del borde derecho para h = 0,15 m; hlim = 0,375 m |
| 8 | Umbral de vuelco = arctan(0,5). Coincidir con el umbral de deslizamiento no equivale a equilibrio neutro |
| 9 | NA = 98 N y NB = 686 N; pérdida de apoyo a h = 1,20 m. Ruedas trabadas: deslizan |
| 10 | La respuesta presupone cilindro macizo uniforme: Kt = 500 J, Kr = 250 J |
| 11 | En las fórmulas impresas de a se perdió el factor g. Debe ser (2/3)g sen β para disco y (1/2)g sen β para aro; μₛ,min = tan β/3 para disco |
| 12 y 14 | W = 10 500 J y K = 44,80 J, respectivamente. En el ej. 14 se usa I = 1,6 × 10⁻² kg·m², confirmado visualmente |
| 13 | vdisco = 5,940 m/s, varo = 5,144 m/s. El TP redondea el primero a 5,95. No es correcto afirmar que todas las fuerzas son iguales para ambos: a igual masa y pendiente, el roce requerido difiere |
| 15 | I = 5,49 kg·m²; K = 215,46 J; h = 1,221 m si parte del reposo sin pérdidas y rueda sin deslizar |
| 16 | c = 0,78125; Δs = 1,184 m y stotal = 3,184 m usando sin 37° sin redondear; compatible aproximadamente con 1,19 m y 3,19 m del TP |
| 17 | La figura muestra fuerza hacia la izquierda desde abajo del núcleo. El valor 0,261 m/s² requiere I = MR²/2; el enunciado no define claramente la distribución de masa. Registrar esa hipótesis |
| 18 | Se recuperan los tres resultados impresos. El roce cambia de sentido al pasar de fuerza central a fuerza superior |
| 19 | 336 N y 384 N requieren que los 100 kg sean la masa del vehículo sin las cuatro ruedas; si incluyera las ruedas cambiarían ambos resultados |
| 20 | hmín = 2,7R usa la aproximación r ≪ R. En B: an,CM = 23,8 m/s², at,CM = 7 m/s² y módulo total = 24,8 m/s². Las etiquetas impresas aCM = 7 y aT = 14 no corresponden a esas componentes; el punto material de la bola no está especificado para interpretar otra aceleración |
| 21 | Se presupone cilindro macizo y polea ideal de inercia despreciable. am = 2acm; con g = 9,8: am = 3,409 m/s², acm = 1,704 m/s², α = 8,522 rad/s² y T = 1,278 N |

Las inconsistencias se señalan para consultar con la cátedra; no se corrigen
silenciosamente los datos ni se atribuyen hipótesis ausentes al enunciado.

[Volver al tema](README.md)
