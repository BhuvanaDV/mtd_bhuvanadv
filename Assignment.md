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

