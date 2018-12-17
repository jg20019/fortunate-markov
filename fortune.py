import random

def learn_quote(starting_words, stopping_words, model, quote):
    words = quote.split()
    if not words:
        return 
    starting_words.append(words[0]) 
    for state, following in zip(words, words[1:]):
        if state in model:
            model[state][following] = model[state].get(following, 0) + 1
        else:
            model[state] = {}
            model[state][following] = 1
    stopping_words.append(words[-1])

def weighted_choice(weights):
    totals = []
    running_total = 0
    for w in weights:
        running_total += w
        totals.append(running_total)

    rnd = random.random() * running_total
    for i, total in enumerate(totals):
        if rnd < total:
            return i

def most_common(word, model):
    following_words = model[word]
    weights = following_words.values() 
    return list(following_words.keys())[weighted_choice(weights)]

def generate_quote(starting_words, stopping_words, model):
    word = random.choice(starting_words)
    out = [word]
    while word not in stopping_words:
        word = most_common(word, model)
        out.append(word)
    return ' '.join(out)

def main():
    quotes = open('fortune-example.txt', 'r').read().split('\n') 
    model = {}
    starting_words = [] 
    stopping_words = []
    for quote in quotes:
        learn_quote(starting_words, stopping_words, model, quote)

    try:
        while True:
            print(generate_quote(starting_words, stopping_words, model))
            input()
    except KeyboardInterrupt:
        print('Bye.')

if __name__ == '__main__':
    main()
