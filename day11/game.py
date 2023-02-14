import random
import pygame
import sys
from pygame.locals import *

FPS = 30 # frames per second, the general speed of the program
WINDOW_WIDTH = 640 # size of window's width in pixels
WINDOW_HEIGHT = 480 # size of window's height in pixels
REVEAL_SPEED = 8 # speed boxes's sliding reveals and covers
BOX_SIZE = 40 # size of box height & width in pixels
GAP_SIZE = 10 # size of gap between boxes in pixels
BOARD_WIDTH = 10 # number of columns of icons
BOARD_HEIGHT = 7 # number of rows of icons

assert (BOARD_WIDTH * BOARD_HEIGHT) % 2 == 0, "Board needs to have a even number of boxes for pairs of matches."

X_MARGIN = int((WINDOW_WIDTH - (BOARD_WIDTH * (BOX_SIZE + GAP_SIZE))) / 2)
Y_MARGIN = int((WINDOW_HEIGHT - (BOARD_HEIGHT * (BOX_SIZE + GAP_SIZE))) / 2)

#               R    G    B       
GRAY        = (100, 100, 100)
NAVY_BLUE   = (60,  60,  100)
WHITE       = (255, 255, 255)
RED         = (255, 0,   0)
GREEN       = (0,   255, 0)
BLUE        = (0,   0,   255)
YELLOW      = (255, 255, 0)
ORANGE      = (255, 128, 0)
PURPLE      = (255, 0,   255)
CYAN        = (0,   255, 255)

BG_COLOR    = NAVY_BLUE
LIGHT_BG_COLOR = GRAY
BOX_COLOR = WHITE
HIGHLIGHT_COLOR = BLUE

DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

ALL_COLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALL_SHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)

assert len(ALL_COLORS) * len(ALL_SHAPES) * 2 >= BOARD_WIDTH * BOARD_HEIGHT, "Board is too big for the number of shapes/colors defined."


def get_randomized_board():
    # Get a list of every possible shape in every possible color.
    icons = []

    for color in ALL_COLORS:
        for shape in ALL_SHAPES:
            icons.append((shape, color))

    random.shuffle(icons) # randomize the order of the icons list
    num_icons_used = int(BOARD_WIDTH * BOARD_HEIGHT / 2) # calculate ho0w many icons are needed
    icons = icons[:num_icons_used] * 2 # make two of each

    random.shuffle(icons)
    # create the board data structure, with randomly placed icons.
    board = []

    for x in range(BOARD_WIDTH):
        column = []
        for y in range(BOARD_HEIGHT):
            column.append(icons[0])
            del icons[0] # remove the icons as we assign them
        board.append(column)
    
    return board


def generate_revealed_boxes_data(val):
    revealed_boxes = []

    for i in range(BOARD_WIDTH):
        revealed_boxes.append([val] * BOARD_HEIGHT)

    return revealed_boxes


def split_into_groups_of(group_size, the_list):
    # splits a list into a list of lists, where the inner lists have at
    # most group_size number of items.
    result = []

    for i in range(0, len(the_list), group_size):
        result.append(the_list[i:i + group_size])
    
    return result


def left_top_coords_of_box(boxx, boxy):
    # Convert board coordinates to pixel coordinates
    left = boxx * (BOX_SIZE + GAP_SIZE) + X_MARGIN
    top = boxy * (BOX_SIZE + GAP_SIZE) + Y_MARGIN
    return (left, top)


def start_game_animation(board):
    # Randomly reveal the boxes 8 at a time.
    covered_boxes = generate_revealed_boxes_data(False)

    boxes = []

    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            boxes.append((x, y))

    random.shuffle(boxes)

    box_groups = split_into_groups_of(8, boxes)

    draw_board(board, covered_boxes)

    for box_group in box_groups:
        reveal_boxes_animation(board, box_group)
        cover_boxes_animation(board, box_group)


def draw_board(board, revealed):
    # Draws all of the boxes in their covered or revealed state.
    for boxx in range(BOARD_WIDTH):
        for boxy in range(BOARD_HEIGHT):
            left, top = left_top_coords_of_box(boxx, boxy)
            if not revealed[boxx][boxy]:
                # Draw a covered box
                pygame.draw.rect(DISPLAYSURF, BOX_COLOR, (left, top, BOX_SIZE, BOX_SIZE))
            else:
                # Draw the (revealed) icon.
                shape, color = get_shape_and_color(board, boxx, boxy)
                draw_icon(shape, color, boxx, boxy)


def get_box_at_pixel(x, y):
    for boxx in range(BOARD_WIDTH):
        for boxy in range(BOARD_HEIGHT):
            left, top = left_top_coords_of_box(boxx, boxy)
            box_rect = pygame.Rect(left, top, BOX_SIZE, BOX_SIZE)
            if box_rect.collidepoint(x, y):
                return (boxx, boxy)
    return (None, None)


def draw_icon(shape, color, boxx, boxy):
    quarter = int(BOX_SIZE * 0.25) # syntactic sugar
    half    = int(BOX_SIZE * 0.5)  # syntactic sugar

    left, top = left_top_coords_of_box(boxx, boxy) # get pixel coords from board coords

    # Draw the shapes
    if shape == DONUT:
        pygame.draw.circle(DISPLAYSURF, color, (left + half, top + half), half - 5)
        pygame.draw.circle(DISPLAYSURF, BG_COLOR, (left + half, top + half), quarter - 5)
    elif shape == SQUARE:
        pygame.draw.rect(DISPLAYSURF, color, (left + quarter, top + quarter, BOX_SIZE - half, BOX_SIZE - half))
    elif shape == DIAMOND:
        pygame.draw.polygon(DISPLAYSURF, color, ((left + half, top), (left + BOX_SIZE - 1, top + half), (left + half, top + BOX_SIZE - 1), (left, top + half)))
    elif shape == LINES:
        for i in range(0, BOX_SIZE, 4):
            pygame.draw.line(DISPLAYSURF, color, (left, top + i), (left + i, top))
            pygame.draw.line(DISPLAYSURF, color, (left + i, top + BOX_SIZE - 1), (left + BOX_SIZE - 1, top + i))
    elif shape == OVAL:
        pygame.draw.ellipse(DISPLAYSURF, color, (left, top + quarter, BOX_SIZE, half))
    

