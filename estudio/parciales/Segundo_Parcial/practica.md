# Segundo parcial — práctica priorizada

## Ruta de trabajo

1. Resolver la hoja sin fecha como diagnóstico de los tres temas.
2. Hacer TP 6: 19 y 22–23; TP 7: 5 y 13; TP 8: 6, 13, 22 y un choque oblicuo.
3. Resolver **S1 ej. 2 y S3 ej. 2** completos: son las cadenas más integradoras.
4. Completar S5 ej. 2–3, S6 ej. 2–3 y S7 completo.
5. Volver a S2 ej. 1 y S3 ej. 1 para límites de contacto y pérdidas porcentuales.

Usar los [IDs y enunciados](patrones.md). Orden sugerido, no predicción del examen.
Los problemas con rulo requieren Newton radial como herramienta auxiliar del
balance energético, sin agregar la rotación del cuerpo si se usa modelo de partícula.

## Antes de mirar resultados

- ¿Qué sistema elegí y dónde empieza/termina cada etapa?
- ¿El resorte está unido al bloque o sólo lo empuja?
- ¿Durante el choque puedo despreciar el impulso externo?
- ¿La masa que oscila es la del bloque o la suma después de pegarse?
- ¿La velocidad está dada respecto del suelo o de otro cuerpo?
- ¿Conservo momento, K, energía mecánica o ninguna de las tres?

## Diagnóstico listo para practicar

Original: [hoja sin fecha](enunciados/hoja-energia-mas-choques-sin-fecha.jpeg).
Las verificaciones siguientes son propias, no una resolución oficial.

### 1. Resorte que impulsa una pelota por una rampa lisa

Datos: m = 0,1 kg, k = 500 N/m, x = 0,20 m.
Modelo de partícula: sin roce ni energía de rotación; altura inicial cero.

$$\frac12kx^2=mgh_{max}\quad\Rightarrow\quad h_{max}=10{,}204\;\mathrm m.$$

El peso y el resorte realizan trabajo conservativo. La normal no realiza
trabajo sobre la partícula en una rampa fija ideal. La expresión da la
**ganancia de altura** desde el estado inicial, no una longitud por el plano.

### 2. Cambios en un sistema masa–resorte de período 2 s

Usar T = 2π√(m/k), ideal y lineal:

| Cambio | Nuevo período |
| --- | --- |
| Duplicar m | 2√2 = 2,828 s |
| Duplicar amplitud | 2 s |
| Duplicar k | 2/√2 = 1,414 s |
| Llevarlo a la Luna, con el mismo dispositivo ideal | 2 s; cambia el equilibrio vertical, no √(m/k) |

### 3. Choque con restitución

Eje positivo a la derecha. m1 = 1 kg, v1i = +2 m/s;
m2 = 5 kg, v2i = −1 m/s; e = 0,5.

$$v_{CM}=\frac{1(2)+5(-1)}6=-0{,}5\;\mathrm{m/s},$$
$$v_{2f}-v_{1f}=0{,}5[2-(-1)]=1{,}5\;\mathrm{m/s}.$$

Con momento conservado: **v1f = −1,75 m/s, v2f = −0,25 m/s**.
Ki = 4,50 J; Kf = 1,6875 J; ΔK = −2,8125 J.
KCM = ½(6)(0,5)² = 0,75 J, antes y después; vCM tampoco cambia.
Es inelástico, pero no perfectamente inelástico: no terminan unidos.

## Dos cadenas que conviene dominar

### S1, ej. 2 — la bala atraviesa el bloque

Tomar t = 0 justo después del impacto, x = 0 y V > 0 para el bloque.
Bloque M = 1 kg; bala mb = 0,05 kg; amplitud A = 0,05 m:

$$\omega=\sqrt{k/M},\quad V=A\omega,\quad
v_{b,salida}=v_{b,entrada}-\frac{MV}{m_b}.$$

El bloque oscila solo: la bala salió. Después:
$x=A\sin\omega t$, $v=A\omega\cos\omega t$, $a=-A\omega^2\sin\omega t$.
$J_{bloque}=MV$, $F_{med}=MV/0{,}01$; la variación de K de la bala se
calcula con sus propias velocidades. Comprobar que la salida siga siendo
físicamente compatible con «atraviesa» para los datos elegidos.

### S3, ej. 2 — los bloques quedan unidos

$$u=\sqrt{2gh},\quad V=\frac{m_1u}{m_1+m_2},\quad
\omega=\sqrt{\frac{k}{m_1+m_2}},\quad A=V/\omega.$$

Durante el choque usar momento, no energía mecánica. Después oscila
M = m1 + m2. Si t = 0 es el primer contacto con el resorte relajado y V > 0,
usar la misma forma seno. En x = A/2: U = E/4 y K = 3E/4.
El impulso sobre cada bloque es mi(vif − vii), igual y opuesto si el
impulso externo es despreciable.

## Controles breves para otras variantes

- **S5 canoa:** la persona recorre 3 m respecto de la canoa. Con masa M
  de persona, Δxcanoa = −3M/(60 + M) m. No son 3 m respecto de la costa.
- **S7 choque elástico:** m2 = m1/2 y v2f = 16 cm/s; convertir unidades
  de forma consistente y verificar K antes/después.
- **S7 péndulo:** desde un extremo hasta rapidez máxima tarda T/4;
  para 3,5° o 1,75°, el resultado es el mismo dentro de la aproximación pequeña.
- **Foto del martinete:** con peso 10000 N, caída 3 m y penetración 0,08 m:
  R = 10000(3 + 0,08)/0,08 = **385000 N**. Es distinto del TP 6 ej. 12,
  que usa peso 9800 N. Durante la penetración también trabaja el peso.

## Errores del material de contraste

La [resolución manuscrita de S1](contraste/2020-09-16-M11-manuscrita-no-validada.pdf)
no debe copiarse como solución validada: en pág. 2 usa v²cima = v²base + 4gR.
Corresponde **v²cima = v²base − 4gR**; por tanto la normal de esa página
tampoco queda validada. La parte bala–resorte es útil como estructura,
pero conviene conservar ω = √(k/M), con sus unidades, hasta el final.

## Registro de práctica

| Ejercicio | Planteo propio | Resultado y unidades | Error / repetir |
| --- | --- | --- | --- |
| Hoja sin fecha, 1–3 | Pendiente | Pendiente | — |
| S1 ej. 2 | Pendiente | Pendiente | — |
| S3 ej. 2 | Pendiente | Pendiente | — |
| S5 ej. 2–3 | Pendiente | Pendiente | — |
| S7 | Pendiente | Pendiente | — |

[Patrones y fuentes](patrones.md) · [Volver](README.md)
