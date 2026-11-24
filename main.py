"""Ridiculous at First Glance, Real by the Second — entry program.

Writes one sentence (<=200 chars) pitching a bizarre startup idea that
sounds like a joke at first glance but holds together as a real business
on a second look. Deterministic: the same pitch every run, no randomness,
no network, no input.
"""

import os

# The pitch in one line: an absurd premise (hire a stranger to fire people)
# with a real market behind it (managers pay per sacking to outsource the
# guilt). It names the thing sold and who pays, and the turn lands last:
# nobody shouts at the messenger. It dodges the crowded field angles —
# goats, pothole-naming, pigeon apologies, professional mourners.
PITCH = (
    "We rent out strangers to fire your staff for you, because managers "
    "pay per sacking to skip the guilt and nobody ever shouts at the messenger."
)


def main() -> None:
    pitch = PITCH.strip()
    assert 1 <= len(pitch) <= 200, f"pitch is {len(pitch)} chars"
    assert pitch.count(".") == 1, "pitch must be exactly one sentence"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(pitch)


if __name__ == "__main__":
    main()
