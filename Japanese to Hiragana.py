
hiragana_dictionary = {'a': 'あ', 'i': 'い', 'u': 'う', 'e': 'え', 'o': 'お', 'ka': 'か', 'ki': 'き', 'ku': 'く', 'ke': 'け', 'ko': 'こ', 'sa': 'さ', 'shi': 'し', 'su': 'す', 'se': 'せ', 'so': 'そ', 'ta': 'た', 'chi': 'ち', 'tsu': 'つ', 'te': 'て', 'to': 'と', 'na': 'な', 'ni': 'に', 'nu': 'ぬ', 'ne': 'ね', 'no': 'の', 'ha': 'は', 'hi': 'ひ', 'fu': 'ふ', 'he': 'へ', 'ho': 'ほ', 'ma': 'ま', 'mi': 'み', 'mu': 'む', 'me': 'め', 'mo': 'も', 'ya': 'や', 'yu': 'ゆ', 'yo': 'よ', 'ra': 'ら', 'ri': 'り', 'ru': 'る', 're': 'れ', 'ro': 'ろ', 'wa': 'わ', 'wo': 'を', 'n': 'ん'}

def latin_to_hiragana(jpword):

    latin = ''
    hiragana = ''

    for char in jpword:
        if char == 'n':
            if latin:
                hiragana = hiragana + hiragana_dictionary['n']
                latin = ''
            latin = 'n'
        else: 
            latin = latin + char
            if latin in hiragana_dictionary:
                hiragana = hiragana + hiragana_dictionary[latin]
                latin = ''
    if latin == 'n':
        hiragana = hiragana + hiragana_dictionary['n']
    return hiragana


jpword = 'haru'

hiragana_version = latin_to_hiragana(jpword)

print(hiragana_version)