def draw_highlight_box(boxx, boxy):
    left, top = left_top_coords_of_box(boxx, boxy)
    pygame.draw.rect(DISPLAYSURF, HIGHLIGHT_COLOR, (left - 5, top - 5, BOX_SIZE + 10, BOX_SIZE + 10), 4)


def reveal_boxes_animation(board, boxes_to_reveal):
    # Do the "box reveal" animation
    for coverage in range(BOX_SIZE, (-REVEAL_SPEED) - 1, -REVEAL_SPEED):
        draw_box_covers(board, boxes_to_reveal, coverage)


def get_shape_and_color(board, boxx, boxy):
    # shape value for x, y spot is stored in board[x][y][0]
    # color value for x, y spot is stored in board[x][y][1]
    return board[boxx][boxy][0], board[boxx][boxy][1]


def draw_box_covers(board, boxes, coverage):
    # Draws boxes being covered/revealed. "boxes" is a list
    # of two-item lists, which have the x & y spot of the box.
    for box in boxes:
        left, top = left_top_coords_of_box(box[0], box[1])
        pygame.draw.rect(DISPLAYSURF, BG_COLOR, (left, top, BOX_SIZE, BOX_SIZE))

        shape, color = get_shape_and_color(board, box[0], box[1])

        draw_icon(shape, color, box[0], box[1])

        if coverage > 0: # only draw the cover if there is an coverage
            pygame.draw.rect(DISPLAYSURF, BOX_COLOR, (left, top, coverage, BOX_SIZE))

    pygame.display.update()
    FPS_CLOCK.tick(FPS)


def cover_boxes_animation(board, boxes_to_cover):
    # Do the "box cover" animation.
    for coverage in range(0, BOX_SIZE + REVEAL_SPEED, REVEAL_SPEED):
        draw_box_covers(board, boxes_to_cover, coverage)


def has_won(revealed_boxes):
    # Returns True if all the boxes have been revealed, otherwise False
    for i in revealed_boxes:
        if False in i:
            return False # return False if any boxes are covered.
    return True


def game_won_animation(board):
    # flash the background color when the player has won
    covered_boxes = generate_revealed_boxes_data(True)

    color1 = LIGHT_BG_COLOR
    color2 = BG_COLOR

    for i in range(13):
        color1, color2 = color2, color1 # swap colors
        DISPLAYSURF.fill(color1)
        draw_board(board, covered_boxes)
        pygame.display.update()
        pygame.time.wait(300)


def main():
    global FPS_CLOCK, DISPLAYSURF
    pygame.init()

    FPS_CLOCK = pygame.time.Clock()

    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    mousex = 0 # used to store x coordinate of mouse event
    mousey = 0 # used to store y coordinate of mouse event

    pygame.display.set_caption("Memory Game")

    main_board = get_randomized_board()
    revealed_boxes = generate_revealed_boxes_data(False)

    first_selection = None # Store the (x, y) of the first box clicked.

    DISPLAYSURF.fill(BG_COLOR)

    start_game_animation(main_board)

    while True: # main game loop
        mouse_clicked = False

        DISPLAYSURF.fill(BG_COLOR) # drawing the window
        draw_board(main_board, revealed_boxes)

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.type == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouse_clicked = True
        
        boxx, boxy = get_box_at_pixel(mousex, mousey)

        if boxx != None and boxy != None:
            # The mouse is currently over a box
            if not revealed_boxes[boxx][boxy]:
                draw_highlight_box(boxx, boxy)

            if not revealed_boxes[boxx][boxy] and mouse_clicked:
                reveal_boxes_animation(main_board, [(boxx, boxy)])
                revealed_boxes[boxx][boxy] = True # set the box as "revealed"

                if first_selection == None: # the current box was the first box clicked
                    first_selection = (boxx, boxy)
                else: # the current box was the second box clicked
                    # Check if there is a match between the two icons
                    icon1_shape, icon1_color = get_shape_and_color(main_board, first_selection[0], first_selection[1])
                    icon2_shape, icon2_color = get_shape_and_color(main_board, boxx, boxy)

                    if icon1_shape != icon2_shape or icon1_color != icon2_color:
                        # Icons don't match. Re-cover up both selections.
                        pygame.time.wait(1000) # 1000 milliseconds = 1 sec
                        cover_boxes_animation(main_board, [(first_selection[0], first_selection[1]), (boxx, boxy)])
                        revealed_boxes[first_selection[0]][first_selection[1]] = False
                        revealed_boxes[boxx][boxy] = False
                    elif has_won(revealed_boxes): # check if all pairs found
                        game_won_animation(main_board)
                        pygame.time.wait(2000)

                        # Reset the board
                        main_board = get_randomized_board()
                        revealed_boxes = generate_revealed_boxes_data(False)

                        # Show the fully unrevealed board for a second.
                        draw_board(main_board, revealed_boxes)
                        pygame.display.update()

                        pygame.time.wait(1000)
                        # Replay the start game animation
                        start_game_animation(main_board)
                    first_selection = None # reset first_selection variable

        # Redraw the screen and wait a clock tick
        pygame.display.update()
        FPS_CLOCK.tick(FPS)


if __name__ == "__main__":
    main()