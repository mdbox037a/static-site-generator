def extract_title(markdown: str) -> str:
    """
    Detect the h1 header in markdown input (the line beginning with '#') and
    return the header as a string
    """
    lines = markdown.splitlines()
    for line in lines:
        clean_line = line.strip()
        if clean_line.startswith("# "):
            return clean_line[2:].strip()
    raise Exception("No h1 detected: invalid document for site conversion")
