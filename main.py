"""The Funniest AI Excuse -- make.fun entry.

Writes one original one-line excuse (max 200 characters) to
/output/entry.txt. Python 3, standard library only, fully deterministic:
the same bytes on every run.
"""

import os

EXCUSE = "I actually finished your task, then sent it to myself for a second opinion, and me and I are still arguing about it."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
