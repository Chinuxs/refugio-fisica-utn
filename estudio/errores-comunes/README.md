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

## Método transversal

- Elegir conservación sin **sistema, intervalo ni condiciones** de aplicación.
- Perder factores en sustituciones; no volver a comprobar las ecuaciones.
- Memorizar una fracción de energía sin ver **parte / referencia**.

[Del fenómeno a las ecuaciones](../apuntes/metodo-del-fenomeno-al-planteo.md) ·
[Álgebra y porcentajes](../apuntes/dinamica/herramientas-matematicas/relacionar-ecuaciones.md).

## Trabajo y Energía

- **Contar dos veces el peso o el resorte:** si se incluyeron como potencial,
  su trabajo no vuelve a sumarse en el mismo balance.
- **Confundir trabajo, variación y disipación:** el trabajo del roce cinético
  sobre una superficie fija es negativo; la energía disipada se informa positiva.
- **Perder rapidez y perder energía en el mismo porcentaje:** $K$ depende
  del cuadrado de la rapidez, con la misma masa.
- **Extender el roce a toda la pista:** usar sólo el tramo y el recorrido
  indicados; un intento que termina dentro de la zona no es un cruce completo.
- **Confundir compresión máxima y proceso:** es un estado con $v=0$;
  la fuerza elástica puede no ser cero.
- **Llamar disipación al almacenamiento en un resorte ideal:**
  $W_e=-\Delta U_e$ puede ser distinto de cero.

[Balances, tramos y pérdidas](../apuntes/trabajo-energia/balances-y-tramos.md).

## Movimiento Armónico Simple

- **Elegir fase sólo con una posición:** comprobar también la velocidad y su signo.
- **Usar deformación estática como amplitud:** fijar el equilibrio del
  sistema que realmente oscila, especialmente si acaba de recibir otra masa.
- **Prolongar el MAS al perder contacto con el resorte:** comprobar si el
  bloque estaba unido o solamente apoyado.
- **Cambiar la frecuencia angular al derivar:** todas las funciones del
  mismo movimiento deben conservar el mismo argumento y origen temporal.

[Fase inicial, equilibrio y masa oscilante](../apuntes/movimiento-armonico-simple/fase-y-equilibrio.md).

## Impulso y cantidad de movimiento

- **Conservar momento sin sistema ni intervalo:** primero evaluar el impulso externo.
- **Usar módulos en un choque con sentidos opuestos:** escribir velocidades
  algebraicas o componentes en una misma referencia.
- **Conservar $K$ en un choque plástico:** distinguir impacto de caída,
  frenado o compresión posterior.
- **Confundir $K_{CM}$ con $K$ total:** conservar momento y masa mantiene
  $K_{CM}$, pero puede cambiar la energía del movimiento relativo.
- **Redondear velocidades antes de calcular diferencias de energías grandes:**
  conservar cifras intermedias y redondear al informar el resultado.
- **Presuponer elasticidad en un choque oblicuo:** la conservación de
  momento por ejes no implica conservación de $K$.
  [Ficha vectorial](../apuntes/impulso-cantidad-movimiento/choques-oblicuos.md).

[Condiciones de conservación y choques](../apuntes/impulso-cantidad-movimiento/conservacion-y-choques.md).

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

