import argparse
from rhyme_analyzer import rhyme_pattern, count_line_syllables

def main():
    parser = argparse.ArgumentParser(description="Command line parser for the Rhyme Analyzer.")
    
    parser.add_argument("--file", type=str, required=True, help="Path to the file containing the lyrics.")
    parser.add_argument("--pattern", action="store_true", help="Shows the rhyme pattern.")
    parser.add_argument("--syllables", action="store_true", help="Shows the syllables on the line")

    args = parser.parse_args()

    with open(args.file) as f:
        lines = [line.strip() for line in f if line.strip() != ""]
    
    if args.pattern:
        print(rhyme_pattern(lines))
    
    if args.syllables:
        print('Total syllables:')
        for count, line in enumerate(lines, start=1):
            print(f"  Line {count}: {count_line_syllables(line)}")


if __name__ == "__main__":
    main()