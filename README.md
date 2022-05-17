# Generador automático de transctipciones 
Este repositorio contiene el código usado para transcribir automáticamente un vídeo. A su vez, se añade un cuaderno de Jupyter para ejecutar traducciones de las transcripciones cómodamente.

### Estructura
El repositorio contiene dos archivos python y un cuaderno Colab:
- "movie.py" transforma automáticamente un archivo de vídeo a un archivo de audio
- "segment.py" reconoce la duración del audio y lo segmenta en fragmentos de 30 segundos para que la transcripción sea posible en equipos con poca RAM
- "speech2text.ipynb" usa los servers de Google Colab para acceder al drive del usuario y usar los archivos de audio segmentados en orden para generar la transcripción del vídeo

A su vez, incluye otro cuaderno de Google Colab (cortesía de Noemi Rámila) para realizar traducciones:
- "traductor.ipynb" es un archivo simple y cómodo para realizar traducciones del español al inglés


### Requisitos
- pydub
- huggingsound
- moviepy
- Python += 3.7 < 3.10


