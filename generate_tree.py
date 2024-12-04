import os

def generate_tree(directory, prefix=""):
    tree = ""
    contents = sorted(os.listdir(directory))
    for i, name in enumerate(contents):
        path = os.path.join(directory, name)
        connector = "└── " if i == len(contents) - 1 else "├── "
        tree += f"{prefix}{connector}{'📁 ' if os.path.isdir(path) else '📄 '}{name}\n"
        if os.path.isdir(path):
            tree += generate_tree(path, prefix + ("    " if i == len(contents) - 1 else "│   "))
    return tree

def update_readme(tree_structure):
    readme_path = "README.md"
    with open(readme_path, "r") as readme:
        content = readme.readlines()

    # Identificar o local onde a estrutura deve ser inserida
    start_marker = "```"
    end_marker = "```"
    start_index = next((i for i, line in enumerate(content) if line.strip() == start_marker), -1)
    end_index = next((i for i, line in enumerate(content[start_index + 1:], start=start_index + 1) if line.strip() == end_marker), -1)

    # Substituir ou adicionar a estrutura no README
    if start_index != -1 and end_index != -1:
        content[start_index:end_index + 1] = [start_marker + "\n", tree_structure, end_marker + "\n"]
    else:
        content.append("\n" + start_marker + "\n" + tree_structure + end_marker + "\n")

    with open(readme_path, "w") as readme:
        readme.writelines(content)

if __name__ == "__main__":
    directory = "."  # Diretório atual
    tree = generate_tree(directory)
    update_readme(tree)
