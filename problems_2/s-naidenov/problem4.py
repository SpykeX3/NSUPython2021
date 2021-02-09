def count_substrings_in_text(p):
    file_path = input("File path ")
    count = 0
    i = 0
    with open(file_path, 'r', encoding='utf-8') as source:
        seq = input("sequence to find ")
        text = ''.join(source.read()[2:].split('\n'))
        while True:
            i = text.find(seq, i + 1)
            if i == -1:
                break
            count += 1
            if count < 6:
                p.append(i)
    return count

if __name__ == '__main__':
    positions = []
    res = count_substrings_in_text(positions)
    print("Found " + str(res))
    print("Positions " + str(positions[:5]))
