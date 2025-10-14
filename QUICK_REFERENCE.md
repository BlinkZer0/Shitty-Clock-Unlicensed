# 🚀 QUICK REFERENCE CARD

## Spaghetti Daddy Please vs CheeseBurger - Side-by-Side

### Basic Operations

| Operation | Spaghetti Daddy Please | CheeseBurger |
|-----------|----------------------|--------------|
| **Store** | `store_noodle(name, val)` | `cheese_slice(name, val)` |
| **Get** | `get_noodle(name)` | `get_ingredient(name)` |
| **Add** | `add_sauce(a, b)` | `stack_burger(a, b)` |
| **Subtract** | `subtract_sauce(a, b)` | `remove_patty(a, b)` |
| **Multiply** | `multiply_sauce(a, b)` | `double_patty(a, b)` |
| **Divide** | `divide_sauce(a, b)` | `slice_burger(a, b)` |
| **Modulo** | `modulo_sauce(a, b)` | `leftover_crumbs(a, b)` |
| **Compare** | `compare_noodles(a, op, b)` | `taste_test(a, op, b)` |
| **Loop** | `boil_noodles(cond, body)` | `grill_loop(cond, body)` |
| **Break** | `break_noodle()` | `burn_burger()` |
| **Continue** | `continue_stirring()` | `flip_burger()` |
| **Output** | `output_noodle(val)` | `serve_to_customer(val)` |

### Arrays

| Operation | Spaghetti Daddy Please | CheeseBurger |
|-----------|----------------------|--------------|
| **Create** | `prepare_noodle_bowl(name, items)` | `prepare_combo_meal(name, items)` |
| **Append** | `add_to_bowl(arr, item)` | `add_to_combo(arr, item)` |
| **Get[i]** | `take_from_bowl(arr, i)` | `take_from_combo(arr, i)` |
| **Length** | `count_noodles_in_bowl(arr)` | `count_combo_items(arr)` |
| **Sort** | `sort_noodle_bowl(arr)` | `organize_combo(arr)` |
| **Max** | `max_noodle_bowl(arr)` | `max_combo_item(arr)` |
| **Min** | `min_noodle_bowl(arr)` | `min_combo_item(arr)` |
| **Sum** | `sum_noodle_bowl(arr)` | `total_combo_value(arr)` |

### Strings

| Operation | Spaghetti Daddy Please | CheeseBurger |
|-----------|----------------------|--------------|
| **Concat** | `twirl_noodles(text)` | `assemble_burger_name(text)` |
| **Length** | `measure_noodle_length(text)` | `measure_burger_name(text)` |
| **Slice** | `cut_noodle(text, s, e)` | `cut_burger_portion(text, s, e)` |

### Math

| Operation | Spaghetti Daddy Please | CheeseBurger |
|-----------|----------------------|--------------|
| **Power** | `al_dente_power(base, exp)` | `super_size_power(base, exp)` |
| **Sqrt** | `measure_noodle_root(val)` | `burger_root(val)` |
| **Abs** | `absolute_noodle(val)` | `absolute_burger(val)` |
| **Prime** | `is_prime_noodle(val)` | `is_prime_burger(val)` |
| **Random** | `random_noodle_range(min, max)` | `random_burger_range(min, max)` |

### Bitwise

| Operation | Spaghetti Daddy Please | CheeseBurger |
|-----------|----------------------|--------------|
| **AND** | `bitwise_noodle_and(a, b)` | `bitwise_burger_and(a, b)` |
| **OR** | `bitwise_noodle_or(a, b)` | `bitwise_burger_or(a, b)` |
| **XOR** | `bitwise_noodle_xor(a, b)` | `bitwise_burger_xor(a, b)` |
| **<<** | `shift_noodle_left(val, amt)` | `shift_burger_left(val, amt)` |
| **>>** | `shift_noodle_right(val, amt)` | `shift_burger_right(val, amt)` |

---

## Common Patterns

