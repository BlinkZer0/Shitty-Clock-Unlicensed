#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║           🍝 FIBONACCI IN SPAGHETTI DADDY PLEASE LANGUAGE 🍝              ║
║                                                                           ║
║  This program demonstrates Turing-completeness by computing the          ║
║  Fibonacci sequence using variables, loops, and conditionals!            ║
║                                                                           ║
║  Licensed under the Overprotective License (OPL-∞)                       ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from spaghetti_clock import SpaghettiDaddyInterpreter

def spaghetti_daddy_please_fibonacci_demo():
    """
    SPAGHETTI_DADDY_PLEASE_START - Fibonacci Sequence Demo

    This polite program computes the first 10 Fibonacci numbers!
    """

    print("="*75)
    print("🍝 SPAGHETTI_DADDY_PLEASE_START FIBONACCI COMPUTATION")
    print("="*75)
    print()
    print("Computing Fibonacci sequence with maximum politeness...")
    print()

    # Create our polite interpreter
    daddy = SpaghettiDaddyInterpreter()

    # SPAGHETTI_DADDY_PLEASE_STORE_NOODLE - Initialize variables
    daddy.spaghetti_daddy_please_store_noodle("previous", 0)
    daddy.spaghetti_daddy_please_store_noodle("current", 1)
    daddy.spaghetti_daddy_please_store_noodle("counter", 0)
    daddy.spaghetti_daddy_please_store_noodle("limit", 10)

    print("🍝 Initial noodle variables:")
    print(f"   previous = {daddy.spaghetti_daddy_please_get_noodle('previous')}")
    print(f"   current = {daddy.spaghetti_daddy_please_get_noodle('current')}")
    print(f"   counter = {daddy.spaghetti_daddy_please_get_noodle('counter')}")
    print(f"   limit = {daddy.spaghetti_daddy_please_get_noodle('limit')}")
    print()
    print("🍝 Fibonacci noodles (THANK_YOU_SPAGHETTI_DADDY):")
    print()

    # SPAGHETTI_DADDY_PLEASE_OUTPUT_NOODLE - Print first number
    daddy.spaghetti_daddy_please_output_noodle("previous")

    # SPAGHETTI_DADDY_PLEASE_BOIL_NOODLES - Loop to compute Fibonacci
    def condition():
        # SPAGHETTI_DADDY_PLEASE_COMPARE_NOODLES
        return daddy.spaghetti_daddy_please_compare_noodles("counter", "LESS", "limit")

    def body():
        # SPAGHETTI_DADDY_PLEASE_OUTPUT_NOODLE - Print current value
        daddy.spaghetti_daddy_please_output_noodle("current")

        # SPAGHETTI_DADDY_PLEASE_ADD_SAUCE - Calculate next Fibonacci number
        next_value = daddy.spaghetti_daddy_please_add_sauce("previous", "current")

        # SPAGHETTI_DADDY_PLEASE_STORE_NOODLE - Update variables
        daddy.spaghetti_daddy_please_store_noodle("previous", daddy.spaghetti_daddy_please_get_noodle("current"))
        daddy.spaghetti_daddy_please_store_noodle("current", next_value)

        # SPAGHETTI_DADDY_PLEASE_ADD_SAUCE - Increment counter
        new_counter = daddy.spaghetti_daddy_please_add_sauce("counter", 1)
        daddy.spaghetti_daddy_please_store_noodle("counter", new_counter)

    # SPAGHETTI_DADDY_PLEASE_BOIL_NOODLES - Execute the loop!
    daddy.spaghetti_daddy_please_boil_noodles(condition, body)

    print()
    print("="*75)
    print("🍝 SPAGHETTI_DADDY_PLEASE_END")
    print("THANK_YOU_SPAGHETTI_DADDY for the delicious Fibonacci noodles!")
    print(f"💖 Politeness level maintained: {daddy.politeness_level}%")
    print("="*75)
    print()
    print("✨ This proves Spaghetti Daddy Please is TURING-COMPLETE! ✨")
    print("   (With maximum politeness, of course)")
    print()

if __name__ == "__main__":
    # SPAGHETTI_DADDY_PLEASE_START
    spaghetti_daddy_please_fibonacci_demo()
    # THANK_YOU_SPAGHETTI_DADDY
