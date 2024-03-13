import pygame


get = pygame.event.get
def event_get():
    events = get()
    print(events)
    return events
pygame.event.get = event_get


import main
