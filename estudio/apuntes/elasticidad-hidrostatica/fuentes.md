# Elasticidad e Hidrostática — fuentes y comprobaciones

## Actualización de cátedra — 7 de noviembre de 2026

Carpeta nueva, dentro de la carpeta del tema:
`11 Modelo cuerpo deformable. Elasticidad. Estática de los fluidos.-20261107`.

| Archivo | Contenido y uso |
| --- | --- |
| `11 Hidrostática.pptx` | **27 diapositivas**, Ing. J. Vazquez, UTN FRLP. 1–8: modelo deformable, esfuerzo normal, Young, curva de tracción, corte, módulo volumétrico y tabla de módulos. 9–16: fluidos, densidad, modelo ideal y ley hidrostática. 17–21: antecedentes, barómetro y atmósfera. 22: Pascal. 23–26: Arquímedes, centro de empuje, flotación y apoyos. 27: cierre |
| `Sears Zemansky Young Freedman - Física Universitaria - Vol 1 - 14 Ed-397-425.pdf` | **29 páginas PDF**, impresas **369–397**, cap. 12. Se usa §12.1–12.3 (PDF 1–10): densidad, presión, medición y flotación; p. 378 incluye tensión superficial cualitativa. La elasticidad procede de las diapositivas, no de este recorte |
| `tp11.pdf` | **4 páginas**, impresas 65–68. Copia binaria idéntica al TP anterior: mismos 21 ejercicios y respuestas; no hay renumeración ni nuevos ejercicios de Elasticidad |

Se extrajo el texto y las ecuaciones de las 27 diapositivas; además se
revisaron visualmente las diapositivas 3–8, 13, 15, 21 y 23–24/26, incluidas
la tabla de módulos y las fórmulas que una extracción lineal puede desordenar.
Del libro se revisaron los desarrollos de §12.1–12.3 y se identificó el
contenido posterior para separar Hidrostática de Hidrodinámica.

**Límite de alcance:** §12.4–12.6 (PDF 11–19) desarrolla flujo, Bernoulli,
viscosidad y turbulencia; el resumen y los ejercicios posteriores mezclan
ambos bloques. No se incorporan esos desarrollos de Hidrodinámica al repaso
del tercer parcial, que el estudiante confirmó como sólo Hidrostática.
El índice de la diapositiva 10 menciona viscosidad, pero no aporta una
práctica cuantitativa de ese contenido. Subir bibliografía no confirma por
sí solo un cambio de temario de examen.

**Qué cambia:** Elasticidad ya tiene fuente de cátedra y cuatro procedimientos
propios E1–E4. Tensión superficial pasa de sólo mencionada en el TP a contar
con explicación cualitativa en la bibliografía suministrada. Continúa sin
ejercicios específicos en el TP; no se agregan problemas de capilaridad
como si fueran consignas del profesor.

Control de identidad: los dos `tp11.pdf` tienen SHA-256
`19f00181e216197a05b0679b9e8deddea16ae293f0c9993a8bb3ce905697823a`.
Los archivos fuente se conservan sin modificaciones, fuera del repositorio.

## Presentación práctica anterior y numeración del TP

Carpeta local:
`E:\UTN\Fisica I\11. Modelo cuerpo deformable. Elasticidad. Estática de los fluidos`.

Se conserva **`tp11.pdf`**, cuatro páginas PDF (impresas 65–68), con
tabla de densidades y **21 ejercicios**. Se revisaron todos los enunciados,
las respuestas y visualmente las figuras de las páginas PDF 2 y 4.
La presentación `Trabajo práctico nº 11 (2).pptx`, atribuida a Ing. Diego Reyes,
tiene 16 diapositivas y ocho ejercicios seleccionados, revisados previamente.
Se adopta la numeración del PDF. Correspondencia con la presentación:

| Diapositivas | Número en PPTX → número en PDF | Contenido usado |
| --- | --- | --- |
| 1 | 2 | Densidad, unidades y lingote |
| 2 | 4 | Barómetro con vino |
| 3–4 | 5 | Agua y kerosene en tubo en U |
| 5 | 6 | Elevador hidráulico y mención de palanca |
| 6–8 | 12 | Bloque flotando en agua y aceite |
| 9–10 | 13 → 11 | Madera con lastre de plomo |
| 11–13 | 18 → 17 | Dinamómetro y balanza inferior |
| 14–16 | 21 → 20 | Equilibrio y volumen de una barra flotante |

