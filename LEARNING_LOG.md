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


## Date: 2026-04-07

**Goals:**
- finish/clean previous questions

**What I asked AI to do:**
- helped with creating shared_vocab()


**What I didn't understand in the generated code:**

**What I learned:**



## Date: 2026-04-08

**Goals:**
- 1 visualization
1. 
- clean all txts

**What I asked AI to do:**


**What I didn't understand in the generated code:**

**What I learned:**