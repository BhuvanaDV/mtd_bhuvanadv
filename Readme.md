# mtd_bhuvanadv
<<<<<<< HEAD

This repository is created for the 1st Batch of 2026 at MTD for the course Competitive Programming and Java Full Stack.

## Notes

### Organizing Your System
We must organize all files and folders properly in our system.

#### Step 1: Create a Software Folder
- Create a folder named `Software` in the `C:` drive.
- Inside the `Software` folder, create one folder for each software you wish to install.
- Download the software setup file (`.exe` or `.msi`).
- Move the downloaded installer from the `Downloads` folder into its respective folder inside the `Software` folder.
- Install the software by double-clicking the installer from that location.

### What Gets Installed?
Whenever we install software, the following components may be installed:

- Program code
- Libraries / Modules / Packages
- Compiler (if applicable)
- Runtime / Execution Environment (if applicable)

To use the software, we generally get one or both of the following types of applications:

- CLI (Command Line Interface)
- GUI (Graphical User Interface)

### Examples

#### Python
When Python is installed, we get:

- CLI: `python`, `pip`
- GUI: `IDLE` (Python Shell)

#### Node.js
When Node.js is installed, we get:

- CLI: `node`, `npm`

#### MySQL
When MySQL is installed, we get:

- CLI: `mysql`
- GUI (Optional): MySQL Workbench

### Environment Variables (PATH)
=======
# Competitive Programming and Java Full Stack - MTD 2026 Batch 1

This repository is created for the **1st Batch of 2026 at MTD** for the course **Competitive Programming and Java Full Stack**.

---

# Notes

## Organizing Your System

We must organize all files and folders properly in our system.

### Step 1: Create a Software Folder

* Create a folder named **Software** in the `C:` drive.
* Inside the **Software** folder, create one folder for each software you wish to install.
* Download the software setup (`.exe`/`.msi`) file.
* Move (Cut & Paste) the downloaded installer from the **Downloads** folder into its respective folder inside the **Software** folder.
* Install the software by double-clicking the installer from this location.

---

## What Gets Installed?

Whenever we install software, the following components may be installed:

* Program code
* Libraries / Modules / Packages
* Compiler (if applicable)
* Runtime / Execution Environment (if applicable)

To use the software, we generally get one or both of the following types of applications:

* CLI (Command Line Interface)
* GUI (Graphical User Interface)

---

## Examples

### Python

When Python is installed, we get:

#### CLI

* `python`
* `pip`

#### GUI

* IDLE (Python Shell)

---

### Node.js

When Node.js is installed, we get:

#### CLI

* `node`
* `npm`

---

### MySQL

When MySQL is installed, we get:

#### CLI

* `mysql`

#### GUI (Optional)

* MySQL Workbench

---

## Environment Variables (PATH)

>>>>>>> 78d426f45061a34f64f11b85a1953771e1b396a9
Some software installations do not make their CLI commands available globally.

In such cases:

1. Copy the installation path of the executable.
<<<<<<< HEAD
2. Add this path to the Environment Variables → PATH.
3. Close and reopen the Command Prompt or Terminal.

> Note: The currently opened terminal will not recognize the changes until it is restarted.

### Required Software Installations

| Software | Purpose |
|---|---|
| Notepad++ | Quick note taking |
| Visual Studio Code (VS Code) | IDE / Code Editor |
| Eclipse IDE | Java Development |
| JDK (Java Development Kit) | Java Compiler, JVM, and Libraries |
| Python | Python Interpreter, Libraries, and IDLE Shell |
| Git | Run Git commands |
| GitHub Desktop | Perform Git operations using GUI |
| MySQL | Practice SQL / RDBMS |
| MongoDB | Practice NoSQL (Server & Compass) |
| Node.js | Practice JavaScript |

### Learning Folder
=======
2. Add this path to **Environment Variables → PATH**.
3. Close and reopen the Command Prompt or Terminal.

> **Note:** The currently opened terminal will not recognize the changes until it is restarted.

