#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║              🍝🍔 EXOTIC FEATURES SHOWCASE 🍔🍝                            ║
║                                                                           ║
║  Demonstrating advanced array, string, math, and bitwise operations      ║
║  in both Spaghetti Daddy Please and CheeseBurger languages!              ║
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
from spaghetti_clock import SpaghettiDaddyInterpreter
from burger_clock import BurgerClockInterpreter

def spaghetti_array_demo():
    """Demonstrate array operations in Spaghetti Daddy Please"""
    print("="*75)
    print("🍝 SPAGHETTI DADDY PLEASE: NOODLE BOWL OPERATIONS")
    print("="*75)
    print()

    daddy = SpaghettiDaddyInterpreter()

    # Create a noodle bowl (array)
    print("📦 SPAGHETTI_DADDY_PLEASE_PREPARE_NOODLE_BOWL:")
    daddy.spaghetti_daddy_please_prepare_noodle_bowl("numbers", [3, 1, 4, 1, 5, 9, 2, 6])
    print(f"   Initial bowl: {daddy.spaghetti_daddy_please_get_noodle('numbers')}")
    print()

    # Array operations
    print("🔢 Array operations:")
    print(f"   Length: {daddy.spaghetti_daddy_please_count_noodles_in_bowl('numbers')}")
    print(f"   Max value: {daddy.spaghetti_daddy_please_max_noodle_bowl('numbers')}")
    print(f"   Min value: {daddy.spaghetti_daddy_please_min_noodle_bowl('numbers')}")
    print(f"   Sum: {daddy.spaghetti_daddy_please_sum_noodle_bowl('numbers')}")
    print()

    # Sort the bowl
    print("📊 SPAGHETTI_DADDY_PLEASE_SORT_NOODLE_BOWL:")
    daddy.spaghetti_daddy_please_sort_noodle_bowl('numbers')
    print(f"   Sorted bowl: {daddy.spaghetti_daddy_please_get_noodle('numbers')}")
    print()

    # Reverse it
    print("🔄 SPAGHETTI_DADDY_PLEASE_REVERSE_NOODLE_BOWL:")
    daddy.spaghetti_daddy_please_reverse_noodle_bowl('numbers')
    print(f"   Reversed bowl: {daddy.spaghetti_daddy_please_get_noodle('numbers')}")
    print()

    # Slicing
    print("✂️ SPAGHETTI_DADDY_PLEASE_SLICE_NOODLE_BOWL:")
    slice_result = daddy.spaghetti_daddy_please_slice_noodle_bowl('numbers', 2, 5)
    print(f"   Slice [2:5]: {slice_result}")
    print()

    # Find element
    print("🔍 SPAGHETTI_DADDY_PLEASE_FIND_IN_BOWL:")
    index = daddy.spaghetti_daddy_please_find_in_bowl('numbers', 5)
    print(f"   Index of 5: {index}")
    print()

def spaghetti_math_demo():
    """Demonstrate math operations in Spaghetti Daddy Please"""
    print("="*75)
    print("🍝 SPAGHETTI DADDY PLEASE: ADVANCED MATH OPERATIONS")
    print("="*75)
    print()

    daddy = SpaghettiDaddyInterpreter()

    # Power operation
    print("💪 SPAGHETTI_DADDY_PLEASE_AL_DENTE_POWER (cooked to perfection):")
    daddy.spaghetti_daddy_please_store_noodle("base", 2)
    daddy.spaghetti_daddy_please_store_noodle("exponent", 10)
    result = daddy.spaghetti_daddy_please_al_dente_power("base", "exponent")
    print(f"   2^10 = {result}")
    print()

    # Square root
    print("🌱 SPAGHETTI_DADDY_PLEASE_MEASURE_NOODLE_ROOT:")
    daddy.spaghetti_daddy_please_store_noodle("number", 144)
    root = daddy.spaghetti_daddy_please_measure_noodle_root("number")
    print(f"   √144 = {root}")
    print()

    # Absolute value
    print("💯 SPAGHETTI_DADDY_PLEASE_ABSOLUTE_NOODLE:")
    daddy.spaghetti_daddy_please_store_noodle("negative", -42)
    absolute = daddy.spaghetti_daddy_please_absolute_noodle("negative")
    print(f"   |-42| = {absolute}")
    print()

    # Prime check
    print("⭐ SPAGHETTI_DADDY_PLEASE_IS_PRIME_NOODLE:")
    primes = []
    for i in range(2, 20):
        if daddy.spaghetti_daddy_please_is_prime_noodle(i):
            primes.append(i)
    print(f"   Primes from 2-20: {primes}")
    print()

    # Random number
    print("🎲 SPAGHETTI_DADDY_PLEASE_RANDOM_NOODLE_RANGE:")
    random_nums = [daddy.spaghetti_daddy_please_random_noodle_range(1, 100) for _ in range(5)]
    print(f"   5 random numbers (1-100): {random_nums}")
    print()

