import yaml
ENCODING = 'utf-8'

def read_raw(file='latexmath.yaml'):
    with open(file, 'r', encoding=ENCODING) as f:
        raw_yaml = f.readlines()
    return raw_yaml

def write_header(raw_yaml):
    with open('ReadMe.md', 'w', encoding=ENCODING) as f:
        for line in raw_yaml:
            if line.startswith('#'):
                f.write(line[2:].rstrip() + '\n')
            else:
                break

def update_readme(yaml_data):
    """Automatically update ReadMe from latexmath.yaml's leading comments."""       
    def get_symbol_table(raw_data, join_str=', ', max_inline_item=8):
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
    symbol_table = get_symbol_table(yaml_data)
    raw = ''.join(read_raw('ReadMe.md'))
    with open('ReadMe.md', 'w', encoding=ENCODING) as f:
        readme = raw.replace("{{参见 ReadMe}}", symbol_table)
        f.write(readme)

def update_compatible(yaml_data):
    headline = '\n'.join([
        "# # 用于 Rime 的 LaTeX 符号输入配置（合并场景）",
        "# （本文件根据 latexmath.yaml 自动生成）",
        "# *author: wklchris@github*"
    ])

    d_compat = {
        "config_version": None,
        "__include": "symbols:/",
        "punctuator": None
    }
    d_update = {k: v for k, v in yaml_data.items() if k in d_compat.keys()}
    d_compat.update(d_update)
    with open('latexmath_compatible.yaml', 'w', encoding=ENCODING) as f:
        f.write(headline + '\n')
        yaml.safe_dump(d_compat, f, sort_keys=False, allow_unicode=True)


def main():
    raw_yaml = read_raw()
    write_header(raw_yaml)
    with open('latexmath.yaml', 'r', encoding=ENCODING) as f:
        yaml_data = yaml.safe_load(f)
    update_readme(yaml_data)
    update_compatible(yaml_data)

main()