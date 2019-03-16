# C4

## What is C4?

C4 is a game that allows 2 players to duel in a game of Connect 4.
The game follows a simple concept; players will take turns dropping their disks
on the 6x7 board. The first player to connect 4 disks vertically, horizontally
or diagonally wins the game.

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

1) You will also need to install pygame. Open up Windows PowerShell or the Terminal,
depending on the operating system you are using. Once open, paste and run the command
displayed below.

```
python3 -m pip install -U pygame --user
```

2) Use Windows PowerShell or Terminal again to git clone the C4 files using
the command below. It will usually be saved in your user directory.

```
git clone https://github.com/osamaramihafez/c4.git
```

You have successfully installed C4!

### Running the Game

1) Go to the directory that you have git cloned the game in.

2) Once in the directory, double click on 'c4' followed by 'src'. You will see
a file called 'c4.py'.

If saved in the User Directory:

```
C:\Users\<User Name>\c4\src
```

3) Right click 'c4.py' and then click "Edit with IDLE"

4) Once python opens with the code, press 'f5'

Congratulations! You are now running C4!

### How to Play

1) While in the main menu, you will have to chose to play singleplayer or
multiplayer. Click on the desired one.

2) Before entering the actual game, select the colour you want for your
disks. If multiplayer was clicked previously, the second player will also get
the opportunity to pick a desired colour. The game will then start.

3.1) [Singleplayer] Click on the location where you would like to place a disk.
Note that the disk will fall to the bottom of the grid or on top on another disk.
The computer will automatically place a disk after your turn. This sequence will
go back and forth.

3.2) [Multiplayer] Click on the location where you would like to place a disk.
Note that the disk will fall to the bottom of the grid or on top on another disk.
Instead of a computer, the second player will choose a location to place their
disk. This sequence will go back and forth.

4) Try to win. The first player to get four disks in a row vertically,
horizontally, or diagonally wins.

5) Once the game is over, there are two options. Click on 'Restart' to play the
same game mode again from scratch. Click on 'Main Menu' to be sent back to the
main menu.

6) To close the application, click on the 'X' on the top right or top left side
of your window.

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

This game is built under the [MIT License](https://tasdikrahman.mit-license.org/)
