from help import *

def main():
    
    # window open 
    run = True
    
    # window instance
    nums = generate_starting_list(50, 5, 100)
    visualizer = Visualizer(800, 600, nums)

    clock = pygame.time.Clock()
    
    sorting = False
    ascending = True

    # generator
    sorting_algorithm = bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting_algorithm_generator = None

    # window open
    while run:
        clock.tick(240)

        # call next() on the generator until complete
        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            create(visualizer, sorting_algo_name, ascending)

        # track key-strokes
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type != pygame.KEYDOWN:
                continue
                
            if event.key == pygame.K_x:
                run = False

            if event.key == pygame.K_r:
                nums = generate_starting_list(50, 5, 100)
                visualizer.set_list(nums)
                sorting = False

            elif event.key == pygame.K_SPACE and not sorting:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(visualizer, ascending)

            elif event.key == pygame.K_a and not sorting:
                ascending = True
            
            elif event.key == pygame.K_d and not sorting:
                ascending = False
            
            elif event.key == pygame.K_i and not sorting:
                sorting_algorithm = insertion_sort
                sorting_algo_name = "Insertion Sort"
            
            elif event.key == pygame.K_b and not sorting:
                sorting_algorithm = bubble_sort
                sorting_algo_name = "Bubble Sort"
            
            elif event.key == pygame.K_s and not sorting:
                sorting_algorithm = selection_sort
                sorting_algo_name = "Selection Sort"
        
    pygame.quit()

if __name__ == "__main__":
    main()