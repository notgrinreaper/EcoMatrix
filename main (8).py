import os
import sys
import time
import math
import random

# --- CONFIGURATION & TERMINAL SETUP ---
WIDTH, HEIGHT = 70, 20
CLEAN_CHARS = [" ", ".", "░", "▒", "▓", "█"]
DIRTY_CHARS = [" ", "x", "*", "#", "%", "@"]

# --- COLOR CODES (No extra libraries needed!) ---
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

def enable_windows_colors():
    """Makes sure colors work properly on Windows Command Prompt/PowerShell."""
    if os.name == 'nt':
        os.system('')

def get_simulated_cpu_load():
    return abs(math.sin(time.time() * 0.1)) * 100

class EcoSystem:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[random.random() for _ in range(width)] for _ in range(height)]

    def update(self, carbon_intensity):
        new_grid = [[0.0 for _ in range(self.width)] for _ in range(self.height)]
        chaos_factor = carbon_intensity / 500.0 

        for y in range(self.height):
            for x in range(self.width):
                total = 0
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        nx, ny = (x + dx) % self.width, (y + dy) % self.height
                        total += self.grid[ny][nx]
                avg = total / 9.0

                if chaos_factor < 0.3:
                    new_val = avg + 0.02 if avg < 0.7 else avg - 0.05
                else:
                    new_val = avg * (1.5 if random.random() > 0.5 else 0.2) + (chaos_factor * 0.1)

                new_grid[y][x] = max(0.0, min(1.0, new_val))

        self.grid = new_grid

    def render(self, carbon_intensity):
        output = []

        # Pick character style AND color based on pollution level
        if carbon_intensity < 200:
            char_set = CLEAN_CHARS
            color = GREEN
        elif carbon_intensity < 500:
            char_set = CLEAN_CHARS
            color = YELLOW
        else:
            char_set = DIRTY_CHARS
            color = RED

        for row in self.grid:
            line = ""
            for val in row:
                char_idx = int(val * (len(char_set) - 1))
                line += char_set[char_idx]
            # Wrap each line in the color code and reset it at the end
            output.append(f"{color}{line}{RESET}")

        return "\n".join(output)

def main():
    enable_windows_colors()
    ecosystem = EcoSystem(WIDTH, HEIGHT)

    modes = [
        {"name": "Hydropower Grid (Norway)", "base_intensity": 40},
        {"name": "Standard Mixed Grid (US-East)", "base_intensity": 350},
        {"name": "Coal-Reliant Grid (Overloaded)", "base_intensity": 780}
    ]

    current_mode_idx = 0
    last_switch_time = time.time()

    # Clear the screen ONCE at the start
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        while True:
            # Move cursor back to top-left instead of clearing screen (Zero Blinking!)
            print("\033[H", end="")

            if time.time() - last_switch_time > 12:
                current_mode_idx = (current_mode_idx + 1) % len(modes)
                last_switch_time = time.time()

            active_grid = modes[current_mode_idx]
            cpu_fluctuation = get_simulated_cpu_load()
            final_intensity = active_grid["base_intensity"] + (cpu_fluctuation * 1.5)

            # UI Header Display
            print(f"{CYAN}{'=' * WIDTH}{RESET}")
            print(f"{GREEN}🌿 ECO-GRID CELLULAR AUTOMATA ENGINE v1.1 | Pure Python Terminal Mode{RESET}")
            print(f"{CYAN}{'=' * WIDTH}{RESET}")
            print(f"📡 Current Energy Profile : {active_grid['name']:<35}")
            print(f"⚡ Simulated AI Model Load: {cpu_fluctuation:.1f}%   ")
            print(f"📉 Carbon Footprint Proxy : {final_intensity:.1f} gCO2e/kWh   ")

            if final_intensity < 200:
                print(f"{GREEN}🟢 STATUS: Clean Runtime. System generating harmonic structures.        {RESET}")
            elif final_intensity < 500:
                print(f"{YELLOW}🟡 STATUS: Balanced Load. System experiencing standard entropy.          {RESET}")
            else:
                print(f"{RED}🔴 ALERT: Dirty Energy Grid! Ecosystem mutating into industrial noise.{RESET}")
            print("-" * WIDTH)

            ecosystem.update(final_intensity)
            print(ecosystem.render(final_intensity))
            print("-" * WIDTH)
            print("Press Ctrl+C inside the terminal window to stop simulation.")

            time.sleep(0.15)

    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\n{GREEN}Simulation safely terminated. Keep building green software! 🌿{RESET}\n")

if __name__ == "__main__":
    main()
