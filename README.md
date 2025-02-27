![alt text](https://github.com/10N351R/Quire/blob/main/Images/Logo.png)
# Quire.py
Author: 10N351R

`Quire.py` was created to generate wordlists for passwords that follow [complex schemas](https://xkcd.com/936/) comprised of easy-to-remember words, separators, and substitutions. 

`Quire.py` has several features including
- Generating complex passwords up to 5 positions
- Appending letters, numbers, symbols, custom strings
- Customizable separators (including blanks)
- Character substitution support 
- Position masks

## Usage 
`Quire.py` requires the following arguments following arguments:

`python3 quire.py --length [1-5] --wordlist '[WORDLIST FILE]' --outfile [OUT FILE]`

### Flags
| Flag          | Description                                                   |
|---------------|---------------------------------------------------------------|
| `-h` (`--help`)   | Show help menu                                                |
| `--separator`    | Separator character between positions                         |
| `--length`       | Number of positions to generate (1-5)                              |
| `--outfile`      | Output file                                                   |
| `--subs`         | Character substitutions (e.g., `'a:@ e:3'`)                     |
| `--wordlist`     | Wordlist file                                                 |
| `--append`       | Append n (numbers), l (letters), s (symbols) (e.g., `ns`, `nnnn`) |
| `--appendstring` | String to append to the end of generated passwords            |
| `-h1`           | Mask for position 1                                           |
| `-h2`           | Mask for position 2                                           |
| `-h3`           | Mask for position 3                                           |
| `-h4`           | Mask for position 4                                           |
| `-h5`           | Mask for position 5                                           |


## Output 
![alt text](https://github.com/10N351R/Quire/blob/main/Images/Output.png)

## Disclaimer
**Ethical Use:** This tool is provided for educational and lawful purposes only. The author is not responsible for any misuse or damaged caused by this tool. By using this tool, you agree to use it ethically and comply with all applicable laws and regulations. Unauthorized use of this tool is strictly prohibited and may result in severe legal consequences.

**Use Of Artificial Intelligence:** This tool was developed with the assistance of Artificial Intelligence (AI), and contains portions of code generated using OpenAI's ChatGPT, an AI language model.
