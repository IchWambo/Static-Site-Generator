
def extract_title(markdown):
    stripped_markdown = markdown.strip()
    split_strings = stripped_markdown.splitlines()
    for i, raw in enumerate(markdown.splitlines()):
        line = raw.lstrip()
        print(i, "RAW:", repr(raw), "LSTRIP:", repr(line))
        if line.startswith("# "):
            return line[2:].strip()
    raise Exception("No Header found.")

def main():
    extract_title

if __name__ == "__main__":
    main()