const courseData = {
    "unit1": {
        "title": "Unit I: Storage Classes & Basics",
        "slides": [
            { "title": "1.1 The C Ecosystem", "content": "C is the foundation of modern computing. Created in 1972 by Dennis Ritchie, it powers Operating Systems (Windows/Linux), Embedded Systems, and IoT devices." },
            { "title": "1.2 Variables & Memory", "content": "A variable is a named memory location. <br><code>int a = 10;</code> reserves 4 bytes.<br><code>char c = 'A';</code> reserves 1 byte." },
            { "title": "1.3 Storage Classes: Auto", "content": "<b>auto:</b> The default class for local variables.<br>Scope: Local block.<br>Life: Ends when function exits.<br>Default Value: Garbage." },
            { "title": "1.4 Storage Classes: Extern", "content": "<b>extern:</b> Global variables shared across multiple files.<br>Scope: Entire program.<br>Life: Until program ends.<br>Default Value: Zero." },
            { "title": "1.5 Storage Classes: Static", "content": "<b>static:</b> Preserves value between function calls.<br><code>static int count = 0;</code><br>It is initialized only ONCE." },
            { "title": "1.6 Storage Classes: Register", "content": "<b>register:</b> Requests storage in CPU registers for faster access.<br>Used for loop counters.<br>Cannot use '&' (address of) on registers." },
            { "title": "1.7 Type Definitions", "content": "<b>typedef:</b> Creates an alias for data types.<br><code>typedef unsigned long ulong;</code><br>Now you can write <code>ulong x;</code>." },
            { "title": "1.8 Enumerations (enum)", "content": "User-defined data type consisting of named constants.<br><code>enum Week {Mon, Tue, Wed};</code><br>Mon=0, Tue=1..." },
            { "title": "1.9 Preprocessor Directives", "content": "Commands for the compiler before compilation.<br><code>#include</code> imports files.<br><code>#define PI 3.14</code> creates macros." },
            { "title": "1.10 Macros vs Constants", "content": "Macros (#define) are text replacements (no memory).<br>Constants (const int) are variables in read-only memory." }
        ]
    },
    "unit2": {
        "title": "Unit II: Pointers & Logic",
        "slides": [
            { "title": "2.1 What is a Pointer?", "content": "A variable that stores the <b>Memory Address</b> of another variable.<br>Syntax: <code>int *ptr;</code>" },
            { "title": "2.2 Address-of Operator (&)", "content": "<code>&x</code> gives the memory location of x.<br><code>scanf(\"%d\", &x);</code> uses this to store input." },
            { "title": "2.3 Dereference Operator (*)", "content": "<code>*ptr</code> gives the <b>Value</b> stored at that address.<br><code>*ptr = 10;</code> changes the value of the target variable." },
            { "title": "2.4 Pointer Arithmetic", "content": "<code>ptr + 1</code> moves the pointer by the <b>size of the data type</b>.<br>For <code>int *p</code> (4 bytes), p+1 moves 4 bytes forward." },
            { "title": "2.5 Void Pointer", "content": "A generic pointer that can point to any data type.<br><code>void *ptr;</code><br>Cannot be dereferenced directly without casting." },
            { "title": "2.6 Null Pointer", "content": "Points to nothing (0x0).<br><code>int *p = NULL;</code><br>Always initialize pointers to NULL to prevent crashes." },
            { "title": "2.7 Dangling Pointer", "content": "A pointer pointing to a memory location that has been deleted (freed).<br>Dangerous! Can cause segmentation faults." },
            { "title": "2.8 Pointer to Pointer", "content": "A pointer that stores the address of another pointer.<br><code>int **pptr;</code><br>Used in dynamic 2D arrays." },
            { "title": "2.9 Recursion Logic", "content": "A function calling itself.<br>Must have a <b>Base Case</b> to stop.<br>Example: Factorial, Fibonacci." },
            { "title": "2.10 Call by Reference", "content": "Passing the address (&) to a function allows the function to modify the original variable." }
        ]
    },
    "unit3": {
        "title": "Unit III: Arrays vs Pointers",
        "slides": [
            { "title": "3.1 Array Basics", "content": "Collection of items stored at contiguous memory locations.<br><code>int arr[5];</code>" },
            { "title": "3.2 Arrays are Pointers", "content": "The name of the array <code>arr</code> acts as a constant pointer to the first element.<br><code>arr == &arr[0]</code>" },
            { "title": "3.3 Accessing via Pointers", "content": "<code>arr[i]</code> is internally converted to <code>*(arr + i)</code>.<br>This is why array indexing starts at 0." },
            { "title": "3.4 Strings in C", "content": "Character arrays terminated by a <b>Null Character ('\\0')</b>.<br><code>char name[] = \"Hello\";</code>" },
            { "title": "3.5 String Functions", "content": "<code>strlen()</code>: Length.<br><code>strcpy()</code>: Copy.<br><code>strcat()</code>: Concatenate.<br><code>strcmp()</code>: Compare." },
            { "title": "3.6 Array of Pointers", "content": "An array where each element is a pointer.<br><code>int *arr[5];</code><br>Used for storing lists of strings." },
            { "title": "3.7 Pointer to Array", "content": "A single pointer that points to a whole array.<br><code>int (*ptr)[5];</code><br>Useful for passing 2D arrays to functions." },
            { "title": "3.8 Dynamic Memory (Malloc)", "content": "<code>malloc(size)</code>: Allocates memory on the Heap.<br>Returns void*.<br>Garbage values initially." },
            { "title": "3.9 Calloc vs Malloc", "content": "<code>calloc(n, size)</code>: Contiguous allocation.<br>Initializes all bytes to <b>Zero</b>.<br>Slightly slower than malloc." },
            { "title": "3.10 Memory Leaks", "content": "Happens when you allocate memory but forget to <code>free()</code> it.<br>Always use <code>free(ptr);</code> when done." }
        ]
    },
    "unit4": {
        "title": "Unit IV: Structures & Files",
        "slides": [
            { "title": "4.1 Structures", "content": "User-defined data type grouping different types.<br><code>struct Student { int roll; char name[20]; };</code>" },
            { "title": "4.2 Structure Memory", "content": "Size is the sum of all members (plus padding).<br>Each member has its own memory space." },
            { "title": "4.3 Unions", "content": "Similar to Struct, but all members <b>share the SAME memory</b>.<br>Size = Size of largest member.<br>Saves memory." },
            { "title": "4.4 Bit Fields", "content": "Allocating specific number of bits to struct members.<br><code>int flag : 1;</code> (Uses only 1 bit)." },
            { "title": "4.5 Typedef Struct", "content": "Simplifies syntax.<br><code>typedef struct { ... } Student;</code><br>Usage: <code>Student s1;</code> (No need to write 'struct')." },
            { "title": "4.6 File Handling", "content": "Storing data permanently on disk.<br><code>FILE *fp;</code><br>Modes: 'r' (read), 'w' (write), 'a' (append)." },
            { "title": "4.7 File Operations", "content": "<code>fopen()</code>: Open file.<br><code>fprintf()</code>: Write to file.<br><code>fscanf()</code>: Read from file.<br><code>fclose()</code>: Close file." },
            { "title": "4.8 Moving File Pointer", "content": "<code>fseek(fp, offset, origin)</code>: Moves cursor.<br><code>rewind(fp)</code>: Resets cursor to start." },
            { "title": "4.9 Command Line Arguments", "content": "Passing inputs when running program.<br><code>int main(int argc, char *argv[])</code><br>argc = count, argv = array of strings." },
            { "title": "4.10 Error Handling", "content": "<code>perror()</code> and <code>strerror()</code> help debug file errors (like 'File Not Found')." }
        ]
    }
};