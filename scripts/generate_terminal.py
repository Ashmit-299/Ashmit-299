from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

ASCII_FILE = BASE_DIR / "assets" / "profile-ascii.txt"
OUTPUT_FILE = BASE_DIR / "assets" / "terminal.svg"

ascii_art = ASCII_FILE.read_text(encoding="utf-8")

SVG = f"""<?xml version="1.0" encoding="UTF-8"?>

<svg
xmlns="http://www.w3.org/2000/svg"
width="1400"
height="760"
viewBox="0 0 1400 760">

<style>

.background {{
fill:#0d1117;
}}

.window {{
fill:#161b22;
stroke:#30363d;
stroke-width:2;
}}

.header {{
fill:#21262d;
}}

.title {{
fill:#c9d1d9;
font-family:Consolas,monospace;
font-size:20px;
}}

.red {{
fill:#ff5f56;
}}

.yellow {{
fill:#ffbd2e;
}}

.green {{
fill:#27c93f;
}}

.ascii {{
fill:#58a6ff;
font-family:'Courier New',monospace;
font-size:10px;
font-weight:bold;
white-space:pre;
}}

.label {{
fill:#58a6ff;
font-family:Consolas,monospace;
font-size:20px;
font-weight:bold;
}}

.value {{
fill:#c9d1d9;
font-family:Consolas,monospace;
font-size:20px;
}}

.footer {{
fill:#3fb950;
font-family:Consolas,monospace;
font-size:18px;
}}

</style>

<rect class="background" width="100%" height="100%"/>

<rect
class="window"
x="25"
y="25"
width="1350"
height="710"
rx="18"/>

<rect
class="header"
x="25"
y="25"
width="1350"
height="45"
rx="18"/>

<circle class="red" cx="55" cy="47" r="8"/>
<circle class="yellow" cx="80" cy="47" r="8"/>
<circle class="green" cx="105" cy="47" r="8"/>

<text
class="title"
x="620"
y="52">
ashmit@github:~$
</text>

<text
class="ascii"
x="45"
y="95"
xml:space="preserve">
{ascii_art}
</text>

<text class="label" x="560" y="110">
ASHMIT OS v2.0
</text>

<text class="footer" x="560" y="140">
&gt; Boot sequence completed.
</text>

<text class="label" x="560" y="185">
User
</text>

<text class="value" x="760" y="185">
Ashmit Pandey
</text>

<text class="label" x="560" y="220">
Role
</text>

<text class="value" x="760" y="220">
AI / ML Engineer
</text>

<text class="label" x="560" y="255">
Status
</text>

<text class="value" x="760" y="255">
Open to Work
</text>

<text class="label" x="560" y="300">
OS
</text>

<text class="value" x="760" y="300">
Windows 11
</text>

<text class="label" x="560" y="335">
Editor
</text>

<text class="value" x="760" y="335">
VS Code
</text>

<text class="label" x="560" y="370">
Languages
</text>

<text class="value" x="760" y="370">
Python • SQL • Java
</text>

<text class="label" x="560" y="405">
Frameworks
</text>

<text class="value" x="760" y="405">
FastAPI • OpenCV
</text>

<text class="label" x="560" y="440">
Libraries
</text>

<text class="value" x="760" y="440">
NumPy • Pandas • MediaPipe
</text>

<text class="label" x="560" y="475">
Database
</text>

<text class="value" x="760" y="475">
PostgreSQL
</text>

<text class="label" x="560" y="510">
Learning
</text>

<text class="value" x="760" y="510">
Deep Learning • LLMs • LangChain
</text>

<text class="label" x="560" y="560">
Projects
</text>

<text class="footer" x="760" y="560">
▶ AI Resume Analyzer
</text>

<text class="footer" x="760" y="590">
▶ AI Hand Gesture Controller
</text>

<text class="footer" x="760" y="620">
▶ Image Automation Pipeline
</text>

<text class="label" x="560" y="680">
Mission
</text>

<text class="footer" x="760" y="680">
Building AI applications that solve real-world problems.
</text>

</svg>
"""

OUTPUT_FILE.write_text(SVG, encoding="utf-8")

print("terminal.svg generated successfully.")