def spaghetti_string_demo():
    """Demonstrate string operations in Spaghetti Daddy Please"""
    print("="*75)
    print("🍝 SPAGHETTI DADDY PLEASE: STRING NOODLE OPERATIONS")
    print("="*75)
    print()

    daddy = SpaghettiDaddyInterpreter()

    # String length
    print("📏 SPAGHETTI_DADDY_PLEASE_MEASURE_NOODLE_LENGTH:")
    daddy.spaghetti_daddy_please_store_noodle("greeting", "Hello Spaghetti Daddy!")
    length = daddy.spaghetti_daddy_please_measure_noodle_length("greeting")
    print(f"   Length of 'Hello Spaghetti Daddy!': {length}")
    print()

    # String slicing
    print("✂️ SPAGHETTI_DADDY_PLEASE_CUT_NOODLE:")
    slice_text = daddy.spaghetti_daddy_please_cut_noodle("Hello Spaghetti Daddy!", 0, 5)
    print(f"   Slice [0:5]: '{slice_text}'")
    print()

    # String concatenation
    print("🌀 SPAGHETTI_DADDY_PLEASE_TWIRL_NOODLES:")
    combined = daddy.spaghetti_daddy_please_twirl_noodles(["Thank", " ", "You", " ", "Daddy"])
    print(f"   Twirled noodles: '{combined}'")
    print()

def spaghetti_bitwise_demo():
    """Demonstrate bitwise operations in Spaghetti Daddy Please"""
    print("="*75)
    print("🍝 SPAGHETTI DADDY PLEASE: BITWISE NOODLE OPERATIONS")
    print("="*75)
    print()

    daddy = SpaghettiDaddyInterpreter()

    daddy.spaghetti_daddy_please_store_noodle("a", 12)  # 1100 in binary
    daddy.spaghetti_daddy_please_store_noodle("b", 10)  # 1010 in binary

    print(f"   a = 12 (binary: 1100)")
    print(f"   b = 10 (binary: 1010)")
    print()

    # Bitwise AND
    and_result = daddy.spaghetti_daddy_please_bitwise_noodle_and("a", "b")
    print(f"   AND: {and_result} (binary: {bin(and_result)})")

    # Bitwise OR
    or_result = daddy.spaghetti_daddy_please_bitwise_noodle_or("a", "b")
    print(f"   OR:  {or_result} (binary: {bin(or_result)})")

    # Bitwise XOR
    xor_result = daddy.spaghetti_daddy_please_bitwise_noodle_xor("a", "b")
    print(f"   XOR: {xor_result} (binary: {bin(xor_result)})")
    print()

    # Bit shifts
    print("   Bit shifting:")
    left_shift = daddy.spaghetti_daddy_please_shift_noodle_left(5, 2)  # 5 << 2 = 20
    print(f"   5 << 2 = {left_shift}")

    right_shift = daddy.spaghetti_daddy_please_shift_noodle_right(20, 2)  # 20 >> 2 = 5
    print(f"   20 >> 2 = {right_shift}")
    print()

