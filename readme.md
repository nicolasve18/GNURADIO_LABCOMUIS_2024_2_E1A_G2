# Parte A: Análisis de Modulación de Amplitud

en esta practica se realizó un análisis de la modulación de amplitud (AM) en tres casos:

- \( k_a A_m = 1 \)
- \( k_a A_m > 1 \)
- \( k_a A_m < 1 \)

## Objetivos

1. **Medir la potencia de la señal \( s(t) \)** con el analizador de espectro.
2. **Calcular el índice de modulación** \( k_a A_m \)


Para cada caso, se completó una tabla con los siguientes datos:

- Potencia de la señal portadora
- Potencia de la banda lateral superior
- Potencia de la banda lateral inferior
- Índice de modulación
- Frecuencia del mensaje
- Relación señal a ruido medida
 

insiso 2 de la parte  A:
Se consideraron los siguientes casos de modulación AM, donde \( N \) es el último dígito del código de estudiante:
1. \( k_a A_m = 1 \)
2. \( k_a A_m = 1 + 0.1 \cdot N \)
3. \( k_a A_m = 1 - 0.1 \cdot N \)

1. Se observó la señal envolvente compleja \( g(t) \) utilizando el bloque **QT GUI Time Sink**.
2. Se midieron las amplitudes de la señal \( s(t) \) con el osciloscopio.
3. Se determinó la profundidad de modulación a partir del índice de modulación utilizando los cursores del osciloscopio.

# Parte B: Medición del Índice de Modulación y Análisis de Banda Ancha
Esta parte b se dividio en dos subpartes:

En la primera parte de la práctica, se utilizó el osciloscopio para realizar mediciones de tiempo de bit y del índice de modulación. Primero, se calculó teóricamente el tiempo de bit para cada uno de los tres casos, dividiendo la cantidad de muestras por símbolo entre la tasa de muestreo (samp_rate). Luego, en el osciloscopio, se ajustó la señal de acuerdo con los requerimientos establecidos y se identificó un bit específico para detener la señal (stop) y medir el tiempo del bit usando los cursores. Este tiempo experimental se comparó con el tiempo teórico previamente calculado.

## Casos a Medir

1. **Señal Modulante al 75%**  
   - Frecuencia de portadora: 300 MHz  
   - Ganancia de TX: 10 dB  
   - 10 muestras por símbolo  

2. **Señal Modulante al 100%**  
   - Frecuencia de portadora: 250 MHz  
   - Ganancia de TX: 15 dB  
   - 5 muestras por símbolo  

3. **Señal Modulante al 150%**  
   - Frecuencia de portadora: 350 MHz  
   - Ganancia de TX: 20 dB  
   - 2 muestras por símbolo  
  ![señal modulada al 150%](https://github.com/Jpw11108/GNURADIO_LABCOMUIS_2024_2_E1A_G2/blob/practica_3/parte_A/imagen_2024-12-04_171444927.png ) 

Para calcular el índice de modulación absoluto en la segunda parte, se utilizó una función del osciloscopio que marca el pico máximo de la señal en tiempo real, necesario para determinar este índice en combinación con la amplitud de la portadora. La amplitud de la portadora se obtuvo ajustando el parámetro Ka a cero, dejando únicamente la señal de la portadora activa.


Para medir el ancho de banda, se empleó una máscara en el analizador de espectro  que permitió observar los picos más altos de la señal. Esto facilitó la determinación del ancho de banda usando el criterio de los 20 dB en esta parte el ancho de banda se mantuvo constante lo que aumento fue su potencia a medida que aumentaba el indice de modulacion absoluto.


## conclusion 
Se observó que al calcular el índice de modulación a partir de las amplitudes obtenidas mediante el osciloscopio, no se obtuvo el valor teórico, sino un valor aproximado. Esto podría deberse a las pérdidas ocasionadas por el cable de conexión entre el radio y el osciloscopio, así como a otros factores adicionales.



