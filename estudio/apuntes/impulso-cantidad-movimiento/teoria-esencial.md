# Impulso y cantidad de movimiento — teoría esencial

## 🎯 Qué recordar

- **Cantidad de movimiento:** $\vec p=m\vec v$. Es vectorial: el sentido cuenta.
- **Impulso:** efecto de una fuerza durante un intervalo; cambia $\vec p$.
- Para un sistema, sumar los momentos de sus partículas: $\vec P=\sum\vec p_j$.
  Las fuerzas internas se cancelan por pares en esa suma; pueden cambiar la
  velocidad de cada partícula, pero no el momento total por sí solas.
- **Conservación:** $\vec P_f=\vec P_i$ si el impulso externo es cero o
  despreciable durante el intervalo elegido. Puede conservarse sólo una componente.
- **Un choque no garantiza conservar energía cinética.** Un sistema puede
  conservar $\vec P$ mientras parte de $K$ pasa a deformación, calor o sonido.

## 🖼️ Esquema / dibujo

```text
SISTEMA = ambos cuerpos; +x hacia la derecha

ANTES                       INTERACCIÓN                       DESPUÉS
m1 → v1i   v2i ← m2       impulso externo ≈ 0              m1 v1f, m2 v2f
       Pi                 ─────────────────→                      Pf

¿Quedan unidos? → misma vf. ¿Elástico? → además Kf=Ki.
```

## 📐 Fórmula

Las relaciones siguientes se aplican en un marco inercial, al conjunto fijo
de partículas elegido como sistema.

| Necesito | Relación | Qué revisar |
| --- | --- | --- |
| Impulso neto de una partícula | $\vec J_{net}=\int\vec F_{net}\,dt=\Delta\vec p$ | Integrar todas las fuerzas relevantes |
| Fuerza media | $\vec F_{med}=\vec J/\Delta t$ | No es necesariamente la fuerza máxima |
| Balance del sistema | $\vec J_{ext}=\Delta\vec P$ | Identificar la frontera y el intervalo |
| Centro de masa | $\vec r_{CM}=\sum m_j\vec r_j/M$ | $M=\sum m_j$; promedio ponderado |
| Movimiento del CM | $\vec P=M\vec v_{CM}$; $\sum\vec F_{ext}=M\vec a_{CM}$ | Masa total constante |
| Velocidad respecto del CM | $\vec v'_j=\vec v_j-\vec v_{CM}$ | No mezclar referencias |
| Energía cinética del sistema | $K=\frac12Mv_{CM}^2+\sum\frac12m_jv_j'^2$ | Traslación del CM + movimiento relativo |

**Choques frontales en 1D**, con velocidades algebraicas y sin impulso externo
apreciable:

$$
m_1v_{1i}+m_2v_{2i}=m_1v_{1f}+m_2v_{2f},\qquad
e=-\frac{v_{1f}-v_{2f}}{v_{1i}-v_{2i}}.
$$

| Tipo | Segunda condición | Energía cinética |
| --- | --- | --- |
| Plástico / perfectamente inelástico | Quedan unidos: $v_{1f}=v_{2f}$, $e=0$ | Disminuye al desaparecer el movimiento relativo |
| Inelástico ordinario | $0<e<1$ | Disminuye |
| Elástico | $e=1$ o $K_i=K_f$ | Se conserva |

La energía total se conserva en todos los casos: cambia su forma. Una explosión
puede **aumentar** $K$ a costa de energía interna. En choques oblicuos, no aplicar
la relación 1D de $e$ a los módulos de las velocidades.

**Unidades:** $p,J$ en kg·m/s = N·s; energía en J. En estos apuntes $J$ sin
flecha representa el impulso en un eje; $\mathrm J$ como unidad significa joule.

## ⚠️ Error frecuente

- Sustituir velocidades por módulos cuando los cuerpos van en sentidos opuestos.
- Conservar el momento de **un solo cuerpo** durante el impacto con otro.
- Conservar momento en toda la bajada o el frenado porque se conserva en el choque.
- Confundir $K$ del CM con $K$ total: el movimiento relativo también aporta energía.
- Interpretar “energía perdida” como energía destruida: es disminución de $K$.

## 🔗 Ver también

- [Resolución por casos](resolucion-por-casos.md)
- [Trabajo y Energía](../trabajo-energia/README.md)
- [Fuentes](fuentes.md) · [Volver al tema](README.md)