### Count Loop
```python
# Spaghetti
daddy.store_noodle("i", 0)
def cond(): return daddy.compare_noodles("i", "LESS", 10)
def body():
    daddy.output_noodle("i")
    daddy.store_noodle("i", daddy.add_sauce("i", 1))
daddy.boil_noodles(cond, body)

# Burger
burger.cheese_slice("i", 0)
def cond(): return burger.taste_test("i", "LESS", 10)
def body():
    burger.serve_to_customer("i")
    burger.cheese_slice("i", burger.stack_burger("i", 1))
burger.grill_loop(cond, body)
```

### Sum Array
```python
# Spaghetti
total = daddy.sum_noodle_bowl("numbers")

# Burger
total = burger.total_combo_value("prices")
```

### Find Prime Numbers
```python
# Spaghetti
daddy.prepare_noodle_bowl("primes", [])
for i in range(2, 100):
    if daddy.is_prime_noodle(i):
        daddy.add_to_bowl("primes", i)

# Burger
burger.prepare_combo_meal("primes", [])
for i in range(2, 100):
    if burger.is_prime_burger(i):
        burger.add_to_combo("primes", i)
```

---

## Comparison Operators

| Spaghetti | Burger | Meaning |
|-----------|--------|---------|
| EQUALS | SAME | == |
| NOT_EQUALS | DIFFERENT | != |
| GREATER | MORE | > |
| LESS | LESS | < |
| GREATER_EQUALS | MORE_OR_SAME | >= |
| LESS_EQUALS | LESS_OR_SAME | <= |

---

## Import and Setup

```python
# Spaghetti Daddy Please
from spaghetti_clock import SpaghettiDaddyInterpreter
daddy = SpaghettiDaddyInterpreter()

# All functions start with daddy.spaghetti_daddy_please_
# Example: daddy.spaghetti_daddy_please_store_noodle("x", 42)

# CheeseBurger
from burger_clock import BurgerClockInterpreter
burger = BurgerClockInterpreter()

# All functions use burger.function_name()
# Example: burger.cheese_slice("x", 42)
```

---

## Complete Examples

### Fibonacci (Spaghetti)
```python
daddy = SpaghettiDaddyInterpreter()
daddy.spaghetti_daddy_please_store_noodle("a", 0)
daddy.spaghetti_daddy_please_store_noodle("b", 1)
daddy.spaghetti_daddy_please_store_noodle("i", 0)

def cond():
    return daddy.spaghetti_daddy_please_compare_noodles("i", "LESS", 10)

def body():
    daddy.spaghetti_daddy_please_output_noodle("a")
    next_val = daddy.spaghetti_daddy_please_add_sauce("a", "b")
    daddy.spaghetti_daddy_please_store_noodle("a", daddy.spaghetti_daddy_please_get_noodle("b"))
    daddy.spaghetti_daddy_please_store_noodle("b", next_val)
    daddy.spaghetti_daddy_please_store_noodle("i", daddy.spaghetti_daddy_please_add_sauce("i", 1))

daddy.spaghetti_daddy_please_boil_noodles(cond, body)
```

### FizzBuzz (Burger)
```python
burger = BurgerClockInterpreter()
burger.cheese_slice("i", 1)

def cond():
    return burger.taste_test("i", "LESS_OR_SAME", 20)

def body():
    mod3 = burger.leftover_crumbs("i", 3)
    mod5 = burger.leftover_crumbs("i", 5)

    if mod3 == 0 and mod5 == 0:
        print("FizzBuzz")
    elif mod3 == 0:
        print("Fizz")
    elif mod5 == 0:
        print("Buzz")
    else:
        burger.serve_to_customer("i")

    burger.cheese_slice("i", burger.stack_burger("i", 1))

burger.grill_loop(cond, body)
```

---

**THANK_YOU_SPAGHETTI_DADDY** 🍝
**🍔 BOTTOM_BUN** 🍔
