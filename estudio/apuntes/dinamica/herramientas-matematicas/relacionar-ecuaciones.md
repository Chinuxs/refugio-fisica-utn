# Relacionar ecuaciones, despejar y comparar resultados

## 🎯 Qué recordar

Cuando el **planteo físico ya está construido**, resolver las incógnitas es
un problema de álgebra: conservar los factores, elegir una operación
justificada y sustituir al final en las **ecuaciones originales**.
No es una fórmula nueva de Física.

## 🖼️ Esquema / dibujo

~~~text
Ecuación (1) y ecuación (2)
        │
        ├── ¿una incógnita despejada? → sustituir
        ├── ¿mismo factor no nulo?    → dividir (si conviene)
        └── ¿términos opuestos?       → sumar/restar
                     ↓
       factor común → despeje → comprobar ambas
                     ↓
       redondear al informar el resultado
~~~

## 📐 Fórmula

### Sustitución y factor común, sin perder términos

**Ejemplo algebraico propio**, con $u,a,b$ en m/s y coeficientes sin
unidad. No representa el enunciado de un choque:

$$
u=3a+2b\quad (1),\qquad 0=4a-5b\quad (2).
$$

De (2) se obtiene $b=4a/5$; se sustituye la **expresión completa**
en (1):

$$
u=3a+2\left(\frac{4a}{5}\right)
=a\left(3+\frac85\right)
=\frac{23}{5}a.
$$

Por tanto $a=5u/23$ y $b=4u/23$. **Comprobación:**
$3(5u/23)+2(4u/23)=u$ y $4(5u/23)-5(4u/23)=0$.
No se puede cancelar $a$ en una suma sin factorizar primero.

### Cuadrados, raíces y signos

Si $v^2=c^2$, las posibilidades algebraicas son $v=\pm|c|$;
el **módulo de una rapidez** es no negativo, pero una componente de
velocidad puede ser positiva o negativa. Usar el dibujo y el sentido
físico para seleccionar el signo, no decidirlo antes de plantear.

En un choque oblicuo: escribir las componentes **con sus signos** y
guardar $\sin\alpha$, $\cos\alpha$ y raíces en forma exacta hasta el
último paso posible. Aproximar antes puede arruinar una resta de
energías, que depende de cuadrados de velocidades.

### Fracción y porcentaje: parte / referencia

Para una disminución de energía cinética del sistema:

$$
\Delta K=K_f-K_i,\qquad
D_K=K_i-K_f=-\Delta K.
$$

Si $K_i>0$, la **fracción de disminución** respecto de la energía
cinética inicial es $D_K/K_i$ y el **porcentaje** es esa fracción
multiplicada por $100\,\%$. No memorizar una «ley de disipación»:
sólo se compara una **parte** con el **total tomado como referencia**.

**Ejemplo propio:** si $K_i=10$ J y $K_f=7$ J,
$\Delta K=-3$ J; la disminución es $3$ J;
la fracción es $3/10=0{,}30$ y el porcentaje **30 %**.
Si $K_i=0$, esa fracción respecto del estado inicial no está definida.
Para un choque pasivo ordinario, esperar $0\leq K_f\leq K_i$;
si no se cumple, revisar hipótesis antes de llamarlo «energía disipada».

**Redondeo:** mantener cifras intermedias y aplicar las cifras
significativas al resultado comunicado; no inventar precisión cuando
la fuente no declara tolerancia o método de medición.

## ⚠️ Error frecuente

- Sustituir $b=4a/5$ como si fuera $4/5$, perdiendo $a$.
- Borrar una letra de una suma en vez de factorizar.
- Elegir sólo la raíz positiva para una **componente** de velocidad.
- Usar $K_f-K_i$ como si fuera una pérdida positiva.
- Redondear senos, cosenos o velocidades antes de comprobar las ecuaciones.

## 🔗 Ver también

- [Descomposición de vectores](descomponer-fuerza-inclinada.md)
- [División de ecuaciones y cancelación](../metodos/dividir-ecuaciones.md)
- [Comparar estados por cocientes](comparar-por-cocientes.md)
- [Verificar resultados](../metodos/verificar-resultado.md)
- [Choques oblicuos](../../impulso-cantidad-movimiento/choques-oblicuos.md)

**Procedencia:** ejercicios algebraicos inventados para enseñar el método.
