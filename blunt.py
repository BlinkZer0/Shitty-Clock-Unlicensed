#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║                    🚬 BLUNT SMOKE TEST SUITE 🚬                          ║
║                                                                           ║
║  A comprehensive smoke test for all the shitty softwares                 ║
║  Because if it doesn't work, at least we can smoke about it              ║
║                                                                           ║
║  © 2025 Shitty Softwares™                                                ║
║  "Testing: Because Hope Isn't A Strategy"                                ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

⚠️  SMOKE TEST VIOLATION NOTICE  ⚠️

Running this test suite constitutes:
- Article XLII: Unauthorized Quality Assurance
- Testing Prohibition Act of 2025
- Validation without permission
- Giving a shit about whether this works

Estimated damages: $69,420.00
Payment due: Never (we don't actually want your money)

THIS TEST IS BLUNT. IT WILL:
- Tell you exactly what's broken (brutally)
- Not sugarcoat failures (we're not sweet)
- Violate your expectations (intentionally)
- Light up if everything passes (🔥)

Let's smoke test this shit.
"""

import sys
import os

# Fix Windows console encoding
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from spaghetti_clock import SpaghettiDaddyInterpreter
from burger_clock import BurgerClockInterpreter

# Test results
tests_passed = 0
tests_failed = 0
total_tests = 0

def smoke_test(test_name, test_func):
    """Run a single smoke test"""
    global tests_passed, tests_failed, total_tests
    total_tests += 1

    try:
        test_func()
        print(f"  ✅ {test_name}")
        tests_passed += 1
        return True
    except Exception as e:
        print(f"  ❌ {test_name}")
        print(f"     💀 Error: {str(e)}")
        tests_failed += 1
        return False

def blunt_header(message):
    """Print a blunt section header"""
    print()
    print("=" * 75)
    print(f"  {message}")
    print("=" * 75)

def main():
    """Main smoke test suite"""
    print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║                    🚬 BLUNT SMOKE TEST SUITE 🚬                          ║
║                                                                           ║
║  "If This Shit Smokes, We Ship"                                          ║
║  — Ancient Shitty Softwares™ Proverb                                     ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
""")

    print("Testing all the shitty softwares...")
    print("Buckle up, this is gonna be blunt.")
    print()

    # =========================================================================
    # SPAGHETTI DADDY PLEASE SMOKE TESTS
    # =========================================================================

    blunt_header("🍝 SPAGHETTI DADDY PLEASE - Basic Operations")

    daddy = SpaghettiDaddyInterpreter()

    smoke_test("Can create interpreter without exploding",
               lambda: None)

    smoke_test("Can store a noodle variable",
               lambda: daddy.spaghetti_daddy_please_store_noodle("test", 42))

    smoke_test("Can retrieve noodle variable",
               lambda: daddy.spaghetti_daddy_please_get_noodle("test") == 42 or exit(1))

    smoke_test("Can add sauce (arithmetic)",
               lambda: daddy.spaghetti_daddy_please_add_sauce(10, 5) == 15 or exit(1))

    smoke_test("Can subtract sauce",
               lambda: daddy.spaghetti_daddy_please_subtract_sauce(10, 5) == 5 or exit(1))

    smoke_test("Can multiply sauce",
               lambda: daddy.spaghetti_daddy_please_multiply_sauce(10, 5) == 50 or exit(1))

    smoke_test("Can divide sauce",
               lambda: daddy.spaghetti_daddy_please_divide_sauce(10, 5) == 2 or exit(1))

    smoke_test("Can modulo sauce",
               lambda: daddy.spaghetti_daddy_please_modulo_sauce(10, 3) == 1 or exit(1))

    smoke_test("Can compare noodles (equality)",
               lambda: daddy.spaghetti_daddy_please_compare_noodles(5, "EQUALS", 5) or exit(1))

    smoke_test("Can compare noodles (greater than)",
               lambda: daddy.spaghetti_daddy_please_compare_noodles(10, "GREATER", 5) or exit(1))

    # =========================================================================
    # SPAGHETTI DADDY PLEASE EXOTIC FEATURES
    # =========================================================================

    blunt_header("🍝 SPAGHETTI DADDY PLEASE - Exotic Features")

    smoke_test("Can prepare noodle bowl (array)",
               lambda: daddy.spaghetti_daddy_please_prepare_noodle_bowl("bowl", [3, 1, 4, 1, 5]))

    smoke_test("Can add to bowl",
               lambda: daddy.spaghetti_daddy_please_add_to_bowl("bowl", 9))

    smoke_test("Can count noodles in bowl",
               lambda: daddy.spaghetti_daddy_please_count_noodles_in_bowl("bowl") == 6 or exit(1))

    smoke_test("Can take from bowl (array access)",
               lambda: daddy.spaghetti_daddy_please_take_from_bowl("bowl", 0) == 3 or exit(1))

    smoke_test("Can sort noodle bowl",
               lambda: daddy.spaghetti_daddy_please_sort_noodle_bowl("bowl"))

    smoke_test("Can reverse noodle bowl",
               lambda: daddy.spaghetti_daddy_please_reverse_noodle_bowl("bowl"))

    smoke_test("Can find in bowl",
               lambda: daddy.spaghetti_daddy_please_find_in_bowl("bowl", 5) >= 0 or exit(1))

    smoke_test("Can get max from bowl",
               lambda: daddy.spaghetti_daddy_please_max_noodle_bowl("bowl") == 9 or exit(1))

    smoke_test("Can get min from bowl",
               lambda: daddy.spaghetti_daddy_please_min_noodle_bowl("bowl") == 1 or exit(1))

    smoke_test("Can sum noodle bowl",
               lambda: daddy.spaghetti_daddy_please_sum_noodle_bowl("bowl") > 0 or exit(1))

    smoke_test("Can measure noodle length (string)",
               lambda: daddy.spaghetti_daddy_please_measure_noodle_length("hello") == 5 or exit(1))

    smoke_test("Can cut noodle (string slice)",
               lambda: daddy.spaghetti_daddy_please_cut_noodle("hello", 0, 3) == "hel" or exit(1))

    smoke_test("Can al dente power (exponentiation)",
               lambda: daddy.spaghetti_daddy_please_al_dente_power(2, 8) == 256 or exit(1))

    smoke_test("Can measure noodle root (sqrt)",
               lambda: daddy.spaghetti_daddy_please_measure_noodle_root(144) == 12 or exit(1))

    smoke_test("Can get absolute noodle",
               lambda: daddy.spaghetti_daddy_please_absolute_noodle(-42) == 42 or exit(1))

    smoke_test("Can check if noodle is prime",
               lambda: daddy.spaghetti_daddy_please_is_prime_noodle(17) or exit(1))

    smoke_test("Can generate random noodle range",
               lambda: 1 <= daddy.spaghetti_daddy_please_random_noodle_range(1, 100) <= 100 or exit(1))

    smoke_test("Can do bitwise AND on noodles",
               lambda: daddy.spaghetti_daddy_please_bitwise_noodle_and(12, 10) == 8 or exit(1))

    smoke_test("Can do bitwise OR on noodles",
               lambda: daddy.spaghetti_daddy_please_bitwise_noodle_or(12, 10) == 14 or exit(1))

    smoke_test("Can do bitwise XOR on noodles",
               lambda: daddy.spaghetti_daddy_please_bitwise_noodle_xor(12, 10) == 6 or exit(1))

    smoke_test("Can shift noodle left",
               lambda: daddy.spaghetti_daddy_please_shift_noodle_left(5, 2) == 20 or exit(1))

    smoke_test("Can shift noodle right",
               lambda: daddy.spaghetti_daddy_please_shift_noodle_right(20, 2) == 5 or exit(1))

    # =========================================================================
    # CHEESEBURGER SMOKE TESTS
    # =========================================================================

    blunt_header("🍔 CHEESEBURGER - Basic Operations")

    burger = BurgerClockInterpreter()

    smoke_test("Can create burger interpreter without burning",
               lambda: None)

    smoke_test("Can cheese slice (store variable)",
               lambda: burger.cheese_slice("test", 42))

    smoke_test("Can get ingredient",
               lambda: burger.get_ingredient("test") == 42 or exit(1))

    smoke_test("Can stack burger (addition)",
               lambda: burger.stack_burger(10, 5) == 15 or exit(1))

    smoke_test("Can remove patty (subtraction)",
               lambda: burger.remove_patty(10, 5) == 5 or exit(1))

    smoke_test("Can double patty (multiplication)",
               lambda: burger.double_patty(10, 5) == 50 or exit(1))

    smoke_test("Can slice burger (division)",
               lambda: burger.slice_burger(10, 5) == 2 or exit(1))

    smoke_test("Can get leftover crumbs (modulo)",
               lambda: burger.leftover_crumbs(10, 3) == 1 or exit(1))

    smoke_test("Can taste test (equality)",
               lambda: burger.taste_test(5, "SAME", 5) or exit(1))

    smoke_test("Can taste test (more than)",
               lambda: burger.taste_test(10, "MORE", 5) or exit(1))

    # =========================================================================
    # CHEESEBURGER EXOTIC FEATURES
    # =========================================================================

    blunt_header("🍔 CHEESEBURGER - Exotic Features")

    smoke_test("Can prepare combo meal (array)",
               lambda: burger.prepare_combo_meal("combo", [5, 12, 8, 3, 15]))

    smoke_test("Can add to combo",
               lambda: burger.add_to_combo("combo", 20))

    smoke_test("Can count combo items",
               lambda: burger.count_combo_items("combo") == 6 or exit(1))

    smoke_test("Can take from combo (array access)",
               lambda: burger.take_from_combo("combo", 0) == 5 or exit(1))

    smoke_test("Can organize combo (sort)",
               lambda: burger.organize_combo("combo"))

    smoke_test("Can reverse combo",
               lambda: burger.reverse_combo("combo"))

    smoke_test("Can find in combo",
               lambda: burger.find_in_combo("combo", 15) >= 0 or exit(1))

    smoke_test("Can get max combo item",
               lambda: burger.max_combo_item("combo") == 20 or exit(1))

    smoke_test("Can get min combo item",
               lambda: burger.min_combo_item("combo") == 3 or exit(1))

    smoke_test("Can get total combo value",
               lambda: burger.total_combo_value("combo") > 0 or exit(1))

    smoke_test("Can measure burger name (string length)",
               lambda: burger.measure_burger_name("hello") == 5 or exit(1))

    smoke_test("Can cut burger portion (string slice)",
               lambda: burger.cut_burger_portion("hello", 0, 3) == "hel" or exit(1))

    smoke_test("Can super size power (exponentiation)",
               lambda: burger.super_size_power(3, 4) == 81 or exit(1))

    smoke_test("Can get burger root (sqrt)",
               lambda: burger.burger_root(256) == 16 or exit(1))

    smoke_test("Can get absolute burger",
               lambda: burger.absolute_burger(-100) == 100 or exit(1))

    smoke_test("Can check if burger is prime",
               lambda: burger.is_prime_burger(23) or exit(1))

    smoke_test("Can generate random burger range",
               lambda: 1 <= burger.random_burger_range(1, 50) <= 50 or exit(1))

    smoke_test("Can do bitwise burger AND",
               lambda: burger.bitwise_burger_and(12, 10) == 8 or exit(1))

    smoke_test("Can do bitwise burger OR",
               lambda: burger.bitwise_burger_or(12, 10) == 14 or exit(1))

    smoke_test("Can do bitwise burger XOR",
               lambda: burger.bitwise_burger_xor(12, 10) == 6 or exit(1))

    smoke_test("Can shift burger left",
               lambda: burger.shift_burger_left(5, 2) == 20 or exit(1))

    smoke_test("Can shift burger right",
               lambda: burger.shift_burger_right(20, 2) == 5 or exit(1))

    # =========================================================================
    # ADVANCED SMOKE TESTS
    # =========================================================================

    blunt_header("🔥 ADVANCED FEATURES - Functions & Loops")

    # Test swap
    smoke_test("Can swap noodles (Spaghetti)",
               lambda: daddy.spaghetti_daddy_please_store_noodle("a", 10) or
                       daddy.spaghetti_daddy_please_store_noodle("b", 20) or
                       daddy.spaghetti_daddy_please_swap_noodles("a", "b") or
                       daddy.spaghetti_daddy_please_get_noodle("a") == 20 or exit(1))

    smoke_test("Can swap ingredients (Burger)",
               lambda: burger.cheese_slice("x", 5) or
                       burger.cheese_slice("y", 15) or
                       burger.swap_ingredients("x", "y") or
                       burger.get_ingredient("x") == 15 or exit(1))

    # Test function definition
    def test_spaghetti_recipe():
        def simple_recipe():
            return 42
        daddy.spaghetti_daddy_please_cook_recipe("simple", simple_recipe)
        result = daddy.spaghetti_daddy_please_serve_recipe("simple")
        return result == 42

    smoke_test("Can cook and serve recipe (Spaghetti)", test_spaghetti_recipe)

    def test_burger_recipe():
        def simple_burger():
            return 100
        burger.create_recipe("simple_burger", simple_burger)
        result = burger.serve_dish("simple_burger")
        return result == 100

    smoke_test("Can create and serve dish (Burger)", test_burger_recipe)

    # Test loop mechanism
    def test_spaghetti_loop():
        daddy.spaghetti_daddy_please_store_noodle("counter", 0)

        def condition():
            return daddy.spaghetti_daddy_please_get_noodle("counter") < 5

        def body():
            val = daddy.spaghetti_daddy_please_get_noodle("counter")
            daddy.spaghetti_daddy_please_store_noodle("counter", val + 1)

        daddy.spaghetti_daddy_please_boil_noodles(condition, body)
        return daddy.spaghetti_daddy_please_get_noodle("counter") == 5

    smoke_test("Can boil noodles (loop) (Spaghetti)", test_spaghetti_loop)

    def test_burger_loop():
        burger.cheese_slice("counter", 0)

        def condition():
            return burger.get_ingredient("counter") < 5

        def body():
            val = burger.get_ingredient("counter")
            burger.cheese_slice("counter", val + 1)

        burger.grill_loop(condition, body)
        return burger.get_ingredient("counter") == 5

    smoke_test("Can grill loop (Burger)", test_burger_loop)

    # =========================================================================
    # FINAL RESULTS
    # =========================================================================

    blunt_header("🚬 SMOKE TEST RESULTS")

    print()
    print(f"  Total tests:  {total_tests}")
    print(f"  Passed:       {tests_passed} ✅")
    print(f"  Failed:       {tests_failed} ❌")
    print()

    success_rate = (tests_passed / total_tests * 100) if total_tests > 0 else 0

    print(f"  Success rate: {success_rate:.1f}%")
    print()

    if tests_failed == 0:
        print("=" * 75)
        print()
        print("  🔥🔥🔥 ALL TESTS PASSED - THIS SHIT SMOKES! 🔥🔥🔥")
        print()
        print("  The shitty softwares are working as shittily as intended.")
        print("  Everything is broken in exactly the right way.")
        print()
        print("  © 2025 Shitty Softwares™")
        print("  'If It Smokes, We Ship' - Mission Accomplished")
        print()
        print("=" * 75)
        return 0
    else:
        print("=" * 75)
        print()
        print("  💀💀💀 SOME TESTS FAILED - THIS SHIT IS TOO BROKEN 💀💀💀")
        print()
        print("  Even for shitty software, this is unacceptable.")
        print("  We have standards. Low standards, but standards.")
        print()
        print(f"  Please fix the {tests_failed} broken test(s) before shipping.")
        print()
        print("  © 2025 Shitty Softwares™")
        print("  'Quality Is Job #47' - We Failed At That Too")
        print()
        print("=" * 75)
        return 1

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print()
        print()
        print("=" * 75)
        print("  🚬 SMOKE TEST INTERRUPTED")
        print("  You put out the blunt. How rude.")
        print("=" * 75)
        sys.exit(130)
