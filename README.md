# C4

## What is C4?

C4 is a game that allows 2 players to duel in a game of Connect 4.
The game follows a simple concept; players will take turns dropping their disks
on the 6x7 board. The first player to connect 4 disks vertically, horizontally
or diagonally wins the game.

![main menu](https://user-images.githubusercontent.com/24720900/54757784-50548b00-4bc1-11e9-85c9-1db55f266923.PNG)

![gmae](https://user-images.githubusercontent.com/24720900/54757786-50548b00-4bc1-11e9-8b19-6c7c2df9b8d3.png)

![help menu](https://user-images.githubusercontent.com/24720900/54757781-4fbbf480-4bc1-11e9-8e4e-437cea88795c.png)

### Requirements

Things you will need before installation:
* Windows OS / Mac OS X / Ubuntu
* 512MB of RAM (Minimum)
* 2MB of Hard Disk Space (Minimum)

### Installation

1) You will need to install the latest version of python 3. The link to the
download page will be below.

```
https://www.python.org/downloads/
```

2) You will need to install Wing for Python if you need to use 
option 2 to run the game (next topic in README). The link to download 
wing is below.

```
https://wingware.com/downloads/wing-personal
```

3) You will also need to install pygame. Open up Windows PowerShell or the Terminal,
depending on the operating system you are using. Once open, paste and run the command
displayed below.

```
python3 -m pip install -U pygame --user
```

4) Use Windows PowerShell or Terminal again to git clone the C4 files using
the command below. It will usually be saved in your user directory. Alternatively, 
you can download the zip folder from the link below.

```
git clone https://github.com/osamaramihafez/c4.git
```
or
```
https://github.com/osamaramihafez/c4/archive/master.zip
```


You have successfully installed C4!

### Running the Game

There are 2 options to run this game. 'Option 1' is to be used if 
'Option 2' does not work.

* Option 1 
    1) Open up PowerShell or Terminal
    2) Go to the directory you saved the game
    3) Enter the src folder
    4) Type the command that works for you
  
    ```
    py c4.py
    ```
   or
    ```
    python c4.py
    ```
 * Option 2
    1) Go to the game directory through file explorer
    2) Enter the 'src' folder
    
    If you saved it in your user directory:
    ```
    C:\Users\<User Name>\c4\src
    ```
    
    3) Open 'c4.py' with Wing
    4) When the file open, run the game by pressing 'f5' or
        by clicking the green play button at the top of your
        screen

Congratulations! You are now running C4!

### How to Play

1) While in the main menu, you will see the button called 'Play'. 
Click on that button to begin your connect four game.

2) Click on the column where you would like to place a disk.
Note that the disk will fall to the bottom of the column or on top on another disk.
The second player will now choose a column to place their disk. This sequence will 
continue to go back and forth until the game is over.

4) Try to win. The first player to get four disks in a row vertically,
horizontally, or diagonally wins.

5) While you are playing the game, you can click the 'back' button to return 
to the main menu. This is useful if you want to visit the 'How to Play' section.
Don't worry, your game progress will be saved!

6) Once the game is over, you can click on 'X' on your window to terminate the 
program. You can also click on the 'restart' button, it will send you to the main 
menu where you can choose to play the game again.

7) For more information, click on the 'How to Play' button in the main menu.

### Documentation

Refer to '[documentation.pdf](https://github.com/osamaramihafez/c4/blob/master/documentation.pdf)' in the c4 directory.

### Built With

* [Python](https://www.python.org/downloads/)
* [Pygame](https://www.pygame.org/wiki/GettingStarted)
* [Wing](https://wingware.com/downloads/wing-personal)

### Authors

The following five people contributed to the development of this game:
* [Liam Aiello](https://github.com/garboguy)
* [Thamodh Egodawatte](https://github.com/tego17)
* [Osama Hafez](https://github.com/osamaramihafez)
* [Venura Perera](https://github.com/venuraperera99)
* [Kevin Subhash](https://github.com/KevinSub)

### License

This game is built under the [MIT License](https://tasdikrahman.mit-license.org/).

### Acknowledgements

We give credit to the following people for helping us develop this game.

* [Harrison Kensley](https://pythonprogramming.net/pygame-start-menu-tutorial/) - With the help of his tutorial, we were able to make a proper GUI with button functionalities.
* [Billie Thompson](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2) - Her README.md template helped guide us in making our very first README.md.
