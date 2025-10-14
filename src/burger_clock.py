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

CHEESEBURGER CLOCK LANGUAGE SPECIFICATION:
==========================================

A fully functional esoteric programming language based on cheeseburgers.

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
        print("   This burger software is licensed under OPL-∞")
        print("   📧 Contact: no-burgers@forbidden-food.void")
        print("   📞 Phone: 1-800-BUR-GERS")
        print("   📍 Address: 404 Sesame Seed Street, Burger Island")
        print("   🕐 Office Hours: When the grill is cold (never)")
        print()
        print("   © 2025 UNLICENSED Burger Software")
        print("   All toppings, condiments, and secret sauces reserved.")
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
            print("   • Burger tokens")
            print("   • Cheese coins")
            print("   • Bacon bucks")
            print("   • Your secret sauce recipe")
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