---

# Required Software Installations

| Software                     | Purpose                                       |
| ---------------------------- | --------------------------------------------- |
| Notepad++                    | Quick note taking                             |
| Visual Studio Code (VS Code) | IDE / Code Editor                             |
| Eclipse IDE                  | Java Development                              |
| JDK (Java Development Kit)   | Java Compiler, JVM, and Libraries             |
| Python                       | Python Interpreter, Libraries, and IDLE Shell |
| Git                          | Run Git commands                              |
| GitHub Desktop               | Perform Git operations using GUI              |
| MySQL                        | Practice SQL / RDBMS                          |
| MongoDB                      | Practice NoSQL (Server & Compass)             |
| Node.js                      | Practice JavaScript                           |

---

# Learning Folder

>>>>>>> 78d426f45061a34f64f11b85a1953771e1b396a9
Choose one drive in your laptop (preferably `D:` or `E:` instead of `C:`) for learning purposes.

Create a folder named:

<<<<<<< HEAD
- `Learning`

If your laptop has only the `C:` drive, create:

- `C:\Learning`

## GitHub Setup

### Step 1: Create a GitHub Account
Create a GitHub account using:

- Your permanent email address
- Your permanent phone number
- Login to your account

### Step 2: Create a Repository
Create a new repository with the following name:

- `mtd2026`

### Step 3: Clone the Repository
Clone the repository into your Learning folder.

#### Steps
1. Open the Learning folder.
=======
```text
Learning
```

If your laptop has only the `C:` drive, create:

```text
C:\Learning
```

---

# GitHub Setup

## Step 1: Create a GitHub Account

Create a GitHub account using:

* Your permanent email address
* Your permanent phone number

Login to your account.

---

## Step 2: Create a Repository

Create a new repository with the following name:

```text
mtd2026
```

---

## Step 3: Clone the Repository

Clone the repository into your **Learning** folder.

### Steps

1. Open the **Learning** folder.
>>>>>>> 78d426f45061a34f64f11b85a1953771e1b396a9
2. Open the terminal in that folder.
3. Run the following command using your repository URL:

```bash
git clone <repository-url>
```

Example:

```bash
git clone https://github.com/your-username/mtd2026.git
```

<<<<<<< HEAD
This creates a copy of your GitHub repository inside the Learning folder. The repo on your laptop will be a folder, and Git can recognize it as a special folder, which is a repository folder.

## Git Basics

### PUSH and PULL
- `push` is used to upload from the local repository to the remote/cloud repository.
- `pull` is used to download from the remote repository to the local repository.

### Common Notes
- `length()` in Java
- `strlen()` in C
- Java: `byte`, `short`, `int`, `long`
- MySQL: `tinyint`, `smallint`, `int`, `bigint`

To avoid plagiarism, copy rights, trademarks, etc., companies use different names for the same thing.

### Update Local Repo with Remote Repo
To update our local repository with respect to the remote repository, we must pull/download:

```bash
git pull
git pull origin main
```

In all repositories, at least one branch is always created and its name is `main`. So when we run:
=======
This creates a copy of your GitHub repository inside the Learning folder.

The repository in our laptop will be a folder, and Git can recognize this as a special folder called a **Repository (Repo)** folder.

---

# PUSH and PULL

* **Push** is to upload data from the local repository to the remote/server/cloud repository.
* **Pull** is to download data from the remote repository to the local repository.

---

## Common Functions

| Language | Function   |
| -------- | ---------- |
| Java     | `length()` |
| C        | `strlen()` |

---

## Data Type Mapping

| Java    | MySQL      |
| ------- | ---------- |
| `byte`  | `tinyint`  |
| `short` | `smallint` |
| `int`   | `int`      |
| `long`  | `bigint`   |

---

> To avoid plagiarism, copyrights, trademarks, etc., companies often use different names for the same concept.

---

# Updating Local Repository

