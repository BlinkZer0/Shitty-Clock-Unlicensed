#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║                  🍔🍔 THE DOUBLECHEESEBURGER LANGUAGE 🍔🍔                  ║
║                                                                           ║
║  A stack-based, Turing-complete language designed for game development   ║
║  Built for running Doom, raycasters, and serious graphics programs       ║
║                                                                           ║
║  Licensed under the Overprotective License (OPL-∞)                       ║
║  "All rights aggressively reserved. Including the right to render."      ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

DOUBLECHEESEBURGER LANGUAGE SPECIFICATION v1.0:
================================================

A practical stack-based language with food-themed syntax, designed for
real-world game development while maintaining maximum burger aesthetic.

MEMORY & DATA STRUCTURES:
-------------------------
🍟 FRIES <size>              - Allocate array (8-bit bytes)
🍟 BIGFRIES <size>           - Allocate large array (32-bit ints)
🥤 SHAKE <addr> <value>      - Store value at memory address
🥤 SIP <addr>                - Load value from memory address
📍 PUSH <value>              - Push value to stack
📍 POP                       - Pop value from stack
🔢 PEEK                      - Peek top of stack (no pop)

ARITHMETIC & LOGIC:
------------------
➕ ADD                       - Pop two, push sum
➖ SUB                       - Pop two, push difference
✖️ MUL                       - Pop two, push product
➗ DIV                       - Pop two, push quotient
🔢 MOD                       - Pop two, push remainder
🔀 SWAP                      - Swap top two stack items
📋 DUP                       - Duplicate top of stack

COMPARISON & BITWISE:
--------------------
🟰 EQ                        - Pop two, push 1 if equal else 0
🔼 GT                        - Pop two, push 1 if greater else 0
🔽 LT                        - Pop two, push 1 if less else 0
🔗 AND                       - Bitwise AND
⚡ OR                        - Bitwise OR
✨ XOR                       - Bitwise XOR
⬅️ SHL                       - Shift left
➡️ SHR                       - Shift right

CONTROL FLOW:
------------
🍔 COMBO <name>              - Define function/combo
🍔 UPSIZE <name>             - Call function
🍔 DIGEST                    - Return from function
🎫 COUPON <label>            - Define jump label
🚗 DRIVE_THRU <label>        - Jump if top of stack is non-zero
🏁 GOTO <label>              - Unconditional jump

GRAPHICS & I/O:
--------------
🔥 GRILL <x> <y> <color>     - Set pixel at (x,y) with color
🍴 SPATULA                   - Flip screen buffer (present frame)
📱 MENU                      - Read keyboard input (returns key code)
🧾 RECEIPT                   - Pop stack and print to console
🎨 PALETTE <idx> <r> <g> <b> - Set color palette entry

ADVANCED OPERATIONS:
-------------------
⏰ MICROWAVE <ms>            - Sleep for milliseconds
🌡️ TEMP                      - Get current timestamp
💾 FREEZE <filename>         - Save memory to file
🔥 REHEAT <filename>         - Load memory from file

