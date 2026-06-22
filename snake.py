import arcade
import random

# --- Constants ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Snake Game"

CELL_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // CELL_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // CELL_SIZE

MOVE_SPEED = 0.15


class SnakeGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)

        # Load images
        self.head_image = arcade.load_texture("assets/snake_head.png")
        self.body_image = arcade.load_texture("assets/snake_body.png")
        self.food_image = arcade.load_texture("assets/apple.png")

        # Snake body positions
        self.snake = [
            (10, 15),
            (9, 15),
            (8, 15),
        ]

        # Starting direction
        self.direction = (1, 0)

        # Timer
        self.timer = 0

        # Game state
        self.game_over = False

        # Score
        self.score = 0

        # Food position
        self.food = None
        self.spawn_food()


    def spawn_food(self):
        """Place food at random position NOT on the snake"""
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            if (x, y) not in self.snake:
                self.food = (x, y)
                break


    def on_draw(self):
        self.clear()

        if self.game_over:
            arcade.draw_text(
                "GAME OVER",
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2 + 30,
                arcade.color.RED,
                font_size=40,
                anchor_x="center",
                anchor_y="center"
            )
            arcade.draw_text(
                f"Score: {self.score}",
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2 - 20,
                arcade.color.WHITE,
                font_size=25,
                anchor_x="center",
                anchor_y="center"
            )
            arcade.draw_text(
                "Press R to Restart",
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 2 - 60,
                arcade.color.WHITE,
                font_size=20,
                anchor_x="center",
                anchor_y="center"
            )
            return

        # --- Draw Food (Apple Image) ---
        food_x = self.food[0] * CELL_SIZE + CELL_SIZE / 2
        food_y = self.food[1] * CELL_SIZE + CELL_SIZE / 2

        arcade.draw_texture_rect(
            self.food_image,
            arcade.rect.XYWH(
                food_x - CELL_SIZE / 2,
                food_y - CELL_SIZE / 2,
                CELL_SIZE,
                CELL_SIZE
            )
        )

        # --- Draw Snake (Images) ---
        for index, (x, y) in enumerate(self.snake):

            pixel_x = x * CELL_SIZE + CELL_SIZE / 2
            pixel_y = y * CELL_SIZE + CELL_SIZE / 2

            if index == 0:
                texture = self.head_image
            else:
                texture = self.body_image

            arcade.draw_texture_rect(
                texture,
                arcade.rect.XYWH(
                    pixel_x - CELL_SIZE / 2,
                    pixel_y - CELL_SIZE / 2,
                    CELL_SIZE,
                    CELL_SIZE
                )
            )

        # --- Draw Score ---
        arcade.draw_text(
            f"Score: {self.score}",
            10,
            SCREEN_HEIGHT - 30,
            arcade.color.WHITE,
            font_size=18
        )


    def on_update(self, delta_time):
        if self.game_over:
            return

        self.timer += delta_time

        if self.timer >= MOVE_SPEED:
            self.timer = 0
            self.move_snake()


    def move_snake(self):
        head_x, head_y = self.snake[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)

        if (new_head[0] < 0 or
            new_head[0] >= GRID_WIDTH or
            new_head[1] < 0 or
            new_head[1] >= GRID_HEIGHT):
            self.game_over = True
            return

        if new_head in self.snake:
            self.game_over = True
            return

        if new_head == self.food:
            self.score += 1
            self.spawn_food()
            self.snake.insert(0, new_head)
        else:
            self.snake.insert(0, new_head)
            self.snake.pop()


    def reset_game(self):
        self.snake = [
            (10, 15),
            (9, 15),
            (8, 15),
        ]
        self.direction = (1, 0)
        self.timer = 0
        self.game_over = False
        self.score = 0
        self.spawn_food()


    def on_key_press(self, key, modifiers):

        if key == arcade.key.R and self.game_over:
            self.reset_game()
            return

        if self.game_over:
            return

        if key == arcade.key.RIGHT and self.direction != (-1, 0):
            self.direction = (1, 0)

        elif key == arcade.key.LEFT and self.direction != (1, 0):
            self.direction = (-1, 0)

        elif key == arcade.key.UP and self.direction != (0, -1):
            self.direction = (0, 1)

        elif key == arcade.key.DOWN and self.direction != (0, 1):
            self.direction = (0, -1)


def main():
    window = SnakeGame()
    arcade.run()


if __name__ == "__main__":
    main()