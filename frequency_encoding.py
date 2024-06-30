import json

# codes by ease of typing, in order. should be assigned proportionally with frequency found from huffman tree.
code_list = [
    "001",
    "010",
    "100",
    "011",
    "110",
    "101",
    "111",
    "002",
    "020",
    "200",
    "022",
    "220",
    "202",
    "222",
    "012",
    "021",
    "102",
    "201",
    "120",
    "210",
    "112",
    "221",
    "121",
    "212",
    "122",
    "211",
]

encoding_dict = {}
# letter frequencies from https://en.wikipedia.org/wiki/Letter_frequency
letter_frequencies = {
    "A": 8.167,
    "B": 1.492,
    "C": 2.782,
    "D": 4.253,
    "E": 12.702,
    "F": 2.228,
    "G": 2.015,
    "H": 6.094,
    "I": 6.966,
    "J": 0.153,
    "K": 0.772,
    "L": 4.025,
    "M": 2.406,
    "N": 6.749,
    "O": 7.507,
    "P": 1.929,
    "Q": 0.095,
    "R": 5.987,
    "S": 6.327,
    "T": 9.056,
    "U": 2.758,
    "V": 0.978,
    "W": 2.361,
    "X": 0.150,
    "Y": 1.974,
    "Z": 0.074,
}

while letter_frequencies:
    highest_freq = max(letter_frequencies.values())
    highest_freq_letter = [
        k for k, v in letter_frequencies.items() if v == highest_freq
    ][0]
    letter_frequencies.pop(highest_freq_letter)
    encoding_dict[highest_freq_letter] = code_list.pop(0)


if __name__ == "__main__":

    # write encoding to json file
    with open("frequency_encoding.json", "w") as f:
        json.dump(encoding_dict, f)
