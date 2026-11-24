import os

# One-line pitch: retired racing pigeons deliver handwritten apologies.
LINE = "We train retired racing pigeons to deliver handwritten apologies across the city for $12 each, because forgetful husbands pay gladly when sorry arrives by bird, not by text."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
