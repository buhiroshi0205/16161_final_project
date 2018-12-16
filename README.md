# AI & Humanity (Fall 2018) Individual Futuring Project

A text-based choose-your-own-adventure game about narrative, information, and surveillance in an AI age.

## Navigating this repository

In the root folder:
- `README.md`: This explanation file you're currently reading
- `draft_storyboard.pdf`: A tentative storyboard for the plot used for drafting stage; the final product significantly differs from it.
- `src`: The folder that contains the code and data to run a basic version of this project

In the `src` folder:
- `main.py`: The script used to run an instance of the game
- `data.json`: All the data about the story to feed to `main.py`
- `visualize.py`: A script for visualizing the storyline based on data.json. This was mainly for development purposes. It requires the package `graphviz` installed.
- `Digraph.gv.svg`: Output from `visualize.py`. The node labels don't make much sense, as they were intended for developer use.

## Playing the game

If you have python3 installed on your computer, then you navigate to the `src` folder in terminal and then run `main.py` by typing `python3 main.py` and pressing enter. From the root directory this looks like:
```sh
$ cd src
$ python3 main.py
```

Otherwise you can also play this game via the browser at <http://www.andrew.cmu.edu/user/bw1/projects/16161F18/>. This link is subject to change after year 2018, but the changes will always be reflected here.