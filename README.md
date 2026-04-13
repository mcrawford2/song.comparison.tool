# What does this project do?
This project analyzes and compares the lyrics of three songs, all from the 1980's. It performs numerical analysis including line count, word count, and average words per line of each individual song. It also finds the top 10 most frequent words, average word length, and the vocabulary shared across all three songs. This project visualizes these findings through three diagram types: a bar chart comparing average word lengths across the songs, a word cloud of the shared vocabulary (weighted by combined frequency), and a venn diagram showing vocabulary overlap between every combination of songs.

# How do I run it?
1. Install necessary imports (re, textwrap, collections, matplotlib.pyplot/plt, wordcloud, matplotlib_venn/venn3)
2. Prepare and load files (song1 - You Make My Dreams Come True by Hall and Oates, song2 - Don't Dream It's Over by Crowded House, song3 - Everybody Wants To Rule The World by Tears for Fears)
3. Run the script. It runs through 'def main():...' and 'if __name__ == "__main__":
    main()', which includes numeroud functions for each yupe of analysis and visualization. They are as follows:
    - def analyze_song(song) - basic song statistics. Strips empty lines, then counts total lines, total words, and computes average words per line for each song.
    - def word_frequency(song) - uses re.findall with the pattern [a-zA-Z']+ to extract words (lowercased, apostrophes preserved for words like don't), counts them with Counter, and returns the 10 most common. 
    - def avg_word_length(song) - extracts all words, sums their character lengths, and divides by total word count.
    - def shared_vocab(song1, song2, song3) - takes the set intersection of all three songs' unique word sets (computed at the top of the file using re.findall into a set).
    - def plot_average_word_lengths(song1, song2, song3) - plots the three average word lengths as a color-coded bar chart using plt.bar. A window will pop up and needs to be closed in order to continue. 
    - def shared_wordcloud(song1, song2, song3) - finds the shared vocabulary of all three songs and weights each word by its combined frequency across all three songs. Displays wordcloud in pop up and needs to be closed in order to continue.
    - def shared_venn_diagram(song1, song2, song3) - draws a three-circle venn diagram. The four overlap regions (Song 1+2, Song 1+3, Song 2+3, and Song 1+2+3) have their words listed in labeled boxes with arrows pointing into the corresponding region. This window also needs to be closed to finish.

# Conclusions

# Two Pass Approach