def burger_array_demo():
    """Demonstrate array operations in CheeseBurger"""
    print("="*75)
    print("🍔 CHEESEBURGER: COMBO MEAL OPERATIONS")
    print("="*75)
    print()

    burger = BurgerClockInterpreter()

    # Create a combo meal (array)
    print("🍟 PREPARE_COMBO_MEAL:")
    burger.prepare_combo_meal("prices", [5, 12, 8, 3, 15, 6, 20, 9])
    print(f"   Initial combo: {burger.get_ingredient('prices')}")
    print()

    # Array operations
    print("🔢 Combo operations:")
    print(f"   Items in combo: {burger.count_combo_items('prices')}")
    print(f"   Most expensive: ${burger.max_combo_item('prices')}")
    print(f"   Cheapest: ${burger.min_combo_item('prices')}")
    print(f"   Total value: ${burger.total_combo_value('prices')}")
    print()

    # Sort the combo
    print("📊 ORGANIZE_COMBO:")
    burger.organize_combo('prices')
    print(f"   Sorted combo: {burger.get_ingredient('prices')}")
    print()

    # Add items
    print("➕ ADD_TO_COMBO:")
    burger.add_to_combo('prices', 25)
    burger.add_to_combo('prices', 7)
    print(f"   After adding items: {burger.get_ingredient('prices')}")
    print()

    # Slice
    print("🔪 SLICE_COMBO:")
    slice_result = burger.slice_combo('prices', 3, 7)
    print(f"   Slice [3:7]: {slice_result}")
    print()

def burger_math_demo():
    """Demonstrate math operations in CheeseBurger"""
    print("="*75)
    print("🍔 CHEESEBURGER: ADVANCED BURGER MATH")
    print("="*75)
    print()

    burger = BurgerClockInterpreter()

    # Power operation
    print("💪 SUPER_SIZE_POWER:")
    result = burger.super_size_power(3, 4)
    print(f"   3^4 = {result} (super-sized!)")
    print()

    # Square root
    print("🌱 BURGER_ROOT:")
    root = burger.burger_root(256)
    print(f"   √256 = {root}")
    print()

    # Absolute value
    print("💯 ABSOLUTE_BURGER:")
    absolute = burger.absolute_burger(-100)
    print(f"   |-100| = {absolute}")
    print()

    # Prime check
    print("⭐ IS_PRIME_BURGER:")
    burger.cheese_slice("test", 17)
    is_prime = burger.is_prime_burger("test")
    print(f"   Is 17 prime? {is_prime}")
    print()

    # Random burgers
    print("🎲 RANDOM_BURGER_RANGE:")
    random_burgers = [burger.random_burger_range(1, 50) for _ in range(5)]
    print(f"   5 random burgers (1-50): {random_burgers}")
    print()

def burger_advanced_demo():
    """Demonstrate advanced burger features"""
    print("="*75)
    print("🍔 CHEESEBURGER: ADVANCED BURGER ASSEMBLY")
    print("="*75)
    print()

    burger = BurgerClockInterpreter()

    # Create a combo and find the median
    print("🎯 Finding median burger price:")
    burger.prepare_combo_meal("menu", [12, 8, 15, 6, 20, 9, 14, 11, 7])
    burger.organize_combo('menu')
    menu = burger.get_ingredient('menu')
    median_index = burger.count_combo_items('menu') // 2
    median = burger.take_from_combo('menu', median_index)
    print(f"   Sorted menu: {menu}")
    print(f"   Median price: ${median}")
    print()

    # Swap ingredients
    print("🔀 SWAP_INGREDIENTS:")
    burger.cheese_slice("burger1", 10)
    burger.cheese_slice("burger2", 20)
    print(f"   Before: burger1={burger.get_ingredient('burger1')}, burger2={burger.get_ingredient('burger2')}")
    burger.swap_ingredients("burger1", "burger2")
    print(f"   After:  burger1={burger.get_ingredient('burger1')}, burger2={burger.get_ingredient('burger2')}")
    print()

    # Bitwise operations for secret sauce recipe
    print("🔗 Bitwise operations (secret sauce encoding):")
    burger.cheese_slice("ingredient_a", 42)
    burger.cheese_slice("ingredient_b", 27)

    and_result = burger.bitwise_burger_and("ingredient_a", "ingredient_b")
    or_result = burger.bitwise_burger_or("ingredient_a", "ingredient_b")
    xor_result = burger.bitwise_burger_xor("ingredient_a", "ingredient_b")

    print(f"   42 & 27 = {and_result}")
    print(f"   42 | 27 = {or_result}")
    print(f"   42 ^ 27 = {xor_result}")
    print()

