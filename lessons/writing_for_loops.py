"""Writing loops practice"""

pets: list[str] = ["Louie", "Bo", "Bear"]
new_list: list[str] = []
for animal in pets:
    print(f"Good boy, {animal}! ")

# PRINT EVERY ELEMENT'S INDEX AND VALUE

names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for idx in range(0, len(names)):
    print(f"{idx}: {names[idx]}")
