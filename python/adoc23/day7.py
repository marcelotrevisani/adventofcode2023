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
    def __init__(self, cards: str, enable_joker: bool = False):
        CARDS_RANK = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
        if enable_joker:
            CARDS_RANK.remove("J")
            CARDS_RANK.append("J")

        self.enable_joker = enable_joker
        self.cards = cards
        self.CARDS_RANK = CARDS_RANK
        self.count = Counter(cards)
        self.game_rank = self.get_game_rank()

    def __repr__(self):
        return f"Cards('{''.join(self.cards)}', {self.game_rank})"

    def get_game_rank(self):
        if self.enable_joker and "J" in self.cards:
            most_commons = self.count.most_common()
            num_j = self.count["J"]
            if num_j == 5:
                return GameRank.FiveOfAKind
            all_num = [val for card, val in most_commons if card != "J"]
            if num_j > 0:
                all_num[0] += num_j
        else:
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
                return self.CARDS_RANK.index(card) < other.CARDS_RANK.index(card_other)
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


def solution2(all_input: str) -> int:
    re_input = re.compile(r"(\w+)\s+(\d+)")
    all_hands_bids = []

    for line in all_input.splitlines():
        cards, bid = re_input.match(line).groups()
        all_hands_bids.append((Cards(cards, enable_joker=True), int(bid)))
    sorted_hands = sorted(all_hands_bids, key=itemgetter(0))
    return sum(
        hand_bid[1] * rank for rank, hand_bid in enumerate(sorted_hands, start=1)
    )
