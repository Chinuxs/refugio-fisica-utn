# Tercer parcial — práctica filtrada y controles

Trabajar con los [enunciados T1–T3](patrones.md), saltando en los tres
el **ejercicio 3 de Venturi**. Saltar también las preguntas sobre CIR,
rodadura, Bernoulli, Pitot y caudal. Los resultados siguientes son
comprobaciones propias, no un solucionario oficial.

## 1. Persona que salta a un tiovivo — T1 y T2

Sistema = tiovivo + persona, eje vertical sin roce. El impulso angular externo
axial se desprecia durante el enganche. El tiovivo parte quieto:

$$I_p=MR_g^2,\quad L_i=mvR,\quad
\omega_f=\frac{mvR}{MR_g^2+mR^2}.$$

| Versión | Datos | Control |
| --- | --- | --- |
| T1 | R = 1,20 m, M = 200 kg, Rg = 1 m, m = 50 kg, v = 3 m/s | Iplataforma = 200 kg·m²; ωf = **0,6618 rad/s** |
| T2 | R = 2 m, M = 150 kg, Rg = 0,90 m, m = 50 kg, v = 3 m/s | Iplataforma = 121,5 kg·m²; ωf = **0,9331 rad/s** |

No usar I = MR²/2: ya dan **radio de giro**. El movimiento final sigue el
sentido del L inicial de la persona. No conservar K en el enganche.
Práctica espejo: **TP 9 ej. 35**, luego 34 y 28.

## 2. Plataforma con persona que se detiene — T3

Tomar positivo el giro inicial de la persona. Datos: m = 70 kg, R = 2,4 m,
vpersona/Tierra = 2 m/s, ωplataforma = −0,20 rad/s;
ωf = +0,15 rad/s, ambos juntos:

$$mRv+I(-0{,}20)=(I+mR^2)(0{,}15).$$

$$I=\frac{mRv-mR^2(0{,}15)}{0{,}15+0{,}20}
=\mathbf{787{,}2\ kg\,m^2}.$$

La velocidad de la persona es **respecto de Tierra**, no de la plataforma.
Práctica espejo: **TP 9 ej. 27**, pero intercambiando incógnita.

## 3. Madera y plomo — T1 y T2

Con la cara superior justo al agua, madera y plomo completamente sumergidos:

$$\rho_mV_mg+\rho_{Pb}V_{Pb}g=\rho_a(V_m+V_{Pb})g,$$
$$V_{Pb}=\frac{(\rho_a-\rho_m)V_m}{\rho_{Pb}-\rho_a}.$$

| Versión | Madera | Control para ρPb = 11300 kg/m³ |
| --- | --- | --- |
| T1 | 0,60 × 0,30 × 0,05 m; ρm = 600 kg/m³ | **349,5 cm³ de plomo** |
| T2 | 0,40 × 0,40 × 0,05 m; ρm = 500 kg/m³ | **388,35 cm³ de plomo** |

El plomo también desplaza agua: no despreciar su empuje.
Práctica espejo: **TP 11 ej. 11**. Seguir con 13, 15 y 20.

## 4. Cubo sumergido y dinamómetro — T3

Cubo de 10 cm de arista, m = 10 kg; cara superior a 0,05 m y cara inferior
a 0,15 m; A = 0,01 m². Usar patm = 101300 Pa como pide el examen:

$$F_{sup}=(p_{atm}+1000g\,0{,}05)A=\mathbf{1017{,}9\ N},$$
$$F_{inf}=(p_{atm}+1000g\,0{,}15)A=\mathbf{1027{,}7\ N}.$$

Empuje: Finf − Fsup = **9,8 N** = ρgV.
Dinamómetro: T = mg − E = **88,2 N**.
Las contribuciones manométricas de las caras son 4,9 y 14,7 N;
no confundirlas con las fuerzas absolutas anteriores.
Práctica espejo: **TP 11 ej. 16**, cuyo bloque tiene otra altura y otro volumen.

## 5. Teoría que sí sirve de los modelos

Responder sin mirar y justificar, no sólo V/F:

| Pregunta | Control conceptual |
| --- | --- |
| ¿Cambia I al cambiar el eje? | Depende del eje. Steiner sólo une ejes paralelos, uno por el CM; no todo cambio de eje obliga a un valor distinto |
| ¿r es siempre el brazo de palanca? | No: d⊥ = r sen φ. Si φ = 90°, d⊥ = r |
| ¿Condiciones de equilibrio? | ΣFext = 0 y Στext = 0; para estática además reposo inicial |
| ¿Unidades de presión? | Pa = N/m²; 1 kPa = 1000 Pa; 1 hPa = 100 Pa; 1 atm = 101325 Pa |
| ¿Presión inversamente proporcional a densidad? | No: a igual profundidad, Δp = ρgh es directamente proporcional |
| ¿Arquímedes empuja hacia abajo con el peso del fluido almacenado? | No: empuje hacia arriba igual al peso del fluido **desplazado** |
| ¿Por qué no se conserva K en el salto al tiovivo? | Hay enganche inelástico; sí puede conservarse Lz si el impulso angular externo es despreciable |

## 6. Cobertura de Estática, aunque no haya un problema numérico en la muestra

Elegir **TP 10 ej. 2** (escalera), **3a** (puntal), **7–8** (normal y vuelco).
Para cada uno: DCL → pivote → Στ = 0 → ΣFx = ΣFy = 0 → límite físico.

- En el 2, el roce real no es siempre μsN; esa igualdad se usa al límite.
- En el 3a, conservar el ángulo entre posición y fuerza al calcular torque.
- En el 7, puede desplazarse la línea de acción de N.
- En el 8, comparar ángulo de deslizamiento con ángulo de vuelco.

No hacer los ejercicios **10–21 del TP 10** para esta preparación: son
Rototraslación, excluida por el profesor. Tampoco el complemento de rodadura
de la guía de Cuerpo Rígido.

## Simulacro adaptado

Propuesta propia, distinta del examen histórico:

1. T3 ej. 1: plataforma, persona y momento angular.
2. T2 ej. 2: flotación y lastre.
3. TP 10 ej. 2: equilibrio y límite de roce.
4. Cinco preguntas de la tabla conceptual anterior.

Registrar el tiempo real, las consultas y el error principal. No se fija
duración ni ponderación oficial: no están informadas.

| Actividad | Estado | Error para repetir |
| --- | --- | --- |
| T1/T2 ej. 1 | Sin comenzar | — |
| T3 ej. 1 | Sin comenzar | — |
| T1/T2 ej. 2 | Sin comenzar | — |
| T3 ej. 2 | Sin comenzar | — |
| TP 10: 2, 3a, 7–8 | Sin comenzar | — |
| Simulacro adaptado | Sin comenzar | — |

[Patrones y cruce con TP](patrones.md) · [Volver](README.md)
