# Impulso y cantidad de movimiento — fuentes

Síntesis propia a partir de
`8. Modelo sistema de partículas/08 Modelo sistema de partículas.-20260905/`.

| Material consultado | Uso |
| --- | --- |
| `08 Modelo Sistemas de Partículas.pptx` | Diap. 3–9: impulso y conservación; 10–20: CM, referencias y energía; 21–26: choques y restitución |
| `tp8.pdf` | Págs. PDF 1–7 (impresas 41–47): selección de casos; ej. 6 y 22 como comprobaciones numéricas |

## Criterios para usar las fuentes

- Se conserva la terminología **cantidad de movimiento**, **centro de masa** y
  **choque plástico**, incluyendo sus equivalentes habituales.
- La conservación se formula por **impulso externo durante el intervalo**,
  para justificar el tratamiento aproximado de choques breves.
- La relación de restitución escrita con velocidades algebraicas se usa en 1D;
  los choques oblicuos se resuelven por componentes. Un choque inelástico
  también puede ocurrir en dos dimensiones.
- “Pérdida de energía interna” en la diapositiva de choque plástico se interpreta
  como desaparición de la **energía cinética relativa al CM**. No significa que
  desaparezca energía total ni energía interna térmica.
- **Ej. 27, pág. PDF 6:** no se explicitan masas iguales en el texto ni en la
  figura. Los valores numéricos impresos corresponden a esa hipótesis.
  Para resolver sin agregarla, mantener las masas en las ecuaciones.
- **Ej. 30:** “cae verticalmente” no determina por sí solo la velocidad vertical
  inmediatamente después de la explosión. Para obtener el resultado usual se
  interpreta que ese fragmento queda instantáneamente en reposo en la cima.
  Antes de calcular tiempos o energía, explicitar ese dato adicional.

La figura fuerza–tiempo del ej. 6 se inspeccionó visualmente: el intervalo
horizontal a 4 N va de 2 a 3 s. La guía separa esa área de las dos triangulares.

## Revisión directa del 15 de noviembre de 2026

Se releyeron las **27 diapositivas**, los **36 ejercicios del TP 8** y el
apoyo de 17 páginas de `N°8 Sistemas de partículas/`. Se añadió el recorte
de Sears que estaba disponible en la carpeta del tema pero no figuraba
en la tabla inicial de fuentes.

## Trazabilidad por concepto

| Apartado | Cátedra contrastada | Complemento / elaboración propia |
| --- | --- | --- |
| Momento, impulso, área y fuerza media | Presentación, diap. 3–5; TP 8.1–7 y 20 | Sears §8.1, pp. 238–242; distinción propia entre área de $F(t)$ y $F(x)$ |
| Sistema, fuerzas y conservación por componentes | Diap. 6–9 y 21; TP 8.11, 15–36 | Sears §8.2–8.3, pp. 243–251; separación propia por intervalos |
| CM, referencias y energía del sistema | Diap. 10–20; TP 8.8–14 | Sears §8.5, pp. 254–258; deducción propia de $K_{CM}=P^2/(2M)$ |
| Restitución y choque frontal | Diap. 22–26; TP 8.15–21, 26 | Sears §8.3–8.4, pp. 247–254; tabla de condiciones y deducción propia de pérdida de $K$ |
| Choque seguido de altura, frenado o resorte | TP 8.22–25; S1.2 y S3.2 | Sears ejemplo 8.8, p. 249 y problemas 8.78–8.79, pp. 268–269; conexiones propias con MAS |
| Canoa y velocidades relativas | TP 8.13 y 35; S5.3 | Sears problema 8.92, p. 270; desplazamiento del CM como elaboración propia |
| Colisión oblicua y explosiones | TP 8.27–32 | Sears §8.2–8.4; figuras y datos del TP, sin agregar masas iguales donde no se indican |

El libro `…265-300.pdf`, idéntico por SHA-256 a `Sist part libro.pdf`,
contiene **pp. impresas 237–272**, capítulo 8. La sección de cohetes §8.6
está en ese recorte; no se agrega al temario sólo por estar en el libro.

## Correcciones y comprobaciones adicionales

| Fuente / ubicación | Criterio comprobado |
| --- | --- |
| Presentación, diap. 3 | La forma para el sistema de partículas de masa total constante no habilita a tratar un sistema abierto con flujo de masa como una única partícula sin balance adicional |
| Diap. 5 | $F_{med}=J/\Delta t$ define la media temporal incluso si $F(t)$ varía; no requiere que la fuerza real sea constante |
| Diap. 22 | $e=-v_f/v_i$ sólo sirve para la componente normal contra un blanco que permanece en reposo; un segundo cuerpo inicialmente quieto puede adquirir velocidad y exige la expresión relativa |
| Diap. 24 | Lo que desaparece en el choque plástico ideal es $K_{rel}$; no toda la energía interna del sistema |
| Diap. 25–26 | La forma escalar de restitución entre velocidades completas es de 1D; los choques inelásticos también pueden ocurrir en 2D. En 2D, usar componentes y dirección de impacto |
| TP 8.13, PDF p. 2 / impresa 42 | $v_{tablón}=-45(1,5)/195=-0,346154$ m/s; $v_{persona}=1,153846$ m/s. El −0,356 m/s de la respuesta del tablón no satisface el balance |
| TP 8.16, PDF p. 4 / impresa 44 | Coincide literalmente con el problema 2 de F1. Con 3 kg a +4 m/s y 8 kg a −1,5 m/s: $P_i=0$, $K_i=33$ J. Unido: $V=0$, $\Delta K=-33$ J. Elástico: velocidades −4 y +1,5 m/s; $\Delta K=0$ |
| TP 8.19 y apoyo PDF p. 13 (rotulado 21) | $v_{camioneta}=20,933333$ m/s y $\Delta K=-8680$ J. Evitar usar 20,9 antes de calcular la energía; la diferencia no es un pequeño error de redondeo final |
| Apoyo PDF pp. 15–17, rotulado 27 / TP vigente 25 | El bloque de 5 kg rebota: $v_{1f}=-\sqrt{98}/3=-3,299832$ m/s. Su altura posterior es $5/9=0,555556$ m; elevar al cuadrado no corrige un sentido mal interpretado |

Las comprobaciones son propias, no un solucionario oficial. La
[auditoría anterior](../../parciales/auditoria-material.md#advertencias-de-los-apuntes-de-apoyo)
conserva las observaciones previas del apoyo de 17 páginas.
Para intentar enunciados, usar la [ruta sin resultados](../../parciales/Segundo_Parcial/practica.md).

[Inventario y límites de lectura](../../parciales/Segundo_Parcial/auditoria-fuentes.md).

[Volver al tema](README.md)

## Comparaciones didácticas

La tabla de [choques y etapas](conservacion-y-choques.md) es **elaboración
propia** que reutiliza diagramas existentes. Referencias registradas el
15/11: presentación diap. 6–9, 10–20, 22–26, TP 8.15–21, 22–25, 26
y S1.2/S3.2 como patrones históricos; Sears §8.2–8.5 es complemento.
No se volvieron a abrir los originales locales.
