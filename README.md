# Discount Calculator

A clean, lightweight Python function designed to calculate the final price of an item after applying a percentage discount, complete with built-in input validation.

## 🚀 How It Works

The script systematically evaluates the input data using conditional control flows (`if` statements) to ensure valid calculations before processing the discount:

* **Type Check:** Instantly rejects prices or discount values that are not numbers (`int` or `float`).
* **Price Validation:** Ensures the original price is a positive value greater than 0.
* **Discount Range:** Validates that the discount percentage falls strictly within a logical range ($0\%$ to $100\%$).
* **Calculation:** Applies the validated percentage reduction to the original price and returns the final cost.

## 🛠️ Variables Evaluated

| Variable | Type | Description |
| :--- | :--- | :--- |
| `price` | `int` / `float` | The original retail price of the item. Must be $> 0$. |
| `discount` | `int` / `float` | The percentage reduction to apply. Must be between $0$ and $100$. |

## 💻 Tech Stack
* **Language:** Python 3.x
* **Concepts:** Data validation, control structures, arithmetic expressions.
