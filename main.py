import os

import pygame
from pygame.math import Vector2
import random
import sys
from Buttons import *
from os import path
import pickle

pygame.init()
prozor = pygame.display.set_mode((400, 600))
sat = pygame.time.Clock()
score_list = []
asteroidPng = "Slike/asteroid.png"
delete_all_asteroid_booster_slika = pygame.image.load("Slike/asteroidx.png")
delete_all_asteroid_booster_slika = pygame.transform.scale(delete_all_asteroid_booster_slika, (100, 100))


def nacrtaj_dugme_bez_centiranja(dugme):
    pygame.draw.rect(prozor, dugme.boja, dugme.rect)
    prozor.blit(dugme.tekst, dugme.rect.topleft)


class Ability:
    def __init__(self, slika, ability, pozicija, bought, equipped, cost):
        self.slika = slika
        self.ability = ability
        self.pozicija = pozicija
        self.bought = bought
        self.equipped = equipped
        self.cost = cost


asteroidx = Ability(pygame.image.load("Slike/asteroidx.png"), "asteroidx", (150, 30), False, False, 5000)
invicibility = Ability(pygame.image.load("Slike/skull.png"), "invicibility", (150, 250), False, False, 1500)
asteroidx.slika = pygame.transform.scale(asteroidx.slika, (100, 100))
invicibility.slika = pygame.transform.scale(invicibility.slika, (100, 100))


class Player:
    def __init__(self, pozicija: Vector2, brzina, slika, booster, health, coins):
        self.pozicija = pozicija
        self.brzina = brzina
        self.slika = slika
        self.booster = booster
        self.health = health
        self.coins = coins

    def move(self):
        x, _ = pygame.mouse.get_pos()
        self.pozicija.x = x

    def checkwalls(self):
        if self.pozicija.x >= 350:
            self.pozicija.x = 350
        if self.pozicija.x <= 0:
            self.pozicija.x = 0


class Booster:
    def __init__(self, slika, boost, pozicija, brzina):
        self.slika = pygame.transform.scale(slika, (50, 50))
        self.boost = boost
        self.pozicija = pozicija
        self.brzina = brzina

    def draw(self):
        prozor.blit(self.slika, self.pozicija)

    def fall(self):
        self.pozicija += self.brzina


class Kometa():
    def __init__(self, slika, pozicija: Vector2, brzina):
        self.slika = pygame.transform.scale(slika, (50, 50))
        self.pozicija = pozicija
        self.brzina = brzina

    def fall(self):
        self.pozicija.y += 10

    def change_pos(self):
        self.pozicija.x = random.randint(0, 350)

    def check_floor(self):
        if self.pozicija.y >= 600:
            self.pozicija.y = 20
            self.change_pos()

    def draw(self):
        prozor.blit(self.slika, self.pozicija)


font = pygame.font.Font(None, 60)
text = font.render("You lose!", True, (255, 255, 255))
score = 0
if path.exists("Saves/bought_items.pickle"):
    with open("Saves/bought_items.pickle", "rb") as f:
        asteroidx.bought = pickle.load(f)
if path.exists("Saves/bought_item_inv.pickle"):
    with open("Saves/bought_item_inv.pickle", "rb") as f:
        invicibility.bought = pickle.load(f)

lista_kometa = [
    Kometa(pygame.image.load("Slike/asteroid.png"), Vector2(random.randint(0, 350), 50), 10),
    Kometa(pygame.image.load("Slike/asteroid.png"), Vector2(random.randint(0, 350), -70), 10),
    Kometa(pygame.image.load("Slike/asteroid.png"), Vector2(random.randint(0, 350), -140), 10),
    Kometa(pygame.image.load("Slike/asteroid.png"), Vector2(random.randint(0, 350), -210), 10),
    Kometa(pygame.image.load("Slike/asteroid.png"), Vector2(random.randint(0, 350), -290), 10),
    Kometa(pygame.image.load("Slike/asteroid.png"), Vector2(random.randint(0, 350), -350), 10),
    Kometa(pygame.image.load("Slike/asteroid.png"), Vector2(random.randint(0, 350), -460), 10)
]

igrac = Player(Vector2(250, 500), 5, pygame.image.load("Slike/igrac.png"), None, 1, 0)
igrac.slika = pygame.transform.scale(igrac.slika, (50, 50))

lista_boostera = [
    Booster(pygame.image.load("Slike/skull.png"), "speed", Vector2(random.randint(0, 350), 0), Vector2(0, 10)),


]


def spawn_booster():

    if random.randrange(0, 100) < 1:

        lista_boostera.append(Booster(pygame.image.load("Slike/skull.png"), "speed", Vector2(random.randint(0, 350), 0), Vector2(0, 10)))
    for booster in lista_boostera:
        booster.draw()
        booster.fall()



