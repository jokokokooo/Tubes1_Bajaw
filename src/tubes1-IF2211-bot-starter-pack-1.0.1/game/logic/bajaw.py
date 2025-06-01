import random
from typing import Optional

from game.logic.base import BaseLogic
from game.models import GameObject, Board, Position
from ..util import get_direction


class Bajaw(BaseLogic):  # Nama bot disesuaikan
    def _init_(self):
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.goal_position: Optional[Position] = None
        self.current_direction = 0

    def next_move(self, board_bot: GameObject, board: Board):
        props = board_bot.properties
        current_position = board_bot.position

        # Kembali ke base jika inventory penuh
        if props.diamonds == props.inventory_size:
            self.goal_position = props.base
        else:
            # Cari diamond terdekat yang cukup ringan
            diamonds = [
                obj for obj in board.game_objects
                if obj.type == "DiamondGameObject"
                and getattr(obj.properties, 'weight', 1) <= (props.inventory_size - props.diamonds)
            ]
            if diamonds:
                # Urutkan berdasarkan jarak Manhattan
                diamonds.sort(key=lambda d: abs(d.position.x - current_position.x) + abs(d.position.y - current_position.y))
                self.goal_position = diamonds[0].position
            else:
                self.goal_position = None

        # Jika punya tujuan, coba bergerak ke arah tujuan
        if self.goal_position:
            delta_x, delta_y = get_direction(
                current_position.x,
                current_position.y,
                self.goal_position.x,
                self.goal_position.y,
            )
            if board.is_valid_move(current_position, delta_x, delta_y):
                return delta_x, delta_y

        # Jika tidak valid atau tidak ada tujuan, jalan acak
        for _ in range(4):
            delta = self.directions[self.current_direction]
            delta_x = delta[0]
            delta_y = delta[1]
            if board.is_valid_move(current_position, delta_x, delta_y):
                if random.random() > 0.4:
                    return delta_x, delta_y
            self.current_direction = (self.current_direction + 1) % len(self.directions)

        # Diam jika tidak bisa bergerak
        return 0, 0