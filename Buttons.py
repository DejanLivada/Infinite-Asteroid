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
shop_main_menu = Dugme(mojFont.render("Back" , True , (255,255,255)) , pygame.Rect(20 , 500 , 150, 60) , (0,0,0))
equip_asteroidx = Dugme(mojFont.render("Equip" , True , (0,0,0)), pygame.Rect(120,170 , 170 , 60) , (255,255,255))
buy_invicibility = Dugme(mojFont.render("Buy" , True , (0,0,0)), pygame.Rect(150,400 , 110 , 60) , (255,255,255))
equip_invicibility = Dugme(mojFont.render("Equip" , True , (0,0,0)), pygame.Rect(120,400 , 170 , 60) , (255,255,255))
shop_next_page= Dugme(mojFont.render("Next" , True , (255,255,255)) , pygame.Rect(250 , 500 , 150, 60) , (0,0,0))