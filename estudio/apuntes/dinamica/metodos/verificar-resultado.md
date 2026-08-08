# Verificar un resultado

## 🎯 Qué recordar

Antes de aceptar la calculadora, pasar el resultado por tres filtros:

1. **unidades**: ¿la dimensión coincide con lo pedido?;
2. **orden de magnitud**: ¿el tamaño es razonable?;
3. **pantalla**: ¿se leyó correctamente la notación científica?

## 🖼️ Esquema / dibujo

```text
resultado de calculadora
          │
          ├── unidades correctas
          ├── estimación aproximada coherente
          └── exponente leído correctamente
                    ↓
             recién entonces aceptar
```

## 📐 Fórmula

Ejemplo dimensional para $v^2/R$:

$$
\frac{\mathrm{m^2/s^2}}{\mathrm m}=\mathrm{m/s^2}
$$

Ejemplo de orden de magnitud:

$$
\frac{18000}{2300}<\frac{18000}{1800}=10
$$

El resultado debe ser menor que $10$; uno del orden de $100$ revela un error.

En la calculadora:

$$
1{,}83\times10^3=1830
$$

## ⚠️ Error frecuente

- Conservar un resultado sólo porque la calculadora lo mostró.
- Omitir unidades durante el cálculo y agregarlas al final “de memoria”.
- Leer $1{,}83\times10^3$ como $1{,}83$.

## 🔗 Ver también

- [Segunda Ley de Newton](../conceptos/segunda-ley-newton.md)
- [Conversión de velocidades](../referencias-rapidas/conversion-velocidades.md)