def sorting_algorithm_demo():
    """Implement bubble sort in both languages!"""
    print("="*75)
    print("🍝🍔 BUBBLE SORT IMPLEMENTATION")
    print("="*75)
    print()

    # Spaghetti version
    print("🍝 Spaghetti Daddy Please Bubble Sort:")
    daddy = SpaghettiDaddyInterpreter()
    daddy.spaghetti_daddy_please_prepare_noodle_bowl("unsorted", [64, 34, 25, 12, 22, 11, 90])
    print(f"   Before: {daddy.spaghetti_daddy_please_get_noodle('unsorted')}")

    n = daddy.spaghetti_daddy_please_count_noodles_in_bowl("unsorted")
    for i in range(n):
        for j in range(0, n - i - 1):
            val_j = daddy.spaghetti_daddy_please_take_from_bowl("unsorted", j)
            val_j1 = daddy.spaghetti_daddy_please_take_from_bowl("unsorted", j + 1)
            if val_j > val_j1:
                # Swap
                arr = daddy.spaghetti_daddy_please_get_noodle("unsorted")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print(f"   After:  {daddy.spaghetti_daddy_please_get_noodle('unsorted')}")
    print()

    # Burger version
    print("🍔 CheeseBurger Bubble Sort:")
    burger = BurgerClockInterpreter()
    burger.prepare_combo_meal("unsorted_burgers", [64, 34, 25, 12, 22, 11, 90])
    print(f"   Before: {burger.get_ingredient('unsorted_burgers')}")

    n = burger.count_combo_items("unsorted_burgers")
    for i in range(n):
        for j in range(0, n - i - 1):
            val_j = burger.take_from_combo("unsorted_burgers", j)
            val_j1 = burger.take_from_combo("unsorted_burgers", j + 1)
            if val_j > val_j1:
                # Swap
                arr = burger.get_ingredient("unsorted_burgers")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print(f"   After:  {burger.get_ingredient('unsorted_burgers')}")
    print()

def main():
    """Run all demos"""
    print("\n")
    print("╔═══════════════════════════════════════════════════════════════════════╗")
    print("║                                                                       ║")
    print("║              🍝🍔 EXOTIC FEATURES DEMONSTRATION 🍔🍝                   ║")
    print("║                                                                       ║")
    print("║  Showcasing arrays, strings, math, bitwise ops, and algorithms!      ║")
    print("║                                                                       ║")
    print("╚═══════════════════════════════════════════════════════════════════════╝")
    print("\n")

    # Spaghetti Daddy Please demos
    spaghetti_array_demo()
    spaghetti_math_demo()
    spaghetti_string_demo()
    spaghetti_bitwise_demo()

    # CheeseBurger demos
    burger_array_demo()
    burger_math_demo()
    burger_advanced_demo()

    # Algorithm demo
    sorting_algorithm_demo()

    print("="*75)
    print("✨ DEMONSTRATION COMPLETE!")
    print("="*75)
    print()
    print("Both languages now support:")
    print("  ✅ Arrays/Lists with full manipulation")
    print("  ✅ String operations")
    print("  ✅ Advanced math (power, sqrt, abs, prime checking)")
    print("  ✅ Bitwise operations (AND, OR, XOR, shifts)")
    print("  ✅ Sorting and searching algorithms")
    print("  ✅ Random number generation")
    print("  ✅ Variable swapping")
    print()
    print("These languages are now INCREDIBLY ROBUST while maintaining")
    print("their absurdist polite/burger themes! 🎉")
    print()
    print("THANK_YOU_SPAGHETTI_DADDY 🍝")
    print("🍔 BOTTOM_BUN 🍔")
    print()

if __name__ == "__main__":
    main()
