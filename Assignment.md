# Day 2 Assignments

## Assignment 1

### 1. Little Endian Memory Representation

* Data is stored from **LSB (Least Significant Byte)** to **MSB (Most Significant Byte)**.
* The least significant byte is stored at the lowest memory address.

#### Example:

For the hexadecimal number:

```text
0x12345678
```

Memory representation in Little Endian:

| Address | Value |
| ------- | ----- |
| 1000    | 78    |
| 1001    | 56    |
| 1002    | 34    |
| 1003    | 12    |

---

### 2. Big Endian Memory Representation

* Data is stored from **MSB (Most Significant Byte)** to **LSB (Least Significant Byte)**.
* The most significant byte is stored at the lowest memory address.

#### Example:

For the hexadecimal number:

```text
0x12345678
```

Memory representation in Big Endian:

| Address | Value |
| ------- | ----- |
| 1000    | 12    |
| 1001    | 34    |
| 1002    | 56    |
| 1003    | 78    |

---

## Assignment 2

### What is Word Size?

Word size refers to the number of bits a processor can process in a single operation.

Common word sizes are:

* 16-bit
* 32-bit
* 64-bit

Example:

* A **64-bit Operating System** can process **64 bits of data at a time**.
* It can access larger amounts of memory compared to a 32-bit operating system.

---

### What does `x64` mean when downloading applications?

When downloading software, you may see:

* **x86** → 32-bit version
* **x64** → 64-bit version

`x64` means the application is designed for a **64-bit processor and operating system**.

Advantages of x64 applications:

* Better performance
* Can utilize more RAM
* Optimized for modern systems

---

## Assignment 3

# Program to Check Whether a System Uses Little Endian or Big Endian Representation

## Java Program

```java
import java.nio.ByteOrder;

public class EndianCheck {
    public static void main(String[] args) {

        if (ByteOrder.nativeOrder() == ByteOrder.LITTLE_ENDIAN) {
            System.out.println("System uses Little Endian format.");
        } else {
            System.out.println("System uses Big Endian format.");
        }
    }
}
```

### Sample Output

```text
System uses Little Endian format.
```

### Explanation

* `ByteOrder.nativeOrder()` returns the byte order used by the underlying system.
* If it matches `ByteOrder.LITTLE_ENDIAN`, the system follows **Little Endian** representation.
* Otherwise, it follows **Big Endian** representation.

---

## Python Program

```python
import sys

if sys.byteorder == "little":
    print("System uses Little Endian format.")
else:
    print("System uses Big Endian format.")
```

### Sample Output

```text
System uses Little Endian format.
```

### Explanation

* `sys.byteorder` returns the byte order of the system.
* If the value is `"little"`, the system uses **Little Endian** representation.
* Otherwise, it uses **Big Endian** representation.

---

## Conclusion

* Most modern computers using Intel and AMD processors use **Little Endian** architecture.
* Therefore, the output on most systems will be:

```text
System uses Little Endian format.
```

# Day 3 --6/7/2026 [Monday]

## Assignment 4

### How floating point numbers are stored using IEEE standards?

Write a program to understand the above concept, if available.

### IEEE 754 Floating Point Representation

Computers cannot store decimal numbers exactly the same way humans write them. Instead, they use a standard called IEEE 754 to store floating-point numbers.

### Why do we need IEEE 754?

Integers such as 10 and 25 are easy to store in binary, but decimal numbers like 3.14 and 45.75 cannot always be represented exactly in binary.

So, IEEE 754 defines a standard format that every computer follows.

### Real-life example

Instead of writing a very large number as a full decimal string, we write it in scientific notation:

$$1.23456789 \times 10^8$$

Similarly, computers use binary scientific notation.

Example:

$$13.25 = 1101.01_2 = 1.10101 \times 2^3$$

### IEEE 754 Single Precision (32-bit)

A float occupies 32 bits.