def crtaj_komete():
    global score
    for kometa in lista_kometa:
        kometa.draw()
        kometa.fall()
        kometa.check_floor()



high_score = 0
if path.exists("Saves/savegame.pickle"):
    with open("Saves/savegame.pickle", "rb") as f:
        high_score = pickle.load(f)
        high_score_text = font.render(f"High Score : {high_score}", True, (255, 255, 255))
if path.exists("Saves/coins.pickle"):
    with open("Saves/coins.pickle", "rb") as f:
        igrac.coins = pickle.load(f)


def god_mode():
    igrac.coins = 999999
    global high_score
    high_score = 999999


def main_menu():
    program_radi = True
    while program_radi:
        for dogadjaj in pygame.event.get():
            if dogadjaj.type == pygame.QUIT:
                program_radi = False
                sys.exit()
            if dogadjaj.type == pygame.MOUSEBUTTONDOWN:
                if play_dugme.rect.collidepoint(dogadjaj.pos):
                    play()
                if shop_dugme.rect.collidepoint(dogadjaj.pos):
                    shop_page1()
                if exit_dugme.rect.collidepoint(dogadjaj.pos):
                    sys.exit()
        os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
        global score
        score = 0
        prozor.fill((0, 250, 217))
        nacrtaj_dugme_bez_centiranja(play_dugme)
        nacrtaj_dugme_bez_centiranja(shop_dugme)
        nacrtaj_dugme_bez_centiranja(exit_dugme)
        pygame.display.flip()
        sat.tick(30)

    pygame.quit()


def death_scr():
    program_radi = True
    while program_radi:
        for dogadjaj in pygame.event.get():
            if dogadjaj.type == pygame.QUIT:
                program_radi = False
                sys.exit()
            if dogadjaj.type == pygame.MOUSEBUTTONDOWN:
                if death_main_menu.rect.collidepoint(dogadjaj.pos):
                    main_menu()
                    program_radi = False
        global lista_kometa
        os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
        lista_kometa = [
            Kometa(pygame.image.load(asteroidPng), Vector2(random.randint(0, 350), 50), 10),
            Kometa(pygame.image.load(asteroidPng), Vector2(random.randint(0, 350), -70), 10),
            Kometa(pygame.image.load(asteroidPng), Vector2(random.randint(0, 350), -140), 10),
            Kometa(pygame.image.load(asteroidPng), Vector2(random.randint(0, 350), -210), 10),
            Kometa(pygame.image.load(asteroidPng), Vector2(random.randint(0, 350), -290), 10),
            Kometa(pygame.image.load(asteroidPng), Vector2(random.randint(0, 350), -350), 10),
            Kometa(pygame.image.load(asteroidPng), Vector2(random.randint(0, 350), -460), 10)
        ]
        score_text_death = font.render(f"Score : {score}", True, (255, 255, 255))
        global score_list
        global high_score_text
        score_list.append(score)
        prozor.fill((0, 0, 0))
        prozor.blit(text, (120, 100))
        prozor.blit(score_text_death, (120, 200))
        prozor.blit(high_score_text, (30, 50))
        nacrtaj_dugme_bez_centiranja(death_main_menu)
        pygame.display.flip()
        sat.tick(30)
        high_score = max(score_list)
        session_high_score = high_score
        if path.exists("Saves/savegame.pickle"):
            with open("Saves/savegame.pickle", "rb") as f:
                high_score = pickle.load(f)
                if session_high_score > high_score:
                    high_score = session_high_score
                    with open("Saves/savegame.pickle", "wb") as f:
                        pickle.dump(high_score, f)

        else:
            with open("Saves/savegame.pickle", "wb") as f:
                pickle.dump(high_score, f)
        with open("Saves/coins.pickle", "wb") as f:
            pickle.dump(igrac.coins, f)
    pygame.quit()


def checkbooster():
    dugmici = pygame.key.get_pressed()
    global booster_iskoriscen
    if dugmici[pygame.K_SPACE] and booster_iskoriscen == False:
        if igrac.booster == "asteroidx":
            global lista_kometa
            global asteroidPng
            lista_kometa = [
                Kometa(pygame.image.load(asteroidPng), Vector2(random.randint(0, 350), 50), 10),
                Kometa(pygame.image.load(asteroidPng), Vector2(random.randint(0, 350), -70), 10),
                Kometa(pygame.image.load(asteroidPng), Vector2(random.randint(0, 350), -140), 10),
                Kometa(pygame.image.load(asteroidPng), Vector2(random.randint(0, 350), -210), 10),
                Kometa(pygame.image.load(asteroidPng), Vector2(random.randint(0, 350), -290), 10),
                Kometa(pygame.image.load(asteroidPng), Vector2(random.randint(0, 350), -350), 10),
                Kometa(pygame.image.load(asteroidPng), Vector2(random.randint(0, 350), -460), 10)
            ]
        if igrac.booster == "invicibility":
            igrac.health += 1

        booster_iskoriscen = True


