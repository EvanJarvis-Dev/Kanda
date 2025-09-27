import pygame
from pygame import gfxdraw
import math
import random
import sys
import os


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Initialise Pygame
pygame.init()
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Kanda")
pygame.display.set_icon(pygame.image.load(resource_path('assets/images/kanda_icon.png')))

YELLOW = (250, 208, 110)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 95, 31)
BLUE = (0, 0, 255)
LIGHT_BLUE = (102, 255, 255)
PURPLE = (128, 0, 128)
GREY = (46, 46, 46)
LIGHT_VIOLET = (207, 159, 255)
LIGHT_ORANGE = (255, 172, 28)

# Fonts
font_title = pygame.font.SysFont('centuryschoolbook', 120)
font_subtitle = pygame.font.SysFont('centuryschoolbook', 80)
font_menu = pygame.font.SysFont('centuryschoolbook', 40)
font_regular = pygame.font.SysFont('centuryschoolbook', 25)

BORDER_THICKNESS = 6
FPS = 60


class Menu:
    """A super class that provides basic functionality, used in all menus"""

    def __init__(self, game):
        self.game = game
        self.text_to_draw = []
        self.borders_to_draw = []

    def draw(self):
        for text, rect in self.text_to_draw:
            display_surface.blit(text, rect)
        for border in self.borders_to_draw:
            pygame.draw.rect(display_surface, BLACK, border[0], BORDER_THICKNESS)


