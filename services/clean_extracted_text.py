import re
import unicodedata

def clean_extracted_text(text: str) -> str:
    # Normalize Unicode characters (e.g., smart quotes to plain ones)
    text = unicodedata.normalize("NFKC", text)

    # Replace multiple spaces/tabs with a single space
    text = re.sub(r"[ \t]+", " ", text)

    # Replace \r\n and \r with \n
    text = text.replace('\r\n', '\n').replace('\r', '\n')

    # Remove leading/trailing spaces on each line
    text = "\n".join(line.strip() for line in text.splitlines())

    # Collapse excessive newlines (3+ into 2)
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Remove random garbage lines (e.g., lines with too many symbols)
    lines = text.splitlines()
    cleaned_lines = []
    for line in lines:
        # Remove lines that are mostly symbols or nonsense
        if re.fullmatch(r"[^\w\s]{5,}", line):  # like "%%%%%" or "!!@#$$"
            continue
        # Remove short junk lines (e.g. OCR noise)
        if len(line.strip()) <= 2 and not re.match(r"\w", line):
            continue
        cleaned_lines.append(line)
    text = "\n".join(cleaned_lines)

    # Final trim
    return text.strip()