| Part | Bits | Purpose |
|------|------|---------|
| Sign | 1 | Shows positive or negative |
| Exponent | 8 | Stores the power of 2 using a bias |
| Mantissa | 23 | Stores the fractional part after the leading 1 |

### 1. Sign bit

- `0` means positive
- `1` means negative

### 2. Exponent

The exponent is stored with a bias of 127.

Example:

- Actual exponent = 3
- Stored exponent = $3 + 127 = 130$
- Binary of 130 = `10000010`

### 3. Mantissa

The leading `1` is not stored because IEEE 754 assumes it is always there.

Example:

For:

$$1.10101 \times 2^3$$

The mantissa stored is:

```text
10101...
```

### Complete example: 13.25

1. Convert to binary:

```text
13.25 = 1101.01
```

2. Normalize:

```text
1101.01 = 1.10101 × 2^3
```

3. Sign bit:

```text
0
```

4. Exponent:

```text
3 + 127 = 130 = 10000010
```

5. Mantissa:

```text
10101000000000000000000
```

### Final IEEE 754 representation

```text
0 10000010 10101000000000000000000
```

### Another example: 5.5

```text
5.5 = 101.1 = 1.011 × 2^2
```

So:

- Sign = `0`
- Exponent = $2 + 127 = 129 = 10000001$
- Mantissa = `01100000000000000000000`

### Why does 0.1 + 0.2 != 0.3?

Some decimal values cannot be represented exactly in binary, so small rounding errors may appear.

Example in Java:

```java
public class FloatingPointExample {
    public static void main(String[] args) {
        double a = 0.1;
        double b = 0.2;
        System.out.println(a + b);
    }
}
```

Output:

```text
0.30000000000000004
```

### Java program to display IEEE 754 representation

```java
public class IEEE754Demo {
    public static void main(String[] args) {
        float num = 13.25f;

        int bits = Float.floatToIntBits(num);

        String binary = String.format("%32s",
                Integer.toBinaryString(bits)).replace(' ', '0');

        System.out.println("Number : " + num);
        System.out.println("IEEE 754 Binary:");
        System.out.println(binary);

        System.out.println("Sign     : " + binary.substring(0, 1));
        System.out.println("Exponent : " + binary.substring(1, 9));
        System.out.println("Mantissa : " + binary.substring(9));
    }
}
```

### Sample output

```text
Number : 13.25
IEEE 754 Binary:
01000001010101000000000000000000
Sign     : 0
Exponent : 10000010
Mantissa : 10101000000000000000000
```

### Java program for user input

```java
import java.util.Scanner;

public class IEEE754UserInput {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a float number: ");
        float num = sc.nextFloat();

        int bits = Float.floatToIntBits(num);

        String binary = String.format("%32s",
                Integer.toBinaryString(bits)).replace(' ', '0');

        System.out.println("\nIEEE 754 Representation");
        System.out.println("-------------------------");
        System.out.println("Binary    : " + binary);
        System.out.println("Sign      : " + binary.substring(0, 1));
        System.out.println("Exponent  : " + binary.substring(1, 9));
        System.out.println("Mantissa  : " + binary.substring(9));

        sc.close();
    }
}
```

### Example run

```text
Enter a float number: 5.5

IEEE 754 Representation
-------------------------
Binary    : 01000000101100000000000000000000
Sign      : 0
Exponent  : 10000001
Mantissa  : 01100000000000000000000
```

### Summary

- IEEE 754 is the standard for storing floating-point numbers.
- A float uses 32 bits: 1 sign bit, 8 exponent bits, and 23 mantissa bits.
- Numbers are stored in normalized binary scientific notation.
- The exponent is stored with a bias of 127.
- Some decimal values, such as 0.1, cannot be represented exactly in binary.

## Assignmnet 5

### Why there are no ++ and -- operators in Python?
## Answer

Python **does not have** the `++` (increment) and `--` (decrement) operators.

Instead, Python uses:

