# Movimiento Circular: fuentes y criterios

[Volver al tema](README.md)

Revisión del **17 de octubre de 2026**. Raíz principal:
**E:\UTN\Fisica I\4. Movimiento Circular**.
Las rutas siguientes son relativas a esa carpeta. La teoría y las
resoluciones son síntesis propias; los archivos originales no se modifican.

## Teoría

| Clave | Archivo | Uso |
| --- | --- | --- |
| C-cinemática | 05 Movimiento circular-20261017/05 Movimiento Circular Cinemática.pptx | 11 diapositivas: ángulos, derivadas, relaciones lineales y angulares, MCU y MCUV |
| C-ampliada | 2025/05 Moviminto Circular.pptx | 24 diapositivas; 15–19: aceleración, dinámica y marcos; 20–24: órbitas, curva plana y peralte |
| Sears-5 | Sears Zemansky Young Freedman - Física Universitaria - Vol 1 - 14 Ed-158-199.pdf | §5.4, páginas PDF 21–26, impresas 150–155: dinámica del movimiento circular |
| Sears-3 | En la carpeta de Movimiento en el Plano: 04 Movimiento en el plano-20261017/Sears Zemansky Young Freedman - Física Universitaria - Vol 1 - 14 Ed-95-128.pdf | §§3.1–3.2 y 3.4; circular en páginas PDF 16–19, impresas 82–85 |

La carpeta de Movimiento en el Plano es
**E:\UTN\Fisica I\3. Movimiento e el Plano - Tiro Oblicuo**.
Se usa como apoyo vectorial y de curvatura; no se amplió el tema de tiro oblicuo.

Las copias de C-cinemática en la raíz, incluida la que dice “R1”, son
idénticas por hash a la de la carpeta de 2026. El recorte Sears-5 se repite
en Dinámica y en la subcarpeta actual. El ZIP de Circular de 2025 contiene
duplicados de C-ampliada, las animaciones y el TP PDF.

## Dos guías con distinta numeración

| Clave | Archivo | Contenido |
| --- | --- | --- |
| C-actual | 05 Movimiento circular-20261017/TP N°5 Movimiento Circular.docx | Seis ejercicios: Tierra, piloto, avión, satélite, nave anular y carretera |
| C-PDF | tp5.pdf | TP 05 de 18 ejercicios, cuatro páginas PDF, impresas 25–28; incluye MCUV, correas, cuerdas, loop y peralte |

La copia de C-actual en la raíz y la de C-PDF en 2025 son duplicados.
En los ejercicios se escribe siempre **C-actual** o **C-PDF**.
Por ejemplo, el ejercicio 2 de C-actual es el piloto; el de C-PDF es un
volante con aceleración angular constante.

Se revisaron el texto y las figuras pertinentes. En DOCX, los ángulos,
radios y agentes se contrastaron con sus imágenes incrustadas.

## Resoluciones de cátedra

| Archivo | Localizador | Uso |
| --- | --- | --- |
| TP 05 Ej 02.pdf | 3 páginas | Aceleraciones tangencial, normal y total |
| TP 05 Ej 05.pdf | 2 páginas | Poleas, diámetros y correa |
| TP 05 Ej 08.pdf | 2 páginas | Giro horizontal con cuerda y papel del peso |
| TP5EJ11.pdf | 4 páginas | Péndulo cónico |
| TP5EJ13.pdf | 7 páginas; en especial pág. 7 | Loop y comprobación de errores del resultado impreso |
| TP5EJ18.pdf | 3 páginas | Dos cuerdas y eje vertical |

El desarrollo de cuerda vertical que ya existía en el repositorio coincide
con **C-PDF, ejercicio 9, páginas PDF 2–3**. Esa fuente permite reemplazar
la atribución anterior de “caso de parcial sin identificar” por un localizador
comprobado, sin afirmar de qué examen pudo haberse tomado.

## Fotos, animaciones y alcance de la revisión

