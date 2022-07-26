# Wordle Helper

## Summary

This is an attempt at making a "Wordle Helper" (and maybe one day a "Wordle Solver").

I'm creating this as part of a livestream on [Twitch](https://www.twitch.tv/conflabermits). The notes span multiple streams, [here](https://github.com/conflabermits/Scripts/blob/master/stream/pilot/004/notes.md), [here](https://github.com/conflabermits/Scripts/blob/master/stream/pilot/005/notes.md), and [here](https://github.com/conflabermits/Scripts/blob/master/stream/pilot/006/notes.md).

## Status

This program is unfinished, but here's what it can do so far:

* Loads a "dictionary" file with about 16k five-letter words.
* Collects user input for misses, yellows, and greens.
* Identifies duplicate letters to ensure logic for misses doesn't remove guesses it shouldn't.
* Filters out any words containing letters that aren't in the solution word.
* Identifies words that have letters matching the given green letters in the right places and filters out the rest.
* Identifies words that have letters matching the given yellow letters in other parts of the word and filters out the rest.
* Sorts and prints the contents of the final word list, as well as its length.

I still need to figure out how best to filter and display the suggested guesses. I should also consider a better way to enter some of this info since the current method might not work for handling duplicate letters under certain conditions.

## Details

### What the program should do

Ideally this Wordle Helper would allow a user to specify which letters are used and where the yellow and green letters are, and return a list of words that could be possible answers.

### Examples

Example where second letter `U` and fourth letter `T` are green, and missed letters include `D`, `L`, `P`, `N`, `M`, `O`, and `E`. Solution word is `RUSTY`.

```text
$ ./wordle_helper.py --misses d l p n m o e --greens 2u 4t
Misses: ['d', 'l', 'p', 'n', 'm', 'o', 'e']
Greens: ['2u', '4t']
Yellows: None
Total suggested guesses: 41
['rusts', 'butts', 'hurts', 'gurts', 'tuath', 'gusty', 'quits', 'kurta', 'tutty', 'rusty', 'quata', 'juxta', 'tutti', 'suits', 'butty', 'qurti', 'quitu', 'jutty', 'busty', 'yurts', 'justs', 'gutti', 'rutty', 'tufts', 'cutty', 'kusti', 'busti', 'hurty', 'sutta', 'fusty', 'tufty', 'cubti', 'gutta', 'yurta', 'gutty', 'suity', 'busts', 'jufts', 'gusts', 'kutta', 'jufti']
```

Example where first guess, `TORTS`, returns `YMMGG` and second guess, `PITTS`, returns `MMGGG`. (`M`=miss; `G`=green; `Y`=yellow.) Solution word is `BUTTS`.

```text
$ #solution=BUTTS #guess1=TORTS=YMMGG #guess2=PITTS=MMGGG ./wordle_helper.py --misses o r p i --greens 3t 4t 5s --yellows 1t
chris@Win11Desktop:/local/git/Scripts/python/wordle$ solution=BUTTS #guess1=TORTS=YMMGG #guess2=PITTS=MMGGG ./wordle_helper.py --misses o r p i --greens 3t 4t 5s --yellows 1t
chris@Win11Desktop:/local/git/Scripts/python/wordle$ ./wordle_helper.py --misses o r p i --greens 3t 4t 5s --yellows 1t
Misses: ['o', 'r', 'p', 'i']
Greens: ['3t', '4t', '5s']
Yellows: ['1t']
All letters: ['t', 't', 's', 't', 'o', 'r', 'p', 'i']
Duplicate letters: {'t'}
Total suggested guesses: 7
['batts', 'butts', 'matts', 'mutts', 'netts', 'watts', 'yetts']
```

### Testing

Some basic test cases, using pytest, were added to catch functional regressions and help identify if changes create a new problem or solve an existing one.

```text
$ pytest --verbose test_wordle_helper.py
============================================== test session starts ==============================================
platform linux -- Python 3.6.9, pytest-6.1.2, py-1.9.0, pluggy-0.13.1 -- /usr/bin/python3
rootdir: /local/git/Scripts/python/wordle
collected 7 items

test_wordle_helper.py::test_load_words PASSED                                                             [ 14%]
test_wordle_helper.py::test_process_misses[missed_letters0-dupe_letters0-expected_result0] PASSED         [ 28%]
test_wordle_helper.py::test_process_misses[missed_letters1-dupe_letters1-expected_result1] PASSED         [ 42%]
test_wordle_helper.py::test_process_greens[green_letters0-expected_result0] PASSED                        [ 57%]
test_wordle_helper.py::test_process_greens[green_letters1-expected_result1] PASSED                        [ 71%]
test_wordle_helper.py::test_process_yellows[yellow_letters0-expected_result0] PASSED                      [ 85%]
test_wordle_helper.py::test_process_yellows[yellow_letters1-expected_result1] PASSED                      [100%]

=============================================== 7 passed in 0.05s ===============================================
```

### Possible requirements or enhancements

* It should verify its inputs to ensure we have letters and numbers where we expect them, and not symbols or emoji.
* It would be cool if guesses were sorted by how many high-value or commonly-used letters they have.
* Another cool feature would be "desired letters" (maybe could use a better name here). You could narrow the suggested guesses by asking the program to only include guesses that have certain letters.
* For the sake of readability, the number of listed guesses should probably be limited to 10 or 20.
* I'm planning to build this as a command line tool first. Building it as a web page, eventually, might be a nice way to break up the logic and the HTML design work.
  * I'm starting this in Python, but I really *really* don't want to mess with how to build and deploy something like this in Python. I might migrate it over to Go if that makes more sense as a server/page/program platform.

### How the word list was made

I used the dictionary file from my countdown script to generate a file containing only five-letter words for this project, using this command:

```egrep "^.....$" ../countdown/words_alpha.txt > five-letter-words.txt```
