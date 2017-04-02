# Daily Challenge for March 22nd, 2017
### Link to challenge
[here](https://www.reddit.com/r/dailyprogrammer/comments/611tqx/20170322_challenge_307_intermediate_scrabble/)

**Description**

What is the longest word you can build in a game of Scrabble one letter at a time? That is, starting with a valid two-letter word, how long a word can you build by playing one letter at a time on either side to form a valid three-letter word, then a valid four-letter word, and so on? (For example, HE could become THE, then THEM, then THEME, then THEMES, for a six-letter result.)

**Formal Inputs & Outputs**

Input Description
Using words found in a standard English language dictionary (or [enable1.txt](https://github.com/dolph/dictionary/blob/master/enable1.txt)).

Output description
Print your solution word and the chain you used to get there

**Notes/Hints**

Source: http://fivethirtyeight.com/features/this-challenge-will-boggle-your-mind/
Finally

This challenge was submitted by /u/franza73, many thanks! Have a good challenge idea? Consider submitting it to /r/dailyprogrammer_ideas

### My solution:
**NOTE:** Download the textfile linked above (`enable.txt`) and rename it to `words.txt`

My solution is naive, however it does produce accurate results. My program ran for roughly 10 minutes. The longest words found were:

* sheathers
* scrapings
* relapsers
