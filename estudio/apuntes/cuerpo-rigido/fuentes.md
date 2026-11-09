# Cuerpo Rígido — fuentes y comprobaciones

Síntesis propia del material local de cátedra en
`9. Cuerpo Rigido/09 Modelo cuerpo rígido. Rotación.-20261103/`.
Los originales permanecen fuera del repositorio, sin modificaciones.

| Material | Uso |
| --- | --- |
| `09 Modelo de Cuerpo Rígido - Rotación.pptx` (30 diapositivas) | 3–4: torque; 5–10: inercia y Steiner; 11–12: sistema y dinámica; 13–16: energía, trabajo y potencia; 19–26: momento angular, impulso y conservación; 22: precesión; 27–28: Kepler |
| `tp9.pdf` (8 páginas PDF, impresas 49–56) | Ej. 1–4: inercia; 5–19: dinámica y poleas; 20–24: energía; 25–35: momento angular y conservación. Los casos indican los números del TP |
| Sears, Zemansky, Young y Freedman, *Física Universitaria*, vol. 1, 14.ª ed., archivo `…301-330.pdf` | Cap. 9, páginas impresas 273–302: cinemática, energía rotacional, inercias, Steiner e integración (§9.1–9.6) |
| Mismo libro, archivo `…331-366.pdf` | Cap. 10, páginas impresas 303–338: torque, dinámica, rodadura/eje instantáneo, trabajo, momento angular, conservación y precesión (§10.1–10.7) |

Los números en los nombres de los recortes **no** coinciden con la paginación
impresa. El TP contiene fórmulas y dibujos que no se extraen bien como texto;
se contrastaron visualmente las figuras de poleas con dos radios y los casos
de energía y momento angular de las páginas PDF 5, 6 y 8.

## Alcance del material de aprendizaje progresivo

Las [fichas introductorias](desde-cero.md) y sus ejemplos cotidianos
(puerta, regla, disco, aro y plataforma) son **elaboraciones didácticas
propias** apoyadas en los conceptos de las fuentes anteriores: **no son
nuevos enunciados de cátedra**. Las [pistas del TP 9](pistas-tp9.md)
remiten a los ejercicios originales sin reproducirlos ni mostrar resultados.
La guía por casos y las comprobaciones de esta página contienen soluciones
parciales y deben reservarse para **después** de un intento personal.

## Criterios

- Se mantienen «momento de una fuerza», «momento de inercia», «momento
  cinético» y «Steiner», con sus equivalentes torque y momento angular.
- La componente $L_z=I_z\omega_z$ no se confunde con la relación vectorial
  general; Sears §10.5 explica la limitación de $\vec L=I\vec\omega$.
- La ley τ = Iα se restringe a los casos indicados; si cambia la distribución
  de masa, se usa la ley del momento angular.
- Rodadura, precesión e impulso se incluyen porque aparecen en el título,
  la presentación o el libro; no se les adjudican ejercicios inexistentes del TP.
- Las fórmulas de poleas suponen cuerda inextensible de masa despreciable,
  sin deslizamiento y eje fijo ideal, salvo indicación de roce.
- Las guías orientan el planteo; no reemplazan los 35 enunciados ni son una
  resolución completa de todos ellos.

## Comprobaciones y advertencias sobre el TP

| Ejercicio | Comprobación / criterio |
| --- | --- |
| 2 | I = 52 kg·m²; ω = 2,660 rad/s = 25,40 rpm. La unidad de ω debe ser rad/s, aunque la respuesta imprime «rad» |
| 6 | Fuerza de 49 N: α = 10,889 rad/s² y W = 294 J. Peso de 49 N colgado: m = 5 kg, a = 3,92 m/s² y α = 6,533 rad/s²; la tensión ya no es 49 N |
| 7 | Con radio 0,07 m, M = 2 kg y torque 0,6 N·m: I = 0,0049 kg·m², t = 1,026 s y N = 10,263 vueltas. Las respuestas 10,3 s y 103,5 vueltas no corresponden a esos datos |
| 8 | Disco de 15 kg: a = 7,612 m/s², T₁ = 380,58 N, T₂ = 437,67 N |
| 14 | «Peso de 8 kg» es dimensionalmente ambiguo. Las respuestas de tensiones corresponden a interpretar masa de 8 kg en cada bloque |
| 16 | ω a los 2 s presupone que parte del reposo; el enunciado no lo explicita |
| 19 | Tomando el disco uniforme de M = 0,8 kg y R = 0,08 m, aro interior de inercia despreciable y r = 0,06 m: α = 21,512 rad/s², a₁ = 1,721 y a₂ = 1,291 m/s². Newton da T₁ = 4,847 N y T₂ = 5,545 N; los 8,87 N impresos para T₂ son incompatibles con m₂ = 0,50 kg y esa aceleración |
| 20 | La distancia pivote–centro de la bola es 0,28 + 0,04 = 0,32 m si se unen por la superficie. Incluir también la inercia propia de la bola; la geometría explica la rapidez lineal impresa |
| 21 | Se imprime ω = 7,289 × 10⁻⁴ rad/s. Usando literalmente ese dato, K ≈ 2,578 × 10³¹ J; la respuesta 2,578 × 10²⁹ J corresponde a ω = 7,289 × 10⁻⁵ rad/s. No cambiar el dato sin indicarlo |
| 22 | La energía a los 5 s presupone partida del reposo y polea discoidal uniforme. Con esas hipótesis resulta K = 120,05 J |
| 23 | Los resultados suponen polea discoidal uniforme, aunque el texto sólo da masa y radio. Con esa hipótesis: a ≈ 7,57 m/s², T ≈ 11,36 N, v ≈ 9,53 m/s |
| 24 | El balance con ambos bloques, polea y resorte da Wroce = −2,20 J |
| 28 | Donde dice distancia final «0,70 cm» debe leerse 0,70 m, consistente con el desplazamiento de 0,60 m desde 1,30 m |
| 29 | 32,40 J es el trabajo para mover sólo la mesa. Incluyendo la mujer: Kfinal = 99,90 J |
| 31 | Ii = 28 kg·m²; If = 9,25 kg·m²; ωf = 6,054 rad/s y ΔK = 113,51 J |
| 32 | Para liberación desde reposo, Lz(t) = −mgℓ cos(θ)t. La expresión sin t de la respuesta tiene dimensiones de torque |
| 34 | ωf = 0,748 rad/s supone momento angular inicial nulo de la niña respecto del eje; si llega corriendo, hay que incluir su aporte |
| 35 | Con el radio de giro dado: ωf = 0,769 rad/s |

Los signos vectoriales se fijan con los ejes elegidos; una respuesta de módulo
no determina por sí sola el sentido. Las discrepancias se explicitan para
consultarlas con la cátedra, sin modificar los originales.

[Volver al tema](README.md)
