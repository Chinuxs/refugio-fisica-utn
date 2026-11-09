# Ficha — energía cinética rotacional

## 🎯 Qué recordar

Un cuerpo que gira tiene energía porque **sus partículas se mueven**. En una rotación rígida alrededor de un eje fijo, las partículas tienen la misma velocidad angular \(\omega\), pero distinta rapidez lineal según qué tan lejos están del eje.

Si el cuerpo también traslada su centro de masa, hay que contar la energía **de traslación más la de rotación respecto del centro de masa**.

## 🖼️ Esquema / dibujo

    ● masa 1 ────── ⊙ eje ───────── ● masa 2
       r₁                              r₂
       Ambas giran con la misma ω.
       Las rapideces son |ω|r₁ y |ω|r₂.

Es un ejemplo esquemático de partículas unidas rígidamente, no un ejercicio de cátedra.

## 📐 Fórmula

Partimos de la energía cinética de cada partícula y usamos \(v_i=r_{\perp i}|\omega|\):

$
K=\sum_i \frac12 m_i v_i^2
=\frac12\left(\sum_i m_i r_{\perp i}^2\right)\omega^2
=\frac12 I\omega^2
$

Para un cuerpo rígido en movimiento plano general:

$
K=\frac12 Mv_{\mathrm{CM}}^2+\frac12 I_{\mathrm{CM}}\omega^2.
$

\(I\) se refiere al eje fijo de la primera expresión. Un disco cuyo centro permanece fijo no tiene energía de traslación de su centro. Unidad: **J**.

## ⚠️ Error frecuente

Contar dos veces una contribución energética o suponer que la energía cinética se conserva en toda situación donde se conserva el momento angular. Las pesas que se acercan al eje pueden requerir **trabajo interno**.

## 🔗 Ver también

- [Recorrido desde cero](desde-cero.md)
- [Momento de inercia](momento-de-inercia.md)
- [Momento angular y conservación](momento-angular.md)
- [Trabajo y energía en teoría esencial](teoria-esencial.md#trabajo-y-energía)
