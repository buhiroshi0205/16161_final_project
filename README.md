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
- `createhtml.py`: Script used to generate an html version of the game playable in a web browser.

## Playing the game

If you have python3 installed on your computer, then you navigate to the `src` folder in terminal and then run `main.py` by typing `python3 main.py` and pressing enter. From the root directory this looks like:
```sh
$ cd src
$ python3 main.py
```

Otherwise you can also play this game via the browser at <http://www.andrew.cmu.edu/user/bw1/projects/16161/>. This link is subject to change after the year 2018, but the changes will always be reflected here.

## Themes explored

#### Choice and narrative

This choose-your-own-adventure game is fundamentally a multi-narrative story. However, all these narratives arise from the same background situation, and roughly talk about the same events. However, the different choices you make influence the narrative and the perspective greatly. Narrative is not something that is set in stone. It is subject to perspective, which is subject to choices. Your choice influences your narrative of the same events.

#### Information and truth

SPOILERS!
I designed this game so that different playthroughs can give you vastly different information about the same events. In a "peaceful" playthrough where you choose mostly conservative choices, your AI is seen to succeed and prevent lots of disasters from happening. However, only if you replay the game and choose the other "risky" route are you exposed to more information that talks about the other side of everything. It reveals that the government is not just using AI to prevent disasters, but also breaking the bottommost bounds of privacy rights. Further, the success of your AI and prevention of disasters was at costs of lots of innocent people being sent to jail. The different information that you get reveals different truths about the same events, as also explored in our group concept map. And sometimes, this difference can be so big that it portrays truth in polar opposites.

#### Risk and ethics

Ethics is often blurry. In each of the endings, you can never be sure if what you did was ethical or not. Choosing conservatively is the least risky, however is it ethical? Choosing actively/liberally is more risky and *maybe* allows you to change the world, but is it ethical? Did you change the world for good or for bad? (SPOILER) Was plugging in the USB to stop the evil masterplan ethical? Was sacrificing yourself worth it? What if the USB didn't even do anything good at all, and that person was actually just a fraud? These uncertainties about ethics are all risks that you take when you make your decisions. Sometimes ethics are easier defined and risks are minimum, other times it's not and the risk of making an ultimately bad decision is high. In such a situation, there doesn't seem to be much one can do, except to do their best to understand the stakes at hand to clarify the risks as much as possible.

#### And other themes as well