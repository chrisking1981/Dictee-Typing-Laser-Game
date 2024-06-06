import pygame
import random
from words import WORDS

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.words = WORDS
        self.current_word = ""
        self.word_x = screen.get_width()
        self.typed_length = 0
        self.word_y = random.randint(0, screen.get_height() - 50)
        self.font = pygame.font.Font(None, 74)
        self.word_speed = 5
        self.next_word()
        self.user_input = ""

    def next_word(self):
        if self.words:
            self.current_word = self.words.pop(0)
            self.typed_length = 0
            self.word_x = self.screen.get_width()
            self.word_y = random.randint(0, self.screen.get_height() - 50)

    def handle_input(self, char):
        if self.current_word and char == self.current_word[0]:
            self.typed_length += 1
            if self.typed_length >= len(self.current_word):
                self.next_word()

    def update(self, event=None):
        if event and event.type == pygame.KEYDOWN:
            self.handle_input(event.unicode)
        self.word_x -= self.word_speed
        if self.word_x < -self.font.size(self.current_word)[0]:
            self.next_word()


    def draw(self):
        self.screen.fill((0, 0, 0))
        word_surface = self.font.render(self.current_word[self.typed_length:], True, (255, 255, 255))
        self.screen.blit(word_surface, (self.word_x, self.word_y))
