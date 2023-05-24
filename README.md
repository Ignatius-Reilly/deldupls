# deldupls.py

Non-recursively looks for duplicate files inside a folder and offer to delete them, keeping only one of the duplicates.

## Warning

`deldupls` **is not intended for commercial use**.

It can delete files in your computer, and this operation may be irreversible.

It was coded by an amateur programmer for personal use and as a learning exercise.
Everybody is free to use it or modify it, but It's your responsibility to understand how it works.
It comes without warranty!

## Parameters:

- path=\<path of the folder where files are located\>
    - path can be absolute or relative to current folder.
    - If no path is selected, the current folder is used.


- safe=\<True | False>
    - If safe=False or not specified it compares files only by size and hash.
    - If safe=True files that are of the same size and have the same hash are additionally compared by content.
