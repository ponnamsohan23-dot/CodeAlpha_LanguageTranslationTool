from googletrans import Translator

translator = Translator()

print("===== Language Translation Tool =====")

text = input("Enter text: ")
src = input("Source language (en, hi, te, fr): ")
dest = input("Target language (en, hi, te, fr): ")

translated = translator.translate(text, src=src, dest=dest)

print("\nTranslated Text:")
print(translated.text)