To update our local repository with respect to the remote repository, we must **PULL** (download).
>>>>>>> 78d426f45061a34f64f11b85a1953771e1b396a9

```bash
git pull
```

<<<<<<< HEAD
we are actually running (by default):
=======
or
>>>>>>> 78d426f45061a34f64f11b85a1953771e1b396a9

```bash
git pull origin main
```

<<<<<<< HEAD
### Steps to Push
1. Tell Git to list the files and folders that are modified, created, or deleted:
=======
In all repositories, at least one branch is always created and its name is `main`.

Thus, when we run:

```bash
git pull
```

we are actually running by default:

```bash
git pull origin main
```

---

# Steps to Push Changes

## Step 1: Add Files

We must first tell Git to list the names of the files and folders that are modified, created, or deleted.
>>>>>>> 78d426f45061a34f64f11b85a1953771e1b396a9

```bash
git add <PATH>
```

<<<<<<< HEAD
2. Commit the changes. Git will create an object and save the content of all files from Step 1 into that object and encrypt it:
=======
Example:

```bash
git add .
```

---

## Step 2: Commit Changes

Git creates an object and saves the content of all the files from Step 1 into that object and encrypts it.
>>>>>>> 78d426f45061a34f64f11b85a1953771e1b396a9

```bash
git commit -m "MESSAGE"
```

<<<<<<< HEAD
3. Push the changes:

```bash
git push origin <branch name>
```
=======
Example:

```bash
git commit -m "Added Java notes"
```

---

## Step 3: Push Changes

```bash
git push origin <branch-name>
```

Example:

```bash
git push origin main
```
# Day 2 - Friday (03-07-2026)

# Git Configuration Commands

## Configure Git Username

```bash
git config --global user.name "neelmyna"
```

## Configure Git Email

```bash
git config --global user.email "abc@xyz.com"
```

## Clone Repository Using PAT (Personal Access Token)

```bash
git clone <Repo_URI>

git clone https://github.com/username/repo_name

git clone https://PAT@github.com/username/repo_name
```

---

# Importance of Data

Data is the most important aspect of computing. It is the primary reason for programming and even for the existence of computers.

Refer to:

* `notes/data_categories.png`

**Assignment 1 Given**

---

# How Numbers Are Stored

## Unsigned Numbers

To store a decimal number in binary, convert it to base-2 representation.

### Example: Store Decimal Number 125

| Decimal Value | Binary Representation |
| ------------- | --------------------- |
| 64            | 1000000               |
| 32            | 0100000               |
| 16            | 0010000               |
| 8             | 0001000               |
| 4             | 0000100               |
| 2             | 0000010               |
| 1             | 0000001               |

125 = 64 + 32 + 16 + 8 + 4 + 1

Binary representation:

```text
1111101
```

Thus, decimal **125** is stored as:

```text
1111101
```

---

### Example: Decimal Positional Representation

When we say the distance from Mysore to Bangalore is **145**, we mean:

```text
1 × 10² + 4 × 10¹ + 5 × 10⁰
= 100 + 40 + 5
= 145
```

---

## Number of Bits Required

| Number | Bits Required |
| ------ | ------------- |
| 5      | 3 bits        |
| 20     | 5 bits        |
| 125    | 7 bits        |

To maintain discipline and standardization, computers use fixed sizes:

* 4 bits → Nibble
* 8 bits → Byte
* 16 bits
* 32 bits → Word Size
* 64 bits → Word Size

---

# Assignment 2 Given

## Number of Values Stored in Bits

| Bits   | Number of Values |
| ------ | ---------------- |
| 1 bit  | 2 values         |
| 2 bits | 4 values         |
| n bits | 2ⁿ values        |

Examples:

* 4 bits can store **16 values**
* Unsigned 4-bit values range from:

```text
0 to 15
```

These 16 values are represented in **Hexadecimal**:

```text
0 to F
```

where:

```text
F = 15
```

---

## Signed Values in 4 Bits

Signed 4-bit values range from:

```text
-8 to +7
```

which again gives:

