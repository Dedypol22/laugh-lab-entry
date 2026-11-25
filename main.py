import os

# One-liner entry: the robot vacuum's deadpan legal defence for eating a sock.
LINE = "Under vacuum law, anything on the floor is lunch. Your sock was on the floor."


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
