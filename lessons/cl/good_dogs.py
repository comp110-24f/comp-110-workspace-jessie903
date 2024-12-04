"""Practice with recursive functions."""


def all_good(scores: list[dict[str, str]], thresh: int, idx: int) -> bool:
    is_good: bool = int(scores[idx]["score"]) >= thresh  # indicates true
    is_last: bool = idx + 1 == len(scores)  # indicates false
    if is_good:  # 1st base case
        if is_last:  # 2nd base case
            return True
        else:
            return all_good(scores, thresh, idx + 1)
    else:
        return False


pack: list[dict[str, str]] = [
    {"name": "Nelli", "score": "10"},
    {"name": "Ada", "score": "9"},
    {"name": "Pip", "score": "7"},
]

print(all_good(scores=pack, thresh=7, idx=0))