```text
16 total values
```

---

# How Negative Numbers Are Stored

Example:

```text
n = -21
```

### Step 1: Take Absolute Value

```text
21
```

### Step 2: Convert to Binary

```text
00010101
```

### Step 3: Find 1's Complement

```text
11101010
```

### Step 4: Add 1 to Obtain 2's Complement

```text
11101011
```

This is how **-21** is stored in memory.

---

## Sign Bit

The Most Significant Bit (MSB) acts as the sign bit.

* MSB = 0 → Positive Number
* MSB = 1 → Negative Number

For:

```text
11101011
```

MSB is `1`, therefore the number is negative.

Verification:

```text
-1 × 2⁷ + 1 × 2⁶ + 1 × 2⁵ + 1 × 2³ + 1 × 2¹ + 1 × 2⁰
= -128 + 64 + 32 + 8 + 2 + 1
= -21
```

---

# Assignment 3 Given

# Data Types in Java

## Primitive Data Types

### Integer Types

| Data Type | Size    |
| --------- | ------- |
| byte      | 1 byte  |
| short     | 2 bytes |
| int       | 4 bytes |
| long      | 8 bytes |

### Floating Point Types

| Data Type | Size    |
| --------- | ------- |
| float     | 4 bytes |
| double    | 8 bytes |

### Other Primitive Types

| Data Type | Size    |
| --------- | ------- |
| boolean   | 1 bit   |
| char      | 2 bytes |

`char` stores Unicode characters.

---

## Reference Types

Reference types store the reference value of an object.

---

# Data Types in Python

* `int`
* `float`
* `bool`
* `str`
* `chr`

In Python, every datatype belongs to a class.

Therefore:

> Every data item in Python is an object.

---

# Operators

## Arithmetic Operators

### Common Arithmetic Operators

```text
+   -   *   /   %
```

### Additional Python Operators

```text
**   //
```

Where:

* `**` → Power operator
* `//` → Floor division operator

---

## Binary Operators

Arithmetic operators are binary operators.

They require two operands.

Example:

```text
5 + 10
```

Operands:

* 5
* 10

Operator:

```text
+
```

---

## Infix Notation

Programming languages generally use **Infix Notation**, where the operator is written between operands.

Example:

```text
5 + 10
```

---

# Expression Evaluation

Compilers generally process instructions:

* Top to Bottom
* Left to Right

However, the execution machine may evaluate expressions differently based on operator precedence and associativity.

---

## Left-to-Right Evaluation

Expressions are normally evaluated from left to right.

Example:

```text
5 - 6 + 3
```

Evaluation:

```text
(5 - 6) + 3
```

because `+` and `-` have equal precedence.

---

## Operator Precedence

Example:

```text
4 + 7 / 2
```

Evaluation:

```text
4 + (7 / 2)
```

Division has higher precedence than addition.

---

## Associativity

Example in Python:

```python
2 ** 3 ** 2
```

Power operator has **right-to-left associativity**.

Thus:

```text
2 ** (3 ** 2)
= 2 ** 9
= 512
```

and not:

```text
(2 ** 3) ** 2 = 64
```

---

## Equivalent in Java

Java does not have a power operator.

Use:

```java
Math.pow(base, exponent)
```

Example:

```java
Math.pow(2, 3);
```

---

## Input and Output of Arithmetic Operators

### Input:

* Numbers

### Output:

* Number

---

# Infix to Postfix Conversion

Although programmers write expressions in **Infix notation**, execution machines internally convert expressions into **Postfix notation** before evaluation.


# Day 3 Notes - 06-07-2026

## Arithmetic Operations in Java

```java
int num = 40 / 7;
System.out.println(num);      // 5

float num2 = 40 / 7;
System.out.println(num2);     // 5.0

double num3 = 40 / 7.0;
System.out.println(num3);     // 5.714285714285714
```

### Explanation

- If both operands are integers, Java performs **integer division**.
- Integer division discards the decimal part.
- If one operand is a floating-point value (`float` or `double`), Java performs **floating-point division**.

