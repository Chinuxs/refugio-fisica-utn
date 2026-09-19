# MAS — teoría esencial

## 🎯 Qué recordar

- **Periódico:** se repite cada $T$. **Oscilatorio:** va y vuelve alrededor de
  un equilibrio. Es **MAS** si la fuerza neta es proporcional y opuesta al
  desplazamiento desde ese equilibrio: $F_x=-kx$.
- $x$: elongación; $A$: máximo valor de $|x|$; $T$: período; $f$: ciclos por
  segundo; $\omega$: frecuencia angular; $\varphi_0$: fase inicial.
- Modelo ideal: resorte de masa despreciable, régimen de Hooke, masa constante
  y sin amortiguamiento ni fuerza impulsora. $T$ no depende de $A$ en ese modelo.
- En un resorte vertical, el peso desplaza el equilibrio. **$x=0$ se fija en el
  equilibrio con la masa colocada**, no en la longitud natural.

## 🖼️ Esquema / dibujo

```text
extremo izquierdo          equilibrio             extremo derecho
     −A                        0                         +A
     v=0                    |v| máximo                   v=0
     a hacia →                 a=0                  ← a hacia
     U máximo               K máximo                U máximo

De un extremo al equilibrio: T/4. De −A a +A: T/2.
```

## 📐 Fórmula

Se usa la convención de la presentación: **$x(t)=A\sin(\omega t+\varphi_0)$**.
También puede usarse coseno, ajustando la fase y las derivadas.

| Necesito | Relación |
| --- | --- |
| Frecuencia y período | $\omega=\sqrt{k/m}=2\pi f=2\pi/T$ |
| Velocidad y aceleración | $v=A\omega\cos(\omega t+\varphi_0)$; $a=-\omega^2x$ |
| Valores máximos en módulo | $v_{\max}=\omega A$; $a_{\max}=\omega^2A$ |
| Velocidad en una posición | $v=\pm\omega\sqrt{A^2-x^2}$; signo según sentido |
| Amplitud desde el estado inicial | $A=\sqrt{x_0^2+(v_0/\omega)^2}$ |
| Energía del oscilador | $E=\frac12kA^2$; $U=\frac12kx^2$; $K=\frac12k(A^2-x^2)$ |

Para el resorte vertical, ese $U$ es el potencial **total efectivo** referido al
equilibrio (elástico + gravitatorio, salvo una constante). La energía elástica
sola usa la deformación desde la longitud natural.

**Péndulo simple:** masa puntual, cuerda inextensible y sin masa, sin roce.
Para ángulos pequeños, $\sin\theta\simeq\theta$ en radianes:

$$
\omega=\sqrt{g/L},\qquad T=2\pi\sqrt{L/g},\qquad
\theta(t)=\theta_{\max}\sin(\omega t+\varphi_0).
$$

La presentación usa aproximadamente $|\theta|<15^\circ$; es una aproximación,
mejor cuanto menor sea el ángulo. $T$ no depende de la masa. El arco es $s=L\theta$.

**Amortiguado / forzado:** si aparece $-bv$ o una fuerza externa periódica,
la ecuación pasa a $m\ddot x+b\dot x+kx=F_0\sin(\Omega t)$.
Con amortiguamiento libre disminuyen amplitud y energía; en respuesta forzada
estacionaria se oscila a $\Omega$. Con poco amortiguamiento, la respuesta es
grande cerca de la frecuencia natural (resonancia).

**Unidades:** $A,x,L$ en m; $T$ en s; $f$ en Hz; $\omega$ en rad/s; fases en rad.

## ⚠️ Error frecuente

- En los extremos, $v=0$ pero $|a|$ es máximo; en el centro sucede lo contrario.
- $A$ es la mitad del recorrido entre extremos. Una carrera de 10 cm da $A=5$ cm.
- $\arcsin(x/A)$ da una rama: para elegir la fase también hace falta el signo de $v$.
- En péndulos, $a_t=-g\sin\theta$; además hay aceleración radial $v^2/L$.
  En el punto más bajo $a_t=0$, pero la aceleración total puede no ser cero.

## 🔗 Ver también

- [Resolución por casos](resolucion-por-casos.md)
- [Trabajo y Energía](../trabajo-energia/README.md)
- [Fuentes](fuentes.md) · [Volver al tema](README.md)
