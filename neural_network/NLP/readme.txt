Bag of Words (BoW) - Natural Language Processing

https://ongspxm.github.io/blog/2014/12/bag-of-words-natural-language-processing/

https://sourcedexter.com/tensorflow-text-classification-python/

Some NLP terminologies before we begin

Natural Language Processing (NLP) is heavily being used in our text classification task. So, before we begin, I want to cover a few terms and concepts that we will be using. This will help you understand why a particular function or process is being called or at the very least clear any confusion you might have.

    Stemming – Stemming is a process applied to a single word to derive its root. Many words that are being used in a sentence are often inflected or derived. To standardize our process, we would like to stem such words and end up with only root words. For example, a stemmer will convert the following words “walking”, “walked”, “walker” to its root word “walk“.
    Tokenization – Tokens are basically words. This is a process of taking in a piece of text and find out all the unique words in the text. We would get a list of words in the text as the output of tokens. For example, for the sentence “Python NLP is just going great” we have the token list [ “Python”, “NLP”, ïs”, “just”, “going”, “great”]. So, as you can see, tokenization involves breaking up the text into words.
    Bag of Words – The Bag of Words model in Text Processing is the process of creating a unique list of words. This model is used as a tool for feature generation. Eg: consider two sentences:
        Star Wars is better than Star Trek.
        Star Trek isn’t as good as Star Wars.

    For the above two sentences, the bag of words will be: [“Star”, “Wars”, “Trek”, “better”, “good”, “isn’t”, “is”, “as”]. The position of each word in the list is hence fixed. Now, to construct a feature for classification from a sentence, we use a binary array ( an array where each element can either be 1 or 0).

    For example, a new sentence, “Wars is good” will be represented as [0,1,0,0,1,0,1,0] . As you can see in the array, position 2 is set to 1 because the word in position 2 is “wars” in the bag of words which is also present in our example sentence. This same holds good for the other words “is” and “good” as well. You can read more about the Bag of Words mode
