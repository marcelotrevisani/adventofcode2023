import pytest

from adoc23.day7 import solution1, solution2, Cards, GameRank


@pytest.mark.parametrize(
    "str_card, game_rank",
    [
        ("32T3K", GameRank.OnePair),
        ("KTJJT", GameRank.TwoPair),
        ("QQQJA", GameRank.ThreeOfAKind),
        ("QQQQA", GameRank.FourOfAKind),
        ("QQQQQ", GameRank.FiveOfAKind),
        ("QQQAA", GameRank.FullHouse),
        ("32TAK", GameRank.HighCard),
    ],
)
def test_cards_game_rank(str_card, game_rank):
    card = Cards(str_card)
    assert card.game_rank == game_rank


@pytest.mark.parametrize(
    "lower_cards, higher_cards",
    [
        ("KKKAQ", "222AA"),
        ("KKKKK", "AAAAA"),
        ("22345", "22456"),
        ("QQQAA", "KKK22"),
        ("88992", "99883"),
        ("77993", "99883"),
    ],
)
def test_greater_than_card(lower_cards, higher_cards):
    assert Cards(lower_cards) < Cards(higher_cards)
    assert Cards(higher_cards) > Cards(lower_cards)


def test_solution1_simple():
    all_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
    assert solution1(all_input) == 6440


def test_solution1(shared_datadir):
    all_input = (shared_datadir / "day7.txt").read_text()
    assert solution1(all_input) == 252656917


def test_solution2_simple():
    all_input = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
    assert solution2(all_input) == 5905


def test_solution2(shared_datadir):
    all_input = (shared_datadir / "day7.txt").read_text()
    assert solution2(all_input) == 253499763
