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


class Player:
    def __init__(self, pozicija: Vector2, brzina, slika , booster):
        self.pozicija = pozicija
        self.brzina = brzina
        self.slika = slika
        self.booster = booster
    def move(self):
        x, _ = pygame.mouse.get_pos()
        self.pozicija.x = x

    def checkwalls(self):
        if self.pozicija.x >= 350:
            self.pozicija.x = 350
        if self.pozicija.x <= 0:
            self.pozicija.x = 0



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

lista_kometa = [
    Kometa(pygame.image.load("Slike/asteroid.png"), Vector2(random.randint(0, 350), 50), 10),
    Kometa(pygame.image.load("Slike/asteroid.png"), Vector2(random.randint(0, 350), -70), 10),
    Kometa(pygame.image.load("Slike/asteroid.png"), Vector2(random.randint(0, 350), -140), 10),
    Kometa(pygame.image.load("Slike/asteroid.png"), Vector2(random.randint(0, 350), -210), 10),
    Kometa(pygame.image.load("Slike/asteroid.png"), Vector2(random.randint(0, 350), -290), 10),
    Kometa(pygame.image.load("Slike/asteroid.png"), Vector2(random.randint(0, 350), -350), 10),
    Kometa(pygame.image.load("Slike/asteroid.png"), Vector2(random.randint(0, 350), -460), 10)
]
igrac = Player(Vector2(250, 500), 5, pygame.image.load("Slike/igrac.png") , "asteroidx")
igrac.slika = pygame.transform.scale(igrac.slika, (50, 50))


def crtaj_komete():
    global score
    for kometa in lista_kometa:
        kometa.draw()
        kometa.fall()
        kometa.check_floor()


if path.exists("Saves/savegame.pickle"):
    with open("Saves/savegame.pickle", "rb") as f:
        high_score = pickle.load(f)
        high_score_text = font.render(f"High Score : {high_score}" , True , (255,255,255))

def main_menu():
    program_radi = True
    while program_radi:
        for dogadjaj in pygame.event.get():
            if dogadjaj.type == pygame.QUIT:
                program_radi = False
            if dogadjaj.type == pygame.MOUSEBUTTONDOWN:
                if play_dugme.rect.collidepoint(dogadjaj.pos):
                    play()
                if shop_dugme.rect.collidepoint(dogadjaj.pos):
                    shop()

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
            if dogadjaj.type == pygame.MOUSEBUTTONDOWN:
                if death_main_menu.rect.collidepoint(dogadjaj.pos):
                    main_menu()
                    program_radi = False
        global lista_kometa

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

    pygame.quit()
booster_iskoriscen = False

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
        booster_iskoriscen = True



def check_death():
    for death in lista_kometa:
        if death.slika.get_rect().move(death.pozicija).colliderect(igrac.slika.get_rect().move(igrac.pozicija)):
            death_scr()

def shop():
    program_radi = True
    while program_radi:
        for dogadjaj in pygame.event.get():
            if dogadjaj.type == pygame.QUIT:
                program_radi = False

        prozor.fill((0, 250, 217))

        prozor.blit(delete_all_asteroid_booster_slika , (150,20))
        nacrtaj_dugme_bez_centiranja(buy_asteroidx)
        pygame.display.flip()
        sat.tick(30)

    pygame.quit()

def play():
    program_radi = True
    while program_radi:
        for dogadjaj in pygame.event.get():
            if dogadjaj.type == pygame.QUIT:
                program_radi = False
        global score
        prozor.fill((0, 0, 0))
        score_text = font.render(f"Score : {score}", True, (255, 255, 255))
        prozor.blit(score_text, (0, 0))
        igrac.move()
        score += 2
        checkbooster()
        igrac.checkwalls()
        check_death()
        prozor.blit(igrac.slika, igrac.pozicija)
        crtaj_komete()
        pygame.display.flip()
        sat.tick(30)


    pygame.quit()


main_menu()
pygame.quit()