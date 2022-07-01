# Summary

This is an attempt at making a "Wordle Helper" (and maybe one day a "Wordle Solver").

I'm creating this as part of a livestream on [Twitch](https://www.twitch.tv/conflabermits). Stream notes [here](https://github.com/conflabermits/Scripts/blob/master/stream/pilot/004/notes.md).

# Status

This program is unfinished, but here's what it can do so far:

* Loads a "dictionary" file with about 16k five-letter words.
* Collects user input for misses and greens. (Collects yellows too but doesn't do anything with them yet.)
* Creates a new word list that filters out any words containing letters that aren't in the solution word.
* Uses the filtered word list to look for words where the green letters are in the right places and puts them in a "final" word list.
* Prints the contents and length of the "final" word list.

## Examples

```text
$ ./wordle_helper.py --misses d l p n m o e --greens 2u 4t
Misses: ['d', 'l', 'p', 'n', 'm', 'o', 'e']
Greens: ['2u', '4t']
Yellows: None
Total suggested guesses: 41
['rusts', 'butts', 'hurts', 'gurts', 'tuath', 'gusty', 'quits', 'kurta', 'tutty', 'rusty', 'quata', 'juxta', 'tutti', 'suits', 'butty', 'qurti', 'quitu', 'jutty', 'busty', 'yurts', 'justs', 'gutti', 'rutty', 'tufts', 'cutty', 'kusti', 'busti', 'hurty', 'sutta', 'fusty', 'tufty', 'cubti', 'gutta', 'yurta', 'gutty', 'suity', 'busts', 'jufts', 'gusts', 'kutta', 'jufti']
```

# Details

## What the program should do

Ideally this Wordle Helper would allow a user to specify which letters are used and where the yellow and green letters are, and return a list of words that could be possible answers.

## Possible requirements or enhancements

* There are three expected types of letter inputs: misses, yellows, and greens.
  * Yellows and greens are location-specific.
  * A letter can be a yellow AND a green.
  * A yellow or green letter can show up more than once.
* It would be cool if guesses were sorted by how many high-value or commonly-used letters they have.
* For the sake of readability, the number of listed guesses should probably be limited to 10 or 20.
* I'm planning to build this as a command line tool first. Building it as a web page, eventually, might be a nice way to break up the logic and the HTML design work.
  * I'm starting this in Python, but I really *really* don't want to mess with how to build and deploy something like this in Python. I might migrate it over to Go if that makes more sense as a server/page/program platform.

## How the word list was made

I used the dictionary file from my countdown script to generate a file containing only five-letter words for this project, using this command:

```egrep "^.....$" ../countdown/words_alpha.txt > five-letter-words.txt```

