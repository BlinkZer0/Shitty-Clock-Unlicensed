#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║                    🍔 THE CHEESEBURGER CLOCK LANGUAGE 🍔                  ║
║                                                                           ║
║  Licensed under the Overprotective License (OPL-∞)                       ║
║  "All rights aggressively reserved. Including the right to tell time."   ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

CHEESEBURGER CLOCK LANGUAGE SPECIFICATION v2.1:
================================================

A fully functional Turing-complete esoteric programming language based on
cheeseburgers and burger assembly.

NOW WITH EXOTIC FEATURES: Arrays, Strings, Advanced Math, Bitwise Operations!
See EXOTIC_FEATURES.md for complete documentation.

SYNTAX:
-------
🍔 TOP_BUN         - Start program
🥬 LETTUCE         - Clear screen operation
🍅 TOMATO          - Display operation
🧀 CHEESE          - Time calculation
🥓 BACON           - Random number generation
🍖 PATTY           - Loop structure
🍟 FRIES           - Conditional (if)
🥤 DRINK           - Wait/sleep operation
🎵 SESAME_SEED     - Individual iteration marker
🍔 BOTTOM_BUN      - End program

TURING-COMPLETE EXTENSIONS (New in v2.0):
-----------------------------------------
🧀 CHEESE_SLICE        - Store variable
🥬 GET_INGREDIENT      - Retrieve variable
🍔 STACK_BURGER        - Addition
🍖 REMOVE_PATTY        - Subtraction
🍖🍖 DOUBLE_PATTY       - Multiplication
🔪 SLICE_BURGER        - Division
🍞 LEFTOVER_CRUMBS     - Modulo
👅 TASTE_TEST          - Comparison
👨‍🍳 CREATE_RECIPE       - Define function
🍽️ SERVE_DISH          - Call function
🔥 GRILL_LOOP          - While loop
🔥 BURN_BURGER         - Break loop
🔄 FLIP_BURGER         - Continue loop
🍽️ SERVE_TO_CUSTOMER   - Output value

