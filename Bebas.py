from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#e5de00"
FOOD_COLOR = "#de0a26"
BACKGROUND_COLOR = "#000000"


class Snake:
  pass 

class Food:
  pass

def next_turn(snake, food):

def change_direction(new_direction):

def check_collisions(snake):

def game_over():



window = Tk()
window.title("Snake game")
window.resizable(False, False)

score = 0
direction = 'down'


label = Label(window, text="Score.{}".format(score), font = ('Consolas'))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()
