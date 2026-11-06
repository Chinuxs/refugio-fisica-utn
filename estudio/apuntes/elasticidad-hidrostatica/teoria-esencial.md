# Elasticidad e Hidrostática — teoría esencial

## 🎯 Qué recordar

- **Modelo deformable:** admite cambios de forma o tamaño. Elasticidad es
  recuperar la forma al retirar la carga; deformación plástica deja cambios
  permanentes. La proporcionalidad esfuerzo–deformación tiene un rango limitado.
- **Hidrostática:** estudia fluidos en reposo. La presión aumenta con la
  profundidad y actúa normal a las superficies.
- **Densidad del fluido** determina presión hidrostática y empuje;
  **densidad del cuerpo** relaciona su masa con su propio volumen.
- **Empuje:** resultante de las fuerzas de presión; equivale al peso del
  fluido desplazado. Un cuerpo que se hunde también recibe empuje.
- **Equilibrio:** sumar fuerzas reales. Si importan sus puntos de aplicación,
  sumar también momentos, como en la barra flotante.

La Hidrostática se basa en los ejercicios de cátedra disponibles. Elasticidad
es un complemento introductorio: [alcance y fuentes](fuentes.md).

## 🖼️ Esquema / dibujo

![Presión al descender en un líquido, empuje sobre un bloque y fuerzas en las dos balanzas del ejercicio 17 del PDF.](assets/presion-empuje-balanzas.svg)

## 📐 Fórmula

### Densidad y unidades

$$\rho=\frac mV,\qquad d_r=\frac{\rho}{\rho_{referencia}}.$$

La densidad relativa no tiene unidades; para sólidos y líquidos suele
referirse al agua, si así se indica. En estos ejercicios:
ρagua = 1000 kg/m³ y g = 9,8 m/s².

| Conversión | Equivalencia |
| --- | --- |
| Masa | 1 g = 10⁻³ kg |
| Área | 1 cm² = 10⁻⁴ m² |
| Volumen | 1 cm³ = 10⁻⁶ m³; 1 L = 10⁻³ m³ |
| Densidad | 1 g/cm³ = 1000 kg/m³ |
| Presión | 1 Pa = 1 N/m²; 1 kPa = 1000 Pa |

### Presión: fijar nivel y referencia

$$p=F_\perp/A\quad\text{si es uniforme},\qquad
p=p_{superficie}+\rho gh.$$

h es la **profundidad vertical**, no el recorrido por un tubo. Para varios
estratos: $p_{fondo}=p_{superficie}+\sum_j\rho_jgh_j$.
Al bajar se suma ρgh; al subir se resta. En un mismo fluido conectado,
homogéneo y en reposo, puntos al mismo nivel tienen igual presión.
En una interfaz ideal la presión es continua (se desprecia tensión superficial).

$$p_{man}=p_{abs}-p_{atm}.$$

