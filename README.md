![BongScript Banner](img/banner.svg)

# BongScript

**BongScript** is a primitive, esoteric, interpreted, toy programming language that uses Bengali inspired syntax. It's designed for learning and experimentation, with support for variables, conditionals, loops, arithmetic operations, and basic printing — all written in a syntax that feels native to Bengali speakers.

---

## ✨ Features

- Bengali-flavored syntax like:
  - `eta holo a = 10;` → variable declaration
  - `lekho ("Hello");` → print statement
  - `sonkhya nao();` → user input of type int
  - `jodi (a > b) { ... }` → if condition
  - `nahole { ... }` → else block
  - `nahole jodi { ... }` → else if block
  - `jotokhon (a != 0) { ... }` → while loop
  - and many more.
- Basic arithmetic (`+`, `-`, `*`, `/`, `%`)
- Logical operators (`==`, `!=`, `>`, `<`, `>=`, `<=`)
- AST-based interpreter
- Simple tokenizer and parser
- Entirely written in **Python**

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/banik000/BongScript.git
cd BongScript
```

### 2. Run a BongScript program
Write your own program in **program.bong** and run as:
```bash
python main.py program.bong
```
Or run any of the demo programs in examples folder as:
```bash
python main.py examples/hello_world.bong
```

## 📋 BongScript Syntax

### 1. Program Block
All BongScript programs must be enclosed within:
```
kaj shuru

// Your Program logic

kaj shesh
```

### 2. Print Statements
To print statements ending with a newline use **lekho**. To print statements in the same line use **ullekho**.
```
kaj shuru

lekho ("Hello World");

ullekho("Bye");
ullekho("World");

kaj shesh
```
Output:
```
Hello World
ByeWorld
```

### 3. Variable Declarations
Variables are declared using **eta holo**. All statements should end with ";".
```
kaj shuru

eta holo a = 10;
eta holo b = 40;
eta holo c = 10.67;

eta holo s1 = "Apple";
eta holo s2 = "Orange";

lekho (a + b);
lekho (a + b + c);
lekho (s1 + s2);

kaj shesh
```
Output:
```
50
60.67      
AppleOrange
```
### 4. If-Else statements
An If statement is reprsented by **jodi** and Else by **nahole**. Else If is represented by **nahole jodi**.

Following is a program to compare two numbers:
```
kaj shuru

eta holo a = 10;
eta holo b = 30;

jodi (a == b)
{
    lekho("Equal");
}
nahole jodi (a > b)
{
    lekho("Greater");
}
nahole
{
    lekho ("Smaller");
}

kaj shesh
```
Output:
```
Smaller
```

### 5. While loops
While loops are represented by **jotokhon**.

Following is a program to print numbers from 1 to 5:
```
kaj shuru

eta holo a = 1;

jotokhon (a != 6)
{
    lekho (a);
    a = a + 1;
}

kaj shesh
```
Output:
```
1
2
3
4
5
```

### 6. Break and Continue statements
Break is represented by **theme jao** and Continue is represented by **egiye jao**.
```
kaj shuru

eta holo n = 0;

jotokhon(n < 10)
{
    n = n + 1;

    jodi(n < 4)
    {
        egiye jao;
    }

    jodi (n > 8)
    {
        theme jao;
    }

    lekho(n);
}

kaj shesh
```
Output:
```
4
5
6
7
8
```

### 7. Taking User Input
Inputs should be taken only during variable declarations.

To take string input use **bhasha nao**. To take int input use **sonkhya nao**. To take float input use **dosomik sonkhya nao**.
```
kaj shuru

eta holo a = sonkhya nao();

eta holo b = dosomik sonkhya nao();

eta holo s1 = bhasha nao();

lekho(a);
lekho(b);
lekho(s1);

kaj shesh
```

### 8. Adding comments
Single-line and Multi-line comments can be added using the keyword **montobbo**.

Following is an example:
```
kaj shuru

montobbo This is a single-line comment;

montobbo 
This is a
multi-line
comment;

kaj shesh
```
## 📜 List of BongScript Keywords 
| BongScript keyword   | Meaning              | Inspired from        | 
| -------------------- | -------------------- | -------------------- |
| kaj shuru            | begin                | SQL Server           |
| kaj shesh            | end                  | SQL Server           |
| eta holo             | let                  | JavaScript           |
| lekho                | println              | Java                 |
| ullekho              | print                | Java                 |
| jodi                 | if                   | Python               |
| nahole               | else                 | Python               |
| nahole jodi          | elif                 | Python               |
| jotokhon             | while                | Python               |
| theme jao            | break                | Python               |
| egiye jao            | continue             | Python               |
| bhasha nao           | input                | Python               |
| sonkhya nao          | integer input        |                      |
| dosomik sonkhya nao  | decimal input        |                      |
| montobbo             | comments             |                      |


## ⚒️ Requirements
* Python 3.7+

No external dependencies required.


## 🥺 To Do
This project is under active development as of May 2025. Following features to be implemented:

* Methods
* Arrays
* Switch case
* Type Casting
* Compound Assignment operators
* More types of loops
* Error handling
* Interactive REPL mode
* Publish to PyPi as a pip package
* VS Code extension for syntax highlighting

## 👨‍💻 Author
Made with ❤️ by Soumyajit Banik.

Made with ❤️ for post-modernist Bengali intellectuals.

![Python Badge](img/badge.svg)

