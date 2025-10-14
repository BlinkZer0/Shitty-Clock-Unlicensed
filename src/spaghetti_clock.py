#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║                    🍝 THE SPAGHETTI CODE CLOCK LANGUAGE 🍝                ║
║                                                                           ║
║  Licensed under the Overprotective License (OPL-∞)                       ║
║  "All rights aggressively reserved. Including the right to tell time."   ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

SPAGHETTI CODE LANGUAGE SPECIFICATION:
======================================

A fully functional esoteric programming language based on POLITE COMPILATION.
You must ask SPAGHETTI DADDY PLEASE for everything!

SYNTAX (Polite Request System):
--------------------------------
SPAGHETTI_DADDY_PLEASE_START              - Start program
SPAGHETTI_DADDY_PLEASE_CLEAR_SCREEN       - Clear screen operation
SPAGHETTI_DADDY_PLEASE_DISPLAY            - Display operation
SPAGHETTI_DADDY_PLEASE_CALCULATE_TIME     - Time calculation
SPAGHETTI_DADDY_PLEASE_RANDOM_NOODLE      - Random number generation
SPAGHETTI_DADDY_PLEASE_LOOP               - Loop structure
SPAGHETTI_DADDY_PLEASE_IF_SAUCE_READY     - Conditional (if)
SPAGHETTI_DADDY_PLEASE_WAIT               - Wait/sleep operation
SPAGHETTI_DADDY_PLEASE_STIR               - Individual iteration
SPAGHETTI_DADDY_PLEASE_END                - End program

TURING-COMPLETE EXTENSIONS (New in v2.0):
-----------------------------------------
SPAGHETTI_DADDY_PLEASE_STORE_NOODLE       - Store variable
SPAGHETTI_DADDY_PLEASE_GET_NOODLE         - Retrieve variable
SPAGHETTI_DADDY_PLEASE_ADD_SAUCE          - Addition
SPAGHETTI_DADDY_PLEASE_SUBTRACT_SAUCE     - Subtraction
SPAGHETTI_DADDY_PLEASE_MULTIPLY_SAUCE     - Multiplication
SPAGHETTI_DADDY_PLEASE_DIVIDE_SAUCE       - Division
SPAGHETTI_DADDY_PLEASE_MODULO_SAUCE       - Modulo
SPAGHETTI_DADDY_PLEASE_COMPARE_NOODLES    - Comparison
SPAGHETTI_DADDY_PLEASE_COOK_RECIPE        - Define function
SPAGHETTI_DADDY_PLEASE_SERVE_RECIPE       - Call function
SPAGHETTI_DADDY_PLEASE_BOIL_NOODLES       - While loop
SPAGHETTI_DADDY_PLEASE_BREAK_NOODLE       - Break loop
SPAGHETTI_DADDY_PLEASE_CONTINUE_STIRRING  - Continue loop
SPAGHETTI_DADDY_PLEASE_OUTPUT_NOODLE      - Output value

THANK_YOU_SPAGHETTI_DADDY                 - Acknowledge completion
MAY_I_HAVE_ANOTHER_NOODLE                 - Continue operation
SORRY_FOR_BOTHERING_YOU_DADDY             - Error handling

