def read_words(words_file):
    with open(words_file, 'r') as f:
        ret = []
        for line in f:
            ret += line.split()
        return ret    
print(read_words("test.txt"))