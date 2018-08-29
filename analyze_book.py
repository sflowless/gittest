import string

def process_file(filename):
    hist = dict()
    fp = open(filename)
    for line in fp:
        process_line(line, hist)
    return hist

def process_line(line, hist):
    line = line.replace('-', '')

    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()

        hist[word] = hist.get(word, 0) + 1

def total_words(hist):
    return sum(hist.values())

def different_words(hist):
    return len(hist)

def most_common(hist):
    t = []
    for key, value in hist.items():
        t.append((value, key))

    t.sort(reverse=True)
    return t

if __name__ == '__main__':
    hist = process_file('text.txt')
    print('Total number of words: ', total_words(hist))
    print('Number of different words: ', different_words(hist))

    t = most_common(hist)
    print('The most common words are: ')
    for freq, word in t[0:10]:
        print(word, '\t', freq)

