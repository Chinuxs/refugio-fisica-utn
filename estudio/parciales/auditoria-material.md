# Auditoría del material de segundo y tercer parcial

Revisión del **5 de noviembre de 2026**. Fuentes externas:
`E:\UTN\Fisica I\8.2do Parcialito` y `E:\UTN\Fisica I\12. 3er Parcialito`.
Los originales externos no se modificaron ni eliminaron. Sólo se copiaron
enunciados seleccionados y una resolución de contraste al repositorio.

## Qué se verificó y hasta dónde

| Material | Resultado / alcance de revisión |
| --- | --- |
| Inventario de ambas carpetas | **39 archivos**, tamaños y SHA-256 registrados en [CSV](inventario-material.csv) |
| Siete exámenes PDF del segundo | Texto completo revisado y figuras relevantes contrastadas visualmente; catalogados por ejercicio y alcance |
| Dos fotos de WhatsApp y foto `Examen fisica.jpg` | Lectura visual; una hoja se descarta de la práctica prioritaria por ser de primer parcial; las otras dos son auxiliares, sin inflar el recuento de PDF |
| Cuatro fotos `2.jpg`, `3.jpg`, `4.jpg`, `7.jpg` | Son formularios/apuntes, no exámenes. Se revisaron visualmente y se detectaron errores; no se usan como patrón ni como fuente normativa |
| `2P 1F Resolución.pdf` | Cuatro páginas manuscritas revisadas; error de signo en la subida al rulo. Se conserva como contraste no validado, no como examen adicional |
| Tres imágenes del tercero | Lectura visual completa, identificación de fecha/comisión y separación de contenido actual/excluido; T1/T2 son variantes cercanas |
| Seis archivos idénticos a fuentes previas | Igualdad **binaria SHA-256** comprobada; se reutilizan los apuntes existentes |
| PDF `N°7 MAS/Ejerc.pdf`, 19 páginas | Texto completo revisado; varios errores de fase, datos copiados y péndulo. No usar resultados sin comprobar |
| PDF `N°8…/ACFr…pdf`, 17 páginas | Texto completo revisado; útil para pasos de sistemas de partículas, con advertencias de signos, redondeo y numeración |
| Otros PDF de apoyo | Identificados como libros o presentaciones de temas ya cubiertos; no cuentan como evaluaciones adicionales ni se certifican todos sus resultados |
| Dos RAR | Se listaron sus miembros: contienen la colección expandida y el paquete MAS respectivamente. **No se certificó equivalencia byte por byte de cada miembro ni integridad por extracción completa** |
| Seis MP4 | Inventariados y calculado su hash; **no reproducidos ni transcritos**, por lo que su contenido no se declara validado |
| Dos `.ppt` antiguos y un `.doc` | Inventariados; la lectura con Office falló. **Contenido pendiente de revisión**, sin usarlos para frecuencias ni conclusiones |

La validación de planteos y controles numéricos está documentada en las guías;
no equivale a resolver todos los incisos de cada examen con cada combinación
de sus datos personalizados.

## Duplicados exactos confirmados

Respecto de las carpetas de teoría/TP ya usadas en el proyecto:

| Archivo en la carpeta del segundo | Fuente previa idéntica |
| --- | --- |
| `06 Trabajo y Energía.pptx` | Presentación de `6. Trabajo & Energia/…20260815/` |
| `08 Modelo Sistemas de Partículas.pptx` | Presentación de `8. Modelo sistema de partículas/…20260905/` |
| `Trabajo y energia libro.pdf` | Sears `…200-230.pdf` de Trabajo y Energía |
| `Sist part libro.pdf` | Sears `…265-300.pdf` de Sistemas de Partículas |
| `Movimiento armónico simple/07 Movimiento Oscilatorio (juan).pptx` | Presentación de `7. MAS/…20260919/` |
| `Movimiento armónico simple/Sears…461-495.pdf` | Mismo recorte de Sears de la carpeta MAS |

Los RAR son **candidatos a almacenamiento redundante**, no archivos
certificados como eliminables. T1 y T2 no son duplicados exactos: cambian
los datos y la comisión, aunque comparten la estructura.

## Advertencias de los apuntes de apoyo

- `2.jpg`: si x = A cos(ωt + φ), entonces **v = −Aω sen(ωt + φ)**.
  La foto omite el signo negativo. No mezclar esa convención con la seno.
- `4.jpg`: **K = ½mv²**, no ½m(Δv)². El teorema trabajo–energía usa
  trabajo **neto de todas las fuerzas**, no sólo de fuerzas no conservativas.
- `7.jpg`: conservar momento requiere impulso externo despreciable;
  no es una regla incondicional de «todos los choques».
- `Ejerc.pdf` MAS, pág. 3: x = 0,1 sen(20t + π/2) no parte del equilibrio
  en t = 0. Para cruce hacia +x usar fase cero; ω = 20 rad/s sí es correcto.
- Mismo PDF, págs. 5–9: aparecen 0,4 Hz frente a 4 Hz, 5 kg frente a
  0,5 kg y una página con cuentas copiadas del ejercicio anterior.
  Conservar los datos del enunciado y revisar unidades; el período se mide en s.
- Mismo PDF, pág. 12: para péndulo de T0 = 3 s, L0 = 2,234 m,
  T1 = 3√1,6 = **3,795 s**, T2 = 3√0,4 = **1,897 s**.
  Los 6,6 y 3,3 s impresos no corresponden al enunciado.
- Mismo PDF, pág. 17: 0,28 m es la proyección horizontal para la altura
  dada; no es exactamente el arco. θ = arccos(0,96) = 0,2838 rad;
  para arco usar s = Lθ.
- PDF de Sistemas de Partículas, pág. 13: la camioneta da
  v = **20,9333 m/s**, ΔK = **−8680 J** sin redondear antes de tiempo.
  Los valores 20,9 y −14955 J impresos no verifican exactamente el balance.
- Mismo PDF, págs. 15–17: con masas 5 y 10 kg y choque elástico, el
  bloque ligero **rebota**, v1f ≈ **−3,30 m/s**. La altura ≈ 0,556 m
  sale al elevar al cuadrado, pero eso no elimina el error de sentido.
  La numeración de estos ejercicios no siempre coincide con el TP vigente.
- La resolución manuscrita de S1, pág. 2, suma energía al subir:
  reemplazar por v²cima = v²base − 4gR. No aceptar la tabla de normales derivada.

## Reproducir el inventario

Desde la raíz del proyecto:

```powershell
py herramientas/auditar_material_parciales.py 'E:\UTN\Fisica I' 'estudio/parciales/inventario-material.csv'
```

El CSV registra archivos físicos, no cada miembro de los RAR. Los hashes
verifican igualdad de bytes, **no corrección conceptual**. El script sólo lee
las fuentes y escribe el CSV de salida; no elimina duplicados.

[Segundo parcial](Segundo_Parcial/README.md) · [Tercer parcial](Tercer_Parcial/README.md)
