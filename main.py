from pathlib import Path

line = "We rent out trained goats to clear your garden weeds for $19 a visit, because a goat eats what a mower misses and never asks for a day off."

out = Path("/output/entry.txt")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(line, encoding="utf-8")
print(len(line))
