"""
Hangman Game - Main module.
"""
import sys

VERSION = "0.2.0"

def run(args):
    """Main entry point."""
    print(f"Hangman Game v{VERSION}")
    if args:
        print(f"Processing: {', '.join(args)}")
        process(args)
    else:
        print("Usage: python hangman.py [arguments]")
        print("Try: python hangman.py --help")

def process(args):
    """Process input arguments."""
    records = []
    for arg in args:
        result = arg.strip()
        if result:
            records.append(result)
            print(f"  Processed: {result}")
    print(f"\nTotal: {len(records)} items processed")
    return records

def main():
    run(sys.argv[1:])

if __name__ == "__main__":
    main()