**No confundir ambas presentaciones:** las referencias «diap. 1–16» de los
casos prácticos y sus erratas pertenecen a `Trabajo práctico nº 11 (2).pptx`.
Las referencias a teoría nueva identifican `11 Hidrostática.pptx` (27).
El TP completo no contiene ejercicios de Elasticidad ni un caso específico
de tensión superficial. Las ampliaciones teóricas no cambian esos hechos.

## Bibliografía complementaria

Consultada el **5 de noviembre de 2026**. Es material externo a la cátedra,
usado para la síntesis complementaria y para comprobar conceptos:

- [OpenStax, University Physics vol. 1, §12.3: esfuerzo, deformación y módulos](https://openstax.org/books/university-physics-volume-1/pages/12-3-stress-strain-and-elastic-modulus): Young, corte y compresión volumétrica.
- [OpenStax §12.4: elasticidad y plasticidad](https://openstax.org/books/university-physics-volume-1/pages/12-4-elasticity-and-plasticity): distinguir rango lineal, recuperación elástica y deformación permanente.
- [OpenStax §14.2: medición de presión](https://openstax.org/books/university-physics-volume-1/pages/14-2-measuring-pressure): presión manométrica, absoluta y barometría.
- [OpenStax §14.4: Arquímedes y flotación](https://openstax.org/books/university-physics-volume-1/pages/14-4-archimedes-principle-and-buoyancy): volumen desplazado, empuje y equilibrio de un cuerpo flotante.

Desde el 7/11 la base principal es la teoría local de cátedra, el TP y el
recorte de Sears suministrado. OpenStax queda como comprobación complementaria
histórica, no como sustituto de la teoría del profesor.
Los diagramas SVG y la redacción son propios. Los originales permanecen intactos.

## Erratas y convenciones de la teoría nueva

| Diapositiva de `11 Hidrostática.pptx` | Criterio aplicado en los apuntes |
| --- | --- |
| 4 y 8 | Se alterna Y y E para módulo de Young. Se escribe Y para no confundirlo con empuje ni energía; S es esfuerzo normal, en Pa, no fuerza de tensión en N |
| 5 | El dibujo tiene ejes F–ΔL: su pendiente inicial es AY/L₀ en N/m. Sólo en S–ε la pendiente es Y. No confundir límite de proporcionalidad con límite elástico; la respuesta elástica puede no ser lineal |
| 7 | El esquema cambia pi a pi + Δp, pero la fracción de B usa F⊥/A. Se entiende como **incremento Δp**, no como presión inicial absoluta: B = −Δp/(ΔV/V₀). K = 1/B, en Pa⁻¹ |
| 12 | Se reutiliza ρ para densidad y densidad relativa. Se distingue ρ = m/V, con unidades, de dr = ρ/ρagua, adimensional |
| 21 | Se escribe hPa, no HPa; 101325 Pa son 1013,25 hPa. La exponencial exige especificar modelo isotérmico de gas ideal con g constante; no usar simultáneamente ρ constante |
| 23 | F₁ = ρgyA y F₂ = ρg(y+h)A son contribuciones manométricas. En la resta intermedia debe aparecer **−p₁A**, no −p₂A. Con presiones absolutas se añade patm a ambas caras y se cancela al restar: E = (p₂ − p₁)A = ρgVsum |
| 24 | «Centro de flotación» se refiere en esa lámina al centro de gravedad del fluido desalojado; los apuntes lo identifican también como centro de empuje, no como CM del cuerpo |
| 26 | Las flechas de T y normal n apuntan hacia arriba, pero ambas ecuaciones las restan. Con y hacia arriba: **E + T − P = 0** y **E + N − P = 0**. No reproducir los signos impresos |

Para un bloque que toca el fondo, el empuje usual requiere que el fluido
actúe sobre las superficies correspondientes. Si sella la cara inferior,
se debe recalcular la resultante de presión (Sears P12.1); no basta con
añadir una normal a ρgV sin revisar el contacto.

## Controles de los procedimientos nuevos

Son **ejemplos propios de comprobación**, no ejercicios agregados al TP.
Los módulos de acero y agua se leen de la tabla de la diapositiva 8.

| Control | Resultado |
| --- | --- |
| Young: L₀ = 2 m, A = 1 mm², F = 100 N, Y = 200 GPa | ΔL = 0,001 m; S = 100 MPa; ε = 0,0005; S/Y coincide con ΔL/L₀ |
| Corte: h = 0,10 m, A = 1 cm², F∥ = 100 N, G = 80 GPa | x = 1,25 × 10⁻⁶ m; x/h = 1,25 × 10⁻⁵ |
| Volumen: V₀ = 1 L, Δp = 1 MPa, B = 2 GPa | ΔV = −5 × 10⁻⁷ m³ = −0,5 cm³; Vf = 999,5 cm³ |

Supuestos: carga y geometría compatibles con cada fórmula, régimen lineal,
deformaciones pequeñas y módulos aproximadamente constantes. Los controles
no certifican un límite de fluencia o rotura que no se haya suministrado.

## Comprobaciones de la práctica anterior y del TP

| Ejercicio del PDF | Resultado y observación |
| --- | --- |
| 2 | 535 g / 25 cm³ = 21,4 g/cm³ = 21400 kg/m³. La diapositiva cambia por error V a 0,00025 en una división; el valor coherente es 0,000025 m³. La identificación como platino es la propuesta por la fuente, no una prueba química |
| 4 | La diapositiva adopta patm = 103000 Pa: h = 10,681 m suponiendo vacío. Con 101325 Pa: h = 10,507 m. No se mezclan esas dos referencias. La presión de vapor no se cuantifica porque no se da temperatura ni composición del vino |
| 5 | Columna equivalente de agua = 4,92 cm; diferencia de superficies = 1,08 cm |
| 6 | F₁ = 225 N; diferencia de presión respecto del exterior común = 750000 Pa. Para una palanca, la ecuación correcta es igualdad de momentos; no usar la proporción ambigua de la diapositiva sin identificar brazos |
| 12 | Aceite: 5 cm; agua: 1 cm; presión manométrica inferior: 490 Pa. Coinciden con las diapositivas |
| 11 | Vplomo = 3,49515 × 10⁻⁴ m³ = 349,5 cm³, incluyendo el empuje sobre el lastre |
| 17 | Con aceite de 916 kg/m³: E = 2,30174 N, T = 17,29826 N y N = 31,70174 N. Control: T + N = 49 N. El PDF confirma las lecturas. Las diapositivas 12–13 sustituyen 916 por 1000 kg/m³ y rotulan fuerzas en kg; la 11 omite la reacción al empuje en el DCL inferior. Soporte superior externo, sin contacto con el vaso ni derrame |
| 20 | Cuerda vertical, sección uniforme y mitad sumergida: centro de empuje a 2,7 m de B; E = 156,8 N, T = 19,6 N, Vsum = 0,016 m³ y Vtotal = 0,032 m³. Cancelar cos α sólo si no es cero |

## Ampliación previa con el TP completo — 5/11/2026

| Ejercicios | Comprobaciones y criterios |
| --- | --- |
| 1 y 3 | Con la tabla y datos del TP: mesfera = 0,11027 kg y ρestrella = 4,75077 × 10¹⁷ kg/m³; las respuestas 0,111 kg y 4,77 × 10¹⁷ presentan pequeñas diferencias numéricas |
| 7–9 | Presa: 2205000 N; compuerta: 14288,4 N·m; piscina: 5,88 × 10⁶ N, 1,96 × 10⁵ N y 5,88 × 10⁵ N. Se cancela la atmósfera común a ambas caras. El ej. 8 imprime N en lugar de N·m |
| 10 | Densidad de la corona = 2702,7 kg/m³; no coincide con oro macizo |
| 13 | Amin hielo = 90/[(1000 − 917)·0,30] = 3,61446 m²; se alcanza la inmersión completa del hielo |
| 14 | ρesfera = 500 kg/m³ y ρaceite = 1250 kg/m³; se respeta el valor impuesto por las fracciones sumergidas |
| 15 | Esfera hueca cerrada, aire interior despreciado: ρmaterial = 1476,0 kg/m³; líquido para suspensión completa = 400 kg/m³; peso = 16,4201 N |
| 16 | Patm = 101300 Pa: Fsup absoluta = 1017,90 N y Finf absoluta = 1029,66 N. Las respuestas impresas 4,9 N y 16,6 N son manométricas, aunque se proporciona patm. En ambos casos E = 11,76 N y T = 86,24 N |
| 18 | Δh ≈ 0,1145 m; T ≈ 3,136 s. Modelo oscilatorio sin amortiguamiento ni masa añadida del fluido; área de flotación constante |
| 19 | m = 0,680 kg; pman inferior = 784 Pa. La figura da 10 cm de capa de aceite; sólo 8 cm del cubo están en aceite |
| 21 | Peso = 132,3 N, brazo horizontal del par a 45° = 0,075 sen 45° m; momento restaurador = 7,0163 N·m. La respuesta imprime N en lugar de N·m |

Se desprecia el empuje del aire, la capilaridad y la tensión superficial en
estos modelos. Las densidades se toman constantes según cada enunciado.
Las correcciones se explicitan para discutirlas con el docente, sin modificar
la presentación ni atribuirle contenidos que no incluye.

[Volver al tema](README.md)
