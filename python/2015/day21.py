from dataclasses import dataclass, field


@dataclass
class Item:
    cost: int
    damage: int
    armor: int


@dataclass
class Player:
    hit: int
    damage: int
    armor: int
    name: str
    cost: int


def winner(player1: Player, player2: Player):
    round: int = 1
    while True:
        # player1's turn
        if player1.damage <= player2.armor:
            player2.hit -= 1
        else:
            player2.hit -= player1.damage - player2.armor

        if player2.hit == 0:
            return player1

        # player2's turn
        if player2.damage <= player2.armor:
            player1.hit -= 1
        else:
            player1.hit -= player2.damage - player1.armor

        if player1.hit == 0:
            return player2

        # print(f"round {round}: {player1}, {player2}")

        round += 1


def modplayer(player: Player, item: Item) -> Player:
    player.cost += item.cost
    player.damage += item.damage
    player.armor += item.armor
    return player


if __name__ == "__main__":
    items: dict = dict()
