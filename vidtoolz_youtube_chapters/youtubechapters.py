import re
import argparse
import sys


def read_timeline_from_file(file_path):
    """Reads a file containing a timeline and returns its format."""
    try:
        with open(file_path, "r") as file:
            text = file.read()
            return format_timeline(text)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None


def format_timeline(text):
    # Pattern to match times like 0, 40s, 1m20s, 10m30
    time_pattern = r"\d+m?\d*s?|\d+m\d{0,2}"

    # Split the text into tokens (time or event)
    tokens = re.findall(rf"({time_pattern})|([^\d,]+)", text, re.IGNORECASE)

    timeline = []
    i = 0

    while i < len(tokens):
        time_match, event_match = tokens[i]

        # If token is a time
        if time_match:
            time_str = normalize_time(time_match)

            # Check if next token is an event
            if i + 1 < len(tokens):
                next_time, next_event = tokens[i + 1]
                if next_event:
                    event = next_event.strip().title()
                    i += 1  # Move past the event
                else:
                    event = "Untitled Event"
            else:
                event = "Untitled Event"

            timeline.append(f"{time_str} {event}")
        i += 1

    return "\n".join(timeline)


def normalize_time(time_str):
    """Converts time formats like 1m20s, 10m30, 40s, 0 to MM:SS."""
    minutes, seconds = 0, 0

    # Handle formats like 1m20s or 10m30
    match = re.match(r"(?:(\d+)m)?(?:(\d+)s?)?", time_str)
    if match:
        minutes = int(match.group(1) or 0)
        seconds = int(match.group(2) or 0)

    return f"{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"


def main():
    parser = argparse.ArgumentParser(description="Format a timeline from input.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-f", "--file_path", type=str, help="Path to the input file.", default=None
    )
    group.add_argument(
        "-t",
        "--text",
        nargs="*",
        help="Supply text or if '-' Read from standard input instead of file.",
    )

    args = parser.parse_args()

    if args.file_path:
        print(read_timeline_from_file(args.file_path))
    elif args.text:
        text = " ".join(args.text)
        if text == "-":
            try:
                text = str(sys.stdin.buffer.readline())
                print(format_timeline(text))
            except ValueError:
                pass
        else:
            print(format_timeline(text))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
