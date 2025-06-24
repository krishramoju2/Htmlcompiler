import markdown
import sys
import os

def convert_md_to_html(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"Error: '{input_file}' does not exist.")
        return

    with open(input_file, "r", encoding="utf-8") as f:
        md_content = f.read()

    html = markdown.markdown(md_content, extensions=["extra", "codehilite", "toc"])

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ Converted '{input_file}' to '{output_file}'")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python converter.py <input.md> <output.html>")
    else:
        input_md = sys.argv[1]
        output_html = sys.argv[2]
        convert_md_to_html(input_md, output_html)
