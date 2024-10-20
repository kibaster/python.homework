from itertools import chain
from random import random,choice,randint
from pprint import pprint

def learn(dataset: list[str]):
    dataset = list(chain(*[sentence.split() for sentence in dataset]))
    words = set(dataset)
    count_of_words = {word:dataset.count(word) for word in words}
    words_combinations = {word:list(dataset[index+1] for index in range(len(dataset)-1) if dataset[index] == word) for word in words }
    return words,count_of_words,words_combinations


def generate(state):
    words,count_of_words,words_combinations = state
    chances = list(chain(*[[word]*cnt for word,cnt in count_of_words.items()]))
    current_word = choice(list(words))
    text = [current_word]
    for _ in range(10):
        if len(words_combinations[current_word])>0:
            next_word = choice(words_combinations[current_word])
            text.append(next_word)
            current_word = next_word
        else: 
            current_word = choice(chances)
    return ' '.join(text)
# pprint(generate(learn([
#    "the dog ran quickly through the park chasing after a ball",
#    "a ball rolled across the park as the kids quickly chased after it",
#    "they quickly ran after the ball which flew across the park",
#    "in the park the dog quickly grabbed the ball and ran off"
# ])))