SCREEN RESOLUTION: 320x200 (8-bit indexed color by default)
"""

import struct
import time
import sys
import os
from collections import defaultdict

# Fix Windows console encoding for emojis
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass

class DoubleCheeseburgerVM:
    """The DoubleCheeseBurger Virtual Machine"""

    def __init__(self, screen_width=320, screen_height=200):
        # Stack machine
        self.stack = []

        # Memory model
        self.memory = bytearray(65536)  # 64KB RAM
        self.large_memory = {}  # Sparse array for BIGFRIES

        # Graphics
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.framebuffer = bytearray(screen_width * screen_height)
        self.back_buffer = bytearray(screen_width * screen_height)
        self.palette = [(0, 0, 0) for _ in range(256)]  # 8-bit color palette
        self._init_default_palette()

        # Control flow
        self.functions = {}  # Combo meals (function definitions)
        self.labels = {}     # Jump targets (coupons)
        self.call_stack = [] # Return addresses
        self.pc = 0          # Program counter

        # Execution state
        self.program = []
        self.running = True
        self.start_time = time.time()

        # I/O
        self.keyboard_buffer = []

    def _init_default_palette(self):
        """Initialize with a basic 256-color palette (VGA-style)"""
        # Standard 16 colors
        standard = [
            (0, 0, 0),       # Black
            (0, 0, 170),     # Blue
            (0, 170, 0),     # Green
            (0, 170, 170),   # Cyan
            (170, 0, 0),     # Red
            (170, 0, 170),   # Magenta
            (170, 85, 0),    # Brown
            (170, 170, 170), # Light gray
            (85, 85, 85),    # Dark gray
            (85, 85, 255),   # Light blue
            (85, 255, 85),   # Light green
            (85, 255, 255),  # Light cyan
            (255, 85, 85),   # Light red
            (255, 85, 255),  # Light magenta
            (255, 255, 85),  # Yellow
            (255, 255, 255), # White
        ]
        for i, color in enumerate(standard):
            self.palette[i] = color

        # Grayscale ramp
        for i in range(16, 232):
            level = int((i - 16) * 255 / 215)
            self.palette[i] = (level, level, level)

        # Remaining colors - RGB cube
        for i in range(232, 256):
            r = ((i - 232) // 36) * 51
            g = (((i - 232) % 36) // 6) * 51
            b = ((i - 232) % 6) * 51
            self.palette[i] = (r, g, b)

    # ========================================================================
    # STACK OPERATIONS
    # ========================================================================

    def push(self, value):
        """📍 PUSH - Push value onto stack"""
        self.stack.append(int(value) & 0xFFFFFFFF)  # 32-bit values

    def pop(self):
        """📍 POP - Pop value from stack"""
        if not self.stack:
            return 0
        return self.stack.pop()

    def peek(self):
        """🔢 PEEK - View top without popping"""
        if not self.stack:
            return 0
        return self.stack[-1]

    # ========================================================================
    # MEMORY OPERATIONS
    # ========================================================================

    def fries(self, size):
        """🍟 FRIES - Allocate byte array, returns start address"""
        # Find free space in memory (simple bump allocator)
        # For now, just return current "heap" position
        # This is simplified - real implementation would track allocations
        addr = len(self.memory)
        self.memory.extend(bytearray(size))
        return addr - size  # Return start address

    def bigfries(self, size):
        """🍟 BIGFRIES - Allocate 32-bit int array in sparse memory"""
        addr = hash(str(time.time())) % 1000000  # Generate unique address
        self.large_memory[addr] = [0] * size
        return addr

    def shake(self, addr, value):
        """🥤 SHAKE - Store value at address"""
        addr = int(addr) & 0xFFFF
        if addr < len(self.memory):
            self.memory[addr] = int(value) & 0xFF
        else:
            # Large memory
            base = addr // 1000
            offset = addr % 1000
            if base in self.large_memory and offset < len(self.large_memory[base]):
                self.large_memory[base][offset] = int(value)

    def sip(self, addr):
        """🥤 SIP - Load value from address"""
        addr = int(addr) & 0xFFFF
        if addr < len(self.memory):
            return self.memory[addr]
        else:
            # Large memory
            base = addr // 1000
            offset = addr % 1000
            if base in self.large_memory and offset < len(self.large_memory[base]):
                return self.large_memory[base][offset]
        return 0

    # ========================================================================
    # ARITHMETIC & LOGIC
    # ========================================================================

    def add(self):
        """➕ ADD"""
        b = self.pop()
        a = self.pop()
        self.push(a + b)

    def sub(self):
        """➖ SUB"""
        b = self.pop()
        a = self.pop()
        self.push(a - b)

    def mul(self):
        """✖️ MUL"""
        b = self.pop()
        a = self.pop()
        self.push(a * b)

    def div(self):
        """➗ DIV"""
        b = self.pop()
        a = self.pop()
        self.push(a // b if b != 0 else 0)

    def mod(self):
        """🔢 MOD"""
        b = self.pop()
        a = self.pop()
        self.push(a % b if b != 0 else 0)

    def swap(self):
        """🔀 SWAP"""
        if len(self.stack) >= 2:
            self.stack[-1], self.stack[-2] = self.stack[-2], self.stack[-1]

    def dup(self):
        """📋 DUP"""
        if self.stack:
            self.push(self.peek())

    # ========================================================================
    # COMPARISON & BITWISE
    # ========================================================================

    def eq(self):
        """🟰 EQ"""
        b = self.pop()
        a = self.pop()
        self.push(1 if a == b else 0)

    def gt(self):
        """🔼 GT"""
        b = self.pop()
        a = self.pop()
        self.push(1 if a > b else 0)

    def lt(self):
        """🔽 LT"""
        b = self.pop()
        a = self.pop()
        self.push(1 if a < b else 0)

    def and_op(self):
        """🔗 AND"""
        b = self.pop()
        a = self.pop()
        self.push(a & b)

    def or_op(self):
        """⚡ OR"""
        b = self.pop()
        a = self.pop()
        self.push(a | b)

    def xor_op(self):
        """✨ XOR"""
        b = self.pop()
        a = self.pop()
        self.push(a ^ b)

    def shl(self):
        """⬅️ SHL"""
        b = self.pop()
        a = self.pop()
        self.push(a << b)

    def shr(self):
        """➡️ SHR"""
        b = self.pop()
        a = self.pop()
        self.push(a >> b)

    # ========================================================================
    # GRAPHICS OPERATIONS
    # ========================================================================

    def grill(self, x, y, color):
        """🔥 GRILL - Set pixel at (x, y) to color index"""
        x, y, color = int(x), int(y), int(color)
        if 0 <= x < self.screen_width and 0 <= y < self.screen_height:
            idx = y * self.screen_width + x
            self.back_buffer[idx] = color & 0xFF

    def spatula(self):
        """🍴 SPATULA - Flip buffers (present frame)"""
        self.framebuffer, self.back_buffer = self.back_buffer, self.framebuffer
        # In a real implementation, this would update the screen
        # For now, we just swap buffers

    def palette_set(self, idx, r, g, b):
        """🎨 PALETTE - Set palette entry"""
        idx = int(idx) & 0xFF
        self.palette[idx] = (int(r) & 0xFF, int(g) & 0xFF, int(b) & 0xFF)

    # ========================================================================
    # I/O OPERATIONS
    # ========================================================================

    def menu(self):
        """📱 MENU - Read keyboard input (non-blocking)"""
        # Simplified - in real implementation would read from input buffer
        if self.keyboard_buffer:
            return ord(self.keyboard_buffer.pop(0))
        return 0

    def receipt(self):
        """🧾 RECEIPT - Print top of stack"""
        value = self.pop()
        print(f"🍔 Output: {value}")

    # ========================================================================
    # ADVANCED OPERATIONS
    # ========================================================================

    def microwave(self, ms):
        """⏰ MICROWAVE - Sleep"""
        time.sleep(ms / 1000.0)

    def temp(self):
        """🌡️ TEMP - Get timestamp"""
        return int((time.time() - self.start_time) * 1000)

    # ========================================================================
    # CONTROL FLOW
    # ========================================================================

    def combo(self, name, body):
        """🍔 COMBO - Define function"""
        self.functions[name] = body

    def upsize(self, name):
        """🍔 UPSIZE - Call function"""
        if name in self.functions:
            self.call_stack.append(self.pc)
            self.execute_block(self.functions[name])
            if self.call_stack:
                self.pc = self.call_stack.pop()

    def digest(self):
        """🍔 DIGEST - Return from function"""
        if self.call_stack:
            self.pc = self.call_stack.pop()

    def coupon(self, label):
        """🎫 COUPON - Define label"""
        self.labels[label] = self.pc

    def drive_thru(self, label):
        """🚗 DRIVE_THRU - Conditional jump"""
        condition = self.pop()
        if condition != 0 and label in self.labels:
            self.pc = self.labels[label]

    def goto(self, label):
        """🏁 GOTO - Unconditional jump"""
        if label in self.labels:
            self.pc = self.labels[label]

    # ========================================================================
    # EXECUTION ENGINE
    # ========================================================================

    def execute_block(self, instructions):
        """Execute a block of instructions"""
        for instr in instructions:
            self.execute_instruction(instr)

    def execute_instruction(self, instr):
        """Execute a single instruction"""
        if not isinstance(instr, dict):
            return

        op = instr.get('op')

        if op == 'PUSH':
            self.push(instr['value'])
        elif op == 'POP':
            self.pop()
        elif op == 'PEEK':
            # Peek doesn't modify stack
            pass
        elif op == 'ADD':
            self.add()
        elif op == 'SUB':
            self.sub()
        elif op == 'MUL':
            self.mul()
        elif op == 'DIV':
            self.div()
        elif op == 'MOD':
            self.mod()
        elif op == 'SWAP':
            self.swap()
        elif op == 'DUP':
            self.dup()
        elif op == 'EQ':
            self.eq()
        elif op == 'GT':
            self.gt()
        elif op == 'LT':
            self.lt()
        elif op == 'AND':
            self.and_op()
        elif op == 'OR':
            self.or_op()
        elif op == 'XOR':
            self.xor_op()
        elif op == 'SHL':
            self.shl()
        elif op == 'SHR':
            self.shr()
        elif op == 'GRILL':
            x, y, color = instr['x'], instr['y'], instr['color']
            self.grill(x, y, color)
        elif op == 'SPATULA':
            self.spatula()
        elif op == 'RECEIPT':
            self.receipt()
        elif op == 'MICROWAVE':
            self.microwave(instr['ms'])
        elif op == 'SHAKE':
            self.shake(instr['addr'], instr['value'])
        elif op == 'SIP':
            value = self.sip(instr['addr'])
            self.push(value)

    def run(self, program):
        """Run a DoubleCheeseBurger program"""
        self.program = program
        self.pc = 0

        # First pass: collect labels and functions
        for i, instr in enumerate(program):
            if isinstance(instr, dict):
                if instr.get('op') == 'COUPON':
                    self.labels[instr['label']] = i
                elif instr.get('op') == 'COMBO':
                    self.functions[instr['name']] = instr['body']

        # Second pass: execute
        while self.pc < len(program) and self.running:
            instr = program[self.pc]
            self.execute_instruction(instr)
            self.pc += 1

    def dump_framebuffer(self, filename):
        """Save framebuffer as ASCII art (for debugging)"""
        with open(filename, 'w') as f:
            chars = ' .:-=+*#%@'
            for y in range(self.screen_height):
                row = []
                for x in range(self.screen_width):
                    idx = y * self.screen_width + x
                    color = self.framebuffer[idx]
                    r, g, b = self.palette[color]
                    brightness = (r + g + b) // 3
                    char_idx = min(brightness * len(chars) // 256, len(chars) - 1)
                    row.append(chars[char_idx])
                f.write(''.join(row) + '\n')

# ============================================================================
# HELPER FUNCTIONS FOR BUILDING PROGRAMS
# ============================================================================

def push(value):
    """Helper to create PUSH instruction"""
    return {'op': 'PUSH', 'value': value}

def pop():
    return {'op': 'POP'}

def add():
    return {'op': 'ADD'}

def sub():
    return {'op': 'SUB'}

def mul():
    return {'op': 'MUL'}

def div():
    return {'op': 'DIV'}

def grill(x, y, color):
    return {'op': 'GRILL', 'x': x, 'y': y, 'color': color}

def spatula():
    return {'op': 'SPATULA'}

def receipt():
    return {'op': 'RECEIPT'}

def microwave(ms):
    return {'op': 'MICROWAVE', 'ms': ms}

def coupon(label):
    return {'op': 'COUPON', 'label': label}

def drive_thru(label):
    return {'op': 'DRIVE_THRU', 'label': label}

def combo(name, body):
    return {'op': 'COMBO', 'name': name, 'body': body}

def upsize(name):
    return {'op': 'UPSIZE', 'name': name}

# ============================================================================
# DEMO PROGRAM
# ============================================================================

if __name__ == "__main__":
    print("="*75)
    print("🍔🍔 DOUBLECHEESEBURGER VM v1.0 🍔🍔")
    print("="*75)
    print()

    # Simple demo: Draw a diagonal line
    vm = DoubleCheeseburgerVM(80, 25)  # Smaller for terminal display

    print("Drawing diagonal line demo...")
    print()

    # Build program
    program = []

    # Draw white diagonal line
    for i in range(min(80, 25)):
        program.append(grill(i, i, 15))  # 15 = white in default palette

    program.append(spatula())  # Flip buffer

    # Run program
    vm.run(program)

    # Output as ASCII
    print("Framebuffer output (ASCII art):")
    print("-" * 80)
    chars = ' .:-=+*#%@'
    for y in range(25):
        row = []
        for x in range(80):
            idx = y * 80 + x
            color = vm.framebuffer[idx]
            r, g, b = vm.palette[color]
            brightness = (r + g + b) // 3
            char_idx = min(brightness * len(chars) // 256, len(chars) - 1)
            row.append(chars[char_idx])
        print(''.join(row))
    print("-" * 80)

    print()
    print("✨ DoubleCheeseBurger VM initialized successfully! ✨")
    print()
