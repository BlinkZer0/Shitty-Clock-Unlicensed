#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║         🍔🍔 DOUBLECHEESEBURGER SIMPLE GRAPHICS DEMO 🍔🍔                  ║
║                                                                           ║
║  Demonstrates basic DoubleCheeseBurger operations:                       ║
║  - Drawing pixels and shapes                                             ║
║  - Using the stack for calculations                                      ║
║  - Basic animation concepts                                              ║
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

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from double_cheeseburger import (
    DoubleCheeseburgerVM,
    push, pop, add, sub, mul, div,
    grill, spatula, receipt, microwave
)

def draw_box_program():
    """Draw a box using DoubleCheeseBurger instructions"""
    program = []

    # Draw a box from (10,10) to (30,20)
    box_x1, box_y1 = 10, 5
    box_x2, box_y2 = 50, 15
    color = 14  # Yellow

    # Top and bottom edges
    for x in range(box_x1, box_x2 + 1):
        program.append(grill(x, box_y1, color))
        program.append(grill(x, box_y2, color))

    # Left and right edges
    for y in range(box_y1, box_y2 + 1):
        program.append(grill(box_x1, y, color))
        program.append(grill(box_x2, y, color))

    program.append(spatula())
    return program


def draw_pattern_program():
    """Draw an interesting pattern"""
    program = []

    # Checkerboard pattern
    for y in range(25):
        for x in range(80):
            if (x // 4 + y // 2) % 2 == 0:
                color = 12  # Light red
            else:
                color = 9   # Light blue
            program.append(grill(x, y, color))

    program.append(spatula())
    return program


def draw_gradient_program():
    """Draw a gradient from left to right"""
    program = []

    width = 80
    height = 25

    for y in range(height):
        for x in range(width):
            # Calculate color based on x position
            # Use grayscale palette (16-231)
            color = 16 + int((x / width) * 100)
            color = min(color, 231)
            program.append(grill(x, y, color))

    program.append(spatula())
    return program


def stack_demo_program():
    """Demonstrate stack operations"""
    program = []

    # Calculate: (5 + 3) * 2 - 1
    # Expected result: (8) * 2 - 1 = 16 - 1 = 15

    program.append(push(5))      # Stack: [5]
    program.append(push(3))      # Stack: [5, 3]
    program.append(add())        # Stack: [8]
    program.append(push(2))      # Stack: [8, 2]
    program.append(mul())        # Stack: [16]
    program.append(push(1))      # Stack: [16, 1]
    program.append(sub())        # Stack: [15]
    program.append(receipt())    # Print and pop: 15

    return program


def render_to_terminal(vm):
    """Render framebuffer as ASCII art"""
    chars = ' .:-=+*#%@'

    for y in range(vm.screen_height):
        row = []
        for x in range(vm.screen_width):
            idx = y * vm.screen_width + x
            color = vm.framebuffer[idx]
            r, g, b = vm.palette[color]
            brightness = (r + g + b) // 3
            char_idx = min(brightness * len(chars) // 256, len(chars) - 1)
            row.append(chars[char_idx])
        print(''.join(row))


if __name__ == "__main__":
    print("="*80)
    print("🍔🍔 DOUBLECHEESEBURGER GRAPHICS DEMOS 🍔🍔")
    print("="*80)
    print()

    # Demo 1: Stack arithmetic
    print("DEMO 1: Stack Arithmetic")
    print("Calculating: (5 + 3) * 2 - 1")
    print()
    vm1 = DoubleCheeseburgerVM(80, 25)
    vm1.run(stack_demo_program())
    print()
    print("-" * 80)
    print()

    # Demo 2: Draw a box
    print("DEMO 2: Drawing a Box")
    print()
    vm2 = DoubleCheeseburgerVM(80, 25)
    vm2.run(draw_box_program())
    render_to_terminal(vm2)
    print("-" * 80)
    print()

    # Demo 3: Checkerboard pattern
    print("DEMO 3: Checkerboard Pattern")
    print()
    vm3 = DoubleCheeseburgerVM(80, 25)
    vm3.run(draw_pattern_program())
    render_to_terminal(vm3)
    print("-" * 80)
    print()

    # Demo 4: Gradient
    print("DEMO 4: Horizontal Gradient")
    print()
    vm4 = DoubleCheeseburgerVM(80, 25)
    vm4.run(draw_gradient_program())
    render_to_terminal(vm4)
    print("-" * 80)
    print()

    print("✨ All demos completed successfully! ✨")
    print("🍔 DoubleCheeseBurger is ready for game development!")
    print()
    print("Next steps:")
    print("  • Run the raycaster demo: python examples/raycaster.py")
    print("  • Start building your own games!")
    print("  • Port Doom! 🎮")
    print()
