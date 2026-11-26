LINE = "I can't come in today — my bed has filed a formal complaint about my absence, and HR (my cat) has approved emergency cuddles until further notice."

# The entry must be one line of under 200 characters.
assert 1 <= len(LINE) < 200, f"line is {len(LINE)} chars"
assert "\n" not in LINE

import os

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)

assert LINE == LINE.strip(), "line must not have leading or trailing whitespace"

with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)

# Read back and verify: a silent bad write must fail loudly, not ship an empty file.
with open(os.path.join(out_dir, "entry.txt"), encoding="utf-8") as f:
    written = f.read()
assert written == LINE, "entry.txt content does not match LINE"
