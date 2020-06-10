import pandas as pd
from nltk.tokenize import RegexpTokenizer
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
# define function to tokenize a column
# modified to return title cased titles

def tokenizer_function(column):
    """
    Takes in a text column
        tokenizes the text in each row
        using pattern [[a-zA-Z]\w+]
        which matches every lowercase and upperase character between a-z that are word characters
    Returns list of strings
    """

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
        tokens = [token.title() for token in tokens]
        texts.append(' '.join(tokens))
    return texts

# define function to search titles based on search term
# return first 25 of titles that contain the search term
# define function to search titles based on search term
# return titles that contain the search term
# the number of titles returned are specified by 'number'
def search_by_query(search_term):
    df = pd.read_csv('../data/combined.csv')

    df['cleaned_titles'] = tokenizer_function(df['title'])
    df_to_return = pd.DataFrame()
    for i in range(len(df)):
        if search_term.lower() in df['cleaned_titles'][i].lower():
            title = df['cleaned_titles'][i]

            if len(df_to_return) == 0 or title not in df_to_return['cleaned_titles'].values:
                df_to_return = df_to_return.append(df.loc[[i]])



    return df_to_return


# find most similar documents in dataframe
def most_similar(base_document_idx, n):
    """function
       finds most similar n documents
       to base_document
       based on cosine similarity
       returns similar documents
       as pandas dataframe"""
    # load saved doc2vec_model
    model = Doc2Vec.load('/Users/bibor/General_Assembly/DSI/Capstone/models/doc2vec_titles')
    # get similar topics
    similars = model.docvecs.most_similar(base_document_idx, topn=n)

    # load original dataframe
    data = pd.read_csv('../data/combined.csv')
    # base document
    row1 = data.loc[base_document_idx, :]

    # list of rows in the original dataframe
    # initialized with the base_document
    list_of_dfs = [row1]

    # iterate through all similar notifications
    for tag, similar_document in similars:
        # find the row in the notifications dataframe corresponding to the tag
        df = data.loc[tag, :]
        # add row to the list of rows
        list_of_dfs.append(df)
    # return all rows as a dataframe
    return pd.DataFrame(list_of_dfs)

def latest_opportunities():
    df = pd.read_csv('../data/combined.csv')
    return df.loc[df['date_posted'] == df['date_posted'].max()]
