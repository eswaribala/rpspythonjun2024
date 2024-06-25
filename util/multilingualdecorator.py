def tr_french(text):
    return text + "=>" + "Bonjour"


def tr_germany(text):
    return text + "=>" + "Guten Morgen"


def tr_japanese(text):
    return text + "=>" + "おはよう"


def tr_chinese(text):
    return text + "=>" + "早上好"


def translate(func):
    translated_data = func("Good Morning")
    print(translated_data)


# function / method is passed as parameter
translate(tr_french)
translate(tr_germany)
translate(tr_chinese)
translate(tr_japanese)
