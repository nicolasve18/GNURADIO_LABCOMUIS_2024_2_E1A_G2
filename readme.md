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

En esta etapa, se realizarán mediciones del tiempo de bit y el índice de modulación absoluto en tres casos de señales moduladas. Además, se estimará el ancho de banda de cada señal medida.

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


## conclusion 
Se observó que al calcular el índice de modulación a partir de las amplitudes obtenidas mediante el osciloscopio, no se obtuvo el valor teórico, sino un valor aproximado. Esto podría deberse a las pérdidas ocasionadas por el cable de conexión entre el radio y el osciloscopio, así como a otros factores adicionales.



