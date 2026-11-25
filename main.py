import os

# The power is pure redundancy: conjuring a banana you already hold
# achieves exactly nothing, which is the whole joke.
ENTRY = "I can conjure a perfectly ripe banana out of thin air, but only while I'm already holding one."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
output_path = os.path.join(output_dir, "entry.txt")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(ENTRY)
