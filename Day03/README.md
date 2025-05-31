# 🍕 Day 3: Python Pizza Deliveries – 100 Days of Code

Welcome to **Day 3** of the **100 Days of Code** challenge!

This simple Python script simulates a pizza ordering system where users choose their pizza size, whether they want pepperoni, and if they want extra cheese. The total cost is calculated based on these choices.

---

## 🧠 Concepts Practiced

- User input with `input()`
- Conditional statements: `if`, `elif`, `else`
- Nested conditionals
- Arithmetic operations
- Formatted strings (`f-strings`)

---

## 💻 Project Overview

The user is asked:

1. **What size pizza** they want:  
   `S` for Small, `M` for Medium, or `L` for Large

2. **If they want pepperoni**:  
   `Y` for Yes, `N` for No

3. **If they want extra cheese**:  
   `Y` for Yes, `N` for No

Based on the inputs, the program calculates the total bill.

---

## 💰 Pricing

| Item                   | Price  |
|------------------------|--------|
| Small Pizza (S)        | $15    |
| Medium Pizza (M)       | $20    |
| Large Pizza (L)        | $25    |
| Add Pepperoni (S)      | +$2    |
| Add Pepperoni (M or L) | +$3    |
| Add Extra Cheese       | +$1    |

---

## 📦 Sample Output

```text
Welcome to Python Pizza Deliveries!
What size pizza do you want? S, M or L: M
Do you want pepperoni on your pizza? Y or N: Y
Do you want extra cheese? Y or N: Y
Your final bill is: $24.
