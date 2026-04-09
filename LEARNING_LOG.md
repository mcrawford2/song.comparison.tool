## Date: 2026-04-04

**Goals:**
- Count word frequencies using a dictionary
- Print the top 10 most common words and basic stats (word count, unique words)

**What I asked AI to do:**
- load the txt files (song1.txt, song2.txt, song3.txt) under pre-written variables (song1, song2, song3)
- help with understanding generated lines, such as with:
    - import re                           # 're' is used for regular expressions to clean and split words.
    - from collections import Counter     # 'Counter' is used to count the frequency of each word in the song.
- it also helped create word_frequency

**What I didn't understand in the generated code:**
- in some AI generated code, lines appeared to be more grayed out than others
- (r...)

**What I learned:**
- dimed code means that code may be inactive in the current context of the rest of the surrounding code
- (r...) refers to a raw string



## Date: 2026-04-06

**Goals:**
- 2 interesting questions:
1. find average word length per song, to help determine reading level
2. find shared vocabulary between all three songs

**What I asked AI to do:**
- While typing, AI automatically generated avg_word_length (lines 48-50)

**What I didn't understand in the generated code:**
- re.findall() for avg_word_length this context, even though it also appeared under word_frequency
- why there needed to be an if/else statement in finding average word length

**What I learned:**
- re.findall() finds all matches and returns them in a list (). In the context of avg_word_length, it extracts all words tohave their letters counted. 
- including else = 0 for avg_word_length prevents a division by zero error.
    - If there are no words extracted from the song, len(words) would be 0, causing a crash because anything / 0 = undefined. The else statement safely returns 0 when the words list is empty.


## Date: 2026-04-08

**Goals:**
- finish/clean previous questions

**What I asked AI to do:**
- Automatic AI code generation helped with creating shared_vocab()

**What I didn't understand in the generated code:**
- after most new functions, a new 'if __name__ == "__main__":' is created. I was unsure if it was stable for there to be multiple of these, or if the overall program would be better with just one main call at the end. 

**What I learned:**
- After asking AI about having multiple 'if __name__ == "__main__":', I learned that it is technicaly ok to have many of them. Each block only runs when the script is executed directly, but having many will make the script harder to read and may lead to issues with wrong orders of execution or duplicating outputs. For cleanliness, I changed the script to have one, all inclusive main call at the end. 



## Date: 2026-04-09

**Goals:**
- 1 visualization
1. bar chart for average word length per song

**What I asked AI to do:**
- fix indentation issues
- fix error:    import matplotlib.pyplot as plt
                ModuleNotFoundError: No module named 'matplotlib'

**What I didn't understand in the generated code:**
- this code was pretty stright forward, the only aspect I did not fully grasp at first was importing matplotlib.pyplot but this was necessary to create data visualizations.

**What I learned:**
- importing the matplotlib.pyplot presented difficulties, as it came with many consecutive errors. The main problem was the environment I was running python in was blocking package installs. I fixed this by selecting a different python interpreter (python.exe). 



## Date: 2026-04-10

**Goals:**
- 1 more visualization
2. wordcloud for shared vocab?
- clean all txts

**What I asked AI to do:**
- how to start creating a wordcloud
- help fixing error when wordcloud led to errors

**What I didn't understand in the generated code:**
- i needed to add "if not shared_words: ... return" in my wordcloud function so that the function wouldn't crash if there were no shared words.
- the initial code only allowed two words in the wordcoud because the words were sized based on their frequency. This is beneficial for _____ but did not work for this wordcloud because with such short txt files, it makes sense for some words to only appear once. i like the size based on frequency, but not if that deletes other important words (reword)

**What I learned:**
- had to pip install wordcloud