pip install transformers
traducir = transformers(source="es", target="en").translate_file()
print(traducir)


#con GoogleTranslator
 pip install deep_translator
from deep_translator import GoogleTranslator
traducir = GoogleTranslator(source="es", target="en").translate_file()
print(traducir)
