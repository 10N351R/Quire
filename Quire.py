import itertools
import argparse
import os
import string

def load_wordlist(filepath):
    """Load words from a file into a list."""
    if not os.path.exists(filepath):
        print(f"Warning: {filepath} not found. Skipping.")
        return []
    with open(filepath, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def apply_substitutions(word, substitutions):
    """Apply substitutions to dynamic parts of the word."""
    for original, replacement in substitutions.items():
        word = word.replace(original, replacement)
    return word

def append_variations(word, append_chars):
    """Append combinations of numbers, letters, and symbols to the word."""
    char_sets = {
        'n': "0123456789",
        'l': string.ascii_letters,
        's': "!@#$%^&*()"
    }
    
    appended_words = {word}
    for char in append_chars:
        if char not in char_sets:
            continue
        new_words = {base + c for base in appended_words for c in char_sets[char]}
        appended_words = new_words
    
    return appended_words

def generate_wordlist(wordlists, hardcoded, separator, substitutions, append_chars, append_string):
    """Generate all possible word combinations."""
    wordlists = [wl if wl else [''] for wl in wordlists]
    seen_words = set()
    
    for combo in itertools.product(*wordlists):
        full_combo = [hardcoded[i] if hardcoded[i] else combo[i] for i in range(len(combo))]
        word = separator.join(full_combo) if separator else ''.join(full_combo)
        
        word = separator.join(
            apply_substitutions(part, substitutions) if not hardcoded[i] else part
            for i, part in enumerate(word.split(separator) if separator else full_combo)
        )
        
        if append_string:
            final_word = word + append_string
            if final_word not in seen_words:
                seen_words.add(final_word)
                yield final_word
        else:
            for appended_word in append_variations(word, append_chars):
                if appended_word not in seen_words:
                    seen_words.add(appended_word)
                    yield appended_word
logo = r"""
___/\/\/\/\____/\/\____/\/\__/\/\/\/\__/\/\/\/\/\/\__/\/\/\/\/\/\_
_/\/\____/\/\__/\/\____/\/\____/\/\____/\/\____/\/\__/\___________
_/\/\____/\/\__/\/\____/\/\____/\/\____/\/\/\/\/\____/\/\/\/\/\___
_/\/\__/\/\____/\/\____/\/\____/\/\____/\/\__/\/\____/\/\_________
___/\/\/\/\/\____/\/\/\/\____/\/\/\/\__/\/\____/\/\__/\/\/\/\/\/\_
                 Quire.py v1.0 - Author: 10N351R
                  
"""

def main():
    print(logo)
    parser = argparse.ArgumentParser(description="A way to create wordlists from easy-to-remember words, separators, and substitutions")
    parser.add_argument('--separator', type=str, default='', help="Separator character between positions")
    parser.add_argument('--length', type=int, choices=range(1, 6), required=True, help="Number of positions to generate (1-5)")
    parser.add_argument('--outfile', type=str, required=True, help="Output file")
    parser.add_argument('--subs', type=str, default='', help="Character substitutions (e.g., 'a:@ e:3')")
    parser.add_argument('--wordlist', type=str, required=True, help="Wordlist file (e.g., ns, nnnn)")
    parser.add_argument('--append', type=str, default='', help="Append n (numbers), l (letters), s (symbols)")
    parser.add_argument('--appendstring', type=str, default='', help="String to append at the end (cannot be used with -append)")
    
    for i in range(1, 6):
        parser.add_argument(f'-h{i}', type=str, help=f"Mask for position {i}")
    
    args = parser.parse_args()
    
    if args.append and args.appendstring:
        print("Error: --append and --appendstring cannot be used together.")
        return
    
    hardcoded = [getattr(args, f'h{i}', '') or '' for i in range(1, args.length + 1)]
    wordlist = load_wordlist(args.wordlist)
    
    substitutions = {pair.split(':')[0]: pair.split(':')[1] for pair in args.subs.split() if ':' in pair}
    
    num_dynamic_positions = args.length - sum(bool(h) for h in hardcoded)
    total_combinations = len(wordlist) ** num_dynamic_positions if num_dynamic_positions > 0 else 1
    
    if args.append:
        append_factors = {'n': 10, 'l': 52, 's': 10}
        for char in args.append:
            total_combinations *= append_factors.get(char, 1)
    
    print(f"Total combinations to generate: {total_combinations}")
    
    if input("Do you want to proceed? (y/n): ").strip().lower() != 'y':
        print("Operation cancelled.")
        return
    
    with open(args.outfile, 'w', encoding='utf-8') as outfile:
        for word in generate_wordlist([wordlist] * args.length, hardcoded, args.separator, substitutions, args.append, args.appendstring):
            outfile.write(word + '\n')
    
    print(f"Wordlist saved to {args.outfile}")

if __name__ == "__main__":
    main()
