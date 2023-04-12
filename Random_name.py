import random


class Random_name:
    def get_random_name():
        name = []
        capital_vow_letter = "аеиоуюя"
        capital_cos_letter = "бвгджзклмнпрстфхцчш"
        vowels = "аеёиоуыэюя"
        consonant = "бвгджзйклмнпрстфхцчшщ"
        start_letter = random.randint(0, 1)
        name += (random.choice(capital_cos_letter)) if start_letter == 1 else random.choice(capital_vow_letter)
        for i in range(random.randint(3, 8)):
            double_letter = random.randint(0, 10)
            double_letter1 = random.randint(0, 10)
            if start_letter == 0:
                name += random.choice(consonant) * 2 if double_letter == 0 \
                    else random.choice(consonant)
                start_letter = 1
            else:
                name += (random.choice(vowels)) * 2 if double_letter1 == 0 \
                    else random.choice(vowels)
                start_letter = 0

        nick = "".join(name).capitalize()
        if Random_name.check_nick(nick) == False:
            nick = Random_name.get_random_name()

        return nick

    def check_nick(nick: str):
        incorrect = ["ёё", "ёщ", "ыё", "ёу", "йэ", "гъ", "кщ", "щф", "щз", "эщ", "щк", "гщ",
                     "щп", "щт", "щш", "щг", "щм", "фщ", "щл", "щд", "дщ", "ьэ", "чц", "чы",
                     "вй", "ёц", "ёэ", "ёа", "йа", "шя", "шы", "ёе", "йё", "гю", "хя", "жю",
                     "йы", "ця", "гь", "сй", "хю", "хё", "ёи", "ёо", "яё", "щщ", "цц", "ёэ",
                     "эё", "ъд", "цё", "щч", "чй", "шй", "шз", "ыф", "жщ", "жш", "жц", "ыэ",
                     "ыю", "жй", "ыы", "жы", "пй", "зщ", "ыо", "жя", "зй", "ыа", "нй", "юю",
                     "цй", "еы", "ёы", "щс", "оы", "щх", "щщ", "щц", "кй", "цщ", "мй", "щй", "иы",
                     "йу", "щэ", "йы", "щы", "щю", "щя", "йй", "йж", "гй", "хй", "тй", "чщ", "фъ",
                     "уы", "юь", "аы", "юы", "эь", "эы", "бй", "яы", "хщ", "дй", "фй"]
        for i in incorrect:
            if i in str(nick).lower():
                return False
        return True

if __name__ == '__main__':

    print(f"итог: {Random_name.get_random_name()}")
