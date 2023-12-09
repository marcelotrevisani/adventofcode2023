from enum import Enum
import re
from collections import Counter
from operator import itemgetter
from typing import Self


class GameRank(Enum):
    FiveOfAKind = 7
    FourOfAKind = 6
    FullHouse = 5
    ThreeOfAKind = 4
    TwoPair = 3
    OnePair = 2
    HighCard = 1


class Cards:
    CARDS_RANK = ("A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2")

    def __init__(self, cards: str):
        self.cards = cards
        self.count = Counter(cards)
        self.game_rank = self.get_game_rank()

    def __repr__(self):
        return f"Cards('{''.join(self.cards)}', {self.game_rank})"

    def get_game_rank(self):
        all_num = list(self.count.values())
        if 5 in all_num:
            return GameRank.FiveOfAKind
        if 4 in all_num:
            return GameRank.FourOfAKind
        if 3 in all_num:
            if 2 in all_num:
                return GameRank.FullHouse
            else:
                return GameRank.ThreeOfAKind
        if 2 in all_num:
            if all_num.count(2) == 2:
                return GameRank.TwoPair
            else:
                return GameRank.OnePair
        return GameRank.HighCard

    def __iter__(self):
        return iter(self.cards)

    def __eq__(self, other: Self):
        return self.cards == other.cards

    def __gt__(self, other: Self):
        if self.game_rank == other.game_rank:
            for card, card_other in zip(self.cards, other.cards):
                if card == card_other:
                    continue
                return Cards.CARDS_RANK.index(card[0]) < Cards.CARDS_RANK.index(
                    card_other[0]
                )
        return self.game_rank.value > other.game_rank.value


def solution1(all_input: str) -> int:
    re_input = re.compile(r"(\w+)\s+(\d+)")
    all_hands_bids = []

    for line in all_input.splitlines():
        cards, bid = re_input.match(line).groups()
        all_hands_bids.append((Cards(cards), int(bid)))
    sorted_hands = sorted(all_hands_bids, key=itemgetter(0))
    return sum(
        hand_bid[1] * rank for rank, hand_bid in enumerate(sorted_hands, start=1)
    )
