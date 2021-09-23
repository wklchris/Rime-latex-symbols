def main():
    """Automatically update ReadMe from latexmath.yaml's leading comments."""
    with open('latexmath.yaml', 'r', encoding='utf-8') as f:
        raw = f.readlines()

    with open('ReadMe.md', 'w', encoding='utf-8') as f:
        for line in raw:
            if line.startswith('#'):
                f.write(line[2:].rstrip() + '\n')
            else:
                break
main()