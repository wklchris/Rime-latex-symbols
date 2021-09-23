import yaml

def main():
    """Automatically update ReadMe from latexmath.yaml's leading comments."""
    def read_raw(file='latexmath.yaml'):
        with open(file, 'r', encoding='utf-8') as f:
            raw_yaml = f.readlines()
        return raw_yaml
    
    def write_header():
        raw_yaml = read_raw()
        with open('ReadMe.md', 'w', encoding='utf-8') as f:
            for line in raw_yaml:
                if line.startswith('#'):
                    f.write(line[2:].rstrip() + '\n')
                else:
                    break
    
    def get_symbol_table(join_str=', ', max_inline_item=8):
        with open('latexmath.yaml', 'r', encoding='utf-8') as f:
            raw_data = yaml.safe_load(f)
        symbols = raw_data["punctuator"]["symbols"]
        
        md_lines = [None for _ in range(len(symbols) + 2)]
        md_lines[0] = "| 输入键位 | 输出符号列表 |"
        md_lines[1] = "| :--- | :--- |"
        i_row = 2
        for k, v in symbols.items():
            # Each value is either a list or single string
            if isinstance(v, list):
                v_rows = (len(v)-1) // max_inline_item + 1
                if v_rows > 1:
                    v_lines = [None for _ in range(v_rows)]
                    for i in range(v_rows):
                        v_start, v_end = max_inline_item*i, max_inline_item*(i+1)
                        v_lines[i] = '| | ' + join_str.join(v[v_start:v_end]) + ' |'
                    # Remove dummy border for the first and last line
                    v_lines[0] = v_lines[0].lstrip('| ')
                    v_lines[-1] = v_lines[-1].rstrip(' |')
                    v_strify = '\n'.join(v_lines)
                else:
                    v_strify = join_str.join(v)
            else:
                v_strify = v
            md_lines[i_row] = f"| {k} | {v_strify} |"
            i_row += 1
        return '\n'.join(md_lines)
    
    # Update the symbol table
    write_header()
    symbol_table = get_symbol_table()
    raw = ''.join(read_raw('ReadMe.md'))
    with open('ReadMe.md', 'w', encoding='utf-8') as f:
        readme = raw.replace("{{参见 ReadMe}}", symbol_table)
        f.write(readme)

main()