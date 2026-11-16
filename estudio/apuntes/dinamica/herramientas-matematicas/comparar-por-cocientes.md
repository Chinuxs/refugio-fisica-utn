# Comparar estados mediante cocientes

## 🎯 Qué recordar

Si una magnitud depende de varias variables y sólo conocemos cuánto
cambian, podemos comparar la misma ley en dos configuraciones compatibles,
sin calcular los valores absolutos individuales.

## 🖼️ Esquema / dibujo

~~~text
estado 1: T₁ = 2π √(m₁/k₁)      estado 2: T₂ = 2π √(m₂/k₂)
              │                               │
              └──── dividir T₂ / T₁ ──────────┘
                       factores relativos
~~~

## 📐 Fórmula

Para masa–resorte ideal, $m_i,k_i>0$:

$$
\frac{T_2}{T_1}=\frac{2\pi\sqrt{m_2/k_2}}{2\pi\sqrt{m_1/k_1}}
=\sqrt{\frac{m_2}{m_1}\frac{k_1}{k_2}}.
$$

**Ejemplo propio:** $m_2=9m_1$ y $k_2=4k_1$. Entonces
$T_2/T_1=\sqrt{9/4}=1{,}5$, aumenta 50 %. También se puede reconocer
la expresión original: $T_2=2\pi\sqrt{9m_1/(4k_1)}
=\tfrac32(2\pi\sqrt{m_1/k_1})=\tfrac32T_1$.

Para el péndulo de ángulos pequeños,
$T_2/T_1=\sqrt{(L_2/L_1)(g_1/g_2)}$. Si sólo $L$ se multiplica por
nueve, el período se triplica. $f_2/f_1=T_1/T_2$.

También sirve en energía cinética: con masa constante y $v_1\ne0$,
$K_2/K_1=(v_2/v_1)^2$. Un cociente no da valores absolutos por sí solo.

## ⚠️ Error frecuente

- Dividir por cero, cancelar sumandos o invertir factores.
- Olvidar raíces y potencias, o comparar leyes de modelos incompatibles.
- Mezclar unidades: los cocientes de magnitudes del mismo tipo son adimensionales.

## 🔗 Ver también

- [Dividir ecuaciones para eliminar incógnitas](../metodos/dividir-ecuaciones.md)
- [Comparar osciladores](../../movimiento-armonico-simple/comparar-osciladores.md)
- [Balances y pérdidas porcentuales](../../trabajo-energia/balances-y-tramos.md)

Ejemplos y deducciones propios, no ejercicios de cátedra.
