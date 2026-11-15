# Segundo parcial — auditoría de fuentes

**15 de noviembre de 2026.** Revisión de estas cuatro carpetas externas,
sin modificar ni eliminar sus originales:

- `E:\UTN\Fisica I\8.2do Parcialito`
- `E:\UTN\Fisica I\6. Trabajo & Energia`
- `E:\UTN\Fisica I\7. MAS`
- `E:\UTN\Fisica I\8. Modelo sistema de partículas`

## Resultado del inventario

**64 archivos físicos, 49 contenidos binarios distintos y 15 copias exactas**
respecto de archivos registrados antes en este mismo inventario. El CSV
[inventario-fuentes.csv](inventario-fuentes.csv) conserva ruta relativa a
`E:\UTN\Fisica I`, tamaño, SHA-256, tipo y coincidencias binarias.
Hay 37 archivos en la carpeta del parcial y 27 en las otras tres carpetas.

Los conteos de evaluaciones son independientes del conteo de archivos:

- **Siete PDF fechados, con 17 problemas**, forman la muestra histórica S1–S7.
- `Parcial_2025_1.png` es F1: una hoja con dos problemas y teoría, sin
  encabezado que confirme año o comisión.
- `Parcial_2025_2.png` es H1: resolución manuscrita con un enunciado impreso
  visible; no otro parcial completo. Se registra el original externo y
  se documenta el problema sin copiar sus datos personales al texto.
- Las fotos auxiliares y las resoluciones no aumentan el denominador de los
  siete exámenes fechados. Los formularios tampoco son evaluaciones.

## Qué se leyó y con qué límite

| Material | Revisión realizada |
| --- | --- |
| Presentaciones actuales de TyE, MAS y Sistemas de Partículas | Texto de **28 + 21 + 27 = 76 diapositivas**, ecuaciones y figuras relevantes; contraste visual de fórmulas con errores o ambigüedades |
| TP 6, 7 y 8 actuales | Texto de **29 + 26 + 36 = 91 ejercicios**, figuras necesarias y comprobaciones seleccionadas; no un solucionario íntegro de los 91 |
| Siete PDF históricos y nueve imágenes de la carpeta del parcial | Lectura de enunciados, fechas visibles, teoría, apuntes y figuras; identificación de recorte y problemas con datos ambiguos |
| `2P 1F Resolución.pdf` | Cuatro páginas manuscritas; se mantiene la advertencia de signo al subir al rulo |
| Cinco PDF `TP6Ej…` y `Trabajo práctico 6.pdf` | Lectura de los desarrollos; contraste de signos, estados y cuentas. Se detectó mezcla de C con máxima compresión y confusión entre $v$ y $v^2$ |
| Apoyos MAS de 19 páginas y Sistemas de Partículas de 17 | Lectura textual y revisión de los planteos relevantes; se conservan y amplían las erratas de la auditoría anterior |
| `Ejercicios de MAS.ppt` y `Resumen clase 12.ppt` | **36 y 32 diapositivas**: archivos abiertos en PowerPoint para extraer y revisar texto, fórmulas y gráficos; dejan de estar pendientes como en la revisión anterior |
| `Ejercitación de cinemática circular.doc` | Texto recuperado con Word: dos problemas de cinemática circular. No se certifica toda su representación gráfica ni se trata como MAS |
| PPSX de MAS y `Presentación.pdf` | Texto del PPSX cotejado con el PPTX; PDF identificado como presentación con fórmulas/gráficos en imágenes. No son exámenes adicionales |
| Tres recortes de Sears, **102 páginas en total** | Extracción de texto y mapa de páginas; contraste focalizado de secciones conceptuales y ejemplos pertinentes. No se resolvió ni verificó cada ejercicio del banco bibliográfico |
| `N°7 MAS.rar` | Prueba de integridad, extracción temporal y comparación SHA-256: sus **siete archivos coinciden exactamente** con la carpeta MAS expandida |
| Seis videos distintos, doce copias físicas | Hash y duración verificados; total **3 h 48 min 59 s**. **No se reprodujeron ni transcribieron íntegramente**; no se les atribuyen afirmaciones orales nuevas |
| `07 Movimiento Oscilatorio.one` | Se intentó abrir una copia temporal con la API de OneNote; devolvió una sección sin páginas accesibles. **Contenido no recuperado ni validado**; no se interpreta como documento vacío |
| `Links.txt` | Dos referencias externas: Classroom y YouTube. Registradas como enlaces; su contenido remoto no se revisó |

Esta revisión amplía la [auditoría del 5 de noviembre](../auditoria-material.md).
No equivale a haber visto todas las clases en video ni a haber certificado
todas las respuestas de las fuentes.

## Duplicados y equivalencias

| Grupo | Evidencia y uso |
| --- | --- |
| Presentaciones actuales y sus copias en la carpeta del parcial | Tres pares idénticos por SHA-256; una fuente primaria por tema |
| Recortes de Sears y copias renombradas del parcial | Tres pares idénticos por SHA-256; se identifican por capítulo y páginas impresas |
| TP actuales y copias en `2022/` o raíz del tema | Tres pares idénticos por SHA-256; se mantiene la numeración vigente |
| Seis MP4 repetidos entre las carpetas del parcial y de los temas | Seis pares idénticos por SHA-256; no se cuentan doce clases distintas |
| PPSX MAS / PPTX actual | Texto extraído por diapositiva idéntico; archivos binarios diferentes |
| `Trabajo práctico 7.pdf` / `Ejerc.pdf` | Texto extraído por página idéntico; archivos binarios diferentes |
| RAR MAS / carpeta expandida | Siete miembros comparados byte a byte por hash después de extracción; el RAR sigue conservado |

La igualdad de texto no certifica igualdad de imágenes, formato ni archivos
incrustados. La igualdad de bytes no certifica corrección física.

## Hallazgos que cambian el estudio

1. **F1 reutiliza ejercicios del TP:** su problema 1 coincide con TP 6.19
   y su problema 2 con TP 8.16. Se añade práctica directa sin presentarla
   como una predicción del examen siguiente.
2. **Hay evidencia de teoría explícita:** F1 y la foto del martinete incluyen
   preguntas conceptuales. Se seleccionan las del alcance actual y se indica
   qué preguntas corresponden a otro tema.
3. **Hay que separar etapas:** bala que atraviesa, cuerpos que se unen y
   cambio de equilibrio vertical no generan el mismo oscilador.
4. **Las resoluciones no son una autoridad automática:** errores de fase,
   frecuencia, signos o redondeo pueden sobrevivir aunque un resultado final
   parezca razonable. Los detalles están en las fuentes de cada tema.

| Tema | Procedencias, erratas y controles |
| --- | --- |
| Trabajo y Energía | [Fuentes](../../apuntes/trabajo-energia/fuentes.md) |
| MAS | [Fuentes](../../apuntes/movimiento-armonico-simple/fuentes.md) |
| Impulso / Sistemas de Partículas | [Fuentes](../../apuntes/impulso-cantidad-movimiento/fuentes.md) |

## Reproducir el inventario

Desde la raíz del repositorio:

```powershell
py herramientas/auditar_material_parciales.py 'E:\UTN\Fisica I' 'estudio/parciales/Segundo_Parcial/inventario-fuentes.csv' --segundo-completo
```

El comando sólo lee fuentes y escribe el CSV. Los archivos temporales de
extracción y las exportaciones de Office no forman parte del repositorio.
Si aparecen nuevas fuentes, actualizar el inventario y el alcance de lectura.

[Patrones](patrones.md) · [Práctica](practica.md) · [Volver al segundo parcial](README.md)
