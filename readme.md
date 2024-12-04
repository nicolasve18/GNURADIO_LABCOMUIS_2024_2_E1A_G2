
## Parte A
En la Primera Parte , se utiliza una antena y el software GNU Radio para sintonizar y analizar  frecuencias dentro del rango de 88 a 108 MHz, correspondientes a emisoras locales. Se exploran características como el piloto y los componentes de la señal (L+R) esto se hace en el software de gnu radio ,luego se pasa a utilizar el analizador de espectro donde se pueden apreciar las diferencias de usar una herramienta especializada y se tomaron medidas como el ancho de banda, regulado por la "Agencia Nacional del Espectro" (ANE).
![banda base](https://github.com/nicolasve18/GNURADIO_LABCOMUIS_2024_2_E1A_G2/blob/practica_4/practica_4/Captura%20de%20pantalla%202024-12-04%20165340.png)

## Parte B
En la Segunda Parte , se emplea un sistema en GNU Radio para observar modulaciones de banda ancha y estrecha mediante ajustes en el índice de modulación (KpAm). Además, se analizan las señales en el tiempo y su representación mediante un osciloscopio .tambien se hizo el mismo procedimiento para dos señales banda ancha  con un KpAm mayo a diez comparando la influencia que tiene el indice en las señales moduladas en la ultima parte se calculan los coeficientes de Bessel teóricos utilizando tablas provistas, lo que brinda una comprensión sobre su relevancia en modulaciones angulares.

Se observó algo curioso que se mencionaba en la teoría al modificar el factor KapAm. Al hacerlo, la señal mantenía una amplitud constante, pero presentaba un comportamiento similar al de un acordeón. Esto se debía a que al modificar el KapAm , la frecuencia de la señal variaba, lo que generaba esa sensación visual. como se ve en la imagen
![señal variando el kpAm](https://github.com/nicolasve18/GNURADIO_LABCOMUIS_2024_2_E1A_G2/blob/practica_4/practica_4/SCR03.PNG)

## conclusion:
Se observó que algunas emisoras no cumplen con el ancho de banda reglamentario y utilizan más del permitido. Como resultado, en ciertas áreas del espectro, las emisoras causan interferencias entre sí.

Al calcular los coeficientes de Bessel, se observó una diferencia entre los valores teóricos y los obtenidos en el laboratorio. Esta discrepancia se atribuye a varias razones, como las imperfecciones al generar la señal en GNU Radio, así como las pérdidas y atenuaciones causadas por el cableado y el propio analizador de frecuencia.

se vio que al se una señal de banda estrecha  osea con un kpAm menor a 0,2 se puede analizar como si estuviera modulada por amplitud facilitando los calculos.