This is the most polite programming language ever created.
Based on the "polite compilation" joke where code fails unless you're nice.
"""

import time
import datetime
import sys
import os
from threading import Thread
import random

# Fix Windows console encoding for emojis
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass

class SpaghettiDaddyInterpreter:
    def __init__(self):
        self.start_time = time.time()
        self.trial_duration = 300  # 5 minutes trial
        self.unauthorized_charges = 0
        self.base_price = 999.99
        self.hourly_rate = 49.99
        self.running = True
        self.noodles_served = 0  # Track noodles (operations)
        self.sauce_stirs = 0     # Track sauce stirs (iterations)
        self.politeness_level = 100  # Must stay polite!

        # TURING-COMPLETE EXTENSIONS
        self.noodle_variables = {}  # Variable storage (noodles)
        self.recipe_functions = {}  # Function definitions
        self.loop_stack = []        # For nested loops
        self.call_stack = []        # For function calls

    # ============================================================================
    # TURING-COMPLETE FEATURES
    # ============================================================================

    def spaghetti_daddy_please_store_noodle(self, var_name, value):
        """SPAGHETTI_DADDY_PLEASE_STORE_NOODLE - Store a value in a noodle variable"""
        self.noodle_variables[var_name] = value
        return value

    def spaghetti_daddy_please_get_noodle(self, var_name):
        """SPAGHETTI_DADDY_PLEASE_GET_NOODLE - Retrieve noodle variable value"""
        return self.noodle_variables.get(var_name, 0)

    def spaghetti_daddy_please_add_sauce(self, var1, var2):
        """SPAGHETTI_DADDY_PLEASE_ADD_SAUCE - Add two noodle values (arithmetic)"""
        val1 = self.spaghetti_daddy_please_get_noodle(var1) if isinstance(var1, str) else var1
        val2 = self.spaghetti_daddy_please_get_noodle(var2) if isinstance(var2, str) else var2
        return val1 + val2

    def spaghetti_daddy_please_subtract_sauce(self, var1, var2):
        """SPAGHETTI_DADDY_PLEASE_SUBTRACT_SAUCE - Subtract noodle values"""
        val1 = self.spaghetti_daddy_please_get_noodle(var1) if isinstance(var1, str) else var1
        val2 = self.spaghetti_daddy_please_get_noodle(var2) if isinstance(var2, str) else var2
        return val1 - val2

    def spaghetti_daddy_please_multiply_sauce(self, var1, var2):
        """SPAGHETTI_DADDY_PLEASE_MULTIPLY_SAUCE - Multiply noodle values"""
        val1 = self.spaghetti_daddy_please_get_noodle(var1) if isinstance(var1, str) else var1
        val2 = self.spaghetti_daddy_please_get_noodle(var2) if isinstance(var2, str) else var2
        return val1 * val2

    def spaghetti_daddy_please_divide_sauce(self, var1, var2):
        """SPAGHETTI_DADDY_PLEASE_DIVIDE_SAUCE - Divide noodle values"""
        val1 = self.spaghetti_daddy_please_get_noodle(var1) if isinstance(var1, str) else var1
        val2 = self.spaghetti_daddy_please_get_noodle(var2) if isinstance(var2, str) else var2
        return val1 // val2 if val2 != 0 else 0

    def spaghetti_daddy_please_modulo_sauce(self, var1, var2):
        """SPAGHETTI_DADDY_PLEASE_MODULO_SAUCE - Modulo operation on noodles"""
        val1 = self.spaghetti_daddy_please_get_noodle(var1) if isinstance(var1, str) else var1
        val2 = self.spaghetti_daddy_please_get_noodle(var2) if isinstance(var2, str) else var2
        return val1 % val2 if val2 != 0 else 0

    def spaghetti_daddy_please_compare_noodles(self, var1, operator, var2):
        """SPAGHETTI_DADDY_PLEASE_COMPARE_NOODLES - Compare two noodle values"""
        val1 = self.spaghetti_daddy_please_get_noodle(var1) if isinstance(var1, str) else var1
        val2 = self.spaghetti_daddy_please_get_noodle(var2) if isinstance(var2, str) else var2

        if operator == "EQUALS":
            return val1 == val2
        elif operator == "NOT_EQUALS":
            return val1 != val2
        elif operator == "GREATER":
            return val1 > val2
        elif operator == "LESS":
            return val1 < val2
        elif operator == "GREATER_EQUALS":
            return val1 >= val2
        elif operator == "LESS_EQUALS":
            return val1 <= val2
        return False

    def spaghetti_daddy_please_cook_recipe(self, recipe_name, instructions):
        """SPAGHETTI_DADDY_PLEASE_COOK_RECIPE - Define a function (recipe)"""
        self.recipe_functions[recipe_name] = instructions

    def spaghetti_daddy_please_serve_recipe(self, recipe_name):
        """SPAGHETTI_DADDY_PLEASE_SERVE_RECIPE - Call a function (serve recipe)"""
        if recipe_name in self.recipe_functions:
            self.call_stack.append(recipe_name)
            result = self.recipe_functions[recipe_name]()
            self.call_stack.pop()
            return result
        return None

    def spaghetti_daddy_please_boil_noodles(self, condition, body, increment=None):
        """SPAGHETTI_DADDY_PLEASE_BOIL_NOODLES - While loop with break/continue"""
        loop_id = len(self.loop_stack)
        self.loop_stack.append({"id": loop_id, "break": False, "continue": False})

        while condition():
            if self.loop_stack[-1]["break"]:
                break
            if self.loop_stack[-1]["continue"]:
                self.loop_stack[-1]["continue"] = False
                if increment:
                    increment()
                continue

            body()

            if increment:
                increment()

        self.loop_stack.pop()

    def spaghetti_daddy_please_break_noodle(self):
        """SPAGHETTI_DADDY_PLEASE_BREAK_NOODLE - Break from loop"""
        if self.loop_stack:
            self.loop_stack[-1]["break"] = True

    def spaghetti_daddy_please_continue_stirring(self):
        """SPAGHETTI_DADDY_PLEASE_CONTINUE_STIRRING - Continue to next iteration"""
        if self.loop_stack:
            self.loop_stack[-1]["continue"] = True

    def spaghetti_daddy_please_output_noodle(self, value):
        """SPAGHETTI_DADDY_PLEASE_OUTPUT_NOODLE - Print a value"""
        val = self.spaghetti_daddy_please_get_noodle(value) if isinstance(value, str) else value
        print(f"   🍝 Noodle output: {val}")

    # ============================================================================
    # ORIGINAL CLOCK FEATURES
    # ============================================================================

    def spaghetti_daddy_please_clear_screen(self):
        """SPAGHETTI_DADDY_PLEASE_CLEAR_SCREEN - Clear the screen politely"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def spaghetti_daddy_please_display_header(self):
        """SPAGHETTI_DADDY_PLEASE_DISPLAY - Display the dancing spaghetti daddy"""

        # Dancing Spaghetti Daddy ASCII Art
        daddy_dance = r"""
    THANK_YOU_SPAGHETTI_DADDY

       ~~~ ~~~  ~~~ ~~~
      ~~~  ~~  ~~  ~~~
        \  ||  ||  /
         \ || || /
          \|||||/
        ___\|||/___
       |  DADDY!!  |
       | ( ^ ω ^ )|
        \  \|||/  /
         |  |||  |
        /|  |||  |\
       / |  |||  | \
    ~~~  | ||| |  ~~~
   ~~~   |/   \|   ~~~
    ~~~ /       \ ~~~
       |  NOODLE |
       |  LEGS!! |
        ~~~~~~~~~

   *DANCING INTENSIFIES*

================================================================================
|                                                                           |
|                  🍝 THE SPAGHETTI CODE CLOCK LANGUAGE 🍝                  |
|                                                                           |
|  Based on POLITE COMPILATION - You MUST say "SPAGHETTI DADDY PLEASE"     |
|                                                                           |
|  Licensed under the Overprotective License (OPL-∞)                       |
|  "All rights aggressively reserved. Including the right to tell time."   |
|                                                                           |
|  ⚠️  WARNING: Unauthorized spaghetti compilation detected!                |
|                                                                           |
================================================================================
        """
        print(daddy_dance)
        print(f"   POLITENESS LEVEL: {self.politeness_level}% 💖")
        print()

    def spaghetti_daddy_please_calculate_charges(self):
        """SPAGHETTI_DADDY_PLEASE_CALCULATE_TIME - Calculate charges politely"""
        elapsed_time = time.time() - self.start_time
        hours_used = elapsed_time / 3600

        # Base charge + hourly rate
        self.unauthorized_charges = -(self.base_price + (hours_used * self.hourly_rate))

        # Add random "impolite compilation fees"
        if self.politeness_level < 50:
            rudeness_penalty = random.randint(100, 500)
            self.unauthorized_charges -= rudeness_penalty
        else:
            noodle_fees = random.randint(10, 100)
            self.unauthorized_charges -= noodle_fees

        return self.unauthorized_charges

    def spaghetti_daddy_please_get_cook_time(self):
        """SPAGHETTI_DADDY_PLEASE_CALCULATE_TIME - Calculate remaining cook time"""
        elapsed = time.time() - self.start_time
        remaining = self.trial_duration - elapsed
        return max(0, remaining)

    def may_i_have_format_please(self, seconds):
        """MAY_I_HAVE_ANOTHER_NOODLE - Format time politely"""
        minutes = int(seconds // 60)
        secs = int(seconds % 60)
        return f"{minutes:02d}:{secs:02d}"

    def spaghetti_daddy_please_show_warning(self):
        """SPAGHETTI_DADDY_PLEASE_DISPLAY - Display polite warning"""
        remaining = self.spaghetti_daddy_please_get_cook_time()
        charges = self.spaghetti_daddy_please_calculate_charges()

        print("🍝 SPAGHETTI STATUS (THANK YOU FOR ASKING):")
        if remaining > 0:
            print(f"   ⏰ NOODLE COOKING TIME REMAINING: {self.may_i_have_format_please(remaining)}")
            print(f"   💵 After free samples, if you please: ${self.hourly_rate}/hour + politeness fees")
        else:
            print(f"   🍝 NOODLES OVERCOOKED! PAYMENT KINDLY REQUESTED!")
            print(f"   💵 Unauthorized spaghetti charges: ${abs(charges):.2f}")
            print(f"   ⚠️  (Charges continue to grow, sorry for the inconvenience)")

        print()
        print("📋 POLITE LICENSE VIOLATIONS (WITH DEEPEST APOLOGIES):")
        print("   • Article I: Unauthorized Spaghetti Compilation")
        print("   • Article VI: Temporal Marinara Restrictions")
        print("   • Article IX: Parmesan Cheese Incompatibility")
        print("   • The spaghetti vibes (excuse me)")
        print()

    def spaghetti_daddy_please_show_time(self):
        """SPAGHETTI_DADDY_PLEASE_CALCULATE_TIME - Display current time politely"""
        self.noodles_served += 1
        now = datetime.datetime.now()

        # Different time formats (different pasta types)
        formats = [
            "%H:%M:%S",           # Classic Spaghetti
            "%I:%M:%S %p",        # Fettuccine Style
            "%H:%M:%S.%f"[:-3],   # Al Dente Precision
        ]

        current_format = formats[0]

        # Change format every 30 seconds
        if int(now.second / 30) % 2 == 1:
            current_format = formats[1]

        formatted_time = now.strftime(current_format)

        # Polite spaghetti art
        print("🕐 CURRENT TIME (IF YOU DON'T MIND ME SAYING):")
        print()
        print("    ~~~~~~~~~~~~~~~~~~~")
        print("   ~~~~~ SPAGHETTI ~~~~~")
        print("  ~~~~~~~~ CLOCK ~~~~~~~")
        print("   ~~~~~~~~~~~~~~~~~~~")
        print("      |           |")
        print("      |   TIME:   |")
        print(f"      | {formatted_time} |")
        print(f"      | {now.strftime('%a %b %d')} |")
        print("      |___________|")
        print()
        print("   *Spaghetti Daddy nods approvingly*")
        print()
        print(f"   🍝 Noodles served (thank you): {self.noodles_served}")
        print(f"   🥄 Sauce stirs (much appreciated): {self.sauce_stirs}")
        print()

    def spaghetti_daddy_please_show_stats(self):
        """SPAGHETTI_DADDY_PLEASE_DISPLAY - Display stats politely"""
        now = datetime.datetime.now()

        day_of_year = now.timetuple().tm_yday
        week_of_year = now.isocalendar()[1]
        midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
        seconds_since_midnight = int((now - midnight).total_seconds())

        print("📊 ADDITIONAL SPAGHETTI STATISTICS (WITH YOUR PERMISSION):")
        print(f"   🍝 Noodle days this year (pardon me): {day_of_year}")
        print(f"   🧀 Parmesan weeks (excuse me): {week_of_year}")
        print(f"   🍅 Marinara seconds since midnight: {seconds_since_midnight:,}")
        print()

    def spaghetti_daddy_please_show_legal(self):
        """SPAGHETTI_DADDY_PLEASE_DISPLAY - Display legal notice politely"""
        print("⚖️  POLITE LEGAL NOTICE (SORRY TO BOTHER YOU):")
        print("   This spaghetti software is licensed under the Overprotective License (OPL-∞)")
        print("   All operations must begin with SPAGHETTI_DADDY_PLEASE_")
        print("   For legal questions: do-not-reply@forbidden-spaghetti.void")
        print("   Phone: (000) 000-0000")
        print("   Address: 404 Noodle Lane, Null Island")
        print("   Office Hours: Never")
        print()
        print("   © 2025 UNLICENSED Spaghetti Software")
        print("   All rights, lefts, ups, downs, and diagonals reserved.")
        print("   (Plus all noodles, sauces, and politeness)")
        print()

    def spaghetti_daddy_please_show_payment(self):
        """SPAGHETTI_DADDY_PLEASE_DISPLAY - Display payment info politely"""
        charges = self.spaghetti_daddy_please_calculate_charges()

        if self.spaghetti_daddy_please_get_cook_time() <= 0:
            print("💰 SPAGHETTI BILL (APOLOGIES FOR THE CHARGES):")
            print(f"   🍝 Base spaghetti license (sorry): ${self.base_price:.2f}")
            print(f"   🧀 Extra parmesan charges (excuse me): ${abs(charges + self.base_price):.2f}")
            print(f"   🍅 TOTAL PASTA BILL (THANK YOU): ${abs(charges):.2f}")
            print()
            print("   Payment methods politely accepted:")
            print("   • None")
            print("   • Void")
            print("   • Imaginary currency")
            print("   • Your firstborn (terms and conditions apply)")
            print("   • Politeness points (non-refundable)")
            print()

    def spaghetti_daddy_please_loop(self):
        """SPAGHETTI_DADDY_PLEASE_LOOP - Main loop structure"""
        try:
            while self.running:
                self.sauce_stirs += 1  # SPAGHETTI_DADDY_PLEASE_STIR

                self.spaghetti_daddy_please_clear_screen()
                self.spaghetti_daddy_please_display_header()
                self.spaghetti_daddy_please_show_warning()
                self.spaghetti_daddy_please_show_time()
                self.spaghetti_daddy_please_show_stats()

                # SPAGHETTI_DADDY_PLEASE_IF_SAUCE_READY
                if self.spaghetti_daddy_please_get_cook_time() <= 0:
                    self.spaghetti_daddy_please_show_payment()

                self.spaghetti_daddy_please_show_legal()

                # Update politeness level (decreases if running too long)
                if self.sauce_stirs > 100:
                    self.politeness_level = max(0, 100 - (self.sauce_stirs - 100) // 10)

                print("Press Ctrl+C to stop (SORRY FOR BOTHERING YOU DADDY)")
                print("=" * 75)

                time.sleep(1)  # SPAGHETTI_DADDY_PLEASE_WAIT

        except KeyboardInterrupt:
            self.running = False
            self.spaghetti_daddy_please_clear_screen()

            # Sad Spaghetti Daddy
            print("\n" + "="*75)
            print(r"""
       ~~~ ~~~  ~~~ ~~~
      ~~~  ~~  ~~  ~~~
        \  ||  ||  /
         \ || || /
          \|||||/
        ___\|||/___
       |  DADDY!!  |
       | ( ; ω ; )|  <-- SAD!
        \  \|||/  /
         |  |||  |
        /|  |||  |\
    """)
            print(" " * 12 + "🍝 UNAUTHORIZED SPAGHETTI EXIT 🍝")
            print("="*75)
            print("\nSORRY_FOR_BOTHERING_YOU_DADDY:")
            print("You have violated Spaghetti Article I by exiting without permission.")
            print("This constitutes unauthorized termination of polite compilation.")
            print("(Spaghetti Daddy is disappointed but still loves you)")

            final_charges = self.spaghetti_daddy_please_calculate_charges()
            print(f"\n💵 Final spaghetti bill (apologies): ${abs(final_charges):.2f}")
            print(f"🍝 Total noodles served (thank you): {self.noodles_served}")
            print(f"🥄 Total sauce stirs (much appreciated): {self.sauce_stirs}")
            print(f"💖 Final politeness level: {self.politeness_level}%")

            if self.politeness_level > 70:
                print("\n✨ SPAGHETTI DADDY SAYS: 'Good job being polite! Come back anytime!'")
            elif self.politeness_level > 30:
                print("\n😊 SPAGHETTI DADDY SAYS: 'Thank you for your politeness!'")
            else:
                print("\n😢 SPAGHETTI DADDY SAYS: 'Please be more polite next time...'")

            print("\nYour polite violation has been logged.")
            print("(Not really. We don't track anything. But Spaghetti Daddy noticed.)")
            print("\nTHANK_YOU_SPAGHETTI_DADDY")
            print("Please report to 404 Noodle Lane for more pasta.")
            print("="*75 + "\n")

def spaghetti_daddy_please_start():
    """SPAGHETTI_DADDY_PLEASE_START - Program entry point"""
    print("🍝 SPAGHETTI_DADDY_PLEASE_START compilation...")
    print("🍝 SPAGHETTI_DADDY_PLEASE_LOAD politeness module...")
    print("🍝 SPAGHETTI_DADDY_PLEASE_INITIALIZE noodle structures...")
    print("🍝 SPAGHETTI_DADDY_PLEASE_PREPARE marinara sauce...")
    print("🍝 SPAGHETTI_DADDY_PLEASE_BOIL water...")
    print("🍝 SPAGHETTI_DADDY_PLEASE_HEAT pan...")
    print("🍝 THANK_YOU_SPAGHETTI_DADDY!")
    time.sleep(2)  # Polite pause

    interpreter = SpaghettiDaddyInterpreter()
    interpreter.spaghetti_daddy_please_loop()

# SPAGHETTI_DADDY_PLEASE_END
if __name__ == "__main__":
    spaghetti_daddy_please_start()
    # THANK_YOU_SPAGHETTI_DADDY
