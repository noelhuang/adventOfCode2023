from helpers.parsers import parse_txt_as_string

parsed = parse_txt_as_string('input.txt')
parsed = parsed.strip()
parsed = parsed.split('\n')
parsed = [parsed[i].split() for i in range(len(parsed))]
print(parsed)

count_to_hands_map = {
    (5,): "FiveOfAKind",
    (1, 4): "FourOfAKind",
    (2, 3): "FullHouse",
    (1, 1, 3): "ThreeOfAKind",
    (1, 2, 2): "TwoPair",
    (1, 1, 1, 2): "OnePair",
    (1, 1, 1, 1, 1): "HighCard"
}

card_values = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
}


def cards_to_hand(cards_bid):
    card_map = {
        "A": 0,
        "K": 0,
        "Q": 0,
        "J": 0,
        "T": 0,
        "9": 0,
        "8": 0,
        "7": 0,
        "6": 0,
        "5": 0,
        "4": 0,
        "3": 0,
        "2": 0,
    }
    cards, bid = cards_bid[0], cards_bid[1]
    for card in cards:
        card_map[card] = card_map[card] + 1
    hand_array = []
    for key, value in card_map.items():
        if value > 0:
            hand_array.append(value)
    hand_array.sort()
    hand_tuple = tuple(hand_array)
    hand = count_to_hands_map[hand_tuple]
    hand_bid = [hand, cards, bid]
    return hand_bid


five_of_a_kinds = []
four_of_a_kinds = []
full_houses = []
three_of_a_kinds = []
two_pairs = []
one_pairs = []
high_cards = []


for row in parsed:
    hand_cards_bid_arr = cards_to_hand(row)
    match hand_cards_bid_arr[0]:
        case 'FiveOfAKind':
            five_of_a_kinds.append(hand_cards_bid_arr[1:])
        case 'FourOfAKind':
            four_of_a_kinds.append(hand_cards_bid_arr[1:])
        case 'FullHouse':
            full_houses.append(hand_cards_bid_arr[1:])
        case 'ThreeOfAKind':
            three_of_a_kinds.append(hand_cards_bid_arr[1:])
        case 'TwoPair':
            two_pairs.append(hand_cards_bid_arr[1:])
        case 'OnePair':
            one_pairs.append(hand_cards_bid_arr[1:])
        case 'HighCard':
            high_cards.append(hand_cards_bid_arr[1:])

# Sort the hands based on their strength, within their own hand class
alphabet = "23456789TJQKA"
five_of_a_kinds = sorted(five_of_a_kinds, key=lambda word: [alphabet.index(c) for c in word[0]])
four_of_a_kinds = sorted(four_of_a_kinds, key=lambda word: [alphabet.index(c) for c in word[0]])
full_houses = sorted(full_houses, key=lambda word: [alphabet.index(c) for c in word[0]])
three_of_a_kinds = sorted(three_of_a_kinds, key=lambda word: [alphabet.index(c) for c in word[0]])
two_pairs = sorted(two_pairs, key=lambda word: [alphabet.index(c) for c in word[0]])
one_pairs = sorted(one_pairs, key=lambda word: [alphabet.index(c) for c in word[0]])
high_cards = sorted(high_cards, key=lambda word: [alphabet.index(c) for c in word[0]])

all_hands = high_cards + one_pairs + two_pairs + three_of_a_kinds + full_houses + four_of_a_kinds + five_of_a_kinds

print(all_hands)
score = 0
for i, row in enumerate(all_hands):
    rank = i + 1
    sub_score = rank * int(row[1])
    score += sub_score
print(score)