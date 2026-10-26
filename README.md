# Arduino Button to Keyboard Event

Este proyecto permite convertir la pulsación de un botón físico conectado a un Arduino en un evento de teclado en tu ordenador (por defecto la tecla 'k').

## 1. Conexión del Hardware

El circuito es muy sencillo gracias al uso de la resistencia interna `PULLUP` del Arduino.

*   **Pin Digital 2:** Conecta un extremo del botón pulsador.
*   **Pin GND:** Conecta el otro extremo del botón pulsador.

**Nota:** No necesitas resistencias externas. El código configura el Pin 2 en modo `INPUT_PULLUP`, lo que mantiene el pin en nivel ALTO (`HIGH`) y detecta la pulsación cuando el botón cierra el circuito a TIERRA (`LOW`).

## 2. Requisitos Previos

Antes de ejecutar el script de Python, instala las librerías necesarias:

```bash
pip install pyserial pynput
```

## 3. Funcionamiento del Script (`listen_button.py`)

El script de Python es interactivo y sigue estos pasos:

1.  **Selección de Puerto:** Al iniciar, el script listará todos los dispositivos serie detectados. Debes introducir el número (índice) correspondiente a tu Arduino.
2.  **Configuración de Tecla:** Luego te preguntará qué carácter quieres que se envíe al pulsar el botón.
    *   Si presionas **Enter** directamente, usará la letra **'k'** por defecto.
    *   Si escribes una letra (ej. 'a'), usará esa letra.
3.  **Escucha de Eventos:** Una vez configurado, el script quedará a la espera. Cada vez que pulses el botón físico, se enviará el evento de teclado al sistema operativo (se escribirá la letra en la ventana que tengas activa).

## 4. Solución de Problemas: Puerto Ocupado

Si al intentar correr el script recibes un error similar a este:
`Error: Could not open serial port ... [Errno 16] Device or resource busy`

**Causa:** El puerto serie está siendo utilizado por otra aplicación.
**Solución:** 
*   **Cierra el Monitor Serial** del IDE de Arduino si lo tienes abierto.
*   Asegúrate de que no haya otra instancia del script `listen_button.py` ejecutándose.
*   El Arduino solo puede comunicarse con un programa a la vez por el puerto serie.

---
*Desarrollado para la integración de Arduino y automatización mediante eventos de teclado.*
