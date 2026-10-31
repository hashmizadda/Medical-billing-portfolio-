"""Export specialty catalogue from the PHP source as a lightweight JSON reference.
Run: python tools/generate_specialty_pages.py
This helper does not run the website; PHP serves the pages dynamically.
"""
from pathlib import Path
import re, json
source = Path(__file__).resolve().parents[1] / "includes" / "data.php"
target = Path(__file__).resolve().parents[1] / "specialties-catalogue-review.json"
text = source.read_text(encoding="utf-8")
# Export slug/name/short fields for content review. Full specialty pages remain PHP-driven.
items = []
pattern = re.compile(r"'([^']+)'\\s*=>\\s*\\['name'=>'([^']+)'\\s*,\\s*'icon'=>'([^']*)'\\s*,\\s*'short'=>'([^']*)'")
for slug, name, icon, short in pattern.findall(text):
    items.append({"slug": slug, "name": name, "icon": icon, "summary": short})
target.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Exported {len(items)} specialties to {target}")
