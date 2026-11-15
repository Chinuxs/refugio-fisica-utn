# Segundo parcial — comprobaciones (revela resultados)

**Abrir después del intento propio o si se pide expresamente una resolución.**
Los controles son elaboración propia; no son un solucionario oficial.
Se conservan aquí los cálculos que antes aparecían en `practica.md`.

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

## F1 — hoja llamada Parcial_2025_1.png

Se verificó la coincidencia con TP 6.19 y TP 8.16. El año del nombre del
archivo no está confirmado por la imagen.

- **Problema 1:** $W_r=\tfrac12(2250)(0,30)^2-10(9,8)(3)=-192,75$ J.
  La energía mecánica disipada es **192,75 J**; el trabajo es negativo.
- **Problema 2:** derecha positiva, $m_1=3$ kg, $v_{1i}=4$ m/s,
  $m_2=8$ kg, $v_{2i}=-1,5$ m/s. $P_i=0$ y $K_i=33$ J.
  Si quedan unidos: $V=0$ y $\Delta K=-33$ J.
  Si el choque es elástico: $v_{1f}=-4$ m/s, $v_{2f}=1,5$ m/s,
  $K_f=33$ J y $\Delta K=0$.
  En ambos casos $v_{CM}=0$. En el caso elástico cada cuerpo puede
  cambiar su velocidad aunque el momento total sea cero.

## H1 — enunciado visible junto a la resolución manuscrita

Fuente externa: `8.2do Parcialito/Parcial_2025_2.png`. No es un examen
completo adicional. Se reconstruye sólo el problema impreso visible:
masa 1 kg, resorte 2000 N/m comprimido 0,30 m, zona horizontal rugosa
y llegada en reposo a 1 m de altura por un plano liso. El inciso e)
pide la rapidez en el plano a 0,50 m de altura.

Con altura inicial cero y modelo de partícula, $E_i=90$ J y $E_f=9,8$ J.
Por tanto **$W_{nc}=-80,2$ J**, mientras la disipación es 80,2 J.
El trabajo del resorte durante su relajación es **+90 J**.
No sumarlo nuevamente si se usa $U_e$ en el balance.

En el plano liso, a 0,50 m de altura: $U_g=4,9$ J y $K=4,9$ J;
la rapidez es **$\sqrt{9,8}=3,1305$ m/s**.
El manuscrito usa el rótulo «trabajo neto» para un balance de energía
mecánica. Hay que distinguirlo del trabajo neto de todas las fuerzas:
como parte y termina en reposo, ese trabajo neto total es **cero**.
El enunciado no permite hallar el coeficiente de roce sin la longitud rugosa.

[Volver a la práctica sin resultados](practica.md) · [Preguntas teóricas](preguntas-teoricas.md)
