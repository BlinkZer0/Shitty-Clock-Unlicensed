#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║              🍔 FIZZBUZZ IN CHEESEBURGER CLOCK LANGUAGE 🍔                ║
║                                                                           ║
║  This program demonstrates Turing-completeness by computing FizzBuzz     ║
║  using variables, loops, conditionals, and modulo operations!            ║
║                                                                           ║
║  Licensed under the Overprotective License (OPL-∞)                       ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import sys
import os

# Fix Windows console encoding for emojis
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from burger_clock import BurgerClockInterpreter

def fizzbuzz_burger_demo():
    """
    🍔 TOP_BUN - FizzBuzz Demo

    This burger program computes FizzBuzz from 1 to 30!
    """

    print("="*75)
    print("🍔 TOP_BUN - FIZZBUZZ BURGER ASSEMBLY")
    print("="*75)
    print()
    print("Grilling FizzBuzz burgers from 1 to 30...")
    print()

    # Create our burger interpreter
    burger = BurgerClockInterpreter()

    # 🧀 CHEESE_SLICE - Initialize burger ingredients
    burger.cheese_slice("counter", 1)
    burger.cheese_slice("limit", 31)
    burger.cheese_slice("three", 3)
    burger.cheese_slice("five", 5)
    burger.cheese_slice("fifteen", 15)

    print("🍔 Initial burger ingredients:")
    print(f"   counter = {burger.get_ingredient('counter')}")
    print(f"   limit = {burger.get_ingredient('limit')}")
    print()
    print("🍔 FizzBuzz burgers (fresh off the grill):")
    print()

    # 🔥 GRILL_LOOP - Loop from 1 to 30
    def condition():
        # 👅 TASTE_TEST - Check if counter < limit
        return burger.taste_test("counter", "LESS", "limit")

    def body():
        current = burger.get_ingredient("counter")

        # 🍞 LEFTOVER_CRUMBS - Check divisibility
        mod_three = burger.leftover_crumbs("counter", "three")
        mod_five = burger.leftover_crumbs("counter", "five")
        mod_fifteen = burger.leftover_crumbs("counter", "fifteen")

        # 🍟 FRIES - Conditionals for FizzBuzz logic
        if mod_fifteen == 0:
            print(f"   🍔 Burger #{current}: FizzBuzz (Triple Deluxe!)")
        elif mod_three == 0:
            print(f"   🍔 Burger #{current}: Fizz (Cheese layer!)")
        elif mod_five == 0:
            print(f"   🍔 Burger #{current}: Buzz (Bacon strips!)")
        else:
            print(f"   🍔 Burger #{current}: {current} (Classic burger)")

        # 🍔 STACK_BURGER - Increment counter
        new_counter = burger.stack_burger("counter", 1)
        burger.cheese_slice("counter", new_counter)

    # 🔥 GRILL_LOOP - Execute the loop!
    burger.grill_loop(condition, body)

    print()
    print("="*75)
    print("🍔 BOTTOM_BUN - FizzBuzz burgers served!")
    print(f"🧀 Total cheese layers: {burger.cheese_count}")
    print(f"🥓 Total bacon strips: {burger.bacon_strips}")
    print("="*75)
    print()
    print("✨ This proves CheeseBurger language is TURING-COMPLETE! ✨")
    print("   (Now with 100% more burger metaphors)")
    print()

def advanced_burger_recipe_demo():
    """
    Demonstrate function definitions (recipes) with recursion!
    """

    print("="*75)
    print("🍔 BONUS: RECURSIVE BURGER RECIPE (Factorial)")
    print("="*75)
    print()

    burger = BurgerClockInterpreter()

    # 👨‍🍳 CREATE_RECIPE - Define a recursive factorial function
    def factorial_recipe():
        n = burger.get_ingredient("n")

        # Base case
        if burger.taste_test("n", "LESS_OR_SAME", 1):
            return 1

        # Recursive case: n * factorial(n-1)
        burger.cheese_slice("n", burger.remove_patty("n", 1))
        result = factorial_recipe()
        burger.cheese_slice("n", burger.stack_burger("n", 1))

        return burger.double_patty(n, result)

    burger.create_recipe("factorial", factorial_recipe)

    # Test factorial of 5
    burger.cheese_slice("n", 5)
    print("🍔 Computing factorial of 5 using recursive burger recipe...")

    # 🍽️ SERVE_DISH - Call the recipe!
    result = burger.serve_dish("factorial")

    print(f"   🍽️ Factorial(5) = {result}")
    print()
    print("🎉 Recursive recipes work! Functions are fully operational!")
    print("="*75)
    print()

if __name__ == "__main__":
    # 🍔 TOP_BUN
    fizzbuzz_burger_demo()
    advanced_burger_recipe_demo()
    # 🍔 BOTTOM_BUN
