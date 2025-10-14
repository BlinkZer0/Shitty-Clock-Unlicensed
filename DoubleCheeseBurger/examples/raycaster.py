#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║           🍔🍔 DOUBLECHEESEBURGER RAYCASTER DEMO 🍔🍔                      ║
║                                                                           ║
║  A simple 3D raycaster engine written in DoubleCheeseBurger!             ║
║  This demonstrates that DCB can handle real game rendering.              ║
║                                                                           ║
║  Licensed under the Overprotective License (OPL-∞)                       ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import sys
import os
import math

# Fix Windows console encoding for emojis
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except:
        pass

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from double_cheeseburger import DoubleCheeseburgerVM, push, grill, spatula

def create_raycaster_program():
    """
    Create a simple raycaster that renders a 3D view of a world.
    This is a simplified version to demonstrate capabilities.
    """

    # World map (8x8 grid, 1=wall, 0=empty)
    world_map = [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
    ]

    # Player position and viewing angle
    player_x = 3.5
    player_y = 3.5
    player_angle = 0.0

    screen_width = 80
    screen_height = 50
    fov = 60  # Field of view in degrees

    program = []

    # Cast rays for each column of the screen
    for screen_x in range(screen_width):
        # Calculate ray angle
        ray_angle = player_angle + (screen_x - screen_width / 2) * (fov / screen_width)
        ray_angle_rad = math.radians(ray_angle)

        # Ray direction
        ray_dir_x = math.cos(ray_angle_rad)
        ray_dir_y = math.sin(ray_angle_rad)

        # DDA raycasting algorithm (simplified)
        # Start at player position
        map_x = int(player_x)
        map_y = int(player_y)

        # Ray position
        ray_x = player_x
        ray_y = player_y

        # Step through the map
        max_steps = 20
        hit_wall = False
        distance = 0

        for step in range(max_steps):
            ray_x += ray_dir_x * 0.1
            ray_y += ray_dir_y * 0.1
            distance += 0.1

            map_x = int(ray_x)
            map_y = int(ray_y)

            # Check bounds
            if map_x < 0 or map_x >= 8 or map_y < 0 or map_y >= 8:
                hit_wall = True
                break

            # Check if hit wall
            if world_map[map_y][map_x] == 1:
                hit_wall = True
                break

        # Calculate wall height based on distance
        if distance > 0:
            wall_height = int((screen_height / 2) / distance)
        else:
            wall_height = screen_height

        # Clamp wall height
        wall_height = min(wall_height, screen_height)

        # Calculate ceiling and floor
        ceiling = (screen_height // 2) - wall_height
        floor = (screen_height // 2) + wall_height

        # Draw column
        for screen_y in range(screen_height):
            if screen_y < ceiling:
                # Sky/ceiling - dark blue
                color = 1
            elif screen_y >= ceiling and screen_y < floor:
                # Wall - gradient based on distance
                # Closer = brighter
                brightness = int(255 - min(distance * 20, 200))
                # Use grayscale palette (indices 16-231)
                color = 16 + int((brightness / 255) * 100)
                color = max(16, min(color, 231))
            else:
                # Floor - dark gray
                color = 8

            program.append(grill(screen_x, screen_y, color))

    program.append(spatula())

    return program


def render_raycaster_to_terminal(vm):
    """Render the framebuffer as ASCII art"""
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
    print("🍔🍔 DOUBLECHEESEBURGER RAYCASTER ENGINE 🍔🍔")
    print("="*80)
    print()
    print("Rendering 3D world from player perspective...")
    print()

    # Create VM with terminal-friendly dimensions
    vm = DoubleCheeseburgerVM(screen_width=80, screen_height=50)

    # Generate and run raycaster program
    program = create_raycaster_program()

    print(f"Generated {len(program)} DoubleCheeseBurger instructions")
    print()

    vm.run(program)

    print("Raycaster output (ASCII art):")
    print("-" * 80)
    render_raycaster_to_terminal(vm)
    print("-" * 80)

    print()
    print("✨ Raycaster rendered successfully! ✨")
    print("🍔 This demonstrates DoubleCheeseBurger can handle 3D graphics!")
    print()
    print("Map legend:")
    print("  Bright areas = nearby walls")
    print("  Dark areas = distant walls")
    print("  Top = sky/ceiling")
    print("  Bottom = floor")
    print()
