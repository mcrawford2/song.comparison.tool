import re
from collections import Counter

import matplotlib.pyplot as plt
from wordcloud import WordCloud
from matplotlib_venn import venn3

# loading songs
with open("song1.txt", "r", encoding="utf-8") as f:
    song1 = f.read()

with open("song2.txt", "r", encoding="utf-8") as f:
    song2 = f.read()

with open("song3.txt", "r", encoding="utf-8") as f:
    song3 = f.read()

# repeating variables
words1 = set(re.findall(r"[a-zA-Z']+", song1.lower()))
words2 = set(re.findall(r"[a-zA-Z']+", song2.lower()))
words3 = set(re.findall(r"[a-zA-Z']+", song3.lower()))

# analysis functions
def analyze_song(song):
    """Analyzes a song's lyrics numerically and returns basic statistics."""
    lines = [line for line in song.splitlines() if line.strip()]
    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    avg_words_per_line = num_words / num_lines if num_lines else 0
    return {
        "num_lines": num_lines,
        "num_words": num_words,
        "avg_words_per_line": avg_words_per_line,
    }


def word_frequency(song):
    """Returns a Counter object with the frequency of each word in the song."""
    words = re.findall(r"[a-zA-Z']+", song.lower())
    return Counter(words)


def avg_word_length(song):
    """Calculates the average word length per song."""
    words = re.findall(r"[a-zA-Z']+", song)
    total_length = sum(len(word) for word in words)
    return total_length / len(words) if words else 0


def shared_vocab(song1, song2, song3):
    """Finds the shared vocabulary between three songs."""
    return words1.intersection(words2).intersection(words3)

# visualization functions
def plot_average_word_lengths(song1, song2, song3):
    """Creates a bar chart to compare the average word lengths of the three songs."""
    avg_lengths = [avg_word_length(song1), avg_word_length(song2), avg_word_length(song3)]
    song_labels = ["Song 1", "Song 2", "Song 3"]

    plt.bar(song_labels, avg_lengths, color=["blue", "orange", "green"])
    plt.xlabel("Songs")
    plt.ylabel("Average Word Length")
    plt.title("Average Word Length Comparison")
    plt.ylim(0, max(avg_lengths) + 1)
    plt.show()

def shared_wordcloud(song1, song2, song3):
    """Creates a word cloud of shared vocabulary between three songs."""
    shared_words = shared_vocab(song1, song2, song3)
    print("Shared words:", shared_words)

    if not shared_words:
        print("No shared vocabulary found!")
        return
    
    # Weight words by their combined frequency across all songs
    freq = word_frequency(song1 + song2 + song3)
    word_dict = {word: freq[word] for word in shared_words}
    
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(word_dict)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Shared Vocabulary Word Cloud")
    plt.show()

def shared_venn_diagram(song1, song2, song3):
    """Creates a Venn diagram to visualize shared vocabulary between three songs."""
    plt.figure(figsize=(8, 8))
    venn3([words1, words2, words3], ("Song 1", "Song 2", "Song 3"))
    plt.title("Shared Vocabulary Venn Diagram")
    plt.show()

# main function to run everything
def main():
    print()
    print("song1 stats:", analyze_song(song1))
    print("song2 stats:", analyze_song(song2))
    print("song3 stats:", analyze_song(song3))
    print()
    print("song1 top words:", word_frequency(song1).most_common(10))
    print("song2 top words:", word_frequency(song2).most_common(10))
    print("song3 top words:", word_frequency(song3).most_common(10))
    print()
    print("song1 average word length:", avg_word_length(song1))
    print("song2 average word length:", avg_word_length(song2))
    print("song3 average word length:", avg_word_length(song3))
    print()
    print("Shared vocabulary between the three songs:", shared_vocab(song1, song2, song3))
    plot_average_word_lengths(song1, song2, song3)
    shared_wordcloud(song1, song2, song3)
    shared_venn_diagram(song1, song2, song3)

if __name__ == "__main__":
    main()
