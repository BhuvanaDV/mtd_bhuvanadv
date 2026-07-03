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