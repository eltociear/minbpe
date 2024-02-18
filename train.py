"""
Train our Tokenizers on some data, just to see them in action.
The whole thing runs in ~25 seconds on my laptop.
"""

from minbpe import BasicTokenizer, RegexTokenizer

# open some text and train a vocab of 512 tokens
text = open("tests/taylorswift.txt", "r", encoding="utf-8").read()

for TokenizerClass, name in zip([BasicTokenizer, RegexTokenizer], ["basic", "regex"]):

    # construct the Tokenizer object and kick off verbose training
    tokenizer = TokenizerClass()
    tokenizer.train(text, 512, verbose=True)
    # writes two files in current directory: name.model, and name.vocab
    tokenizer.save(name)