---

## Assignments

- Assignment 4 - IEEE 754 Floating Point Representation
- Assignment 5 - Why Python has no `++` and `--`
- Assignment 6 - Precedence of Relational Operators
- Assignment 7 - Minimum Relational Operators

---

# Relational Operators

Relational operators compare two values and return a **boolean** value.

| Operator | Meaning |
|----------|---------|
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or Equal to |
| `>=` | Greater than or Equal to |
| `==` | Equal to |
| `!=` | Not Equal to |

### Properties

- Input: Numbers
- Output: Boolean (`true` or `false`)
- All relational operators are **binary operators**.

---

## Operator Precedence

Highest to Lowest

1. Arithmetic Operators
2. Relational Operators
3. Logical Operators
4. Assignment Operator

### Note

The **post-increment (`num++`)** and **post-decrement (`num--`)** operators first use the current value and then perform the increment/decrement.

Example:

```java
int num = 5;
int result = num++;

System.out.println(result); // 5
System.out.println(num);    // 6
```

---

# Intervals

## Closed Interval

```
[10, 20]
```

Includes both endpoints.

```java
i >= 10 && i <= 20
```

---

## Open Interval

```
(20, 40)
```

Excludes both endpoints.

```java
i > 20 && i < 40
```

Values included: **21 to 39**

---

## Left Open Interval

```
(15, 25]
```

Left endpoint excluded and right endpoint included.

```java
i > 15 && i <= 25
```

Values included: **16 to 25**

---

# for Loop Examples

```java
for(int i = 1; i <= 10; i++)
```

Equivalent to

```java
for(int i = 1; i < 11; i++)
```

---

# Logical Operators

| Operator | Meaning |
|----------|---------|
| `&` | Logical AND |
| `|` | Logical OR |
| `!` | Logical NOT |
| `&&` | Short-Circuit AND |
| `||` | Short-Circuit OR |

### Note

In **Python**, only the **short-circuit logical operators** are available:

- `and`
- `or`
- `not`

---

## Properties

- Input: Boolean values
- Output: Boolean value

---

# Short-Circuit Example

```java
int a = 3, b = 5, c = 10;

if (a-- <= b || b++ != c)
    System.out.println("Mysuru");
else
    System.out.println("Hunasuru");

System.out.println(a + " " + b + " " + c);
```

### Explanation

- `a-- <= b` is `true`.
- Since `||` is short-circuit OR, the second condition is **not evaluated**.
- `b` is not incremented.

Output

```
Mysuru
2 5 10
```

---

# Non Short-Circuit Example

```java
int a = 3, b = 5, c = 10;

if (a-- <= b | b++ != c)
    System.out.println("Mysuru");
else
    System.out.println("Hunasuru");

System.out.println(a + " " + b + " " + c);
```

### Explanation

- `|` evaluates **both operands**.
- `b++` executes.

Output

```
Mysuru
2 6 10
```

---

# Increment Operator Example

```java
int x = 4, y = 5, z = 1;

x++;
System.out.println(x + " " + y + " " + z);

++x;
System.out.println(x + " " + y + " " + z);

y = z++;
System.out.println(x + " " + y + " " + z);

x = ++y;
System.out.println(x + " " + y + " " + z);

z = x++ + ++x;
System.out.println(x + " " + y + " " + z);
```

---

# Bitwise Operators

| Operator | Meaning |
|----------|---------|
| `~` | Bitwise NOT |
| `&` | Bitwise AND |
| `|` | Bitwise OR |
| `^` | Bitwise XOR |
| `<<` | Left Shift |
| `>>` | Right Shift |

---

## Pending Topic

- Problems on Bitwise Operators

---

# Miscellaneous Notes

## Expression

```
4 + 7 - 2 + 1
```

---

## Assignment Statement

```java
x = y;
```

---

## Exponentiation (Python)

```python
3 ** 2
```

Output

```
9
```

