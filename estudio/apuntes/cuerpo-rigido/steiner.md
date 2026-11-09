# Ficha — teorema de Steiner

## 🎯 Qué recordar

El momento de inercia **cambia cuando cambia el eje**. Si ya conocemos la inercia de un cuerpo respecto de un eje que pasa por su **centro de masa**, Steiner permite encontrar la inercia respecto de **otro eje paralelo**.

Imaginá una regla uniforme: hacerla girar alrededor de su centro y hacerla girar alrededor de un extremo no requieren la misma respuesta al torque.

## 🖼️ Esquema / dibujo

    Regla uniforme (vista de frente)
    extremo A              CM             extremo B
        ⊙───────────────────⊙──────────────────┤
        ↑                   ↑
      eje A               eje CM
        |<---- d = ℓ/2 ---->|

Ambos símbolos ⊙ representan ejes **perpendiculares a la hoja** y paralelos entre sí; \(\ell\) es la longitud de la regla.

## 📐 Fórmula

$
I_A=I_{\mathrm{CM}}+Md^2
$

- \(I_{\mathrm{CM}}\): inercia respecto del eje paralelo por el centro de masa.
- \(M\): masa total del cuerpo.
- \(d\): separación perpendicular entre **los dos ejes**, no distancia a una partícula.
- Para una regla de longitud \(\ell\), del centro al extremo \(d=\ell/2\).

Steiner **no** sirve para ejes que cambian de orientación; el eje conocido debe pasar por el centro de masa.

## ⚠️ Error frecuente

Sumar \(Md^2\) a una inercia que no corresponde al eje por el centro de masa, o confundir \(d\) con el radio del objeto.

## 🔗 Ver también

- [Recorrido desde cero](desde-cero.md)
- [Momento de inercia](momento-de-inercia.md)
- [Teoría esencial, fórmulas y tabla de cuerpos](teoria-esencial.md#inercia-siempre-indicar-el-eje)
