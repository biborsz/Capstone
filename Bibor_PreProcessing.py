import pandas as pd
from nltk.tokenize import RegexpTokenizer

# define function to tokenize a column

def tokenizer_function(column):
    """
    Takes in a text column
        tokenizes the text in each row
        using pattern [[a-zA-Z]\w+]
        which matches every lowercase and upperase character between a-z that are word characters
    Returns list of strings
    """
    # imports
    from nltk.tokenize import RegexpTokenizer

    # instantiate empty list of tokenized text
    texts = []

    # define tokenizer pattern
    pattern = '[a-zA-Z]\w+'
    # instantiate tokenizer
    tokenizer = RegexpTokenizer(pattern=pattern)

    # create for loop to tokenize each row and add the list of tokens to texts
    for text in column:
        tokens = tokenizer.tokenize(text)

        # transform tokens into lower case strings
        tokens = [token.lower() for token in tokens]
        texts.append(tokens)
    return texts