---

## Object Example

```java
obj1.x_axis

Point p = new Point(3, 4);
```

---

# Key Takeaways

- Integer division removes the decimal part.
- Floating-point division retains decimal values.
- Relational operators return boolean values.
- `&&` and `||` are short-circuit operators.
- `&` and `|` always evaluate both operands.
- Post-increment uses the value first, then increments.
- Pre-increment increments first, then uses the value.
- Bitwise operators work on individual bits of integers.

# DAY 4 – TUESDAY (07-07-2026)

## Primitive vs Object

### Primitive Variable (Java)

```java
int number = 10;
```

- `number` is a **primitive variable**.
- It stores only the value `10`.
- No additional properties or methods are associated with it.

---

### Primitive Array in C/C++

```c
int array[10];
```

- The array contains **10 integer elements only**.
- It is treated as a primitive collection of integers.
- No built-in methods or object behavior.

---

### Array in Java

```java
int[] array = new int[10];
```

- In Java, an array is an **object**.
- It stores integer elements along with object-related information.
- Arrays have properties such as:
  - `length`

Example:

```java
System.out.println(array.length);
```

---

# High Cohesion (SRP)

## High Cohesion

A solution should solve **only one problem at a time**.

> **Do one job at a time.**

This concept is known as **High Cohesion**.

### Example

Instead of writing one class that performs multiple unrelated tasks,

- Student Management
- Fee Calculation
- Report Generation

Create separate classes:

- Student
- FeeCalculator
- ReportGenerator

Each class has **one responsibility**.

---

# SOLID Principles

SOLID is a set of five object-oriented design principles.

- **S** – Single Responsibility Principle (SRP)
- **O** – Open/Closed Principle (OCP)
- **L** – Liskov Substitution Principle (LSP)
- **I** – Interface Segregation Principle (ISP)
- **D** – Dependency Inversion Principle (DIP)

---

# Naming Variables

## Generic Information

```java
int number;
```

Very generic.

---

## Specific Information

```java
int age;
```

More meaningful.

---

## Specialized Information

```java
int student_age;
```

Highly descriptive.

Choose meaningful variable names whenever possible.

---

# Class Example

```java
class StudentAge {
    int age;
    int maxAge;
    int minAge;
}
```

Example Objects

```java
StudentAge vtu_age;
```

- Minimum Age = 18
- Maximum Age = 60

```java
StudentAge jntu_age;
```

- Minimum Age = 16
- Maximum Age = 80

---

# Problem 1: Check if a Year is Leap Year

### Logic

A year is a leap year if:

- Divisible by 400

OR

- Divisible by 4 but **not** divisible by 100.

### Formula

```text
(year % 400 == 0) ||
(year % 4 == 0 && year % 100 != 0)
```

---

# Problem 2: Check if a Number is a Perfect Square

### Logic

A number is a perfect square if:

```text
√number × √number = number
```

Examples

| Number | Perfect Square |
|---------|----------------|
| 4 | Yes |
| 9 | Yes |
| 16 | Yes |
| 25 | Yes |
| 18 | No |
| 20 | No |

---

# Problem 3: Find Student Result Based on Average Marks

| Average Score | Result |
|---------------|--------|
| 0 – 49 | Fail |
| 50 – 69 | Second Class |
| 70 – 89 | First Class |
| 90 – 100 | Distinction |

---

# Steps to Solve a Programming Problem

## Step 1 – Understand the Problem

- Understand what is being asked.
- Remove unwanted information.
- Clearly identify:
  - Input (I/P)
  - Output (O/P)
- Identify all important requirements.

---

## Step 2 – Build the Solution

Develop the solution using:

- Trial and Error
- Mathematical Formula
- Algorithm

> Do **not** think about programming syntax at this stage.

---

## Step 3 – Write the Fake Code (Pseudocode)

Convert the solution into simple English-like steps before coding.

---

## Step 4 – Validate the Solution (Optional)

