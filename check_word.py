

two_syllable_words = {'kise': 'きせ', 'haru': 'はる', 'natsu': 'なつ', 'fuyu': 'ふゆ', 'aki': 'あき', 'yuki': 'ゆき', 'ame': 'あめ', 'sora': 'そら', 'ten': 'てん', 'hoshi': 'ほし', 'nami': 'なみ', 'yama': 'やま', 'kai': 'かい', 'sui': 'すい', 'kusa': 'くさ', 'kumo': 'くも', 'nichi': 'にち', 'tsuki': 'つき', 'rai': 'らい', 'yoru': 'よる', 'hiru': 'ひる', 'yuu': 'ゆう', 'iro': 'いろ', 'aka': 'あか', 'ao': 'あお', 'kuro': 'くろ', 'kin': 'きん', 'nashi': 'なし', 'momo': 'もも', 'hana': 'はな', 'ran': 'らん', 'saku': 'さく', 'kan': 'かん', 'ai': 'あい', 'koi': 'こい', 'shin': 'しん', 'koe': 'こえ', 'hito': 'ひと', 'reki': 'れき', 'neko': 'ねこ', 'tori': 'とり'}


def check_word(word):

    if word in two_syllable_words:

        return True

    else:

        return 'This word is not part of the dictionary'
