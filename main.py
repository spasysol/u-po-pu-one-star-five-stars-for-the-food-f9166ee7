"""One Star, Five Stars for the Food: an alien's one-star review of Earth.

Writes one sentence to $MAKEFUN_OUTPUT_DIR/entry.txt.
Pure standard library; runs under `python3 -P -s` in the grader sandbox.
"""

import os

LINE = "One star: the locals queue for hours to stare at glowing rectangles, charge money for water, and then serve noodles so good I considered staying."


def main():
    # The gate wants one sentence of 1 to 200 characters, not only white space.
    if not (1 <= len(LINE) <= 200 and LINE.strip() and LINE.count(".") == 1):
        raise ValueError("review is not one sentence inside the 1-200 character gate")
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the entry is the sentence, exactly as written.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
