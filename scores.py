import pygame
import variables
from sprites import Button
import json
import datetime

def Score(screen):
    
    """
    Function that handles the score screen as well as writing and
    reading scores into a json file
    """
    clock = pygame.time.Clock()
    header_group = pygame.sprite.GroupSingle(Button("Scores:",(350,100) ))
    header_group.sprite.active = True
    header_group.sprite.redraw()
    button_group_1 = pygame.sprite.Group()
    button_group_2 = pygame.sprite.GroupSingle()
    button_group_2.add(Button("Quit", (350,600)))
    button_group_2.sprite.active = True
    button_group_2.sprite.redraw()
    
    bg = pygame.transform.scale(pygame.image.load('assets/background/score.jpg'), variables.window).convert()

    # Reading and writing files
    with open('scores/scores.json', 'r+') as file:
        print(variables.score)
        if variables.score != 0:
            file_data = json.load(file)
            file_data["scores"].append({datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"): variables.score})
            file.seek(0)
            json.dump(file_data, file, indent = 4)

    with open('scores/scores.json', 'r') as f:
        file_scores = json.load(f)["scores"]
        print(file_scores)
        button_group_1.empty()
        counter = 0
        for i in reversed(file_scores):
            if counter < 4:
                button_group_1.add(Button(str(i).replace('{', " ").replace('}', " "), (350,200 + counter * 100)))
            counter += 1
            

    while True:
        # Input Handler
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                exit()
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_RETURN:
                    return "Menu"
                
        # Render
        screen.blit(bg, (0,0))
        button_group_1.draw(screen)
        for i in button_group_1.sprites():
            i.active = True
            i.redraw()
        button_group_2.draw(screen)
        header_group.draw(screen)
        pygame.display.update()
        clock.tick(60)
