from translate import Translator
translator= Translator(from_lang="english", to_lang="russian")

translation = translator.translate(input("пользователь, а что перевести: "))
print  (translation)
