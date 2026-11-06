# Elasticidad e Hidrostática — fuentes y comprobaciones

## Material disponible y alcance

Carpeta local:
`E:\UTN\Fisica I\11. Modelo cuerpo deformable. Elasticidad. Estática de los fluidos`.

Ahora incluye **`tp11.pdf`**, cuatro páginas PDF (impresas 65–68), con
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

**El TP 11 completo está disponible. No contiene ejercicios de Elasticidad.**
Su título incluye «Tensión superficial», pero sus 21 ejercicios no desarrollan
un caso específico de ese contenido; queda pendiente confirmar su alcance.
El título del tema conserva el nombre de la carpeta; la sección de
Elasticidad es introductoria y su alcance queda pendiente de confirmar.
No se incluyen dinámica de fluidos, Bernoulli ni viscosidad por inferencia.

## Bibliografía complementaria

Consultada el **5 de noviembre de 2026**. Es material externo a la cátedra,
usado para la síntesis complementaria y para comprobar conceptos:

- [OpenStax, University Physics vol. 1, §12.3: esfuerzo, deformación y módulos](https://openstax.org/books/university-physics-volume-1/pages/12-3-stress-strain-and-elastic-modulus): Young, corte y compresión volumétrica.
- [OpenStax §12.4: elasticidad y plasticidad](https://openstax.org/books/university-physics-volume-1/pages/12-4-elasticity-and-plasticity): distinguir rango lineal, recuperación elástica y deformación permanente.
- [OpenStax §14.2: medición de presión](https://openstax.org/books/university-physics-volume-1/pages/14-2-measuring-pressure): presión manométrica, absoluta y barometría.
- [OpenStax §14.4: Arquímedes y flotación](https://openstax.org/books/university-physics-volume-1/pages/14-4-archimedes-principle-and-buoyancy): volumen desplazado, empuje y equilibrio de un cuerpo flotante.

El tratamiento principal y los datos de Hidrostática proceden del archivo local.
Los diagramas SVG y la redacción son propios. Los originales permanecen intactos.

## Comprobaciones, correcciones e hipótesis

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

## Nuevos ejercicios del PDF

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
