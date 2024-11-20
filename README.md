# Proyecto: Evolución de Estrategias en Tic-Tac-Toe mediante Algoritmos Genéticos

Este proyecto implementa un algoritmo genético para evolucionar y optimizar estrategias en el juego Tic-Tac-Toe. El objetivo es desarrollar estrategias efectivas que puedan competir contra diferentes oponentes, incluyendo estrategias predefinidas como la aleatoria, heurística y Minimax.

## Tabla de Contenidos

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Prerequisitos](#prerequisitos)
- [Instalación](#instalación)
- [Ejecución](#ejecución)
  - [1. Ejecutar el Algoritmo Genético](#1-ejecutar-el-algoritmo-genético)
  - [2. Generar las Gráficas](#2-generar-las-gráficas)
- [Resultados](#resultados)
- [Notas Adicionales](#notas-adicionales)
- [Contacto](#contacto)

## Descripción del Proyecto

Este proyecto utiliza un algoritmo genético (AG) para evolucionar estrategias de juego en Tic-Tac-Toe. El AG simula un proceso evolutivo donde una población de individuos (estrategias) se somete a selección, cruce y mutación a lo largo de varias generaciones para mejorar su desempeño.

## Estructura del Proyecto

El proyecto contiene los siguientes archivos:

- `tic_tac_toe.py`: Módulo con la lógica del juego Tic-Tac-Toe.
- `strategies.py`: Módulo con estrategias predefinidas (aleatoria, heurística, Minimax).
- `genetic_algorithm.py`: Implementación del algoritmo genético.
- `main.py`: Script principal para ejecutar el algoritmo genético y evaluar las estrategias.
- `plot_results.py`: Script para generar las gráficas de resultados.
- `fitness_history.pkl`: Archivo generado que almacena la historia de aptitud.
- `evaluation_results.pkl`: Archivo generado que almacena los resultados de evaluación.
- `grafica_aptitud.png`: Gráfica de la evolución de la aptitud a lo largo de las generaciones.
- `grafica_comparativa.png`: Gráfica comparativa de tasas de victoria, empate y derrota.

## Prerequisitos

- Python 3.x
- Paquetes de Python:
  - `numpy`
  - `matplotlib`

## Instalación

1. **Clonar el repositorio o descargar los archivos:**

   Clona este repositorio en tu máquina local o descarga los archivos necesarios.

2. **Crear un entorno virtual (opcional pero recomendado):**

   ```bash
   python -m venv env
   ```

   Activa el entorno virtual:

   - En Windows:

     ```bash
     env\Scripts\activate
     ```

   - En macOS/Linux:

     ```bash
     source env/bin/activate
     ```

3. **Instalar las dependencias:**

   Asegúrate de tener `pip` actualizado:

   ```bash
   pip install --upgrade pip
   ```

   Instala los paquetes necesarios:

   ```bash
   pip install numpy matplotlib
   ```

## Ejecución

### 1. Ejecutar el Algoritmo Genético

Ejecuta el script principal `main.py` para iniciar el algoritmo genético:

```bash
python main.py
```

Este script realizará lo siguiente:

- Ejecutará el algoritmo genético con los parámetros especificados (tamaño de población, generaciones, tasas de mutación y cruce).
- Guardará el mejor individuo (estrategia evolucionada) en `best_individual.pkl`.
- Guardará la historia de aptitud en `fitness_history.pkl`.
- Evaluará el mejor individuo contra estrategias predefinidas y guardará los resultados en `evaluation_results.pkl`.

**Nota:** La ejecución puede tardar varios minutos dependiendo de los parámetros y la potencia de tu máquina.

### 2. Generar las Gráficas

Una vez que el algoritmo genético haya finalizado, ejecuta el script `plot_results.py` para generar las gráficas:

```bash
python plot_results.py
```

Este script:

- Cargará los datos de `fitness_history.pkl` y generará la gráfica de evolución de la aptitud, guardándola como `grafica_aptitud.png`.
- Cargará los datos de `evaluation_results.pkl` y generará la gráfica comparativa de estrategias, guardándola como `grafica_comparativa.png`.

**Nota:** Si ves advertencias relacionadas con `plt.show()`, puedes ignorarlas o comentar las líneas `plt.show()` en el script, ya que las gráficas se guardarán correctamente.

## Resultados

- **grafica_aptitud.png**: Muestra cómo la aptitud máxima y promedio evolucionan a lo largo de las generaciones.

- **grafica_comparativa.png**: Compara las tasas de victoria, empate y derrota de la estrategia evolucionada contra otras estrategias predefinidas.

Puedes incluir estas gráficas en tu presentación o informe para ilustrar los resultados obtenidos.

## Notas Adicionales

- **Parámetros del Algoritmo Genético:**

  Puedes ajustar los parámetros del algoritmo genético modificando los valores en `main.py`:

  ```python
  if __name__ == '__main__':
      ga = GeneticAlgorithm(
          population_size=50,     # Tamaño de la población
          generations=50,         # Número de generaciones
          mutation_rate=0.01,     # Tasa de mutación
          crossover_rate=0.7      # Tasa de cruce
      )
      # ...
  ```

- **Rendimiento:**

  - Dado que el número de estados posibles en Tic-Tac-Toe es grande, el programa puede consumir bastante memoria y tiempo de procesamiento.
  - Si experimentas problemas de rendimiento, considera reducir el tamaño de la población o el número de generaciones.

- **Comprensión del Código:**

  - Se recomienda revisar y entender cada uno de los archivos para tener una mejor comprensión del funcionamiento del algoritmo.
  - Los comentarios en el código ayudan a entender la lógica implementada.

- **Entorno sin Interfaz Gráfica:**

  - Si ejecutas el script en un entorno sin interfaz gráfica, las gráficas no se mostrarán interactivamente, pero se guardarán en los archivos correspondientes.

- **Posibles Mejoras:**

  - Implementar optimizaciones en la representación de los estados del juego.
  - Probar con diferentes métodos de selección, cruce y mutación.
  - Integrar técnicas adicionales como coevolución o aprendizaje por refuerzo.

## Contacto

Si tienes alguna pregunta o sugerencia sobre este proyecto, puedes contactarme a través de:

- **Nombre:** Christian Eulogio Sánchez
- **Correo electrónico:** [christianeulogio@ciencias.unam.mx](christianeulogio@ciencias.unam.mx)
- **Institución:** Facultad de Ciencias,  UNAM

¡Gracias por tu interés en este proyecto!