def give_coins():
    igrac.coins += 0.010


def check_death():
    for death in lista_kometa:
        if death.slika.get_rect().move(death.pozicija).colliderect(igrac.slika.get_rect().move(igrac.pozicija)):
            igrac.health -= 1
            death.change_pos()
            if igrac.health == 0:
                death_scr()


def shop_page1():
    program_radi = True
    while program_radi:
        for dogadjaj in pygame.event.get():
            if dogadjaj.type == pygame.QUIT:
                program_radi = False
                sys.exit()
            if dogadjaj.type == pygame.MOUSEBUTTONDOWN:
                if buy_asteroidx.rect.collidepoint(dogadjaj.pos) and igrac.coins >= 500 and asteroidx.bought == False:
                    igrac.coins -= 500
                    asteroidx.bought = True
                    with open("Saves/bought_items.pickle", "wb") as f:
                        pickle.dump(asteroidx.bought, f)
                if shop_main_menu.rect.collidepoint(dogadjaj.pos):
                    return
                if equip_asteroidx.rect.collidepoint(dogadjaj.pos) and asteroidx.bought == True:
                    asteroidx.equipped = True
                    invicibility.equipped = False
                    igrac.booster = asteroidx.ability
                if buy_invicibility.rect.collidepoint(
                        dogadjaj.pos) and igrac.coins >= 200 and invicibility.bought == False:
                    igrac.coins -= 200
                    invicibility.bought = True
                    asteroidx.equipped = False
                    with open("Saves/bought_item_inv.pickle", "wb") as f:
                        pickle.dump(invicibility.bought, f)
                if equip_invicibility.rect.collidepoint(dogadjaj.pos) and invicibility.bought == True:
                    invicibility.equipped = True
                    asteroidx.equipped = False
                    igrac.booster = invicibility.ability
            # if shop_next_page.rect.collidepoint(dogadjaj.pos):
            #   shop_page2()
        prozor.fill((0, 250, 217))
        prozor.blit(asteroidx.slika, asteroidx.pozicija)
        prozor.blit(invicibility.slika, invicibility.pozicija)
        coins_text = mali_font.render(f"Coins : {int(igrac.coins)}", True, (255, 255, 255))
        os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
        prozor.blit(coins_text, (0, 0))
        if asteroidx.bought == True and asteroidx.equipped == False:
            nacrtaj_dugme_bez_centiranja(equip_asteroidx)
        if asteroidx.bought == False:
            asteroidx_price = mali_font.render("Price: 500", True, (255, 255, 255))
            prozor.blit(asteroidx_price, (120, 130))
            nacrtaj_dugme_bez_centiranja(buy_asteroidx)
        if invicibility.bought == False:
            nacrtaj_dugme_bez_centiranja(buy_invicibility)
            invicibility_price = mali_font.render("Price: 200", True, (255, 255, 255))
            prozor.blit(invicibility_price, (120, 370))
        if invicibility.bought == True and invicibility.equipped == False:
            nacrtaj_dugme_bez_centiranja(equip_invicibility)
        # nacrtaj_dugme_bez_centiranja(shop_next_page)
        nacrtaj_dugme_bez_centiranja(shop_main_menu)
        pygame.display.flip()
        sat.tick(30)

    pygame.quit()


def shop_page2():
    program_radi = True
    while program_radi:
        for dogadjaj in pygame.event.get():
            if dogadjaj.type == pygame.QUIT:
                program_radi = False

        prozor.fill((0, 250, 217))

        pygame.display.flip()
        sat.tick(30)

    pygame.quit()


def play():
    global booster_iskoriscen
    igrac.health = 1
    booster_iskoriscen = False
    program_radi = True
    while program_radi:
        for dogadjaj in pygame.event.get():
            if dogadjaj.type == pygame.QUIT:
                program_radi = False
                sys.exit()
        global score
        global high_score_text
        high_score_text = font.render(f"High Score : {high_score}", True, (255, 255, 255))
        prozor.fill((0, 0, 0))
        score_text = font.render(f"Score : {score}", True, (255, 255, 255))
        prozor.blit(score_text, (0, 0))
        igrac.move()
        score += 2
        checkbooster()
        spawn_booster()
        give_coins()
        igrac.checkwalls()
        check_death()
        prozor.blit(igrac.slika, igrac.pozicija)
        crtaj_komete()

        pygame.display.flip()
        sat.tick(30)

    pygame.quit()


main_menu()
pygame.quit()
