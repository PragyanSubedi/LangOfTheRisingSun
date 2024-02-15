# Lang of the Rising Sun

![Lang of the Rising Sun](https://github.com/PragyanSubedi/LangOfTheRisingSun/blob/main/assets/cover.png)

This repo houses code to learn Japanese using Machine Learning.

(Disclaimer: I am a Nepalese-born individual with my first language as Nepalese and second language as English. This repository is my effort to simplify the Japanese learning process for others like me.)

---

## Hiragana Writing System

The writing system used in this repository for Japanese is "Hiragana".

"Hiragana (ひらがな) is a Japanese syllabary, part of the Japanese writing system. It is a phonetic lettering system. The word hiragana literally means "common" or "plain" kana (originally also "easy", as contrasted with kanji)." - <a href="https://en.wikipedia.org/wiki/Hiragana" target="__blank__"> Wikipedia </a>

To learn the Hiragana writing system, I've created the following notebook: <a href="hiragana_basics.ipynb" target="__blank__"> Hiragana Basics </a>

## Development Progress

- [x] Add Jupyter notebook showcasing Hiragana Basics

<img src ="https://github.com/PragyanSubedi/LangOfTheRisingSun/blob/main/assets/hiragana_basics.png" alt="Hiragana Basics" height="100">

- [ ] Add Jupyter notebook showcasing Kanji Basics
- [x] Add text-to-text translation for converting English text to Japanese text
- [ ] Add speech-to-text component for converting English speech into English text
- [ ] Add text-to-speech component for converting Japanese text to Japanese speech

## Translate English to Japanese: en_to_jp.py

The `en_to_jp.py` file contains code to translate English code to Japanese.

To run it,

1. Download the <a href="https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt" target="__blank"> mBART-50 many to many multilingual machine translation</a> model files for Pytorch and place it in `checkpoint/kanji_model`

2. Run `en_to_jp.py` as follows:

```
python -m en_to_jp "cherry blossoms"

# Output:
cherry blossoms: ['桜']
```
