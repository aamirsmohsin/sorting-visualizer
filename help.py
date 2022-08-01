import pygame
import random
import math

pygame.init()

class Visualizer:

    # color schemes
    black = 0, 0, 0
    white = background_color = 255, 255, 255
    green = 0, 255, 0
    red = 255, 0, 0
    grey = 128, 128, 128

    # alternating bar colors
    gradients = [(128, 128, 128), (160, 160, 160), (192, 192, 192)]

    # font size
    font = pygame.font.SysFont('comicsans', 15)
    large_font = pygame.font.SysFont('comicsans', 20)

    # screen padding
    side_padding = 100
    top_padding = 150

    # constructor
    def __init__(self, width, height, list):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        self.set_list(list)

        pygame.display.set_caption("Sorting Visualization")
    
    # define position attributes
    def set_list(self, list):
        self.list = list
        
        self.min_val = min(list)
        self.max_val = max(list)

        # availalbe screen space / length of list
        self.block_width = round((self.width - self.side_padding) / len(list))
        
        # available screen space / range of values
        self.block_height = math.floor((self.height - self.top_padding) / (self.max_val - self.min_val))
        
        # first x-coordinate
        self.start_x = self.side_padding // 2

# create a list of random numbers
def generate_starting_list(n, min_val, max_val):
    nums = []

    for index in range(n):
        val = random.randint(min_val, max_val)
        nums.append(val)

    return nums

# draw the visualizer
def create(draw_info, algo_name, ascending):
    
    # draw background color
    draw_info.window.fill(draw_info.background_color)

    # draw algorithm and ascending/descending
    title = draw_info.large_font.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1, draw_info.black)
    draw_info.window.blit(title, (draw_info.width/2 - title.get_width()/2, 5))
    
    # draw controls
    controls = draw_info.font.render("R - Reset | Space - Start Sorting | A - Ascending | D - Descending", 1, draw_info.black)
    draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2, 35))

    # draw sorting controls
    sorting = draw_info.font.render("I - Insertion Sort | B - Bubble Sort | S - Selection Sort", 1, draw_info.black)
    draw_info.window.blit(sorting, (draw_info.width/2 - sorting.get_width()/2, 65))

    draw_list(draw_info)
    
    # render changes
    pygame.display.update()

# draw the array
def draw_list(draw_info, color_positions={}, clear_bg=False):
    nums = draw_info.list

    # draw over existing array
    if clear_bg:
        clear_rect = (draw_info.side_padding // 2, draw_info.top_padding, draw_info.width - draw_info.side_padding, 
                    draw_info.height - draw_info.top_padding)
        pygame.draw.rect(draw_info.window, draw_info.background_color, clear_rect)

    # draw new array
    for index, val in enumerate(nums):
        
        # left
        x = draw_info.start_x + index * draw_info.block_width
        
        # top
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

        color = draw_info.gradients[index % 3]

        if index in color_positions:
            color = color_positions[index]

        # draw column
        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))
    
    if clear_bg:
        pygame.display.update()

# bubble sort with ascending and descending options
def bubble_sort(draw_info, ascending=True):
    nums = draw_info.list

    for i in range(len(nums) - 1):
        for j in range(len(nums) - 1 - i):
            if (nums[j] > nums[j + 1] and ascending) or (nums[j] < nums[j + 1] and not ascending):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                draw_list(draw_info, {j: draw_info.green, j + 1: draw_info.red}, True)
                yield True

# insertion sort with ascending and descending options
def insertion_sort(draw_info, ascending=True):
    nums = draw_info.list

    for index in range(1, len(nums)):
        current = nums[index]

        while True:
            ascending_sort = index > 0 and nums[index - 1] > current and ascending
            descending_sort = index > 0 and nums[index - 1] < current and not ascending

            if not ascending_sort and not descending_sort:
                break
            
            nums[index] = nums[index - 1]
            index -= 1
            nums[index] = current
            draw_list(draw_info, {index - 1: draw_info.green, index: draw_info.red}, True)
            yield True

# selection sort with ascending and descending options
def selection_sort(draw_info, ascending=True):
    nums = draw_info.list

    for i in range(len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index] and ascending:
                min_index = j
            elif nums[j] > nums[min_index] and not ascending:
                min_index = j
        
        nums[i], nums[min_index] = nums[min_index], nums[i]
        draw_list(draw_info, {i: draw_info.green, min_index: draw_info.red}, True)
        yield True