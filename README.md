<p align="center">
    <img width=40% src="https://github.com/vreaw/Game-of-Life/blob/main/media/life.gif">
</p>


<h1 align="center"> The Game of life </h1>

This is a simple implementation of Conway’s Game of Life in python3. The source code emphasises simplicity and intuitive code rather than efficiency.

## Getting started

Because this is just a small educational script, I have chosen not to distribute it on PyPI. The only dependencie is `matplotlib`, which can be installed easily via `pip`:

```bash
pip3 install matplotlib
```
To get started, navigate to a directory where you want to use the project, then clone it with:

```bash
git clone https://github.com/vreaw/Game-of-Life.git
```
Move into the directory that was just created (either through your filesystem or with `cd Game-of-Life `), and you are ready to go!

```bash
python3 life.py
```

## About Conway’s Game of Life
The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970.
It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. It is Turing complete and can simulate a universal constructor or any other Turing machine.

# Rules
Each cell with one or no neighbours dies because of loneliness. Each cell with four or more neighbours dies because of overpopulation. Each cell with two or three neighbours survives.
