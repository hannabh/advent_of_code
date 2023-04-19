with open('../data/input_6.txt') as f:
    signal = f.read()


def find_marker(signal, length):
    for i in range(len(signal)):
        chars = signal[i:i+length]
        if len(set(chars)) == length:
            return length + i


print("Part A: ", find_marker(signal, 4))
print("Part B: ", find_marker(signal, 14))
