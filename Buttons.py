import pygame
pygame.init()
mojFont = pygame.font.SysFont('Consolas', 60)
mali_font = pygame.font.SysFont('Consolas', 30)

class Dugme:
    def __init__(self , tekst , rect , boja):
        self.tekst = tekst
        self.rect = rect
        self.boja = boja
play_dugme = Dugme(mojFont.render("Play" , True , (255,255,255)) , pygame.Rect(130 , 100 , 150 , 60) , (0,0,0))
shop_dugme = Dugme(mojFont.render("Shop" , True , (255,255,255)) , pygame.Rect(130 , 250 , 150, 60) , (0,0,0))
exit_dugme = Dugme(mojFont.render("Exit" , True , (255,255,255)) , pygame.Rect(130 , 400 , 150, 60) , (0,0,0))
death_main_menu = Dugme(mali_font.render("Back to Main Menu" , True , (255,255,255)) , pygame.Rect(60 , 400 , 300, 40) , (4, 255, 0))
buy_asteroidx = Dugme(mojFont.render("Buy" , True , (0,0,0)), pygame.Rect(150,170 , 110 , 60) , (255,255,255))