- `+= 1` → Increase the value by 1
- `-= 1` → Decrease the value by 1

This makes the code **simple**, **easy to read**, and **less confusing**.

---

# What is Increment?

Increment means **adding 1** to a variable.

Instead of writing:

```python
count++
```

Python uses:

```python
count += 1
```

### Example

```python
count = 5

count += 1

print(count)
```

### Output

```text
6
```

### Explanation

- Initial value = **5**
- `count += 1` means **count = count + 1**
- New value = **6**

---

# What is Decrement?

Decrement means **subtracting 1** from a variable.

Instead of writing:

```python
count--
```

Python uses:

```python
count -= 1
```

### Example

```python
count = 8

count -= 1

print(count)
```

### Output

```text
7
```

### Explanation

- Initial value = **8**
- `count -= 1` means **count = count - 1**
- New value = **7**

---

# Why Doesn't Python Use `++` and `--`?

Python was designed to be:

- Easy to learn
- Easy to read
- Simple to understand

The operators `++` and `--` can sometimes confuse beginners because they behave differently in some other programming languages.

Python avoids this confusion by using clear statements like:

```python
x += 1
```

instead of

```python
x++
```

---

# Real-Life Example

Imagine you have **10 chocolates**.

### Add one chocolate

```python
chocolates = 10

chocolates += 1

print(chocolates)
```

### Output

```text
11
```

---

### Eat one chocolate

```python
chocolates = 10

chocolates -= 1

print(chocolates)
```

### Output

```text
9
```

---

# What Happens if You Use `++` in Python?

```python
x = 5

++x

print(x)
```

### Output

```text
5
```

### Explanation

In Python, `++x` **does not increment** the value.

It is treated as:

```python
+(+x)
```

which simply means **positive of a positive number**, so the value remains unchanged.

---

# Summary

| Operator | Python Equivalent | Meaning |
|----------|-------------------|---------|
| `++` | `+= 1` | Increase value by 1 |
| `--` | `-= 1` | Decrease value by 1 |

### Key Points

- Python **does not support** `++` and `--`.
- Use `+= 1` to increment a value.
- Use `-= 1` to decrement a value.
- This makes Python code **clear, readable, and easy to understand**.

## Assignment 6
# Relational Operators Precedence in Python
### Do all relational operators have same precedence or do they have different precedences? All relational operators have the same precedence in Python.

## Question
**Do all relational operators have the same precedence or do they have different precedences?**

### Answer
**All relational operators have the same precedence in Python.**

This means Python evaluates all relational operators (`<`, `>`, `<=`, `>=`, `==`, `!=`) at the **same priority level**.

When multiple relational operators appear in an expression, Python evaluates them from **left to right** (or as a chained comparison, when applicable).

---

# Relational Operators

| Operator | Meaning |
|----------|---------|
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal to |
| `>=` | Greater than or equal to |
| `==` | Equal to |
| `!=` | Not equal to |

---

# Example 1

```python
a = 10
b = 20

print(a < b)
```

### Output

```text
True
```

Explanation:

- Is **10 less than 20?**
- **Yes**, so the output is **True**.

---

# Example 2

```python
x = 15
y = 15

print(x == y)
```

### Output

```text
True
```

Explanation:

- Both values are equal.
- Therefore, the result is **True**.

---

# Example 3

```python
a = 5
b = 10
c = 15

print(a < b < c)
```

### Output

```text
True
```

### Explanation

Python checks:

```text
5 < 10   → True
10 < 15  → True
```

Since both conditions are **True**, the final result is:

```text
True
```

---

# Example 4

```python
a = 20
b = 10

print(a > b)
```

### Output

```text
True
```

Explanation:

- Is **20 greater than 10?**
- **Yes**, so the output is **True**.

---

# Real-Life Example

Imagine the marks of three students:

```text
Rahul = 60
Anu = 75
Ravi = 90
```

Python expression:

```python
print(60 < 75 < 90)
```

Python checks:

```text
60 < 75 → True
75 < 90 → True
```

Final Output:

```text
True
```

This means the marks are increasing correctly.

---

# Important Points

- All relational operators have **the same precedence**.
- Python evaluates them **from left to right**.
- Relational operators always return either:
  - `True`
  - `False`

---

# Summary

- All relational operators (`<`, `>`, `<=`, `>=`, `==`, `!=`) have the **same precedence**.
- They are used to compare values.
- The result of every relational operation is either **True** or **False**.

## Assigment 7
### What are the minimum relational operators using which all other relational operators can be implemented?
## Answer

The **minimum relational operators** required are:

- `<` (Less than)
- `==` (Equal to)

Using only these **two operators**, we can implement all the other relational operators.

---

# Why only `<` and `==`?

- `<` tells whether one value is smaller than another.
- `==` tells whether two values are equal.

Using these two, we can derive all the remaining operators.

---

# How to Implement Other Operators

| Operator | Can be implemented as |
|----------|------------------------|
| `>` | `b < a` |
| `<=` | `(a < b) or (a == b)` |
| `>=` | `(b < a) or (a == b)` |
| `!=` | `not (a == b)` |

---

# Example 1: Greater Than (`>`)

Instead of writing:

```python
a > b
```

We can write:

```python
b < a
```

### Example

```python
a = 20
b = 10

print(b < a)
```

### Output

```text
True
```

### Explanation

Since **10 is less than 20**, it means **20 is greater than 10**.

---

# Example 2: Less Than or Equal To (`<=`)

Instead of writing:

```python
a <= b
```

We can write:

```python
(a < b) or (a == b)
```

### Example

```python
a = 10
b = 10

print((a < b) or (a == b))
```

### Output

```text
True
```

### Explanation

- `10 < 10` → False
- `10 == 10` → True

False OR True = **True**

---

# Example 3: Greater Than or Equal To (`>=`)

Instead of writing:

```python
a >= b
```

We can write:

```python
(b < a) or (a == b)
```

### Example

```python
a = 15
b = 10

print((b < a) or (a == b))
```

### Output

```text
True
```

### Explanation

- `10 < 15` → True
- So the answer is **True**.

---

# Example 4: Not Equal To (`!=`)

Instead of writing:

```python
a != b
```

We can write:

```python
not (a == b)
```

### Example

```python
a = 5
b = 8

print(not (a == b))
```

### Output

```text
True
```

### Explanation

- `5 == 8` → False
- `not False` → True

So, **5 is not equal to 8**.

---

# Real-Life Example

Imagine two students' marks:

```text
Rahul = 80
Anu = 90
```

Check if Rahul scored more than Anu.

Instead of writing:

```python
80 > 90
```

We can write:

```python
90 < 80
```

Output:

```text
False
```

This means Rahul did **not** score more than Anu.

---

## DAY-4 [7/7/26]
# Assignment 8

# 1. What is Pythonic?

## Definition
**Pythonic** means writing Python code in a way that follows Python's style, philosophy, and best practices. Pythonic code is simple, readable, and easy to understand.

Python follows the principle:

> **"Readability counts."**

A Pythonic program is:
- Simple
- Clean
- Easy to read
- Easy to maintain
- Uses Python's built-in features whenever possible

### Example

### Non-Pythonic Code
```python
numbers = [1, 2, 3, 4, 5]
square = []

for i in numbers:
    square.append(i * i)

print(square)
```

### Pythonic Code
```python
numbers = [1, 2, 3, 4, 5]

square = [i * i for i in numbers]

print(square)
```

**Output**
```
[1, 4, 9, 16, 25]
```

The second approach is shorter, cleaner, and more Pythonic.

---

# 2. What is PEP 8?

## Definition
**PEP 8 (Python Enhancement Proposal 8)** is the official style guide for writing Python code.

