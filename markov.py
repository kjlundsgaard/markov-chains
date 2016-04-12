from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path) as file_object:

        poem = file_object.read()


    return poem


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    words = text_string.split()

    # len(words) -2 so we avoid indexerror by trying to append out of avail index 
    for i in range(len(words) - 2):
        bigram = (words[i], words[i + 1])
        if bigram in chains:
            chains[bigram].append(words[i + 2])
        else:
            chains[bigram] = [words[i + 2]]

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    # initialize key bigram by selecting a random choice of chain key
    key_bigram = choice(chains.keys()) 
    # initalize text by joining strings in key bigram to make first string
    text = " ".join(key_bigram)

    while key_bigram in chains:
        # get a random choice value from chains at the key_bigramth element
        random_value = choice(chains[key_bigram])
        # now text is equal to old text but new random value
        text = text + " " + random_value
        # generate new key bigram from last two words of previous text
        key_bigram = (key_bigram[1], random_value)

    return text


# input_path = "green-eggs.txt"
input_path = "gettysburg.txt"
# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
