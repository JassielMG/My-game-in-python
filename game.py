import string
from Words import words
from Words import esp_words
from Display_hangman import Display
from Music import music
import random
import time
import string
import os
import unidecode
import pygame

class Game(Display,music):
    def __init__(self,word,language):
        self.word = word.upper()
        self.word_letters = set(self.word)
        self.complete = set()
        self.alphabet = set(string.ascii_uppercase)
        self.used_letters = set()
        self.language = language
        self.score = 0

    def play_hangman(self):

        self.errors = 0
        self.end=True

        while self.end:

            word_list = [letter if letter in self.used_letters else '_' for letter in self.word]

            print(self.word)
            print('Current word: ', ' '.join(word_list))
            self.show_hangman()


            if self.end == True:
                print('You have used these letters: ', ' '.join(self.used_letters))
                user_letter = input('Ingresa una letra: ').upper()
                self.word_test(user_letter)

        return True



    def show_hangman(self):
        show_image = [Display.nobody, Display.head, Display.body, Display.left_arm,
                      Display.right_arm, Display.left_leg, Display.right_leg, Display.dead]

        for i in range(len(show_image)):
            if self.errors == i and i !=  7:
                show_image[i](self)
            elif self.errors == len(show_image) - 1:
                os.system('clear')
                show_image[-1](self)


                music.music_end(self)
                self.end = False

                print('Se murio... la palabra era :  ', self.word)
                print(f'Puntaje final: {self.score}')

                if i == 7:
                    self.score=0



    def word_test(self,user_letter):

        if user_letter in (self.alphabet - self.used_letters):
            self.used_letters.add(user_letter)
            if user_letter in self.word_letters:
                music.music_success_letter(self)

                os.system('clear')
                self.word_letters.remove(user_letter)
            else:
                music.music_wrong_letter(self)

                os.system('clear')
                self.errors += 1
        elif user_letter in self.used_letters:
            self.music_repeat_letter()

            os.system('clear')
            print('La letra ya esta utilizada, intenta con otra!')

        else:
            self.music_invalid_character()
            os.system('clear')
            print('Carecter invalido, porfavor intenta otra vez')

        if set(self.word_letters) == set():
            self.music_success_word()

            self.score += len(self.word) * 10

            self.reset_word()


    def reset_word(self):

        self.used_letters = set()
        self.word = self.choice_word(self.language)
        self.word = self.word.upper()
        self.word_letters = set(self.word)
        self.complete = set()
        self.play_hangman()


    def choice_word(self,language):
        if language == 1:
            word = unidecode.unidecode(random.choice(words))
        elif language == 2:
            word = unidecode.unidecode(random.choice(esp_words))
        return word


def menu():
    salir = False
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load('music_efects/battle_cry.wav')
    pygame.mixer.music.play()

    while not salir:
        try:
            language = int(input("""
            *********************** Welcome to hangman game ********************
            
            Instrucciones: Consigue el puntaje mas alto adivinando todas las palabras que puedas antes
            de que se forme la figura del ahorcado.
            
            Selecciona el idioma de las palabras (press 1 or 2): 
             (1) English
             (2) Español
            """))
            if language == 1 or language == 2:
                salir=True
            else:
                raise ValueError
        except ValueError:
            print('Option invalid try again..')

    return language


def choice_word(language):
    if language == 1:
        word = unidecode.unidecode(random.choice(words))
    elif language == 2:
        word = unidecode.unidecode(random.choice(esp_words))
    return word

def play_again():
    respuesta = False
    s = False
    while not s:
        try:
            r = str(input(" QUieres jugar otra vez? (y/n):"))
            if r == 'y' or r == 'Y':
                s = True
                respuesta = True
            elif r == 'n' or r == 'N':
                s = True
                respuesta = False
            else:
                raise ValueError
        except ValueError:
            print('presiona y o n para responder...')

    return respuesta



if __name__ == '__main__':
    language = menu()
    os.system('clear')

    retorno = True

    while retorno:

        word = choice_word(language)
        playing = Game(word,language)
        game = playing.play_hangman()


        if play_again()== True:
            os.system('clear')
            retorno = True
        else:
            print("Fin del Juego - Gracias Por Jugar :)")
            retorno = False