This parody language actually executes and displays a working clock!
"""

import time
import datetime
import sys
import os
from threading import Thread
import random

class BurgerClockInterpreter:
    def __init__(self):
        self.start_time = time.time()
        self.trial_duration = 300  # 5 minutes trial
        self.unauthorized_charges = 0
        self.base_price = 999.99
        self.hourly_rate = 49.99
        self.running = True
        self.cheese_count = 0  # Track cheese layers (time checks)
        self.bacon_strips = 0  # Track bacon strips (random events)

        # TURING-COMPLETE EXTENSIONS
        self.burger_ingredients = {}  # Variable storage (ingredients)
        self.recipes = {}            # Function definitions
        self.grill_stack = []        # For nested loops
        self.order_stack = []        # For function calls

    # ============================================================================
    # TURING-COMPLETE FEATURES
    # ============================================================================

    def cheese_slice(self, var_name, value):
        """🧀 CHEESE_SLICE - Store a value in a burger ingredient variable"""
        self.burger_ingredients[var_name] = value
        return value

    def get_ingredient(self, var_name):
        """🥬 GET_INGREDIENT - Retrieve burger ingredient value"""
        return self.burger_ingredients.get(var_name, 0)

    def stack_burger(self, var1, var2):
        """🍔 STACK_BURGER - Add two ingredient values (arithmetic)"""
        val1 = self.get_ingredient(var1) if isinstance(var1, str) else var1
        val2 = self.get_ingredient(var2) if isinstance(var2, str) else var2
        return val1 + val2

    def remove_patty(self, var1, var2):
        """🍖 REMOVE_PATTY - Subtract ingredient values"""
        val1 = self.get_ingredient(var1) if isinstance(var1, str) else var1
        val2 = self.get_ingredient(var2) if isinstance(var2, str) else var2
        return val1 - val2

    def double_patty(self, var1, var2):
        """🍖🍖 DOUBLE_PATTY - Multiply ingredient values"""
        val1 = self.get_ingredient(var1) if isinstance(var1, str) else var1
        val2 = self.get_ingredient(var2) if isinstance(var2, str) else var2
        return val1 * val2

    def slice_burger(self, var1, var2):
        """🔪 SLICE_BURGER - Divide ingredient values"""
        val1 = self.get_ingredient(var1) if isinstance(var1, str) else var1
        val2 = self.get_ingredient(var2) if isinstance(var2, str) else var2
        return val1 // val2 if val2 != 0 else 0

    def leftover_crumbs(self, var1, var2):
        """🍞 LEFTOVER_CRUMBS - Modulo operation on ingredients"""
        val1 = self.get_ingredient(var1) if isinstance(var1, str) else var1
        val2 = self.get_ingredient(var2) if isinstance(var2, str) else var2
        return val1 % val2 if val2 != 0 else 0

    def taste_test(self, var1, operator, var2):
        """👅 TASTE_TEST - Compare two ingredient values"""
        val1 = self.get_ingredient(var1) if isinstance(var1, str) else var1
        val2 = self.get_ingredient(var2) if isinstance(var2, str) else var2

        if operator == "SAME":
            return val1 == val2
        elif operator == "DIFFERENT":
            return val1 != val2
        elif operator == "MORE":
            return val1 > val2
        elif operator == "LESS":
            return val1 < val2
        elif operator == "MORE_OR_SAME":
            return val1 >= val2
        elif operator == "LESS_OR_SAME":
            return val1 <= val2
        return False

    def create_recipe(self, recipe_name, instructions):
        """👨‍🍳 CREATE_RECIPE - Define a function (recipe)"""
        self.recipes[recipe_name] = instructions

    def serve_dish(self, recipe_name):
        """🍽️ SERVE_DISH - Call a function (serve recipe)"""
        if recipe_name in self.recipes:
            self.order_stack.append(recipe_name)
            result = self.recipes[recipe_name]()
            self.order_stack.pop()
            return result
        return None

    def grill_loop(self, condition, body, increment=None):
        """🔥 GRILL_LOOP - While loop with break/continue"""
        loop_id = len(self.grill_stack)
        self.grill_stack.append({"id": loop_id, "break": False, "continue": False})

        while condition():
            if self.grill_stack[-1]["break"]:
                break
            if self.grill_stack[-1]["continue"]:
                self.grill_stack[-1]["continue"] = False
                if increment:
                    increment()
                continue

            body()

            if increment:
                increment()

        self.grill_stack.pop()

    def burn_burger(self):
        """🔥 BURN_BURGER - Break from loop"""
        if self.grill_stack:
            self.grill_stack[-1]["break"] = True

    def flip_burger(self):
        """🔄 FLIP_BURGER - Continue to next iteration"""
        if self.grill_stack:
            self.grill_stack[-1]["continue"] = True

    def serve_to_customer(self, value):
        """🍽️ SERVE_TO_CUSTOMER - Print a value"""
        val = self.get_ingredient(value) if isinstance(value, str) else value
        print(f"   🍔 Burger output: {val}")

    # ============================================================================
    # EXOTIC BURGER FEATURES (Advanced Operations)
    # ============================================================================

    def prepare_combo_meal(self, var_name, items=None):
        """🍟 PREPARE_COMBO_MEAL - Create an array/list"""
        if items is None:
            items = []
        self.burger_ingredients[var_name] = list(items)
        return self.burger_ingredients[var_name]

    def add_to_combo(self, combo_name, item):
        """➕ ADD_TO_COMBO - Append to array"""
        if combo_name not in self.burger_ingredients:
            self.burger_ingredients[combo_name] = []
        item_val = self.get_ingredient(item) if isinstance(item, str) and item in self.burger_ingredients else item
        self.burger_ingredients[combo_name].append(item_val)
        return self.burger_ingredients[combo_name]

    def take_from_combo(self, combo_name, index):
        """🎯 TAKE_FROM_COMBO - Get array element"""
        combo = self.burger_ingredients.get(combo_name, [])
        idx = self.get_ingredient(index) if isinstance(index, str) else index
        return combo[idx] if 0 <= idx < len(combo) else None

    def count_combo_items(self, combo_name):
        """🔢 COUNT_COMBO_ITEMS - Get array length"""
        combo = self.burger_ingredients.get(combo_name, [])
        return len(combo)

    def slice_combo(self, combo_name, start, end):
        """🔪 SLICE_COMBO - Array slicing"""
        combo = self.burger_ingredients.get(combo_name, [])
        start_idx = self.get_ingredient(start) if isinstance(start, str) else start
        end_idx = self.get_ingredient(end) if isinstance(end, str) else end
        return combo[start_idx:end_idx]

    def organize_combo(self, combo_name, reverse=False):
        """📊 ORGANIZE_COMBO - Sort an array"""
        if combo_name in self.burger_ingredients:
            self.burger_ingredients[combo_name].sort(reverse=reverse)
        return self.burger_ingredients.get(combo_name, [])

    def assemble_burger_name(self, text):
        """🏗️ ASSEMBLE_BURGER_NAME - String concatenation"""
        if isinstance(text, list):
            return ''.join(str(t) for t in text)
        return str(text)

    def measure_burger_name(self, text):
        """📏 MEASURE_BURGER_NAME - String length"""
        val = self.get_ingredient(text) if isinstance(text, str) and text in self.burger_ingredients else text
        return len(str(val))

    def cut_burger_portion(self, text, start, end=None):
        """✂️ CUT_BURGER_PORTION - String slicing"""
        val = self.get_ingredient(text) if isinstance(text, str) and text in self.burger_ingredients else text
        text_str = str(val)
        if end is None:
            return text_str[start:]
        return text_str[start:end]

    def super_size_power(self, base, exponent):
        """💪 SUPER_SIZE_POWER - Exponentiation"""
        base_val = self.get_ingredient(base) if isinstance(base, str) else base
        exp_val = self.get_ingredient(exponent) if isinstance(exponent, str) else exponent
        return base_val ** exp_val

    def burger_root(self, value):
        """🌱 BURGER_ROOT - Square root"""
        val = self.get_ingredient(value) if isinstance(value, str) else value
        import math
        return int(math.sqrt(val))

    def absolute_burger(self, value):
        """💯 ABSOLUTE_BURGER - Absolute value"""
        val = self.get_ingredient(value) if isinstance(value, str) else value
        return abs(val)

    def max_combo_item(self, combo_name):
        """⬆️ MAX_COMBO_ITEM - Maximum value in array"""
        combo = self.burger_ingredients.get(combo_name, [])
        return max(combo) if combo else None

    def min_combo_item(self, combo_name):
        """⬇️ MIN_COMBO_ITEM - Minimum value in array"""
        combo = self.burger_ingredients.get(combo_name, [])
        return min(combo) if combo else None

    def total_combo_value(self, combo_name):
        """💰 TOTAL_COMBO_VALUE - Sum all values in array"""
        combo = self.burger_ingredients.get(combo_name, [])
        return sum(combo)

    def reverse_combo(self, combo_name):
        """🔄 REVERSE_COMBO - Reverse an array"""
        if combo_name in self.burger_ingredients:
            self.burger_ingredients[combo_name].reverse()
        return self.burger_ingredients.get(combo_name, [])

    def find_in_combo(self, combo_name, item):
        """🔍 FIND_IN_COMBO - Find index of item in array"""
        combo = self.burger_ingredients.get(combo_name, [])
        item_val = self.get_ingredient(item) if isinstance(item, str) and item in self.burger_ingredients else item
        try:
            return combo.index(item_val)
        except ValueError:
            return -1

    def is_prime_burger(self, value):
        """⭐ IS_PRIME_BURGER - Check if number is prime"""
        val = self.get_ingredient(value) if isinstance(value, str) else value
        if val < 2:
            return False
        for i in range(2, int(val ** 0.5) + 1):
            if val % i == 0:
                return False
        return True

    def random_burger_range(self, min_val, max_val):
        """🎲 RANDOM_BURGER_RANGE - Generate random number in range"""
        min_v = self.get_ingredient(min_val) if isinstance(min_val, str) else min_val
        max_v = self.get_ingredient(max_val) if isinstance(max_val, str) else max_val
        return random.randint(min_v, max_v)

    def swap_ingredients(self, var1, var2):
        """🔀 SWAP_INGREDIENTS - Swap two variables"""
        temp = self.burger_ingredients.get(var1, 0)
        self.burger_ingredients[var1] = self.burger_ingredients.get(var2, 0)
        self.burger_ingredients[var2] = temp

    def bitwise_burger_and(self, var1, var2):
        """🔗 BITWISE_BURGER_AND - Bitwise AND"""
        val1 = self.get_ingredient(var1) if isinstance(var1, str) else var1
        val2 = self.get_ingredient(var2) if isinstance(var2, str) else var2
        return val1 & val2

    def bitwise_burger_or(self, var1, var2):
        """⚡ BITWISE_BURGER_OR - Bitwise OR"""
        val1 = self.get_ingredient(var1) if isinstance(var1, str) else var1
        val2 = self.get_ingredient(var2) if isinstance(var2, str) else var2
        return val1 | val2

    def bitwise_burger_xor(self, var1, var2):
        """✨ BITWISE_BURGER_XOR - Bitwise XOR"""
        val1 = self.get_ingredient(var1) if isinstance(var1, str) else var1
        val2 = self.get_ingredient(var2) if isinstance(var2, str) else var2
        return val1 ^ val2

    def shift_burger_left(self, var, amount):
        """⬅️ SHIFT_BURGER_LEFT - Bitwise left shift"""
        val = self.get_ingredient(var) if isinstance(var, str) else var
        amt = self.get_ingredient(amount) if isinstance(amount, str) else amount
        return val << amt

    def shift_burger_right(self, var, amount):
        """➡️ SHIFT_BURGER_RIGHT - Bitwise right shift"""
        val = self.get_ingredient(var) if isinstance(var, str) else var
        amt = self.get_ingredient(amount) if isinstance(amount, str) else amount
        return val >> amt

    # ============================================================================
    # ORIGINAL CLOCK FEATURES
    # ============================================================================

    def clear_screen(self):
        """🥬 LETTUCE operation - Clear the screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_burger_header(self):
        """🍅 TOMATO operation - Display the burger header"""
        burger_art = """
         _....._
       .'       '.
      /  🍔  🕐  🍔 \\
     |  THE BURGER  |
     |  CLOCK LANG  |
      \\  COMPILER  /
       '.       .'
         '-----'

================================================================================
|                                                                           |
|                    🍔 THE CHEESEBURGER CLOCK LANGUAGE 🍔                  |
|                                                                           |
|  Licensed under the Overprotective License (OPL-∞)                       |
|  "All rights aggressively reserved. Including the right to tell time."   |
|                                                                           |
|  ⚠️  WARNING: Unauthorized burger assembly detected!                     |
|                                                                           |
================================================================================
        """
        print(burger_art)

    def calculate_burger_charges(self):
        """🧀 CHEESE operation - Calculate charges (cheese layers)"""
        elapsed_time = time.time() - self.start_time
        hours_used = elapsed_time / 3600

        # Base charge + hourly rate
        self.unauthorized_charges = -(self.base_price + (hours_used * self.hourly_rate))

        # 🥓 BACON - Add random "burger assembly fees"
        burger_fees = random.randint(10, 100)
        self.bacon_strips += 1
        self.unauthorized_charges -= burger_fees

        return self.unauthorized_charges

    def get_grill_time_remaining(self):
        """🧀 CHEESE operation - Calculate trial time (burger cooking time)"""
        elapsed = time.time() - self.start_time
        remaining = self.trial_duration - elapsed
        return max(0, remaining)

    def format_burger_time(self, seconds):
        """Format remaining time as burger cooking duration"""
        minutes = int(seconds // 60)
        secs = int(seconds % 60)
        return f"{minutes:02d}:{secs:02d}"

    def display_burger_warning(self):
        """🍅 TOMATO operation - Display burger license warning"""
        remaining = self.get_grill_time_remaining()
        charges = self.calculate_burger_charges()

        print("🍔 BURGER STATUS:")
        if remaining > 0:
            print(f"   🔥 GRILL TIME REMAINING: {self.format_burger_time(remaining)}")
            print(f"   💵 After free samples: ${self.hourly_rate}/hour + condiment fees")
        else:
            print(f"   🔥 BURGER OVERCOOKED! PAYMENT REQUIRED!")
            print(f"   💵 Unauthorized burger consumption: ${abs(charges):.2f}")
            print(f"   ⚠️  (Charges grow like cheese melting...)")

        print()
        print("🥬 LETTUCE VIOLATIONS (License breaches):")
        print("   • Article I: Unauthorized Burger Assembly")
        print("   • Article VI: Temporal Condiment Restrictions")
        print("   • Article IX: Secret Sauce Incompatibility")
        print("   • The burger vibes")
        print()

    def display_burger_time(self):
        """🧀 CHEESE operation - Display current time"""
        self.cheese_count += 1
        now = datetime.datetime.now()

        # Different time formats (burger styles)
        formats = [
            "%H:%M:%S",           # Classic Burger
            "%I:%M:%S %p",        # Deluxe Burger
            "%H:%M:%S.%f"[:-3],   # Triple Cheese Burger
        ]

        current_format = formats[0]

        # Change format every 30 seconds (different burger types)
        if int(now.second / 30) % 2 == 1:
            current_format = formats[1]

        formatted_time = now.strftime(current_format)

        # Display with ASCII burger art
        print("🕐 CURRENT BURGER TIME:")
        print()
        print("     .-\"\"\"\"-.")
        print("    /        \\")
        print("   /_        _\\")
        print("  // \\      / \\\\")
        print("  |\\__\\    /__/|")
        print("   \\    ||    /      " + formatted_time)
        print("    \\        /       " + now.strftime('%A, %B %d, %Y'))
        print("     \\  __  /")
        print("      '.__.'")
        print()
        print(f"   🧀 Cheese layers counted: {self.cheese_count}")
        print(f"   🥓 Bacon strips added: {self.bacon_strips}")
        print()

    def display_condiments(self):
        """🍅 TOMATO operation - Display additional time info (condiments)"""
        now = datetime.datetime.now()

        day_of_year = now.timetuple().tm_yday
        week_of_year = now.isocalendar()[1]
        midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
        seconds_since_midnight = int((now - midnight).total_seconds())

        print("🍅 CONDIMENT STATISTICS (Extra Time Info):")
        print(f"   🥬 Lettuce days this year: {day_of_year}")
        print(f"   🧅 Onion rings (weeks): {week_of_year}")
        print(f"   🥒 Pickle seconds since midnight: {seconds_since_midnight:,}")
        print()

    def display_burger_legal(self):
        """🍅 TOMATO operation - Display legal notice"""
        print("⚖️  BURGER LAW ENFORCEMENT:")
        print("   This burger software is licensed under the Overprotective License (OPL-∞)")
        print("   For legal questions: do-not-reply@forbidden-burgers.void")
        print("   Phone: (000) 000-0000")
        print("   Address: 404 Sesame Seed Street, Null Island")
        print("   Office Hours: Never")
        print()
        print("   © 2025 UNLICENSED Burger Software")
        print("   All rights, lefts, ups, downs, and diagonals reserved.")
        print("   (Plus all toppings, condiments, and secret sauces)")
        print()

    def display_payment_menu(self):
        """🍅 TOMATO operation - Display payment reminder (menu prices)"""
        charges = self.calculate_burger_charges()

        if self.get_grill_time_remaining() <= 0:
            print("💰 BURGER BILL:")
            print(f"   🍔 Base burger license: ${self.base_price:.2f}")
            print(f"   🧀 Extra cheese charges: ${abs(charges + self.base_price):.2f}")
            print(f"   🍟 TOTAL MEAL DEAL: ${abs(charges):.2f}")
            print()
            print("   Payment methods accepted:")
            print("   • None")
            print("   • Void")
            print("   • Imaginary currency")
            print("   • Your firstborn (terms and conditions apply)")
            print("   • Your secret sauce recipe (non-refundable)")
            print()

    def burger_program_loop(self):
        """🍖 PATTY operation - Main burger program loop"""
        try:
            while self.running:  # 🎵 SESAME_SEED iterations
                self.clear_screen()              # 🥬 LETTUCE
                self.display_burger_header()      # 🍅 TOMATO
                self.display_burger_warning()     # 🍅 TOMATO
                self.display_burger_time()        # 🧀 CHEESE
                self.display_condiments()         # 🍅 TOMATO

                # 🍟 FRIES conditional - Check if trial expired
                if self.get_grill_time_remaining() <= 0:
                    self.display_payment_menu()   # 🍅 TOMATO

                self.display_burger_legal()       # 🍅 TOMATO

                print("Press Ctrl+C to stop the grill (and face burger law)")
                print("=" * 75)

                time.sleep(1)  # 🥤 DRINK - Wait operation

        except KeyboardInterrupt:
            self.running = False
            self.clear_screen()
            print("\n" + "="*75)
            print(" " * 18 + "🍔 UNAUTHORIZED BURGER FLIP 🍔")
            print("="*75)
            print("\nYou have violated Burger Article I by flipping the burger early!")
            print("This constitutes unauthorized termination of burger assembly.")

            final_charges = self.calculate_burger_charges()
            print(f"\n💵 Final burger bill: ${abs(final_charges):.2f}")
            print(f"🧀 Total cheese layers: {self.cheese_count}")
            print(f"🥓 Total bacon strips: {self.bacon_strips}")
            print("\nYour burger violation has been logged.")
            print("(Not really. We don't track burgers. But you should feel hungry.)")
            print("\nPlease report to 404 Sesame Seed Street for processing.")
            print("="*75 + "\n")

def execute_burger_code():
    """🍔 TOP_BUN - Program entry point"""
    print("🍔 Assembling burger clock language compiler...")
    print("🥬 Adding lettuce (clearing operations)...")
    print("🍅 Slicing tomatoes (display functions)...")
    print("🧀 Melting cheese (time calculations)...")
    print("🥓 Frying bacon (random generators)...")
    print("🍖 Grilling patty (main loop)...")
    print("🥤 Pouring drink (wait functions)...")
    print("🍟 Preparing fries (conditionals)...")
    time.sleep(2)  # Dramatic burger assembly

    interpreter = BurgerClockInterpreter()
    interpreter.burger_program_loop()  # 🍖 PATTY

# 🍔 BOTTOM_BUN - Program exit point
if __name__ == "__main__":
    execute_burger_code()
