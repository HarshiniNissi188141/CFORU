from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Logo or Title
        self.set_font('Arial', 'B', 16)
        self.set_text_color(231, 76, 60) # Red color for "C FOR U"
        self.cell(0, 10, 'C FOR U: THE ULTIMATE MIND MAP', 0, 1, 'C')
        self.set_font('Arial', 'I', 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 5, 'Course: CS105ES (Programming for Problem Solving)', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, f'Page {self.page_no()} | Founder: Harshini Rachakonda', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 6, f'  {title}', 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 6, body)
        self.ln()

# Create PDF object
pdf = PDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# --- CONTENT BASED ON YOUR JNTUH SYLLABUS ---

# UNIT 1
pdf.chapter_title('UNIT I: The Foundation (Basics)')
pdf.chapter_body(
"""1. History & Importance:
   - Created by Dennis Ritchie (1972) at Bell Labs.
   - Why? To write the UNIX Operating System.
   
2. Data Types (Memory Size):
   - int (2/4 bytes)
   - float (4 bytes)
   - char (1 byte)
   - double (8 bytes)

3. Operators:
   - Arithmetic (+, -, *, /, %)
   - Relational (>, <, ==)
   - Logical (&&, ||, !)

4. Control Flow (The Brain):
   - Conditional: if, else-if, switch
   - Loops: 
     * while (Entry check)
     * do-while (Exit check)
     * for (Fixed iterations)
""")

# UNIT 2
pdf.chapter_title('UNIT II: Modularity (Functions)')
pdf.chapter_body(
"""1. Functions:
   - Divide big problems into small pieces.
   - Types: Library (printf) vs User-Defined.
   
2. Parameter Passing:
   - Call by Value: Sends a copy (Original safe).
   - Call by Reference: Sends address (Original changes).

3. Storage Classes:
   - auto (Local)
   - extern (Global)
   - static (Retains value between calls)
   - register (Stored in CPU for speed)
""")

# UNIT 3
pdf.chapter_title('UNIT III: Arrays & Strings')
pdf.chapter_body(
"""1. Arrays:
   - Collection of similar items.
   - 1D Array: int arr[5];
   - 2D Array: Matrix format.

2. Strings:
   - Character array ending with '\\0' (Null character).
   - Functions (string.h): strlen(), strcpy(), strcat(), strcmp().
""")

# UNIT 4
pdf.chapter_title('UNIT IV: Pointers & Structures')
pdf.chapter_body(
"""1. Pointers (The Power of C):
   - Stores address of another variable.
   - (*): Value at address.
   - (&): Address of variable.

2. Structures (struct):
   - Groups different data types.
   - Size = Sum of all members.

3. Unions:
   - Like struct, but shares memory.
   - Size = Size of largest member.
""")

# UNIT 5
pdf.chapter_title('UNIT V: Files & Algorithms')
pdf.chapter_body(
"""1. File Handling:
   - fopen(), fclose(), fprintf(), fscanf().
   - Modes: "r" (read), "w" (write), "a" (append).

2. Searching:
   - Linear Search: Slow, checks one by one.
   - Binary Search: Fast, requires sorted array.

3. Sorting:
   - Bubble Sort: Swaps adjacent elements.
   - Selection Sort: Finds min and places at start.
   - Insertion Sort: Card-game style sorting.
""")

# Save the PDF
output_path = "static/mindmap.pdf"
pdf.output(output_path)

print(f"SUCCESS! PDF generated at: {output_path}")