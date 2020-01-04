# Notes - Chapter 11: "Web Scraping"

## Modules of focus

* **webbrowser** - Comes with Python and opens a browser to a specific page.
* **requests** - Downloads files and web pages from the internet.
* **bs4** - Parses HTML, the format that web pages are written in.
* **selenium** - Launches and controls a web browser. The selenium module is able to fill in forms and simulate mouse clicks in this browser

## webbrowser

> A web browser tab will open to the URL https://inventwithpython.com/. This is about the only thing the webbrowser module can do.

    import webbrowser
    webbrowser.open('https://inventwithpython.com/')

You can also use the **pyperclip** module to grab and use clipboard content.

    import pyperclip
    address = pyperclip.paste()

## requests

> ~~The requests module was written because Python’s urllib2 module is too complicated to use. In fact, take a permanent marker and black out this entire paragraph. Forget I ever mentioned urllib2.~~ If you need to download things from the web, just use the requests module.

    >>> import requests
    >>> res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
    >>> type(res)
    <class 'requests.models.Response'>
    >>> res.status_code == requests.codes.ok
    True
    >>> len(res.text)
    178981
    >>> print(res.text[:250])
    The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare

    This eBook is for the use of anyone anywhere at no cost and with
    almost no restrictions whatsoever.  You may copy it, give it away or
    re-use it under the terms of the Proje

What happens when the request fails?

    >>> import requests
    >>> res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
    >>> res.raise_for_status()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/usr/lib/python3/dist-packages/requests/models.py", line 935, in raise_for_status
        raise HTTPError(http_error_msg, response=self)
    requests.exceptions.HTTPError: 404 Client Error: Not Found for url: https://inventwithpython.com/   page_that_does_not_exist

A better idea: call raise_for_status() after calling requests.get(). You want to be sure that the download has actually worked before your program continues.

    >>> try:
            res.raise_for_status()
        except Exception as exc:
            print('There was a problem: %s' % (exc))
    There was a problem: 404 Client Error: Not Found for url: https://inventwithpython.com/page_that_does_not_exist

In the chapter, there's a bit about saving file chunks, but it made me feel queasy so I am omitting it.

## HTML

No, you're not learning HTML here. But here are some basics:

* The tags tell the browser how to format the web page.
* A starting tag and closing tag can enclose some text to form an element.
* The text (or inner HTML) is the content between the starting and closing tags.
* Some tags have extra properties in the form of attributes within the angle brackets. For example, the \<a\> tag encloses text that should be a link. The URL that the text links to is determined by the href attribute.

        Al's free <a href="https://inventwithpython.com">Python books</a>.

* Some elements have an id attribute that is used to uniquely identify the element in the page.

You can view the source of any website from most browsers, but the real juice is in the Developer Tools. Use the Developer Tools to find and inspect the elements of a page.

## bs4

Now the fun begins. Using bs4 is gonna feel like a mix between reading hieroglyphics, looking for a needle in a haystack, and using the claw machine from an arcade. It's not impossible to get what you're looking for, but you should be prepared to spend more than a few minutes trying to decypher someone else's HTML, pin down which element has the thing you're looking for, and carefully direct bs4 to help you find it programmatically.

Using bs4 and the BeautifulSoup class is going to look a lot like this:

    >>> import requests, bs4
    >>> res = requests.get('https://nostarch.com')
    >>> res.raise_for_status()
    >>> noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
    >>> type(noStarchSoup)
    <class 'bs4.BeautifulSoup'>

At this point in the chapter, there are a bunch of great and simple examples demonstrating how use the select(), getText(), get(), and attrs methods. Go ahead and dig into that. Instead I'm going to demo some real world examples I put together based on my whims and wants.

## Web scraping demos

These are some actual things I actually wrote to attempt to solve my actual first world problems.

### Find socks

My wife asked me if the python stuff I'm learning can be used to tell her when socks arrive on the New York And Company website. "Sure", I said, as I began work on a script that I had every intentino of finishing. Seven months later and I put together something that just takes in a query string and returns either "No results found" or the number of results found.

https://github.com/conflabermits/Scripts/blob/master/python/sock_scanner/sock_scanner.py

    $ ./sock_scanner.py --query socks
    26 results found!
    $ ./sock_scanner.py --query quijibo
    No results found.

### Get price of Uniqlo clothes

On a particularly cold day in December, while debating with myself whether or not I should move south, I went to the mall with my wife. I poked around in the store looking at their warmer threads and thought that if I waited until after Christmas or New Years I could probably get a better deal on some of their microfleece undershirts and underpants. I put together a simple script that takes in a URL and returns the price of the item.

https://github.com/conflabermits/Scripts/blob/master/python/uniqlo/uniqlo_product_price_scanner.py

    $ ./uniqlo_product_price_scanner.py --url "https://www.uniqlo.com/us/en/men-heattech-ultra-warm-turtleneck-long-sleeve-t-shirt-420942.html"
    Item price is 29.90
    $ ./uniqlo_product_price_scanner.py --url "https://www.uniqlo.com/us/en/men-heattech-extra-warm-turtleneck-long-sleeve-t-shirt-418797.html?dwvar_418797_color=COL08&cgid=men-heattech-collection#start=14&cgid=men-heattech-collection"
    Item price is 24.90
    $ ./uniqlo_product_price_scanner.py --url "https://www.uniqlo.com/us/en/duck-billed-platypus"
    There was a problem with the response from the URL: 410 Client Error: Gone for url: https://www.uniqlo.com/us/en/duck-billed-platypus

### Pokedex list generator

On my week off I spent a bunch of time playing the new Pokemon game. I set a goal that I, for the first time ever in a core Pokemon game, would catch and trade as much as I needed to in order to fill the Pokedex. Stop judging. What I needed was an easier way to track which of the 400 pokemon I had registered already and which remained. Since I was sharing this responsibility with my wife I decided a Google Sheets page was easiest, but I needed a quick and easy way to fill the cells with the number and names of all 400 pokemon, and I wasn't about to do it manually.

https://github.com/conflabermits/Scripts/blob/master/python/pokemon/pokedex_list_generator.py

    $ ./pokedex_list_generator.py --url "https://pokemondb.net/pokedex/game/sword-shield"
    #001,Grookey,Grass
    #002,Thwackey,Grass
    #003,Rillaboom,Grass
    #004,Scorbunny,Fire
    #005,Raboot,Fire
    #006,Cinderace,Fire
    ...
    #397,Dragapult,Dragon,Ghost
    #398,Zacian,Fairy,Steel
    #399,Zamazenta,Fighting,Steel
    #400,Eternatus,Poison,Dragon
    $ ./pokedex_list_generator.py --url "https://pokemondb.net/pokedex/game/pot-pan"
    There was a problem with the response from the URL: 404 Client Error: Not Found for url: https://pokemondb.net/pokedex/game/pot-pan

## selenium

> The selenium module lets Python directly control the browser by programmatically clicking links and filling in login information

I wasn't able to test any of this. Also, the chapter explains all of this better than I ever could. Go read the chapter if you're interested in this.