Una superficie abierta al aire tiene presión manométrica cero, pero su presión
absoluta es patm. Esta distinción se verifica en
[OpenStax §14.2](https://openstax.org/books/university-physics-volume-1/pages/14-2-measuring-pressure).

### Pascal: transmitir presión

$$\frac{F_1}{A_1}=\frac{F_2}{A_2}.$$

Para pistones ideales a igual altura o con desnivel despreciable, despreciando
sus pesos y el roce; la presión exterior común se cancela. Con desnivel,
agregar la corrección hidrostática.
No se iguala la presión de todo el líquido si cambia la altura.
En un sistema incompresible sin pérdidas, $A_1\Delta x_1=A_2\Delta x_2$:
ganar fuerza requiere mayor recorrido del pistón pequeño.

### Arquímedes y flotación

$$E=\rho_{fluido}gV_{desplazado},\qquad P=mg.$$

En varios líquidos: $E=\sum_j\rho_jgV_j$, donde Vj es el volumen del cuerpo
sumergido en cada uno. Para un cuerpo homogéneo que flota libremente en un
solo líquido, despreciando el aire:

$$E=P\quad\Rightarrow\quad
\frac{V_{sum}}{V_{total}}=\frac{\rho_{cuerpo}}{\rho_{fluido}}.$$

Con cuerda, lastre u otros apoyos, plantear Newton en lugar de imponer E = P
al cuerpo aislado. El empuje pasa por el centro del volumen desplazado en
un líquido homogéneo; no necesariamente por el CM del cuerpo. Véase
[OpenStax §14.4](https://openstax.org/books/university-physics-volume-1/pages/14-4-archimedes-principle-and-buoyancy).

### Presión variable y estabilidad — ampliación con el TP completo

En una pared vertical rectangular con el borde superior al nivel del agua,
ancho b y profundidad H, integrar la presión manométrica:

$$F=\int_0^H\rho gh\,b\,dh=\frac12\rho gbH^2,
\qquad h_{centro\ de\ presión}=\frac{2H}{3}.$$

La resultante queda por debajo del centro geométrico de la pared. Para
hallar un momento usar su brazo respecto de la bisagra (ej. 7–9).
En una cara horizontal a profundidad constante, sí puede usarse F = pA.

Un flotador puede tener peso igual al empuje y aun así volcar: para su
estabilidad importan las **líneas de acción**. Al inclinarlo, el centro del
volumen desplazado cambia; si el par peso–empuje restaura la orientación,
es enderezador (ej. 21).

Para una boya cilíndrica vertical con área de flotación A constante,
el empuje adicional ante un pequeño descenso y es ρgAy. Al restar el
equilibrio, resulta $F_{rest}=-\rho gAy$, equivalente a un resorte ideal
de constante $k_{ef}=\rho gA$ (ej. 18).

**Tensión superficial:** está mencionada en el título del TP, sin ejercicios
ni desarrollo específico. No se da por cubierto ese contenido con estos casos.

### Elasticidad — complemento bibliográfico, alcance de cátedra pendiente

Para una barra uniforme con carga axial y pequeñas deformaciones:

$$\sigma=\frac{F}{A},\qquad \varepsilon=\frac{\Delta L}{L_0},\qquad
\sigma=Y\varepsilon\quad\Rightarrow\quad\Delta L=\frac{FL_0}{AY}.$$

σ es esfuerzo normal, ε deformación relativa y Y módulo de Young.
σ e Y se miden en Pa; ε es adimensional. F es la fuerza axial interna,
no la suma de las dos fuerzas opuestas en los extremos.
Para compresión uniforme de volumen: $B=-\Delta p/(\Delta V/V_0)$;
para corte: $G=(F_\parallel/A)/(\Delta x/L_0)$ en régimen lineal.
No confundir estos módulos con k de un resorte.

Fuentes complementarias:
[OpenStax §12.3](https://openstax.org/books/university-physics-volume-1/pages/12-3-stress-strain-and-elastic-modulus)
y [§12.4](https://openstax.org/books/university-physics-volume-1/pages/12-4-elasticity-and-plasticity).

## ⚠️ Error frecuente

- Convertir cm³ a m³ multiplicando sólo por 0,01: hay que elevar al cubo.
- Usar Vtotal en el empuje cuando el cuerpo está parcialmente sumergido.
- Decir «misma altura, misma presión» entre líquidos desconectados sin justificarlo.
- Confundir presión con fuerza o expresar fuerzas en kg.
- Contar el peso del bloque dentro de la lectura inferior aunque lo sostenga
  un soporte externo: la balanza del vaso recibe la reacción al empuje.
- Reemplazar aceite por agua en un cálculo sólo por costumbre.

## 🔗 Ver también

- [Casos de los 21 ejercicios del TP 11](resolucion-por-casos.md)
- [Fuentes y correcciones](fuentes.md)
- [Estática: fuerzas y momentos](../estatica-rototraslacion/teoria-esencial.md)
- [Laboratorio 3: constante de un resorte](../../laboratorios/laboratorio-3.md)
- [Volver al tema](README.md)
