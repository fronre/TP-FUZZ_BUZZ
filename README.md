# 🧪 TP01 – FizzBuzz (TDD Training)

## 🎯 Goal
This kata aims to introduce the **Test-Driven Development (TDD)** approach through a simple but classic problem: **FizzBuzz**.  
The objective is to progressively implement the `fizz_buzz()` function using the TDD workflow — write a failing test first, then write just enough code to make it pass, and finally refactor your solution.

---

## 🧩 Kata 1 – FizzBuzz
FizzBuzz is one of the most famous coding exercises for beginners.  
It is a simple exercise but an excellent one to start learning the **TDD flow** with.

---

## 🧾 Requirements
Write a `fizz_buzz` method that accepts a number as input and returns it as a string.

---

## 📝 Notes
- Start with the minimal failing solution.  
- Keep the three main rules in mind and always write just sufficient enough code.  
- Refactor your code after each passing test.  
- Write assertions that match the exact requirements.  

---

## ⚙️ Rules
1. For multiples of three, return `"Fizz"` instead of the number.  
2. For multiples of five, return `"Buzz"`.  
3. For numbers that are multiples of both three and five, return `"FizzBuzz"`.  
4. Otherwise, return the number as a string.  

---

## 💡 Example Table
| Input | Output     |
|-------|-------------|
| 1     | "1"         |
| 3     | "Fizz"      |
| 5     | "Buzz"      |
| 15    | "FizzBuzz"  |

---

## 🔁 TDD Workflow
1. 🟥 Write a **failing test** first  
2. 🟩 Write the **minimum code** to make the test pass  
3. 🟦 **Refactor** your code  
4. 🔁 Repeat the process until all requirements are covered  

---

## 🧠 Example Implementation (Python)

### `src/fizz_buzz.py`
```python
def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "fizzbuzz"
    if number % 3 == 0:
        return "fizz"
     if number % 5 == 0:
        return "buzz"
:
        return str(number)