It provides rules and recommendations that make Python programs consistent and readable.

Following PEP 8 helps developers write code that is easier to understand and maintain.

---

## Some Important PEP 8 Rules

### 1. Use meaningful variable names

✔ Good
```python
student_name = "Bhuvana"
```

✘ Bad
```python
a = "Bhuvana"
```

---

### 2. Use 4 spaces for indentation

✔ Correct
```python
if True:
    print("Hello")
```

---

### 3. Use snake_case for variable and function names

```python
student_name = "Bhuvana"

def calculate_total():
    pass
```

---

### 4. Use PascalCase for class names

```python
class Student:
    pass
```

---

### 5. Leave blank lines between functions and classes

This improves readability.

---

## Advantages of PEP 8

- Improves readability
- Makes code consistent
- Easier to debug
- Easier for team collaboration
- Makes maintenance easier

---

# Assignment 9

# Evolution of Programming Languages

Programming languages have evolved over time to make programming easier, faster, and more efficient.

---

## 1. Machine Language (1GL)

### Definition
Machine language is the lowest-level programming language.

It consists only of binary digits:
- 0
- 1

Example:
```
10110110
```

### Advantages
- Executes very fast.
- Directly understood by the CPU.

### Disadvantages
- Very difficult to write.
- Difficult to debug.
- Machine dependent.

---

## 2. Assembly Language (2GL)

### Definition
Assembly language uses mnemonics instead of binary numbers.

Example:
```assembly
MOV A, B
ADD A, C
```

An **Assembler** converts assembly language into machine language.

### Advantages
- Easier than machine language.
- Faster execution.

### Disadvantages
- Machine dependent.
- Still difficult for large programs.

---

## 3. Domain-Oriented Languages (3GL)

These languages were developed for specific domains.

### Examples
- COBOL → Business applications
- FORTRAN → Scientific calculations

### Advantages
- Easier than assembly language.
- Domain-specific features.

### Disadvantages
- Limited to particular domains.

---

## 4. Domain-Friendly Languages

These are general-purpose programming languages.

### Examples
- C
- Pascal

They can be used for many different types of applications.

### Advantages
- Portable
- Faster
- Structured programming

---

## 5. Object-Oriented Programming Languages (OOPL)

Object-Oriented Programming introduced concepts such as:
- Class
- Object
- Inheritance
- Encapsulation
- Polymorphism
- Abstraction

Examples:
- Simula 67
- C with Classes
- C++

---

## C++

C++ = C + Object-Oriented Programming

C++ added object-oriented features to the C language.

### Relationship

- Every C program is a C++ program.
- Every C++ program is **not** a C program.

Reason:
- C++ is a **superset** of C.
- C is a **subset** of C++.

---

## Why Java Was Introduced

Although C++ is powerful, it has some drawbacks, such as:

- Friend functions
- Private inheritance
- Global variables
- Global functions
- Operator overloading
- Objects can be created in the Stack area

Because of these issues, software experts wanted a **Strict Object-Oriented Programming Language**.

Hence, **Java** was introduced.

Java focuses on:
- Simplicity
- Security
- Portability
- Robustness
- Better object-oriented programming

---

# Assignment 10

# Why is There No Function Overloading in Python?

## Definition of Function Overloading

Function overloading means creating multiple functions with the **same name** but **different parameters**.

Languages like Java and C++ support function overloading.

Example in Java:

```java
add(int a, int b)

add(int a, int b, int c)
```

Both functions have the same name but different parameter lists.

---

## Why Doesn't Python Support Function Overloading?

Python does **not** support traditional function overloading because:

- Function names act as references to objects.
- When another function with the same name is created, the previous one is replaced.

Only the latest function definition remains.

---

## Example

```python
def add(a, b):
    return a + b

def add(a, b, c):
    return a + b + c

print(add(10, 20, 30))
```

**Output**
```
60
```

If we try:

```python
print(add(10, 20))
```