class UserMenu(Menu):
    """A class to display the user menu"""

    def __init__(self, game, *args):
        super().__init__(game)

        self.title_text = font_title.render("KANDA", True, BLACK)
        self.title_rect = self.title_text.get_rect()
        self.title_rect.center = (WINDOW_WIDTH//2, 50)
        self.text_to_draw.append([self.title_text, self.title_rect])

        self.subtitle_text = font_menu.render("User Menu", True, BLACK)
        self.subtitle_rect = self.subtitle_text.get_rect()
        self.subtitle_rect.center = (WINDOW_WIDTH//2, 130)
        self.text_to_draw.append([self.subtitle_text, self.subtitle_rect])

        self.create_user_text = font_menu.render("Create User", True, BLACK)
        self.create_user_rect = self.create_user_text.get_rect()
        self.create_user_rect.center = ((WINDOW_WIDTH//4) - (WINDOW_WIDTH//8), WINDOW_HEIGHT//2 + 50)
        self.create_user_border = pygame.Rect(0, 0, 250, 100)
        self.create_user_border.center = self.create_user_rect.center
        self.text_to_draw.append([self.create_user_text, self.create_user_rect])
        self.borders_to_draw.append([self.create_user_border, CreateUser])

        self.settings_text = font_menu.render("Settings", True, BLACK)
        self.settings_rect = self.settings_text.get_rect()
        self.settings_rect.center = ((WINDOW_WIDTH//4)+(WINDOW_WIDTH//8), WINDOW_HEIGHT//2 + 50)
        self.settings_border = pygame.Rect(0, 0, 250, 100)
        self.settings_border.center = self.settings_rect.center
        self.text_to_draw.append([self.settings_text, self.settings_rect])
        self.borders_to_draw.append([self.settings_border, Settings])

        self.login_text = font_menu.render("Login", True, BLACK)
        self.login_rect = self.login_text.get_rect()
        self.login_rect.center = (((3*WINDOW_WIDTH)//4)-(WINDOW_WIDTH//8), WINDOW_HEIGHT//2 + 50)
        self.login_border = pygame.Rect(0, 0, 250, 100)
        self.login_border.center = self.login_rect.center
        self.text_to_draw.append([self.login_text, self.login_rect])
        self.borders_to_draw.append([self.login_border, Login])

        self.guest_text = font_menu.render("Guest", True, BLACK)
        self.guest_rect = self.guest_text.get_rect()
        self.guest_rect.center = (((3*WINDOW_WIDTH)//4)+(WINDOW_WIDTH//8), WINDOW_HEIGHT//2 + 50)
        self.guest_border = pygame.Rect(0, 0, 250, 100)
        self.guest_border.center = self.guest_rect.center
        self.text_to_draw.append([self.guest_text, self.guest_rect])
        self.borders_to_draw.append([self.guest_border, MainMenu])

    def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
                break
            elif event.type == pygame.MOUSEBUTTONUP:
                for border, menu in self.borders_to_draw:
                    if border.collidepoint(pygame.mouse.get_pos()):
                        self.game.current_menu = menu(self.game, self.game.current_menu)

        # Fill the display surface
        display_surface.fill(YELLOW)
        self.draw()


class CreateUser(Menu):
    """A class to display the create user menu"""

    def __init__(self, game, *args):
        super().__init__(game)

        self.title_text = font_subtitle.render("Create User", True, BLACK)
        self.title_rect = self.title_text.get_rect()
        self.title_rect.center = (WINDOW_WIDTH//2, 50)
        self.text_to_draw.append([self.title_text, self.title_rect])

        self.instruct_1_text = font_regular.render("Your username must be between 1 and 14 characters.", True, BLACK)
        self.instruct_1_rect = self.instruct_1_text.get_rect()
        self.instruct_1_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 150)
        self.text_to_draw.append([self.instruct_1_text, self.instruct_1_rect])

        self.instruct_2_text = font_regular.render("It must also only contain letters and numbers.", True, BLACK)
        self.instruct_2_rect = self.instruct_2_text.get_rect()
        self.instruct_2_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 100)
        self.text_to_draw.append([self.instruct_2_text, self.instruct_2_rect])

        self.instruct_3_text = font_regular.render("The username must have not been taken.", True, BLACK)
        self.instruct_3_rect = self.instruct_3_text.get_rect()
        self.instruct_3_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 50)
        self.text_to_draw.append([self.instruct_3_text, self.instruct_3_rect])

        self.prompt_1_text = font_menu.render("Enter the username here:", True, BLACK)
        self.prompt_1_rect = self.prompt_1_text.get_rect()
        self.prompt_1_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 40)
        self.text_to_draw.append([self.prompt_1_text, self.prompt_1_rect])

        self.prompt_2_text = font_menu.render("Press enter to continue", True, BLACK)
        self.prompt_2_rect = self.prompt_2_text.get_rect()
        self.prompt_2_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 100)
        self.text_to_draw.append([self.prompt_2_text, self.prompt_2_rect])

        self.return_text = font_menu.render("Return", True, BLACK)
        self.return_rect = self.return_text.get_rect()
        self.return_rect.center = (WINDOW_WIDTH - 150, WINDOW_HEIGHT - 75)
        self.return_border = pygame.Rect(0, 0, 250, 100)
        self.return_border.center = self.return_rect.center
        self.text_to_draw.append([self.return_text, self.return_rect])
        self.borders_to_draw.append([self.return_border, UserMenu])

        self.input = ''
        self.input_text = font_menu.render(self.input, True, BLACK)
        self.input_rect = self.input_text.get_rect()
        self.input_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 100)
        self.input_border = pygame.Rect(0, 0, 590, 60)
        self.input_border.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 100)

    def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
                break
            elif event.type == pygame.MOUSEBUTTONUP:
                for border, menu in self.borders_to_draw:
                    if border.collidepoint(pygame.mouse.get_pos()):
                        self.game.current_menu = menu(self.game)
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalnum() and len(self.input) < 14:
                    self.input += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    self.input = self.input[:-1]
                elif event.key == pygame.K_RETURN:
                    error = False
                    with open(resource_path("assets/other/Users.txt"), 'r') as users:
                        for line in users:
                            user = line.split(', ')
                            if user[0] == self.input:
                                error = True
                    self.text_to_draw[1][0] = font_regular.render("Your username must be between 1 and 14 characters.", True, BLACK)
                    self.text_to_draw[3][0] = font_regular.render("The username must have not been taken.", True, BLACK)
                    if error:
                        self.text_to_draw[3][0] = font_regular.render("The username must have not been taken.", True, PURPLE)
                    elif len(self.input) == 0:
                        self.text_to_draw[1][0] = font_regular.render("Your username must be between 1 and 14 characters.", True, PURPLE)
                    else:
                        with open(resource_path('assets/other/Users.txt'), 'a') as users:
                            print(f"{self.input}, 0, 0, 0", file=users)
                        self.game.current_menu = UserMenu(self.game)

        self.input_text = font_menu.render(self.input, True, BLACK)
        self.input_rect = self.input_text.get_rect()
        self.input_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 100)

        display_surface.fill(YELLOW)
        self.draw()
        pygame.draw.rect(display_surface, BLACK, self.input_border, BORDER_THICKNESS)
        display_surface.blit(self.input_text, self.input_rect)


class Settings(Menu):
    """A class to display the settings menu"""

    def __init__(self, game, previous_menu):
        super().__init__(game)

        self.previous_menu = previous_menu

        self.title_text = font_subtitle.render("Settings", True, BLACK)
        self.title_rect = self.title_text.get_rect()
        self.title_rect.center = (WINDOW_WIDTH//2, 40)
        self.text_to_draw.append([self.title_text, self.title_rect])

        self.music_plus_text = font_title.render("+", True, BLACK)
        self.music_plus_rect = self.music_plus_text.get_rect()
        self.music_plus_rect.midright = (WINDOW_WIDTH - 70, WINDOW_HEIGHT//2 - 100)
        self.music_plus_border = pygame.Rect(0, 0, 100, 100)
        self.music_plus_border.center = self.music_plus_rect.center
        self.text_to_draw.append([self.music_plus_text, self.music_plus_rect])
        self.borders_to_draw.append([self.music_plus_border, ""])

        self.music_minus_text = font_title.render("-", True, BLACK)
        self.music_minus_rect = self.music_minus_text.get_rect()
        self.music_minus_rect.midleft = (70, WINDOW_HEIGHT//2 - 100)
        self.music_minus_border = pygame.Rect(0, 0, 100, 100)
        self.music_minus_border.center = self.music_minus_rect.center
        self.text_to_draw.append([self.music_minus_text, self.music_minus_rect])
        self.borders_to_draw.append([self.music_minus_border, ""])

        self.sound_plus_text = font_title.render("+", True, BLACK)
        self.sound_plus_rect = self.sound_plus_text.get_rect()
        self.sound_plus_rect.midright = (WINDOW_WIDTH - 70, WINDOW_HEIGHT//2 + 100)
        self.sound_plus_border = pygame.Rect(0, 0, 100, 100)
        self.sound_plus_border.center = self.sound_plus_rect.center
        self.text_to_draw.append([self.sound_plus_text, self.sound_plus_rect])
        self.borders_to_draw.append([self.sound_plus_border, ""])

        self.sound_minus_text = font_title.render("-", True, BLACK)
        self.sound_minus_rect = self.sound_minus_text.get_rect()
        self.sound_minus_rect.midleft = (70, WINDOW_HEIGHT//2 + 100)
        self.sound_minus_border = pygame.Rect(0, 0, 100, 100)
        self.sound_minus_border.center = self.sound_minus_rect.center
        self.text_to_draw.append([self.sound_minus_text, self.sound_minus_rect])
        self.borders_to_draw.append([self.sound_minus_border, ""])

        self.music_bar_border = pygame.Rect(0, 0, 800, 100)
        self.music_bar_border.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 100)
        self.borders_to_draw.append([self.music_bar_border, ""])

        self.sound_bar_border = pygame.Rect(0, 0, 800, 100)
        self.sound_bar_border.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 100)
        self.borders_to_draw.append([self.sound_bar_border, ""])

        self.return_text = font_menu.render("Return", True, BLACK)
        self.return_rect = self.return_text.get_rect()
        self.return_rect.center = (WINDOW_WIDTH - 150, WINDOW_HEIGHT - 75)
        self.return_border = pygame.Rect(0, 0, 250, 100)
        self.return_border.center = self.return_rect.center
        self.text_to_draw.append([self.return_text, self.return_rect])
        self.borders_to_draw.append([self.return_border, ""])

        self.music_bar_fill = pygame.Rect(0, 0, 800 * self.game.music_volume, 100)
        self.music_bar_fill.midleft = self.music_bar_border.midleft
        self.sound_bar_fill = pygame.Rect(0, 0, 800 * self.game.sound_volume, 100)
        self.sound_bar_fill.midleft = self.sound_bar_border.midleft

        self.music_volume_text = font_menu.render("Music volume: {}".format(int(self.game.music_volume * 10)), True, BLACK)
        self.music_volume_rect = self.music_volume_text.get_rect()
        self.music_volume_rect.bottomleft = ( self.music_minus_border.left,  self.music_minus_border.top - 10)

        self.sound_volume_text = font_menu.render("Sound volume: {}".format(int(self.game.sound_volume * 10)), True, BLACK)
        self.sound_volume_rect = self.sound_volume_text.get_rect()
        self.sound_volume_rect.bottomleft = ( self.sound_minus_border.left,  self.sound_minus_border.top - 10)

    def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
                break
            elif event.type == pygame.MOUSEBUTTONUP:
                if self.return_border.collidepoint(pygame.mouse.get_pos()):
                    self.game.current_menu = self.previous_menu
                elif self.music_plus_border.collidepoint(pygame.mouse.get_pos()):
                    if self.game.music_volume < 1:
                        self.game.music_volume += 0.1
                        self.game.music_volume = round(self.game.music_volume, 1)
                elif self.music_minus_border.collidepoint(pygame.mouse.get_pos()):
                    if self.game.music_volume > 0:
                        self.game.music_volume -= 0.1
                        self.game.music_volume = round(self.game.music_volume, 1)
                elif self.sound_plus_border.collidepoint(pygame.mouse.get_pos()):
                    if self.game.sound_volume < 1:
                        self.game.sound_volume += 0.1
                        self.game.sound_volume = round(self.game.sound_volume, 1)
                elif self.sound_minus_border.collidepoint(pygame.mouse.get_pos()):
                    if self.game.sound_volume > 0:
                        self.game.sound_volume -= 0.1
                        self.game.sound_volume = round(self.game.sound_volume, 1)
                self.game.hit_sound.set_volume(self.game.sound_volume)
                pygame.mixer.music.set_volume(self.game.music_volume)

        self.update()

        # Fill the display surface
        display_surface.fill(YELLOW)
        self.draw()
        pygame.draw.rect(display_surface, BLACK, self.music_bar_fill, 0)
        pygame.draw.rect(display_surface, BLACK, self.sound_bar_fill, 0)
        display_surface.blit(self.music_volume_text, self.music_volume_rect)
        display_surface.blit(self.sound_volume_text, self.sound_volume_rect)

    def update(self):
        self.music_bar_fill = pygame.Rect(0, 0, 800 * self.game.music_volume, 100)
        self.music_bar_fill.midleft = self.music_bar_border.midleft
        self.sound_bar_fill = pygame.Rect(0, 0, 800 * self.game.sound_volume, 100)
        self.sound_bar_fill.midleft = self.sound_bar_border.midleft
        self.music_volume_text = font_menu.render("Music volume: {}".format(int(self.game.music_volume * 10)), True, BLACK)
        self.sound_volume_text = font_menu.render("Sound volume: {}".format(int(self.game.sound_volume * 10)), True, BLACK)


class Login(Menu):
    """A class to display the create user menu"""

    def __init__(self, game, *args):
        super().__init__(game)
        self.title_text = font_subtitle.render("Login", True, BLACK)
        self.title_rect = self.title_text.get_rect()
        self.title_rect.center = (WINDOW_WIDTH//2, 50)
        self.text_to_draw.append([self.title_text, self.title_rect])

        self.name_border = pygame.Rect(0, 0, 590, 60)
        self.name_border.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
        self.borders_to_draw.append([self.name_border, ""])

        self.prompt_text = font_menu.render("Enter your username here:", True, BLACK)
        self.prompt_rect = self.prompt_text.get_rect()
        self.prompt_rect.bottomleft = self.name_border.left, self.name_border.top - 10
        self.text_to_draw.append([self.prompt_text, self.prompt_rect])

        self.prompt_2_text = font_menu.render("Press enter to continue", True, BLACK)
        self.prompt_2_rect = self.prompt_2_text.get_rect()
        self.prompt_2_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 100)
        self.text_to_draw.append([self.prompt_2_text, self.prompt_2_rect])

        self.input = ""
        self.input_text = font_menu.render(self.input, True, BLACK)
        self.input_rect = self.input_text.get_rect()
        self.input_rect.center = self.name_border.center

        self.return_text = font_menu.render("Return", True, BLACK)
        self.return_rect = self.return_text.get_rect()
        self.return_rect.center = (WINDOW_WIDTH - 150, WINDOW_HEIGHT - 75)
        self.return_border = pygame.Rect(0, 0, 250, 100)
        self.return_border.center = self.return_rect.center
        self.text_to_draw.append([self.return_text, self.return_rect])
        self.borders_to_draw.append([self.return_border, UserMenu])

    def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
                break
            elif event.type == pygame.MOUSEBUTTONUP:
                if self.return_border.collidepoint(pygame.mouse.get_pos()):
                    self.game.current_menu = UserMenu(self.game)
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalnum() and len(self.input) < 14:
                    self.input += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    self.input = self.input[:-1]
                elif event.key == pygame.K_RETURN:
                    with open(resource_path("assets/other/Users.txt"), 'r') as users:
                        for line in users:
                            user = line.split(', ')
                            if user[0] == self.input:
                                self.game.current_user = user[0]
                                self.game.current_menu = MainMenu(self.game)

        self.input_text = font_menu.render(self.input, True, BLACK)
        self.input_rect = self.input_text.get_rect()
        self.input_rect.center = self.name_border.center

        # Fill the display surface
        display_surface.fill(YELLOW)
        self.draw()
        display_surface.blit(self.input_text, self.input_rect)


class MainMenu(Menu):
    """A class to display the main menu"""

    def __init__(self, game, *args):
        super().__init__(game)
        self.title_text = font_title.render("KANDA", True, BLACK)
        self.title_rect = self.title_text.get_rect()
        self.title_rect.center = (WINDOW_WIDTH//2, 50)
        self.text_to_draw.append([self.title_text, self.title_rect])

        self.subtitle_text = font_menu.render("Main Menu", True, BLACK)
        self.subtitle_rect = self.subtitle_text.get_rect()
        self.subtitle_rect.center = (WINDOW_WIDTH//2, 130)
        self.text_to_draw.append([self.subtitle_text, self.subtitle_rect])

        self.logout_text = font_menu.render("Logout", True, BLACK)
        self.logout_rect = self.logout_text.get_rect()
        self.logout_rect.center = ((WINDOW_WIDTH//4), WINDOW_HEIGHT//2)
        self.logout_border = pygame.Rect(0, 0, 260, 100)
        self.logout_border.center = self.logout_rect.center
        self.text_to_draw.append([self.logout_text, self.logout_rect])
        self.borders_to_draw.append([self.logout_border, self.logout])

        self.settings_text = font_menu.render("Settings", True, BLACK)
        self.settings_rect = self.settings_text.get_rect()
        self.settings_rect.center = ((WINDOW_WIDTH//4) * 2, WINDOW_HEIGHT//2)
        self.settings_border = pygame.Rect(0, 0, 260, 100)
        self.settings_border.center = self.settings_rect.center
        self.text_to_draw.append([self.settings_text, self.settings_rect])
        self.borders_to_draw.append([self.settings_border, Settings])

        self.leader_board_text = font_menu.render("Leader board", True, BLACK)
        self.leader_board_rect = self.leader_board_text.get_rect()
        self.leader_board_rect.center = ((WINDOW_WIDTH//4) * 3, WINDOW_HEIGHT//2)
        self.leader_board_border = pygame.Rect(0, 0, 260, 100)
        self.leader_board_border.center = self.leader_board_rect.center
        self.text_to_draw.append([self.leader_board_text, self.leader_board_rect])
        self.borders_to_draw.append([self.leader_board_border, LeaderBoardMenu])

        self.guide_text = font_menu.render("Guide", True, BLACK)
        self.guide_rect = self.guide_text.get_rect()
        self.guide_rect.center = ((WINDOW_WIDTH//3), WINDOW_HEIGHT//2 + 160)
        self.guide_border = pygame.Rect(0, 0, 260, 100)
        self.guide_border.center = self.guide_rect.center
        self.text_to_draw.append([self.guide_text, self.guide_rect])
        self.borders_to_draw.append([self.guide_border, Guide])

        self.play_text = font_menu.render("Play", True, BLACK)
        self.play_rect = self.play_text.get_rect()
        self.play_rect.center = ((WINDOW_WIDTH//3) * 2, WINDOW_HEIGHT//2 + 160)
        self.play_border = pygame.Rect(0, 0, 260, 100)
        self.play_border.center = self.play_rect.center
        self.text_to_draw.append([self.play_text, self.play_rect])
        self.borders_to_draw.append([self.play_border, PlayMenuStage])

        current_user = str(self.game.current_user).split(', ')
        user_name = current_user[0]
        if user_name != "0":
            self.user_text = font_regular.render(f"Logged in as: {user_name}", True, BLACK)
        else:
            self.user_text = font_regular.render("You are not logged in.", True, BLACK)
        self.user_rect = self.user_text.get_rect()
        self.user_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT - 20)
        self.text_to_draw.append([self.user_text, self.user_rect])

    def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                for border, menu in self.borders_to_draw:
                    if border.collidepoint(pygame.mouse.get_pos()):
                        self.game.current_menu = menu(self.game, self.game.current_menu)

        # Fill the display surface
        display_surface.fill(YELLOW)
        self.draw()

    def logout(self, *args):
        self.game.current_user = 0
        return UserMenu(self.game)


class LeaderBoardMenu(Menu):
    """A class to display the main menu"""

    def __init__(self, game, *args):
        super().__init__(game)
        self.title_text = font_subtitle.render("Leader Board", True, BLACK)
        self.title_rect = self.title_text.get_rect()
        self.title_rect.center = (WINDOW_WIDTH//2, 40)
        self.text_to_draw.append([self.title_text, self.title_rect])

        self.stageone_text = font_menu.render("Stage 1", True, BLACK)
        self.stageone_rect = self.stageone_text.get_rect()
        self.stageone_rect.center = ((WINDOW_WIDTH//4), WINDOW_HEIGHT//2)
        self.stageone_border = pygame.Rect(0, 0, 260, 100)
        self.stageone_border.center = self.stageone_rect.center
        self.text_to_draw.append([self.stageone_text, self.stageone_rect])
        self.borders_to_draw.append([self.stageone_border, LeaderBoard, 1])

        self.stagetwo_text = font_menu.render("Stage 2", True, BLACK)
        self.stagetwo_rect = self.stagetwo_text.get_rect()
        self.stagetwo_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)
        self.stagetwo_border = pygame.Rect(0, 0, 260, 100)
        self.stagetwo_border.center = self.stagetwo_rect.center
        self.text_to_draw.append([self.stagetwo_text, self.stagetwo_rect])
        self.borders_to_draw.append([self.stagetwo_border, LeaderBoard, 2])

        self.stagethree_text = font_menu.render("Stage 3", True, BLACK)
        self.stagethree_rect = self.stagethree_text.get_rect()
        self.stagethree_rect.center = ((WINDOW_WIDTH//4) * 3, WINDOW_HEIGHT//2)
        self.stagethree_border = pygame.Rect(0, 0, 260, 100)
        self.stagethree_border.center = self.stagethree_rect.center
        self.text_to_draw.append([self.stagethree_text, self.stagethree_rect])
        self.borders_to_draw.append([self.stagethree_border, LeaderBoard, 3])

        self.total_text = font_menu.render("Total score", True, BLACK)
        self.total_rect = self.total_text.get_rect()
        self.total_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 160)
        self.total_border = pygame.Rect(0, 0, 260, 100)
        self.total_border.center = self.total_rect.center
        self.text_to_draw.append([self.total_text, self.total_rect])
        self.borders_to_draw.append([self.total_border, LeaderBoard, 0])

        self.return_text = font_menu.render("Return", True, BLACK)
        self.return_rect = self.return_text.get_rect()
        self.return_rect.center = (WINDOW_WIDTH - 150, WINDOW_HEIGHT - 75)
        self.return_border = pygame.Rect(0, 0, 250, 100)
        self.return_border.center = self.return_rect.center
        self.text_to_draw.append([self.return_text, self.return_rect])
        self.borders_to_draw.append([self.return_border, MainMenu, None])

    def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
                break
            elif event.type == pygame.MOUSEBUTTONUP:
                for border, menu, stage in self.borders_to_draw:
                    if border.collidepoint(pygame.mouse.get_pos()):
                        self.game.current_menu = menu(self.game, stage)

        # Fill the display surface
        display_surface.fill(YELLOW)
        self.draw()


class LeaderBoard(Menu):
    """A class to display the main menu"""

    def __init__(self, game, stage, *args):
        super().__init__(game)
        self.stage = stage

        self.title_text = font_subtitle.render("Leader Board", True, BLACK)
        self.title_rect = self.title_text.get_rect()
        self.title_rect.center = (WINDOW_WIDTH//2, 40)
        self.text_to_draw.append([self.title_text, self.title_rect])

        if self.stage != 0:
            self.stage_text = font_menu.render(f"Stage {self.stage}:", True, BLACK)
        else:
            self.stage_text = font_menu.render("Total score:", True, BLACK)
        self.stage_rect = self.stage_text.get_rect()
        self.stage_rect.midleft = (25, 50)
        self.text_to_draw.append([self.stage_text, self.stage_rect])

        self.number_text = font_menu.render("No.", True, BLACK)
        self.number_rect = self.number_text.get_rect()
        self.number_rect.center = (100, 125)
        self.text_to_draw.append([self.number_text, self.number_rect])

        self.username_text = font_menu.render("Username:", True, BLACK)
        self.username_rect = self.username_text.get_rect()
        self.username_rect.center = (250, 125)
        self.text_to_draw.append([self.username_text, self.username_rect])

        self.score_text = font_menu.render("Score:", True, BLACK)
        self.score_rect = self.score_text.get_rect()
        self.score_rect.center = (800, 125)
        self.text_to_draw.append([self.score_text, self.score_rect])

        self.return_text = font_menu.render("Return", True, BLACK)
        self.return_rect = self.return_text.get_rect()
        self.return_rect.center = (WINDOW_WIDTH - 150, 75)
        self.return_border = pygame.Rect(0, 0, 250, 100)
        self.return_border.center = self.return_rect.center
        self.text_to_draw.append([self.return_text, self.return_rect])
        self.borders_to_draw.append([self.return_border, LeaderBoardMenu])

        users_to_order = []
        with open(resource_path("assets/other/Users.txt"), "r") as users:
            for line in users:
                user = line.split(', ')
                user[3] = user[3].strip()

                if self.stage != 0:
                    users_to_order.append([user[0], int(user[self.stage])])
                else:
                    users_to_order.append([user[0], int(user[1]) + int(user[2]) + int(user[3])])
            sorted_users = sorted(users_to_order, key=lambda x: x[1])
            sorted_users.reverse()

        self.users_for_leader_board = []

        for user in sorted_users:
            current_position = sorted_users.index(user) + 1
            if current_position > 10:
                break
            colour = BLACK
            if self.game.current_user != 0:
                temp_user = self.game.current_user.split(', ')
                if temp_user[0] == user[0]:
                    colour = ORANGE

            number_text = font_menu.render(str(current_position), True, colour)
            number_rect = number_text.get_rect()
            number_rect.midright = (130, 175 + (40*(current_position-1)))
            self.text_to_draw.append([number_text, number_rect])

            name_text = font_menu.render(user[0], True, colour)
            name_rect = name_text.get_rect()
            name_rect.midleft = (150, 175 + (40*(current_position-1)))
            self.text_to_draw.append([name_text, name_rect])

            score_text = font_menu.render(str(user[1]), True, colour)
            score_rect = score_text.get_rect()
            score_rect.midleft = (740, 175 + (40*(current_position-1)))
            self.text_to_draw.append([score_text, score_rect])

    def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
                break
            elif event.type == pygame.MOUSEBUTTONUP:
                for border, menu in self.borders_to_draw:
                    if border.collidepoint(pygame.mouse.get_pos()):
                        self.game.current_menu = menu(self.game)

        # Fill the display surface
        display_surface.fill(YELLOW)
        self.draw()
        pygame.draw.rect(display_surface, BLACK, (50, 150, 1000, 5))
        pygame.draw.rect(display_surface, BLACK, (140, 100, 5, 460))
        pygame.draw.rect(display_surface, BLACK, (730, 100, 5, 460))


class Guide(Menu):
    """A class to display the main menu"""

    def __init__(self, game, *args):
        super().__init__(game)

        self.title_text = font_subtitle.render("Guide", True, BLACK)
        self.title_rect = self.title_text.get_rect()
        self.title_rect.center = (WINDOW_WIDTH//2, 40)
        self.text_to_draw.append([self.title_text, self.title_rect])

        arrow_image = pygame.image.load("assets/images/arrow_right.png")
        arrow_image_width = arrow_image.get_width()
        arrow_image_height = arrow_image.get_height()

        self.arrow_right = pygame.transform.smoothscale(arrow_image, (arrow_image_width//5, arrow_image_height//5))
        self.arrow_right_rect = self.arrow_right.get_rect()
        self.arrow_right_rect.center = WINDOW_WIDTH//2 + 200, WINDOW_HEIGHT//2 + 200

        self.arrow_left = pygame.transform.flip(self.arrow_right, True, False)
        self.arrow_left_rect = self.arrow_left.get_rect()
        self.arrow_left_rect.center = WINDOW_WIDTH//2 - 200, WINDOW_HEIGHT//2 + 200

        self.page_number = 1
        self.page_number_text = font_menu.render(f"Page: {self.page_number}/8", True, BLACK)
        self.page_number_rect = self.page_number_text.get_rect()
        self.page_number_rect.center = WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 200

        self.return_text = font_menu.render("Return", True, BLACK)
        self.return_rect = self.return_text.get_rect()
        self.return_rect.center = (WINDOW_WIDTH - 150, 75)
        self.return_border = pygame.Rect(0, 0, 250, 100)
        self.return_border.center = self.return_rect.center
        self.text_to_draw.append([self.return_text, self.return_rect])
        self.borders_to_draw.append([self.return_border, MainMenu])

        self.guide_images = []
        self.guide_rects = []
        for i in range(1, 9):
            temp_image = pygame.image.load("assets/images/guide{}.png".format(i))

            self.guide_images.append(pygame.transform.smoothscale(temp_image, (600, 320)))

            self.guide_rects.append(self.guide_images[i - 1].get_rect())
            self.guide_rects[i - 1].center = WINDOW_WIDTH//2, WINDOW_HEIGHT//2
        self.image_rect = pygame.Rect(10, 10, 610, 330)
        self.image_rect.center = self.guide_rects[0].center

    def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
                break
            elif event.type == pygame.MOUSEBUTTONUP:
                for border, menu in self.borders_to_draw:
                    if border.collidepoint(pygame.mouse.get_pos()):
                        self.game.current_menu = menu(self.game)
                if self.arrow_right_rect.collidepoint(pygame.mouse.get_pos()):
                    if self.page_number < 8:
                        self.page_number += 1
                elif self.arrow_left_rect.collidepoint(pygame.mouse.get_pos()):
                    if self.page_number > 1:
                        self.page_number -= 1
                self.page_number_text = font_menu.render(f"Page: {self.page_number}/8", True, BLACK)
                self.page_number_rect = self.page_number_text.get_rect()
                self.page_number_rect.center = WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 200

        # Fill the display surface
        display_surface.fill(YELLOW)
        self.draw()
        display_surface.blit(self.guide_images[self.page_number - 1], self.guide_rects[self.page_number - 1])
        display_surface.blit(self.arrow_left, self.arrow_left_rect)
        display_surface.blit(self.arrow_right, self.arrow_right_rect)
        display_surface.blit(self.page_number_text, self.page_number_rect)
        pygame.draw.rect(display_surface, BLACK, self.image_rect, BORDER_THICKNESS)


class PlayMenuStage(Menu):
    """A class to display the main menu"""

    def __init__(self, game, *args):
        super().__init__(game)

        self.title_text = font_subtitle.render("Play", True, BLACK)
        self.title_rect = self.title_text.get_rect()
        self.title_rect.center = (WINDOW_WIDTH//2, 40)
        self.text_to_draw.append([self.title_text, self.title_rect])

        self.stage_choose_text = font_menu.render("Select the stage:", True, BLACK)
        self.stage_choose_rect = self.stage_choose_text.get_rect()
        self.stage_choose_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 100)
        self.text_to_draw.append([self.stage_choose_text, self.stage_choose_rect])

        self.stageone_text = font_menu.render("Stage 1", True, BLACK)
        self.stageone_rect = self.stageone_text.get_rect()
        self.stageone_rect.center = ((WINDOW_WIDTH//4), WINDOW_HEIGHT//2 + 50)
        self.stageone_border = pygame.Rect(0, 0, 260, 100)
        self.stageone_border.center = self.stageone_rect.center
        self.text_to_draw.append([self.stageone_text, self.stageone_rect])
        self.borders_to_draw.append([self.stageone_border, PlayMenuDifficulty, 1])

        self.stagetwo_text = font_menu.render("Stage 2", True, BLACK)
        self.stagetwo_rect = self.stagetwo_text.get_rect()
        self.stagetwo_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 50)
        self.stagetwo_border = pygame.Rect(0, 0, 260, 100)
        self.stagetwo_border.center = self.stagetwo_rect.center
        self.text_to_draw.append([self.stagetwo_text, self.stagetwo_rect])
        self.borders_to_draw.append([self.stagetwo_border, PlayMenuDifficulty, 2])

        self.stagethree_text = font_menu.render("Stage 3", True, BLACK)
        self.stagethree_rect = self.stagethree_text.get_rect()
        self.stagethree_rect.center = ((WINDOW_WIDTH//4) * 3, WINDOW_HEIGHT//2 + 50)
        self.stagethree_border = pygame.Rect(0, 0, 260, 100)
        self.stagethree_border.center = self.stagethree_rect.center
        self.text_to_draw.append([self.stagethree_text, self.stagethree_rect])
        self.borders_to_draw.append([self.stagethree_border, PlayMenuDifficulty, 3])

        self.return_text = font_menu.render("Return", True, BLACK)
        self.return_rect = self.return_text.get_rect()
        self.return_rect.center = (WINDOW_WIDTH - 150, WINDOW_HEIGHT - 75)
        self.return_border = pygame.Rect(0, 0, 250, 100)
        self.return_border.center = self.return_rect.center
        self.text_to_draw.append([self.return_text, self.return_rect])
        self.borders_to_draw.append([self.return_border, MainMenu, 0])

    def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
                break
            elif event.type == pygame.MOUSEBUTTONUP:
                for border, menu, stage in self.borders_to_draw:
                    if border.collidepoint(pygame.mouse.get_pos()):
                        self.game.current_stage = stage
                        self.game.current_menu = menu(self.game)

        # Fill the display surface
        display_surface.fill(YELLOW)
        self.draw()


class PlayMenuDifficulty(Menu):
    """A class to display the main menu"""

    def __init__(self, game, *args):
        super().__init__(game)

        self.title_text = font_subtitle.render("Play", True, BLACK)
        self.title_rect = self.title_text.get_rect()
        self.title_rect.center = (WINDOW_WIDTH//2, 40)
        self.text_to_draw.append([self.title_text, self.title_rect])

        self.difficulty_choose_text = font_menu.render("Select the difficulty:", True, BLACK)
        self.difficulty_choose_rect = self.difficulty_choose_text.get_rect()
        self.difficulty_choose_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 - 100)
        self.text_to_draw.append([self.difficulty_choose_text, self.difficulty_choose_rect])

        self.easy_text = font_menu.render("Easy", True, BLACK)
        self.easy_rect = self.easy_text.get_rect()
        self.easy_rect.center = ((WINDOW_WIDTH//4), WINDOW_HEIGHT//2 + 50)
        self.easy_border = pygame.Rect(0, 0, 260, 100)
        self.easy_border.center = self.easy_rect.center
        self.text_to_draw.append([self.easy_text, self.easy_rect])
        self.borders_to_draw.append([self.easy_border, Play, 1])

        self.medium_text = font_menu.render("Medium", True, BLACK)
        self.medium_rect = self.medium_text.get_rect()
        self.medium_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 50)
        self.medium_border = pygame.Rect(0, 0, 260, 100)
        self.medium_border.center = self.medium_rect.center
        self.text_to_draw.append([self.medium_text, self.medium_rect])
        self.borders_to_draw.append([self.medium_border, Play, 2])

        self.hard_text = font_menu.render("Hard", True, BLACK)
        self.hard_rect = self.hard_text.get_rect()
        self.hard_rect.center = ((WINDOW_WIDTH//4) * 3, WINDOW_HEIGHT//2 + 50)
        self.hard_border = pygame.Rect(0, 0, 260, 100)
        self.hard_border.center = self.hard_rect.center
        self.text_to_draw.append([self.hard_text, self.hard_rect])
        self.borders_to_draw.append([self.hard_border, Play, 3])

        self.return_text = font_menu.render("Return", True, BLACK)
        self.return_rect = self.return_text.get_rect()
        self.return_rect.center = (WINDOW_WIDTH - 150, WINDOW_HEIGHT - 75)
        self.return_border = pygame.Rect(0, 0, 250, 100)
        self.return_border.center = self.return_rect.center
        self.text_to_draw.append([self.return_text, self.return_rect])
        self.borders_to_draw.append([self.return_border, PlayMenuStage, 0])

    def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
                break
            elif event.type == pygame.MOUSEBUTTONUP:
                for border, menu, difficulty in self.borders_to_draw:
                    if border.collidepoint(pygame.mouse.get_pos()):
                        self.game.difficulty = difficulty
                        self.game.current_menu = menu(self.game)

        # Fill the display surface
        display_surface.fill(YELLOW)
        self.draw()


class Play:
    def __init__(self, game, *args):
        self.game = game

        self.text_to_draw = []

        self.title_text = font_subtitle.render("Kanda", True, BLACK)
        self.title_rect = self.title_text.get_rect()
        self.title_rect.bottomleft = (10, 95)
        self.text_to_draw.append([self.title_text, self.title_rect])

        self.stage = self.game.current_stage
        self.stage_text = font_menu.render("Stage: {}".format(self.stage), True, BLACK)
        self.stage_rect = self.stage_text.get_rect()
        self.stage_rect.topleft = (self.title_rect.right + 10, 5)
        self.text_to_draw.append([self.stage_text, self.stage_rect])

        self.diff = self.game.difficulty
        if self.diff == 1:
            self.difficulty = 'Easy'
            self.difficulty_multiplier = 1
            self.balls = 16
        elif self.diff == 2:
            self.difficulty = 'Medium'
            self.difficulty_multiplier = 1.5
            self.balls = 12
        elif self.diff == 3:
            self.difficulty = 'Hard'
            self.difficulty_multiplier = 2
            self.balls = 8

        self.difficulty_text = font_menu.render("Difficulty: {}".format(self.difficulty), True, BLACK)
        self.difficulty_rect = self.difficulty_text.get_rect()
        self.difficulty_rect.bottomleft = (self.title_rect.right + 10, 98)
        self.text_to_draw.append([self.difficulty_text, self.difficulty_rect])

        self.score = 0
        self.score_text = font_menu.render("Score: {}".format(self.score), True, BLACK)
        self.score_rect = self.score_text.get_rect()
        self.score_rect.topleft = (self.difficulty_rect.right + 10, 5)

        self.balls_text = font_menu.render("Balls left: {}".format(self.balls), True, BLACK)
        self.balls_rect = self.balls_text.get_rect()
        self.balls_rect.bottomleft = (self.difficulty_rect.right + 10, 98)

        if self.stage == 1:
            pygame.mixer.music.load(resource_path("assets/sounds/Sunny_Sands.mp3"))
        elif self.stage == 2:
            pygame.mixer.music.load(resource_path("assets/sounds/Starlit_Skies.mp3"))
        elif self.stage == 3:
            pygame.mixer.music.load(resource_path("assets/sounds/No_Stopping_Now.mp3"))
        pygame.mixer.music.play(-1)

        self.ball = Ball(self.game)
        self.ball_group = pygame.sprite.GroupSingle(self.ball)
        self.peg_group = pygame.sprite.Group()
        self.cannon = Cannon(self.game)
        self.cannon_group = pygame.sprite.GroupSingle(self.cannon)

        with open(resource_path("assets/other/Stages.txt"), "r") as stages:
            lines = [line.strip() for line in stages.readlines()]
            count = -1
            for line in lines:
                count += 1
                if line == "Stage " + str(self.stage):
                    starting_position = count
                    break

            # Create a tuple containing the three values for the amount of each type of peg
            ratio_pegs = tuple(int(item) for item in lines[starting_position + 2].split(", "))
            # Change the count, so it starts at the index for the peg positions
            count += 3
            peg_positions = []

            # Add to the list all the peg positions needed
            same_stage = True
            while same_stage:
                count += 1
                if count < len(lines):
                    if lines[count] != "":
                        peg_positions.append(lines[count])
                    else:
                        break
                else:
                    break

            # Change the peg positions list so that it is a list of tuples not strings
            peg_positions = [tuple(int(position) for position in item.split(", ")) for item in peg_positions]
            # Shuffle the peg positions (To randomise the type of peg)
            random.shuffle(peg_positions)

            # Set temporary variables for tracking the amount of each colour peg we need
            blue_to_use = ratio_pegs[0]
            orange_to_use = ratio_pegs[1]
            purple_to_use = ratio_pegs[2]

            # Add pegs to the peg group for each position, passing the colour and position
            for peg_position in peg_positions:
                if blue_to_use > 0:
                    self.peg_group.add(Peg(BLUE, peg_position))
                    blue_to_use -= 1
                elif orange_to_use > 0:
                    self.peg_group.add(Peg(ORANGE, peg_position))
                    orange_to_use -= 1
                elif purple_to_use > 0:
                    self.peg_group.add(Peg(PURPLE, peg_position))
                    purple_to_use -= 1

            self.orange_pegs = ratio_pegs[1]
        self.TOTAL_ORANGE = self.orange_pegs

        self.orange_pegs_text = font_menu.render(f"Orange pegs:", True, BLACK)
        self.orange_pegs_rect = self.orange_pegs_text.get_rect()
        self.orange_pegs_rect.midleft = (928, 27)
        self.text_to_draw.append([self.orange_pegs_text, self.orange_pegs_rect])

        self.orange_pegs_left_text = font_menu.render(f"{self.orange_pegs}/{self.TOTAL_ORANGE}", True, BLACK)
        self.orange_pegs_left_rect = self.orange_pegs_left_text.get_rect()
        self.orange_pegs_left_rect.midleft = (1000, 70)

        self.rects = []
        # These are the walls for the game
        self.rects.append(pygame.Rect(0, 0, 5, WINDOW_HEIGHT))
        self.rects.append(pygame.Rect(WINDOW_WIDTH - 130, 100, 5, WINDOW_HEIGHT))
        self.rects.append(pygame.Rect(0, 100, WINDOW_WIDTH, 5))

        # These are the lines for the HUD
        self.rects.append(pygame.Rect(WINDOW_WIDTH - 5, 0, 5, WINDOW_HEIGHT))
        self.rects.append(pygame.Rect(0, 0, WINDOW_WIDTH, 5))
        self.rects.append(pygame.Rect(self.title_rect.right + 3, 0, 3, 100))
        self.rects.append(pygame.Rect(self.difficulty_rect.right + 3, 0, 3, 100))
        self.rects.append(pygame.Rect(self.title_rect.right + 3, self.stage_rect.bottom, 885 - self.title_rect.w, 3))
        self.rects.append(pygame.Rect(895, 0, 3, 100))

        # This is the outline of the bar for score meter
        self.rects.append(pygame.Rect(WINDOW_WIDTH - 120, 150, 40, 400))
        self.rects.append(pygame.Rect(WINDOW_WIDTH - 120, 190, 40, 5))
        self.rects.append(pygame.Rect(WINDOW_WIDTH - 120, 270, 40, 5))
        self.rects.append(pygame.Rect(WINDOW_WIDTH - 120, 390, 40, 5))

        self.score_two_text = font_menu.render("2x", True, BLACK)
        self.score_two_rect = self.score_two_text.get_rect()
        self.score_two_rect.center = (WINDOW_WIDTH - 40, 390)
        self.text_to_draw.append([self.score_two_text, self.score_two_rect])

        self.score_five_text = font_menu.render("5x", True, BLACK)
        self.score_five_rect = self.score_five_text.get_rect()
        self.score_five_rect.center = (WINDOW_WIDTH - 40, 270)
        self.text_to_draw.append([self.score_five_text, self.score_five_rect])

        self.score_ten_text = font_menu.render("10x", True, BLACK)
        self.score_ten_rect = self.score_ten_text.get_rect()
        self.score_ten_rect.center = (WINDOW_WIDTH - 40, 190)
        self.text_to_draw.append([self.score_ten_text, self.score_ten_rect])

        self.score_meter_rect = pygame.Rect(0, 0, 40, (self.TOTAL_ORANGE - self.orange_pegs)/self.TOTAL_ORANGE + 1)
        self.score_meter_rect.bottomleft = (WINDOW_WIDTH - 120, 550)

        self.score_meter_multiplier = 1

        # Semi circle rect
        self.semi_rect = pygame.Rect(0, 0, WINDOW_WIDTH, 200)
        self.semi_rect.midbottom = ((WINDOW_WIDTH - 125)//2, 100)

    def loop(self):
        self.play_loop()

    def play_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
                break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.current_menu = Pause(self.game, self)
            elif event.type == pygame.MOUSEBUTTONDOWN and not self.ball.shot:
                self.ball.shoot(self.cannon.find_tip_direction())
                self.balls -= 1

        self.update()
        self.cannon.rotate_cannon(pygame.mouse.get_pos())
        # Fill the display surface
        display_surface.fill(YELLOW)
        self.draw()

    def update(self):
        self.score_text = font_menu.render("Score: {}".format(self.score), True, BLACK)
        self.score_rect = self.score_text.get_rect()
        self.score_rect.topleft = (self.difficulty_rect.right + 10, 5)

        self.balls_text = font_menu.render("Balls left: {}".format(self.balls), True, BLACK)
        self.balls_rect = self.balls_text.get_rect()
        self.balls_rect.bottomleft = (self.difficulty_rect.right + 10, 98)

        self.orange_pegs_left_text = font_menu.render(f"{self.orange_pegs}/{self.TOTAL_ORANGE}", True, BLACK)
        self.orange_pegs_left_rect = self.orange_pegs_left_text.get_rect()
        self.orange_pegs_left_rect.midleft = (1000, 70)

        if not self.check_collisions():
            self.ball.update()

        if self.ball.fallen:
            for peg in self.peg_group:
                if peg.hit:
                    peg.kill()

            if self.orange_pegs <= 0:
                self.score += int(self.balls * 500 * self.difficulty_multiplier)
                self.game.current_menu = Win(self.game, self.score, self.stage)
            elif self.balls <= 0:
                self.check_collisions()
                if self.orange_pegs <= 0:
                    self.score += int(self.balls * 500 * self.difficulty_multiplier)
                    self.game.current_menu = Win(self.game, self.score, self.stage)
                self.game.current_menu = Lose(self.game)

    def draw(self):
        self.cannon_group.draw(display_surface)
        self.cannon.aim_sight()
        # Creating the base of the cannon
        pygame.gfxdraw.aacircle(display_surface, (WINDOW_WIDTH - 125)//2, 100, 50, GREY)
        pygame.gfxdraw.filled_circle(display_surface, (WINDOW_WIDTH - 125)//2, 100, 50, GREY)
        # Erasing top part of circle to create semicircle
        pygame.draw.rect(display_surface, YELLOW, self.semi_rect)

        self.ball_group.draw(display_surface)
        self.peg_group.draw(display_surface)

        pygame.draw.rect(display_surface, ORANGE, self.score_meter_rect)

        for text, rect in self.text_to_draw:
            display_surface.blit(text, rect)
        for rect in self.rects:
            pygame.draw.rect(display_surface, BLACK, rect, 5)

        display_surface.blit(self.score_text, self.score_rect)
        display_surface.blit(self.balls_text, self.balls_rect)
        display_surface.blit(self.orange_pegs_left_text, self.orange_pegs_left_rect)

    def check_collisions(self):
        """Check for collisions between the ball and pegs"""
        # Find the center of the ball currently
        ball_center = self.ball.position

        # Find the center of the ball when it will be next updated
        future_ball_center = ball_center + self.ball.velocity

        # Find the ball and peg radius
        ball_radius = self.ball.radius
        peg_radius = self.peg_group.sprites()[0].radius

        # Find the distance when the peg and the ball are touching
        touching_distance = ball_radius + peg_radius

        # For every peg, check if the ball will collide with it
        for peg in self.peg_group:
            # Store the position of the current peg to a variable
            peg_center = peg.position

            # Find the vector of the distance of where the ball will be and the current position of the peg
            distance_vector = peg_center - future_ball_center

            # Check if the length of the distance is less than the combined radii of the peg and ball
            if distance_vector.length() <= touching_distance:
                # Set the ball bounce variable to true
                self.bounce = True

                # Use the ball's bounce method to bounce the ball
                # Pass the center of the peg and the current touching distance
                self.ball.bounce(peg_center, touching_distance)

                # Play the sound
                if not peg.hit:
                    pygame.mixer.Sound.play(self.game.hit_sound)

                    # Make the peg hit
                    peg.hit_peg()

                    if peg.colour == ORANGE:
                        self.orange_peg_remove()
                        self.score += int(200 * self.score_meter_multiplier * self.difficulty_multiplier)
                    elif peg.colour == PURPLE:
                        self.score += int(1000 * self.score_meter_multiplier * self.difficulty_multiplier)
                    else:
                        self.score += int(100 * self.score_meter_multiplier * self.difficulty_multiplier)
                return True
        return False

    def orange_peg_remove(self):
        """Updates the orange peg variable"""
        self.orange_pegs -= 1

        # Update the score meter rectangle
        self.score_meter_rect = pygame.Rect(0, 0, 40, ((self.TOTAL_ORANGE - self.orange_pegs)/self.TOTAL_ORANGE) * 400)
        self.score_meter_rect.bottomleft = (WINDOW_WIDTH - 120, 550)

        # Find the corresponding score meter multiplier to use
        if (self.TOTAL_ORANGE - self.orange_pegs)/self.TOTAL_ORANGE > 9/10:
            self.score_meter_multiplier = 10
        elif (self.TOTAL_ORANGE - self.orange_pegs)/self.TOTAL_ORANGE > 7/10:
            self.score_meter_multiplier = 5
        elif (self.TOTAL_ORANGE - self.orange_pegs)/self.TOTAL_ORANGE > 4/10:
            self.score_meter_multiplier = 2


class Ball(pygame.sprite.Sprite):
    """A class to create and manage the ball"""
    def __init__(self, game):
        """Initialise the ball"""
        # Initialise it as a sprite
        super().__init__()
        self.game = game

        # Create a surface for the ball
        self.image = pygame.Surface((31, 31), pygame.SRCALPHA)
        self.radius = 15

        # Draw a circle for the ball
        pygame.gfxdraw.aacircle(self.image, 15, 15, self.radius, BLACK)
        pygame.gfxdraw.filled_circle(self.image, 15, 15, self.radius, BLACK)

        # Get the rect
        self.rect = self.image.get_rect()

        # Set the position as a vector
        self.position = pygame.math.Vector2(WINDOW_WIDTH//2, 700)
        self.velocity = pygame.math.Vector2(0, 0)

        # Set the rect corresponding to the vector
        self.rect.center = (self.position.x, self.position.y)

        # Create the directional vector
        self.direction = pygame.math.Vector2(1, 1)

        self.point_of_intersection = pygame.math.Vector2(2131, 1)

        # Create a variable that determines if the ball has fallen into the pit
        self.fallen = False
        self.shot = False

    def update(self):
        """Update the ball"""
        # Check if the ball will still be in the playing area next shot
        if self.rect.left + self.velocity.x < 5:
            # If the ball will be to the left of the screen we want to set it to the left
            self.rect.left = 5
            # Updating our position vector from the rect
            self.position.x = self.rect.centerx
            # Bouncing the ball
            self.velocity.x = self.velocity.x * -0.6
        elif self.rect.right + self.velocity.x > WINDOW_WIDTH - 130:
            # If the ball will be to the left of the screen we want to set it to the left
            self.rect.right = WINDOW_WIDTH - 130
            # Updating our position vector from the rect
            self.position.x = self.rect.centerx
            # Bouncing the ball
            self.velocity.x = self.velocity.x * -0.6
        elif self.rect.bottom > WINDOW_HEIGHT + 100:
            self.fallen = True
            self.shot = False
        else:
            # If it is still in play we want to make it go downwards
            self.position = self.velocity + self.position
            # Adding gravity to our velocity
            self.velocity += self.game.GRAVITY

        # Updating any changes made to the position to the rect
        self.rect.center = (self.position.x, self.position.y)

    def shoot(self, values):
        """Repositions the ball and velocity to shoot"""

        cannon_tip, tip_direction = values
        # Place the ball in the cannons position
        self.position = cannon_tip
        self.rect.center = self.position

        # Change the velocity of the ball
        self.velocity.x = 16 * tip_direction.x
        self.velocity.y = 16 * tip_direction.y

        self.shot = True
        self.fallen = False

    def bounce(self, peg_position, touching_distance):
        """Bounces the ball off of the pegs"""
        # Set the position to the edge of the peg
        # Store a temporary velocity that is the in the same direction but much slower
        temp_velocity = pygame.math.Vector2(self.velocity.x * 0.001, self.velocity.y * 0.001)

        direction = peg_position - self.position
        # Create a while loop
        touching = False
        while not touching:
            # Keep edging the ball towards the peg
            self.position += temp_velocity

            # Find the distance between the peg and the ball
            direction = peg_position - self.position

            # Check if the ball is touching the peg
            if direction.length() <= touching_distance:
                # Break out of the while loop
                touching = True

        # Change the direction vector, so it has a length of one
        direction = direction.normalize()

        # Store the current velocity so we have a copy
        old_velocity = self.velocity

        # Find the dot product between the velocity and the direction
        dot_product = old_velocity.dot(direction)

        # Adjust the velocity so that the ball bounces off the peg
        self.velocity.x = old_velocity.x + (-2 * direction.x * dot_product)
        self.velocity.y = old_velocity.y + (-2 * direction.y * dot_product)

        # Scale the velocity so some speed is lost
        self.velocity.scale_to_length(self.velocity.length() * 0.8)

        # Set the center of the ball to the position vector
        self.rect.center = self.position


class Cannon(pygame.sprite.Sprite):
    """An object that can shoot a ball"""
    def __init__(self, game):
        """Initialise the cannon"""
        super().__init__()
        self.game = game
        # Create a surface for the Cannon
        self.image = pygame.Surface((35, 110), pygame.SRCALPHA)
        self.image.fill(YELLOW)

        pygame.draw.rect(self.image, BLACK, (0, 0, 35, 110))

        # Copy of the original image
        self.orig_image = self.image

        # Get the rect
        self.rect = self.image.get_rect()

        # Set the position as a vector
        self.position = pygame.math.Vector2((WINDOW_WIDTH-125)//2, 100)

        # Set the rect corresponding to the vector
        self.rect.midtop = (self.position.x, self.position.y)

        # Set the angle
        self.angle = 0

        # Vector for the difference between the center and the point of rotation
        self.offset = pygame.math.Vector2(0, 55)

        # Create the directional vector
        self.direction = pygame.math.Vector2(math.sin(math.radians(-self.angle)), math.cos(math.radians(self.angle)))

    def rotate_cannon(self, mouse_cursor):
        """Rotates the cannon"""
        # Use trigonometry to find the angle
        if mouse_cursor[1] > 100:
            self.angle = math.degrees(math.atan(((mouse_cursor[0] - (WINDOW_WIDTH-125)//2)/(100 - mouse_cursor[1]))))

        # Makes sure the cannon does not rotate into the HUD
        if self.angle > 90:
            angle_to_use = 90
        elif self.angle < -90:
            angle_to_use = -90
        else:
            angle_to_use = self.angle

        # Rotate the image
        self.image = pygame.transform.rotate(self.orig_image, -angle_to_use)
        # Rotate the offset vector
        offset_rotated = self.offset.rotate(angle_to_use)
        # Create a new rect with the center of the sprite + the offset
        self.rect = self.image.get_rect(center=self.position+offset_rotated)

    def find_tip_direction(self):
        """Returns the tip and direction of the cannon"""
        # Find the x and y coordinates
        x = ((WINDOW_WIDTH-125)//2) - (110 * math.sin(math.radians(self.angle)))
        y = 100 + (110 * math.cos(math.radians(self.angle)))

        self.direction = pygame.math.Vector2(math.sin(math.radians(-self.angle)), math.cos(math.radians(self.angle)))

        # Return the x and y coordinates as a vector
        return pygame.math.Vector2(x, y), self.direction

    def aim_sight(self):
        """Finds and draws the sight to aim"""
        cannon_position, tip_direction = self.find_tip_direction()
        # Finds what the velocity of the ball would be if were shot now
        ball_velocity = tip_direction * 16

        # Creates 10 dots at where the position of the ball would be, equidistant in terms of time
        aim_rect = pygame.Rect(0, 0, 3, 3)
        for i in range(10):
            new_position = cannon_position + (i * 2 * ball_velocity) + (1/2 * self.game.GRAVITY * ((i * 2) ** 2))
            aim_rect.center = new_position
            pygame.draw.rect(display_surface, BLACK, aim_rect)


class Peg(pygame.sprite.Sprite):
    """A class to create the pegs"""
    def __init__(self, colour, position):
        """Initialises the peg"""
        # Initialise it as a sprite
        super().__init__()

        # Set the colour and position
        self.colour = colour
        self.position = position

        # Set radius
        self.radius = 8

        # Create a surface for the peg
        self.image = pygame.Surface((17, 17), pygame.SRCALPHA)

        # Draw a circle for the peg
        pygame.gfxdraw.aacircle(self.image, 8, 8, self.radius, self.colour)
        pygame.gfxdraw.filled_circle(self.image, 8, 8, self.radius, self.colour)

        # Set the rect and position of rect
        self.rect = self.image.get_rect()
        self.rect.center = self.position

        # Create the boolean variable that represents whether it has been hit or not
        self.hit = False

    def hit_peg(self):
        """Changes colour of peg and marks it as hit"""
        # Find the colour to use from the type
        if self.colour == BLUE:
            colour_to_use = LIGHT_BLUE
        elif self.colour == ORANGE:
            colour_to_use = LIGHT_ORANGE
        else:
            colour_to_use = LIGHT_VIOLET

        # Redraw the peg as being marked as hit
        pygame.gfxdraw.aacircle(self.image, 8, 8, self.radius, colour_to_use)
        pygame.gfxdraw.filled_circle(self.image, 8, 8, self.radius, colour_to_use)

        # Set the hit variable to true
        self.hit = True


class Pause(Menu):

    def __init__(self, game, current_play):
        super().__init__(game)
        self.current_play = current_play

        self.title_text = font_subtitle.render("Pause Menu", True, BLACK)
        self.title_rect = self.title_text.get_rect()
        self.title_rect.center = (WINDOW_WIDTH//2, 40)
        self.text_to_draw.append([self.title_text, self.title_rect])

        self.return_text = font_menu.render("Return", True, BLACK)
        self.return_rect = self.return_text.get_rect()
        self.return_rect.center = ((WINDOW_WIDTH//2), WINDOW_HEIGHT//2 - 100)
        self.return_border = pygame.Rect(0, 0, 260, 100)
        self.return_border.center = self.return_rect.center
        self.text_to_draw.append([self.return_text, self.return_rect])
        self.borders_to_draw.append([self.return_border, self.current_play])

        self.settings_text = font_menu.render("Settings", True, BLACK)
        self.settings_rect = self.settings_text.get_rect()
        self.settings_rect.center = ((WINDOW_WIDTH//2), WINDOW_HEIGHT//2 + 50)
        self.settings_border = pygame.Rect(0, 0, 260, 100)
        self.settings_border.center = self.settings_rect.center
        self.text_to_draw.append([self.settings_text, self.settings_rect])
        self.borders_to_draw.append([self.settings_border, Settings])

        self.quit_text = font_menu.render("Quit", True, BLACK)
        self.quit_rect = self.quit_text.get_rect()
        self.quit_rect.center = ((WINDOW_WIDTH//2), WINDOW_HEIGHT//2 + 200)
        self.quit_border = pygame.Rect(0, 0, 260, 100)
        self.quit_border.center = self.quit_rect.center
        self.text_to_draw.append([self.quit_text, self.quit_rect])
        self.borders_to_draw.append([self.quit_border, MainMenu])

    def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
                break
            elif event.type == pygame.MOUSEBUTTONUP:
                for border, menu in self.borders_to_draw:
                    if border.collidepoint(pygame.mouse.get_pos()):
                        if border == self.return_border:
                            self.game.current_menu = menu
                        elif border == self.settings_border:
                            self.game.current_menu = menu(self.game, self.game.current_menu)
                        else:
                            self.game.current_menu = menu(self.game)
                            pygame.mixer.music.load(resource_path("assets/sounds/Sunset_By_the_Lake.mp3"))
                            pygame.mixer.music.set_volume(self.game.music_volume)
                            pygame.mixer.music.play(-1)

        # Fill the display surface
        display_surface.fill(YELLOW)
        self.draw()


class Win(Menu):

    def __init__(self, game, score, stage):
        super().__init__(game)

        pygame.mixer.music.load(resource_path("assets/sounds/Sunset_By_the_Lake.mp3"))
        pygame.mixer.music.set_volume(self.game.music_volume)
        pygame.mixer.music.play(-1)

        self.score = score
        self.stage = stage
        self.highscore_text = font_menu.render("You are not logged in.", True, BLACK)
        if self.game.current_user != 0:
            with open(resource_path("assets/other/Users.txt"), "a+") as file:
                file.seek(0)
                users = [line for line in file]
                index = 0
                for line in users:
                    user = line.strip().split(', ')
                    if user[0] == self.game.current_user:
                        user = line.strip().split(', ')
                        self.highscore_text = font_menu.render(f"Your High Score is {user[self.stage]}.", True, BLACK)
                        break
                    else:
                        index += 1
                current_user = self.game.current_user
                if self.score > int(user[self.stage].strip()):
                    user[self.stage] = self.score
                    users[index] = f"{user[0]}, {user[1]}, {user[2]}, {user[3]}\n"
                    self.game.current_user = user[0]
                    file.seek(0)
                    file.truncate()
                    self.highscore_text = font_menu.render(f"You have achieved a new High Score for this stage!", True, BLACK)
                    for user in users:
                        file.write(user)

        with open(resource_path("assets/other/Users.txt"), "r") as file:
            file.seek(0)
            users = [line for line in file]
            current_high = 0
            is_high_user = False
            current_high_user = 0
            for user in users:
                temp_user = user.strip().split(', ')
                if int(temp_user[self.stage]) > current_high:
                    current_high = int(temp_user[self.stage])
                    current_high_user = temp_user[0]
                    if temp_user[0] == self.game.current_user:
                        if self.score == current_high:
                            is_high_user = True
                        else:
                            is_high_user = False
                    else:
                        is_high_user = False
                        if self.score == int(temp_user[self.stage].strip()):
                            is_high_user = True
            if self.score > current_high:
                is_high_user = True

        if is_high_user:
            self.high_text = font_regular.render("Congrats! You have achieved the highest score for this stage!", True, BLACK)
        else:
            self.high_text = font_regular.render(f"The current highest score for this stage is {current_high} held by {current_high_user}", True, BLACK)

        self.high_rect = self.high_text.get_rect()
        self.high_rect.center = ((WINDOW_WIDTH // 2), WINDOW_HEIGHT // 2 + 75)
        self.text_to_draw.append([self.high_text, self.high_rect])

        self.highscore_rect = self.highscore_text.get_rect()
        self.highscore_rect.center = ((WINDOW_WIDTH // 2), WINDOW_HEIGHT // 2 + 25)
        self.text_to_draw.append([self.highscore_text, self.highscore_rect])

        self.title_text = font_subtitle.render("Stage complete!", True, BLACK)
        self.title_rect = self.title_text.get_rect()
        self.title_rect.center = ((WINDOW_WIDTH // 2), 100)
        self.text_to_draw.append([self.title_text, self.title_rect])

        self.score_text = font_menu.render("Your score was: {0}".format(self.score), True, BLACK)
        self.score_rect = self.score_text.get_rect()
        self.score_rect.center = ((WINDOW_WIDTH // 2), WINDOW_HEIGHT // 2 - 50)
        self.text_to_draw.append([self.score_text, self.score_rect])

        self.return_text = font_menu.render("Return", True, BLACK)
        self.return_rect = self.return_text.get_rect()
        self.return_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT - 75)
        self.return_border = pygame.Rect(0, 0, 250, 100)
        self.return_border.center = self.return_rect.center
        self.text_to_draw.append([self.return_text, self.return_rect])
        self.borders_to_draw.append([self.return_border, MainMenu])

    def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
                break
            elif event.type == pygame.MOUSEBUTTONUP:
                for border, menu in self.borders_to_draw:
                    if border.collidepoint(pygame.mouse.get_pos()):
                        self.game.current_menu = menu(self.game)

        # Fill the display surface
        display_surface.fill(YELLOW)
        self.draw()


class Lose(Menu):
    def __init__(self, game):
        super().__init__(game)

        pygame.mixer.music.load(resource_path("assets/sounds/Sunset_By_the_Lake.mp3"))
        pygame.mixer.music.set_volume(self.game.music_volume)
        pygame.mixer.music.play(-1)

        self.title_text = font_subtitle.render("Stage Failed!", True, BLACK)
        self.title_rect = self.title_text.get_rect()
        self.title_rect.center = ((WINDOW_WIDTH // 2), 100)
        self.text_to_draw.append([self.title_text, self.title_rect])

        self.return_text = font_menu.render("Return", True, BLACK)
        self.return_rect = self.return_text.get_rect()
        self.return_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT - 75)
        self.return_border = pygame.Rect(0, 0, 250, 100)
        self.return_border.center = self.return_rect.center
        self.text_to_draw.append([self.return_text, self.return_rect])
        self.borders_to_draw.append([self.return_border, MainMenu])

    def loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
                break
            elif event.type == pygame.MOUSEBUTTONUP:
                for border, menu in self.borders_to_draw:
                    if border.collidepoint(pygame.mouse.get_pos()):
                        self.game.current_menu = menu(self.game)

        # Fill the display surface
        display_surface.fill(YELLOW)
        self.draw()


class Game:
    """Class to manage the running of the entire game"""

    def __init__(self):
        self.running = True
        self.current_menu = UserMenu(self)
        self.clock = pygame.time.Clock()

        self.music_volume = 0.5
        self.sound_volume = 0.5

        pygame.mixer.init()
        pygame.mixer.music.load(resource_path("assets/sounds/Sunset_By_the_Lake.mp3"))
        pygame.mixer.music.set_volume(self.music_volume)
        pygame.mixer.music.play(-1)

        self.hit_sound = pygame.mixer.Sound(resource_path("assets/sounds/Coffee1.mp3"))
        self.hit_sound.set_volume(self.sound_volume)

        self.current_user = 0
        self.current_stage = 0
        self.difficulty = 0

        self.GRAVITY = pygame.math.Vector2(0.0000001, 0.3)

        self.loop()

    def loop(self):
        while self.running:
            self.current_menu.loop()

            pygame.display.update()

            self.clock.tick(FPS)


my_game = Game()

pygame.quit()
