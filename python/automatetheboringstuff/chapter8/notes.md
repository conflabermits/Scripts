# Chapter 8 notes

## "Reading and Writing Files"

### Basics

* What is a file
* What is a directory
* What is the root folder on Windows, OSX, and Linux
* How other volumes are mounted on Windows, OSX, and Linux
* Windows uses backslashes (\\) while OSX and Linux use forward slashes (/)
* Absolute path vs relative path
* "*" refers to current working directory
* "**" refers to the parent directory of the current working directory
* Plaintext vs binary files

### Using the OS module

Using os.path.join to pull together OS-compatible paths:

    import os
    os.path.join('usr', 'bin', 'spam')

    'usr\\bin\\spam'

OK, cool... but how do I get the root folder ("C:\" or "/") in the mix? [STACK OVERFLOW TO THE RESCUE](https://stackoverflow.com/questions/17429044/constructing-absolute-path-with-os-path-join)!

> Using `os.sep` as root worked for me:
> 
>       path.join(os.sep, 'python', 'bin')
> 
> Linux: `/python/bin`
> 
> Windows: `\python\bin`
> 
> Adding `path.abspath()` to the mix will give you drive letters on Windows as well and is still compatible with Linux:
> 
>       path.abspath(path.join(os.sep, 'python', 'bin'))
> 
> Linux: `/python/bin`
> 
> Windows: `C:\python\bin`

    os.path.abspath(os.path.join(os.sep, 'usr', 'bin', 'python3'))
    
    '/usr/bin/python3'

More os module stuff:
* Get the current working directory:

        os.getcwd()

* Change directory:

        os.chdir('C:\\Users\\conflabermits\\AppData')

* Create new directory/directories:

        os.makedirs('C:\\local')
        os.makedirs('C:\\local\\temp\\20191121')

* Calling os.path.abspath(path) will return a string of the absolute path of the argument. This is an easy way to convert a relative path into an absolute one.

        os.path.abspath('.')
        os.path.abspath('.\\Scripts')

* Calling os.path.isabs(path) will return True if the argument is an absolute path and False if it is a relative path.

        os.path.isabs('.')
        os.path.isabs(os.path.abspath('.'))

* Calling os.path.relpath(path, start) will return a string of a relative path from the start path to path. If start is not provided, the current working directory is used as the start path.

        os.getcwd()
        '/home/chris/Scripts/python/automatetheboringstuff/chapter8'
        
        os.path.relpath('/usr/bin/python3')
        '../../../../../../usr/bin/python3'
        
        os.path.relpath('/usr/bin/python3', '/')
        'usr/bin/python3'
        
        os.path.relpath('/usr/bin/python3', '/home/chris')
        '../../usr/bin/python3'

Dir name vs base name:
* Calling `os.path.dirname(path)` will return a string of everything that comes before the last slash in the path argument.
* Calling `os.path.basename(path)` will return a string of everything that comes after the last slash in the path argument.

![Image Example](https://automatetheboringstuff.com/images/000041.png)

    os.getcwd()
    '/home/chris/Scripts/python/automatetheboringstuff/chapter8'

    testdir = os.path.join(os.getcwd(), 'testdir')
    testfile = os.path.join(os.getcwd(), 'testfile.txt')
    print(testdir)
    /home/chris/Scripts/python/automatetheboringstuff/chapter8/testdir

    print(testfile)
    /home/chris/Scripts/python/automatetheboringstuff/chapter8/testfile.txt

    os.path.dirname(testdir)
    '/home/chris/Scripts/python/automatetheboringstuff/chapter8'

    os.path.basename(testdir)
    'testdir'

    os.path.dirname(testfile)
    '/home/chris/Scripts/python/automatetheboringstuff/chapter8'

    os.path.basename(testfile)
    'testfile.txt'

`os.path.split()` will split a full path into a tuple with the dirname and basenames as its two values.

    calcFilePath = 'C:\\Windows\\System32\\calc.exe'
    os.path.split(calcFilePath)
    ('C:\\Windows\\System32', 'calc.exe')

If you want to split a path into a list of its successive dirnames/basenames, use the split() string method.

    calcFilePath = 'C:\\Windows\\System32\\calc.exe'
    calcFilePath.split(os.path.sep)
    ['C:', 'Windows', 'System32', 'calc.exe']

Examples for getsize, listdir, etc.

    os.getcwd()

    os.path.getsize('notes.md')
    4100

    os.path.getsize('testdir')
    4096

    os.listdir()
    ['notes.md', 'testdir', 'testfile.txt']

    os.listdir('.')
    ['notes.md', 'testdir', 'testfile.txt']

    os.listdir('./')
    ['notes.md', 'testdir', 'testfile.txt']

    os.listdir('../')
    ['chapter8']

    totalSize = 0
    for filename in os.listdir():
        totalSize = totalSize + os.path.getsize(filename)
    print(totalSize)

Other useful methods:

* Calling `os.path.exists(path)` will return True if the file or folder referred to in the argument exists and will return False if it does not exist.
* Calling `os.path.isfile(path)` will return True if the path argument exists and is a file and will return False otherwise.
* Calling `os.path.isdir(path)` will return True if the path argument exists and is a folder and will return False otherwise.

### Manipulating files

There are three steps to reading or writing files in Python.

1. Call the `open()` function to return a `File` object.
    * `open()` will take a second argument to specify which mode to open the file with:
        * `'r'`: readonly (default mode; no write)
        * `'w'`: write (overwrites existing file; creates new file if needed)
        * `'a'`: append (writes without overwriting; creates new file if needed)
        * `'x'`: create (no write, only create)
1. Call the `read()` or `write()` method on the `File` object.
1. Close the file by calling the `close()` method on the `File` object.

Sonnet example:

    sonnetFile = open('sonnet29.txt')

    sonnetFile.readlines()
    ["When, in disgrace with fortune and men's eyes,\n", 'I all alone beweep my outcast state,\n', 'And trouble deaf heaven with my bootless cries,\n', 'And look upon myself and curse my fate,\n']

    sonnetFile.close()

    sonnetFile.readlines()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: I/O operation on closed file.

#### Reading vs writing vs appending

Reading

    testfile = open('testfile.txt', 'r')

    testfile.readlines()
    ['test text\n']

    testfile.close()

Writing

    testfile = open('testfile.txt', 'w')

    testfile.readlines()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    io.UnsupportedOperation: not readable

    testfile.close()

Creating

    testfile = open('testfile.txt', 'x')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    FileExistsError: [Errno 17] File exists: 'testfile.txt'

Write + read

    testfile = open('testfile.txt', 'w+')

    testfile.readlines()
    []

    testfile.write('First line')
    10

    testfile.write('Second line')
    11

    testfile.readlines()
    []

    testfile.close()

    testfile = open('testfile.txt', 'r')

    testfile.readlines()
    ['First lineSecond line']

    testfile.close()

Append + read

    testfile = open('testfile.txt', 'a+')

    testfile.readlines()
    []

    testfile.write('Another line\n')
    13

    testfile.readlines()
    []

    testfile.close()

    testfile = open('testfile.txt', 'r')

    testfile.readlines()
    ['First lineSecond lineAnother line\n']

    testfile.close()

Append without read

    testfile = open('testfile.txt', 'a')

    testfile.readlines()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    io.UnsupportedOperation: not readable

    testfile.write('Last line\n')
    10

    testfile.close()

    testfile = open('testfile.txt', 'r')

    testfile.readlines()
    ['First lineSecond lineAnother line\n', 'Last line\n']

    testfile.close()

# LEFT OFF AT: Saving Variables with the shelve Module
# REMAINING: Saving Variables with the pprint.pformat() Function
