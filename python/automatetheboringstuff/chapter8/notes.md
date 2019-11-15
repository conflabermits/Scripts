# Chapter 8 notes

## "Reading and Writing Files"

### Basics

* What is a file
* What is a directory
* What is the root folder on Windows, OSX, and Linux (W/O/L)
* How other volumes are mounted on W/O/L
* Windows uses backslashes (\) while OSX and Linux use forward slashes (/)
* Absolute path vs relative path
* "*" refers to current working directory
* "**" refers to the parent directory of the current working directory

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

* `os.path.split()` will split a full path into a tuple with the dirname and basenames as its two values.

        calcFilePath = 'C:\\Windows\\System32\\calc.exe'
        os.path.split(calcFilePath)
        ('C:\\Windows\\System32', 'calc.exe')

* If you want to split a path into a list of its successive dirnames/basenames, use the split() string method.

        calcFilePath = 'C:\\Windows\\System32\\calc.exe'
        calcFilePath.split(os.path.sep)
        ['C:', 'Windows', 'System32', 'calc.exe']

## LEAVING OFF ON "FINDING FILE SIZES AND FOLDER CONTENTS" SECTION