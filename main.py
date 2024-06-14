# Gra Ping Pong - projekt na zajęcia z "Podstaw programowania"

# Wczytywanie modułów
import pgzrun
from random import randint, choice

# Definicja klasy dla paletek
class Palette:
    def __init__(self, palette, position, width = 140, ball_width = 10):
        """Palette i jej właściwości"""
        self.palette = palette
        self.palette.x = position[0]
        self.palette.y = position[1]
        self.palette.speed = 5
        self.palette.pcenter = width // 2
        self.palette.ball_width = ball_width

    def drawing(self):
        """Wywołanie metody obiektu"""
        self.palette.draw()

    def move(self, direction):
        """Aktualizacja pozycji w osi X"""
        if direction == "left":
            self.palette.x -= self.palette.speed
            if self.palette.x < self.palette.pcenter:
                self.palette.x = self.palette.pcenter + 5
        elif direction == "right":
            self.palette.x += self.palette.speed
            if self.palette.x > (WIDTH - self.palette.pcenter):
                self.palette.x = WIDTH - self.palette.pcenter + 5

    def bounce(self):
        """Sprawdzanie, czy piłeczka odbija się od paletki"""
        # Jeśli środek paletki jest zbut daleko od środka piłeczki, to nie odbijamy
        if (self.palette.distance_to(ball) > self.palette.pcenter + self.palette.ball_width):
            return False
        # Jeśli środek paletki jest dalej niż 20 pikseli od środka piłeczki w osi y, to nie odbijamy
        if abs(self.palette.y - ball.y) > self.palette.ball_width * 2:
            return False
        # Dodatkowo zmieniamy kierunki lewo/prawo dla piłeczki
        if self.palette.x > ball.x and ball.direction_x == "left":
            ball.direction_x = "right"
        elif self.palette.x < ball.x and ball.direction_x == "right":
            ball.direction_x = "left"

        # i odbijamy piłeczkę
        return True

#Definicje funkcji dodatkowych
def update_ball_position():
    # Aktualizacja pozycji w osi X
    if ball.direction_x == "left":
        ball.x -= ball.speed
    elif ball.direction_x == "right":
        ball.x += ball.speed

    # Aktualizacja pozycji w osi Y
    if ball.direction_y == "up":
        ball.y -= ball.speed
    elif ball.direction_y == "down":
        ball.y += ball.speed

    # Sprawdzanie, czy piłeczka odbije się od lewej lub prawej krawędzi okna
    if ball.x < 5:
        ball.direction_x = "right"
    elif ball.x > WIDTH > 5:
        ball.direction_x = "left"

    # Sprawdzenie, czy ktoś wygrał
    if ball.y < 5:
        ball.winner = "GRACZ B"
    elif ball.y > HEIGHT - 5:
        ball.winner = "GRACZ A"

def update_palettes():
    # Gracz A
    if keyboard.a:
        palette_a.move("left")
    elif keyboard.s:
        palette_a.move("right")
    # Gracz B
    if keyboard.k:
        palette_b.move("left")
    elif keyboard.l:
        palette_b.move("right")

def check_bounce():
    if palette_a.bounce():
        ball.direction_y = "down"
    if palette_b.bounce():
       ball.direction_y = "up"

def check_winner():
    if ball.winner:
        winner_txt = f"Wygrywa: {ball.winner}"
        screen.draw.text(winner_txt, (WIDTH // 3, HEIGHT // 2), color="white", fontsize=60)

# Start programu
WIDTH = 1280
HEIGHT = 640
TITLE = "Gra Ping Pong. Miłej gry :)."

# Definicja wyświetlanych obiektów i ich współrzędne X oraz Y
palette_a = Palette(Actor("paletka.png"), (randint(70, 1210), 10))
palette_b = Palette(Actor("paletka.png"), (randint(70, 1210), 630))

ball = Actor("ball.png")
ball.y = HEIGHT // 2
ball.x = WIDTH // 2

# Dodanie własnych właściwości
ball.direction_x = choice(("left", "right"))
ball.direction_y = choice(("up", "down"))
ball.speed = 1
ball.winner = None

# Funkcje sterujące
def update():
    update_ball_position()
    update_palettes()
    check_bounce()

def draw():
    screen.blit("tlo.png", (0, 0))
    palette_a.drawing()
    palette_b.drawing()
    ball.draw()
    check_winner()

# Uruchomienie modułu Pygame Zero
pgzrun.go()
