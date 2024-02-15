import sys
import warnings

warnings.filterwarnings("ignore")
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast


def translate_to_japanese(input_text):
    model = MBartForConditionalGeneration.from_pretrained("checkpoint/kanji_model")
    tokenizer = MBart50TokenizerFast.from_pretrained("checkpoint/kanji_model")

    print("Successfully Loaded Model")

    # Translate English to Japanese
    tokenizer.src_lang = "en_XX"
    encoded_text = tokenizer(input_text, return_tensors="pt")
    generated_tokens = model.generate(
        **encoded_text, forced_bos_token_id=tokenizer.lang_code_to_id["ja_XX"]
    )

    translated_text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    return f"{input_text}: {translated_text}"


if __name__ == "__main__":
    # Check if the user provided text as a command line argument
    if len(sys.argv) < 2:
        print("Please provide the text to be translated as an argument.")
        sys.exit(1)

    input_text = " ".join(
        sys.argv[1:]
    )  # Concatenate all command line arguments into a single string

    translated_text = translate_to_japanese(input_text)
    print(translated_text)
