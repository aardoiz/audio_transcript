# Generador automático de transctipciones 
Este repositorio contiene el código usado para transcribir automáticamente un vídeo.

### Estructura
El repositorio contiene tres archivos:
- "movie.py" transforma automáticamente un archivo de vídeo a un archivo de audio
- "segment.py" reconoce la duración del audio y lo segmenta en fragmentos de 30 segundos para que la transcripción sea posible en equipos con poca RAM
- "speech2text.ipynb" usa los servers de Google Colab para acceder al drive del usuario y usar los archivos de audio segmentados en orden para generar la transcripción del vídeo

### Requisitos
- pydub
- huggingsound
- moviepy
- Python += 3.7 < 3.10


