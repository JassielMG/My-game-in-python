import pygame
class music:

    def music_end(self):
        pygame.mixer.init()
        pygame.init()
        pygame.mixer.music.load('music_efects/ahorcado.wav')
        pygame.mixer.music.load('music_efects/lost_game.wav')
        pygame.mixer.music.play()

    def music_success_letter(self):
        pygame.mixer.init()
        pygame.init()
        pygame.mixer.music.load('music_efects/correct-dingg.wav')
        pygame.mixer.music.play()

    def music_wrong_letter(self):
        pygame.mixer.init()
        pygame.init()
        pygame.mixer.music.load('music_efects/quejido.wav')
        pygame.mixer.music.play()

    def music_repeat_letter(self):
        pygame.mixer.init()
        pygame.init()
        pygame.mixer.music.load('music_efects/advertencia.wav')
        pygame.mixer.music.play()

    def music_invalid_character(self):
        pygame.mixer.init()
        pygame.init()
        pygame.mixer.music.load('music_efects/caracter_invalido.wav')
        pygame.mixer.music.play()


    def music_success_word(self):
        pygame.mixer.init()
        pygame.init()
        pygame.mixer.music.load('music_efects/muy_bien.wav')
        pygame.mixer.music.play()

    def music_intro_game(self):
        pygame.mixer.init()
        pygame.init()
        pygame.mixer.music.load('music_efects//battle_cry.wav')
        pygame.mixer.music.play()