**Output**
```
TypeError:
add() missing 1 required positional argument: 'c'
```

The first function no longer exists because it was overwritten by the second one.

---

## How Does Python Achieve Similar Functionality?

Python uses:
- Default arguments
- Variable-length arguments (`*args`)
- Keyword arguments (`**kwargs`)

### Example using `*args`

```python
def add(*numbers):
    return sum(numbers)

print(add(10, 20))
print(add(10, 20, 30))
print(add(10, 20, 30, 40))
```

**Output**
```
30
60
100
```

---

## Conclusion

Python does not support traditional function overloading because each new function with the same name replaces the previous one. Instead, Python provides flexible features like `*args`, default parameters, and `**kwargs` to achieve similar behavior.

---

# Assignment 11

# Why is There No Implicit Type Casting in Python?

## What is Type Casting?

Type casting means converting one data type into another.

There are two types:

1. Implicit Type Casting (Automatic)
2. Explicit Type Casting (Manual)

---

## What is Implicit Type Casting?

Implicit type casting means the programming language automatically converts one data type into another without the programmer writing conversion code.

Some languages perform many automatic conversions.

---

## Why Doesn't Python Perform General Implicit Type Casting?

Python is a **strongly typed** language.

It avoids automatic conversions that may:
- Lose data
- Produce unexpected results
- Cause logical errors

Python requires the programmer to explicitly convert incompatible data types.

This makes programs:
- Safer
- More predictable
- Easier to debug

---

## Example (Without Explicit Conversion)

```python
age = "21"

print(age + 5)
```

**Output**
```
TypeError:
can only concatenate str (not "int") to str
```

Python does not automatically convert `"21"` into the integer `21`.

---

## Correct Way (Explicit Type Casting)

```python
age = "21"

print(int(age) + 5)
```

**Output**
```
26
```

Here, `int(age)` explicitly converts the string into an integer.

---

## Another Example

```python
num = 15

print(float(num))
```

**Output**
```
15.0
```

The programmer explicitly requests the conversion.

---

## Advantages of Explicit Type Casting

- Prevents accidental errors
- Makes the code more readable
- Improves program reliability
- Gives the programmer full control over data conversion

---

## Conclusion

Python avoids general implicit type casting because it is a strongly typed language. Instead of automatically converting incompatible data types, Python requires **explicit type casting** using functions such as `int()`, `float()`, `str()`, and `bool()`. This makes Python programs safer, clearer, and less prone to unexpected behavior.

## Day-5 8/7/2026[Wednesday]

-- refer neelmyna github files assignment file for that

## Day-6 9/7/2026[Thursday]
#  Assignment12:
    1.Write a program to find sum of digits of a number
        a. Extract digits from the number and solve the problem
        b. Use Pythonic
    2.Find smallest and biggest digit in a number
    3.Check if a number is Prime
    4.Print Prime numbers in decreasing order between M and N (M < N)
    5.Print Prime digits in a number
    6.Print distinct Composite digits in a number
    7.Find sum of Odd digits in a number
    8.Find sum of Even placed digits in a number
    9.Find Odd placed Even digits in a number

// javascript mini project

    
<!DOCTYPE html>
<html>
<head>
    <title>Product Form</title>
</head>
<body>

<h2>Name: <input type="text" id="name"></h2>

<h2>Price: <input type="number" id="price"></h2>

<h2>Quantity: <input type="number" id="quantity"></h2>

<button onclick="submitForm()">Submit</button>

<script>
function submitForm() {
    let name = document.getElementById("name").value;
    let price = document.getElementById("price").value;
    let quantity = document.getElementById("quantity").value;

    alert(
        "Name: " + name +
        "\nPrice: " + price +
        "\nQuantity: " + quantity
    );
}
</script>

</body>
</html>

Output
Enter Name, Price, and Quantity.
Click Submit.
A popup displays:
Name: Apple
Price: 120
Quantity: 5