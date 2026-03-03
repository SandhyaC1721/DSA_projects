import heapq
from collections import Counter

# Step 1: Read file
with open("input.txt", "r") as file:
    text = file.read()

# Step 2: Count frequency
frequency = Counter(text)

# Step 3: Build heap
heap = [[freq, [char, ""]] for char, freq in frequency.items()]
heapq.heapify(heap)

# Step 4: Build Huffman Tree
while len(heap) > 1:
    left = heapq.heappop(heap)
    right = heapq.heappop(heap)

    for pair in left[1:]:
        pair[1] = '0' + pair[1]
    for pair in right[1:]:
        pair[1] = '1' + pair[1]

    heapq.heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])

# Step 5: Get Huffman codes
huffman_codes = sorted(heap[0][1:], key=lambda p: (len(p[-1]), p))
codes = {char: code for char, code in huffman_codes}

# Step 6: Encode text
encoded_text = ""
for char in text:
    encoded_text += codes[char]

# Save compressed data
with open("compressed.txt", "w") as file:
    file.write(encoded_text)

print("Compression Done ✅")
print("Huffman Codes:", codes)
print("Original Length:", len(text) * 8, "bits")
print("Compressed Length:", len(encoded_text), "bits")