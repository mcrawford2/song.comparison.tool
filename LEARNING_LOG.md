## Date: 2026-04-04

**Goals:**
- Count word frequencies using a dictionary
- Print the top 10 most common words and basic stats (word count, unique words)

**What I asked AI to do:**
- Load the txt files (song1.txt, song2.txt, song3.txt) under pre-written variables (song1, song2, song3)
- Help with understanding generated lines, such as with:
    - import re                           # 're' is used for regular expressions to clean and split words.
    - from collections import Counter     # 'Counter' is used to count the frequency of each word in the song.
- It also helped create word_frequency

**What I didn't understand in the generated code:**
- In some AI generated code, lines appeared to be more grayed out than others
- (r...)

**What I learned:**
- Dimed code means that code may be inactive in the current context of the rest of the surrounding code
- (r...) refers to a raw string



## Date: 2026-04-06

**Goals:**
- 2 interesting questions:
1. Find average word length per song, to help determine reading level
2. Find shared vocabulary between all three songs

**What I asked AI to do:**
- While typing, AI automatically generated avg_word_length (lines 48-50)

**What I didn't understand in the generated code:**
- re.findall() for avg_word_length this context, even though it also appeared under word_frequency
- Why there needed to be an if/else statement in finding average word length

**What I learned:**
- re.findall() finds all matches and returns them in a list (). In the context of avg_word_length, it extracts all words tohave their letters counted. 
- Including else = 0 for avg_word_length prevents a division by zero error.
    - If there are no words extracted from the song, len(words) would be 0, causing a crash because anything / 0 = undefined. The else statement safely returns 0 when the words list is empty.


## Date: 2026-04-08

**Goals:**
- Finish/clean previous questions

**What I asked AI to do:**
- Automatic AI code generation helped with creating shared_vocab()

**What I didn't understand in the generated code:**
- After most new functions, a new 'if __name__ == "__main__":' is created. I was unsure if it was stable for there to be multiple of these, or if the overall program would be better with just one main call at the end. 

**What I learned:**
- After asking AI about having multiple 'if __name__ == "__main__":', I learned that it is technicaly ok to have many of them. Each block only runs when the script is executed directly, but having many will make the script harder to read and may lead to issues with wrong orders of execution or duplicating outputs. For cleanliness, I changed the script to have one, all inclusive main call at the end. 



## Date: 2026-04-09

**Goals:**
- 1 visualization
1. Bar chart for average word length per song

**What I asked AI to do:**
- Fix indentation issues
- Fix error:    import matplotlib.pyplot as plt
                ModuleNotFoundError: No module named 'matplotlib'

**What I didn't understand in the generated code:**
- This code was pretty stright forward, the only aspect I did not fully grasp at first was importing matplotlib.pyplot but this was necessary to create data visualizations.

**What I learned:**
-Importing the matplotlib.pyplot presented difficulties, as it came with many consecutive errors. The main problem was the environment I was running python in was blocking package installs. I fixed this by selecting a different python interpreter (python.exe). 



## Date: 2026-04-12 - 2026-04-10

**Goals:**
- 2 more visualizations
2. Wordcloud for shared vocab
3. Venn diagram for shared vocab

**What I asked AI to do:**
- How to start creating a wordcloud (needed to pip install)
- Help fixing error when initial wordcloud led to errors
- Add labels (words) to venn diagram, rather than just undefined numbers
- Make long word lists easier to read by wrapping into multiple lines, make sure words don't overlap

**What I didn't understand in the generated code:**
- I didn't understand the need to add "if not shared_words: ... return" in my wordcloud function 
- Why the initial code only allowed two words in the wordcoud, because even if the words were sized based on their frequency, other words should still be appearing smaller. It is possible that this occured because the txt files are so short, so words that overlap in songs but only appear once per song might have been left out of the wordcloud.

**What I learned:**
- I had to pip install wordcloud in order to successfully create a wordcloud
- "if not shared_words:... return" is important so that the function doesn't crash if there are no shared words.
- Editing visualizations to be truly visually understandable and efficient methods of communication information makes a big difference. Had I not changed the labels of the venn diagram, it would have taken more effort from the reader to grasp what the output of the visualization was.