Las seis fotos de la raíz se inspeccionaron visualmente. Las del
31/05/2022 muestran el loop, sus ejes y componentes; las de junio/julio,
peralte y aplicaciones de Newton. Algunas partes son poco legibles;
no se reconstruyeron datos numéricos faltantes a partir de ellas.

**2025/Animaciones con GeoGebra TP 05.docx** contiene recursos para MCU,
aceleraciones, peralte, órbitas y péndulo cónico. Se leyó el documento y se
identificaron los enlaces; no se validó el funcionamiento actual de los
sitios. Pueden abrirse desde el archivo original para acompañar el estudio.

Los videos incrustados en las presentaciones se inventariaron y se
extrajeron fotogramas de muestreo. No se realizó una transcripción integral
de audio ni se los usa como evidencia exclusiva de una afirmación.
El tratamiento de videos de Dinámica y del material de tiro está registrado
en [las fuentes de Dinámica](../dinamica/fuentes.md#videos-fotos-y-apoyo-de-movimiento-en-el-plano).

## Discrepancias y decisiones

- **C-cinemática, diap. 3:** la posición vectorial de un círculo no se
  escribe sumando “radio” y “ángulo” como componentes de longitud.
  Se usa $\vec r=R\hat e_R$, o su expresión cartesiana.
- **Diap. 5 y 7:** se distingue valor medio de instantáneo; las unidades
  de aceleración angular son rad/s², no s⁻¹.
- **C-ampliada, diap. 20:** una órbita geosincrónica tiene el período de
  rotación terrestre. Permanecer sobre un mismo punto exige además órbita
  circular ecuatorial y el mismo sentido de rotación: geoestacionaria.
  Los 24 h de las fuentes se tratan como dato del ejercicio.
- **C-actual, ejercicio 2:** se calcula la rapidez para $a_r=5{,}5g$,
  siguiendo literalmente la aceleración indicada. No se confunde con una
  lectura de apoyo de $5{,}5mg$ ni se extrapola el modelo a un límite médico.
- **C-PDF, ejercicio 7(c), página PDF 1:** el dato 500 → 3000 rpm en
  5 s da **145,83 vueltas**, no 112,5. Se comprobó la página visual:
  es una discrepancia del resultado, no de la extracción de texto.
- **C-PDF, ejercicio 8:** una piedra suspendida en un círculo horizontal
  necesita componente vertical de tensión. La respuesta 22,8 N concuerda
  con incluir el peso; la rapidez angular límite 39,53 rad/s es una
  aproximación que lo desprecia en ese cálculo.
- **C-PDF, ejercicio 9:** el TP indica velocidad angular constante en
  a–c, pero el DCL lateral de peso y tensión tiene resultante tangencial.
  Se explicita la acción tangencial que haría falta para mantener MCU;
  para un giro libre, cada rapidez debe ser local.
- **C-PDF, ejercicio 10:** la consigna pide “velocidad” y la respuesta da
  $\omega$. Se diferencian rapidez lineal y angular, con sus unidades.
- **C-PDF, ejercicio 13(e), página PDF 3:** con $v=14\ \mathrm{m/s}$,
  $R=5\ \mathrm m$, $m=100\ \mathrm{kg}$ y el ángulo de la figura,
  resulta $a_r=39{,}2\ \mathrm{m/s^2}$ y $N=4410\ \mathrm N$.
  No son 32,9 m/s² ni 44.100 N. Coincide con la resolución TP5EJ13,
  pág. 7. Se evita redondear $\alpha$ antes de obtener $a_t=8{,}49\ \mathrm{m/s^2}$.
- **C-PDF, ejercicio 16:** si el ancho se mide sobre la calzada,
  $\Delta h=L\sin\beta$; si es la proyección horizontal,
  $\Delta h=L\tan\beta$. El valor impreso 0,923 m corresponde a la primera
  interpretación, aproximadamente.

La [guía por casos](resolucion-por-casos.md) clasifica todos los ejercicios
de ambas guías. Las resoluciones desarrollan los casos representativos
indicados en su índice; no se presenta como resuelto un ejercicio que sólo
está clasificado.
