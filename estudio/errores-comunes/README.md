# Errores frecuentes

Este registro reúne confusiones que conviene detectar durante la resolución de
problemas y la preparación de evaluaciones.

## Cinemática

- Confundir trayectoria con desplazamiento.
- Pensar que velocidad cero implica aceleración cero.
- Mezclar la descripción cinemática con las causas dinámicas.
- Confundir velocidad con rapidez.

## Dinámica

- Dibujar una fuerza centrípeta adicional.
- No elegir ejes convenientes.
- No descomponer correctamente las fuerzas.
- Aplicar fórmulas antes de construir el diagrama de cuerpo libre.
- Confundir una fuerza individual con la fuerza resultante.

## Movimiento Circular

- Pensar que rapidez constante implica aceleración nula.
- Confundir velocidad angular con velocidad tangencial.
- Usar el valor en rpm como si estuviera en rad/s. Ver
  [significado del dato y conversión rápida](../apuntes/movimiento-circular/Movimiento_Circular_UTN_FRLP.md#velocidad-angular-frecuencia-y-período).
- No identificar la dirección radial.
- Usar `mv²/r` como una fuerza extra y no como la resultante radial.
- No analizar por separado las direcciones radial y tangencial.

## Cuerpo Rígido y Rotación

- **Usar cualquier distancia como brazo de palanca:** el torque depende
  de la distancia **perpendicular a la línea de acción** de la fuerza;
  también importan signo y eje. [Ficha de torque](../apuntes/cuerpo-rigido/torque.md).
- **Confundir equilibrio de torques con ausencia de fuerzas:** torques
  opuestos pueden cancelarse; para equilibrio estático hay que revisar
  también la resultante de fuerzas.
- **Tratar la inercia como una propiedad independiente del eje:**
  medir todas las distancias al mismo eje y recordar que cada aporte
  depende de \(r_\perp^2\). Un aro y un disco de igual M y R no tienen
  la misma I. [Ficha de inercia](../apuntes/cuerpo-rigido/momento-de-inercia.md).
- **Aplicar Steiner a ejes no paralelos** o partir de una inercia cuyo
  eje no pasa por el centro de masa. [Ficha de Steiner](../apuntes/cuerpo-rigido/steiner.md).
- **Omitir la energía de rotación** de una pieza que gira, o sumar
  energía de traslación del centro de masa cuando está fijo.
  [Ficha de energía](../apuntes/cuerpo-rigido/energia-rotacional.md).
- **Convertir rpm como si fueran rad/s:** una vuelta son \(2\pi\)
  radianes y un minuto, 60 segundos. [Conversión en la guía desde cero](../apuntes/cuerpo-rigido/desde-cero.md#conversión-breve-para-no-mezclar-unidades).
- **Conservar el momento angular del objeto equivocado** o suponer que
  conservar momento angular implica conservar energía cinética. Para
  plataformas con masas móviles, elegir el **sistema completo** y
  examinar el torque externo respecto del eje.
  [Ficha de momento angular](../apuntes/cuerpo-rigido/momento-angular.md).

Para practicar sin mirar respuestas: [pistas graduales del TP 9](../apuntes/cuerpo-rigido/pistas-tp9.md).