- Test the pseudocode.
- Verify correctness.
- Check different test cases.
- Improve efficiency if possible.
- Optimize the solution.

---

## Step 5 – Code It

Finally, convert the pseudocode into the desired programming language (Java, C, C++, Python, etc.).

---

# Key Takeaways

- Primitive variables store only values.
- Java arrays are objects.
- Follow **High Cohesion (Single Responsibility Principle)**.
- Use meaningful variable names.
- Solve one problem at a time.
- Before coding:
  1. Understand
  2. Build Logic
  3. Write Pseudocode
  4. Validate
  5. Code


# Steps to Solve a Problem

## 1. Understand the Problem
- Read the problem carefully.
- Remove or ignore unwanted information.
- Clearly identify the **Input (I/P)** data.
- Clearly identify the **Output (O/P)** data.
- Remember only the relevant and important information required to solve the problem.

---

## 2. Build the Solution
- Develop the solution using:
  - Trial and Error method, or
  - A specific algorithm, or
  - A mathematical formula.
- **Do not use any programming concepts at this stage.**

---

## 3. Write the Algorithm
An algorithm is a step-by-step procedure to solve a problem.

Each step should be:
- Finite
- Simple
- Unambiguous
- Follow the **SRP (Single Responsibility Principle)**

---

## 4. Write the Fake Code (Pseudocode)
- Convert the algorithm into pseudocode.
- The pseudocode should resemble programming logic without following any specific programming language syntax.

---

## 5. Code It
- Convert the pseudocode into an actual program using the chosen programming language.

---

## 6. Validate / Test / Verify (Optional)
- Test the pseudocode and the program.
- Verify whether the output is correct.
- Analyze the efficiency of the solution.
- Check if a better or more optimized solution is possible.

---

## Assignments
- Assignment 8 given.

---

# Evolution of Programming Languages

## 1. Machine Language
- The first generation of programming language.
- Consists of only binary numbers (0s and 1s).
- Very difficult for humans to understand and write.

---

## 2. Human-Friendly Language (Assembly Language)
- Uses mnemonics instead of binary instructions.
- Easier than Machine Language.
- Requires an assembler to convert assembly code into machine code.

---

## 3. Domain-Oriented Languages
Languages designed for specific application domains.

Examples:
- COBOL
- FORTRAN

Initially, only domain-oriented languages existed.

---

## 4. Domain-Friendly Languages
General-purpose programming languages that are easier for programmers.

Examples:
- C
- Pascal

These languages are not restricted to a specific domain.

---

## 5. Object-Oriented Programming Languages (OOPL)
Examples:
- C++
- C with Classes
- Simula 67

These languages introduced Object-Oriented Programming concepts.

---

# C++

**C++ = C + Object-Oriented Programming**

- C++ extended the C language by adding Object-Oriented concepts.
- It mainly introduced features such as inheritance, classes, objects, polymorphism, and encapsulation.

### Relationship Between C and C++

- Every **C program** is also a **C++ program**.
- But every **C++ program** is **not** a C program.

Reason:
- **C++ is a superset of C.**
- **C is a subset of C++.**

---

# Why Java Was Introduced

Although C++ became very popular, it had several design issues, such as:

- Friend functions
- Private inheritance
- Global variables
- Global functions
- Operator overloading
- Objects can be created in the Stack area

Because of these issues, software experts wanted a **Strict Object-Oriented Programming Language (Strict OOPL)**.

As a result,
**Java** was introduced.

Java was designed to:
- Be more secure.
- Reduce complexity.
- Remove many problematic features of C++.
- Promote pure object-oriented programming principles (with some practical exceptions).

---

# Assignments

- Assignment 9 given.
- Assignment 10 given.
- Assignment 11 given.

## Day-5 8/7/2026[Wednesday]

## DAY7 THURSDAY 09-07-2026

- Formatting the output is taught. Assignment12 given.

DAY8 FRIDAY 10-07-2026 Functions Call Stack match-case Problem solving on Loops/iterations range function with yield