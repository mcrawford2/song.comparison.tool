# loading songs
with open("song1.txt", "r", encoding="utf-8") as f:
	song1 = f.read()

with open("song2.txt", "r", encoding="utf-8") as f:
	song2 = f.read()

with open("song3.txt", "r", encoding="utf-8") as f:
	song3 = f.read()
	


def analyze_song(song):
    """Analyzes a song's lyrics numerically and returns basic statistics."""
    lines = [line for line in song.splitlines() if line.strip()]  # Ignore blank lines.
    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    avg_words_per_line = num_words / num_lines if num_lines else 0
    return {
        "num_lines": num_lines,
        "num_words": num_words,
        "avg_words_per_line": avg_words_per_line,
    }

import re                           # 're' is used for regular expressions to clean and split words.
from collections import Counter     # 'Counter' is used to count the frequency of each word in the song.

def word_frequency(song):
    """Returns a Counter object with the frequency of each word in the song."""
    # Normalize by lowercasing and removing punctuation for cleaner counts.
    words = re.findall(r"[a-zA-Z']+", song.lower())
    return Counter(words)

if __name__ == "__main__":
    print()
    print("song1 stats:", analyze_song(song1)) #number of lines, number of words, average words per line
    print("song2 stats:", analyze_song(song2))
    print("song3 stats:", analyze_song(song3))
    print()
    print("song1 top words:", word_frequency(song1).most_common(10)) # top 10 most common words
    print("song2 top words:", word_frequency(song2).most_common(10))
    print("song3 top words:", word_frequency(song3).most_common(10))



def avg_word_length(song):
    """Calculates the average word length per song."""
    words = re.findall(r"[a-zA-Z']+", song)  # Extract words, ignoring punctuation.
    total_length = sum(len(word) for word in words)
    if words:
        return total_length / len(words)
    else:
        return 0

if __name__ == "__main__":
    print()
    print("song1 average word length:", avg_word_length(song1))
    print("song2 average word length:", avg_word_length(song2))
    print("song3 average word length:", avg_word_length(song3))



def shared_vocab(song1, song2, song3):
    """Finds the shared vocabulary between three songs."""
    words1 = set(re.findall(r"[a-zA-Z']+", song1.lower()))
    words2 = set(re.findall(r"[a-zA-Z']+", song2.lower()))
    words3 = set(re.findall(r"[a-zA-Z']+", song3.lower()))
    shared_words = words1.intersection(words2).intersection(words3)
    return shared_words

if __name__ == "__main__":
    print()
    print("Shared vocabulary between the three songs:", shared_vocab(song1, song2, song3))