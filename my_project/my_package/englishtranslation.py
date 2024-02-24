def hiragana_english(jpword):

    two_syllable_words = {'kise': 'きせ', 'haru': 'はる', 'natsu': 'なつ', 'fuyu': 'ふゆ', 'aki': 'あき', 'yuki': 'ゆき', 'ame': 'あめ', 'sora': 'そら', 'ten': 'てん', 'hoshi': 'ほし', 'nami': 'なみ', 'yama': 'やま', 'kai': 'かい', 'sui': 'すい', 'kusa': 'くさ', 'kumo': 'くも', 'nichi': 'にち', 'tsuki': 'つき', 'rai': 'らい', 'yoru': 'よる', 'hiru': 'ひる', 'yuu': 'ゆう', 'iro': 'いろ', 'aka': 'あか', 'ao': 'あお', 'kuro': 'くろ', 'kin': 'きん', 'nashi': 'なし', 'momo': 'もも', 'hana': 'はな', 'ran': 'らん', 'saku': 'さく', 'kan': 'かん', 'ai': 'あい', 'koi': 'こい', 'shin': 'しん', 'koe': 'こえ', 'hito': 'ひと', 'reki': 'れき', 'neko': 'ねこ', 'tori': 'とり'}

    japanese_to_english = {'kise': 'season', 'haru': 'spring', 'natsu': 'summer', 'fuyu': 'winter', 'aki': 'autumn', 'yuki': 'snow', 'ame': 'rain', 'sora': 'sky', 'ten': 'heaven', 'hoshi': 'star', 'nami': 'wave', 'yama': 'mountain', 'kai': 'sea', 'sui': 'water', 'kusa': 'grass', 'kumo': 'cloud', 'nichi': 'sun', 'tsuki': 'moon', 'rai': 'thunder', 'yoru': 'night', 'hiru': 'daytime', 'yuu': 'evening', 'iro': 'color', 'aka': 'red', 'ao': 'blue', 'kuro': 'black', 'kin': 'gold', 'gin': 'silver', 'nashi': 'pear', 'momo': 'peach', 'hana': 'flower', 'bara': 'rose', 'ran': 'orchid', 'saku': 'bloom', 'kan': 'feeling', 'ai': 'love', 'koi': 'love', 'shin': 'heart', 'koe': 'voice', 'hito': 'person', 'reki': 'history', 'neko': 'cat', 'tori': 'bird'}

    while jpword in two_syllable_words and jpword in japanese_to_english:

        hiraganaword = two_syllable_words[jpword]

        enword = japanese_to_english[jpword]

        hiragana_and_english = f'{hiraganaword}, {enword}'

        return hiragana_and_english

jpword = 'sora'

hiragana_and_english = hiragana_english(jpword)

print(hiragana_and_english)
