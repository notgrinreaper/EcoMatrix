import os
import sys
import time
import math
import random

# --- CONFIGURATION & TERMINAL SETUP ---
WIDTH, HEIGHT = 70, 20
CLEAN_CHARS = [" ", ".", "░", "▒", "▓", "█"]  # Smooth organic growth symbols
DIRTY_CHARS = [" ", "x", "*", "#", "%", "@"]  # Chaotic, structural decay symbols

def clear_screen():
    """Clears the terminal screen cleanly across operating systems."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_simulated_cpu_load():
    """Simulates fluctuating computational loads over time using trigonometry."""
    return abs(math.sin(time.time() * 0.1)) * 100

# --- THE SIMULATION ENGINE ---
class EcoSystem:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        # Initialize grid with random energy levels (0.0 to 1.0)
        self.grid = [[random.random() for _ in range(width)] for _ in range(height)]

    def update(self, carbon_intensity):
        """Updates the grid based on local mathematical physics rules warped by carbon intensity."""
        new_grid = [[0.0 for _ in range(self.width)] for _ in range(self.height)]

        # Carbon levels change how volatile the system rules are
        # High carbon = high mutations/entropy
        chaos_factor = carbon_intensity / 500.0 

        for y in range(self.height):
            for x in range(self.width):
                # Calculate average energy of 8 surrounding neighbors
                total = 0
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        nx, ny = (x + dx) % self.width, (y + dy) % self.height
                        total += self.grid[ny][nx]
                avg = total / 9.0

                # Apply growth logic injected with carbon-chaos mutations
                if chaos_factor < 0.3:
                    # Clean grid: peaceful, flowing diffusion
                    new_val = avg + 0.02 if avg < 0.7 else avg - 0.05
                else:
                    # Dirty grid: extreme volatility, rapid depletion or over-saturation
                    new_val = avg * (1.5 if random.random() > 0.5 else 0.2) + (chaos_factor * 0.1)

                # Keep values safely bound between 0.0 and 1.0
                new_grid[y][x] = max(0.0, min(1.0, new_val))

        self.grid = new_grid

    def render(self, carbon_intensity):
        """Converts numerical energy values into distinct visual ASCII character sets."""
        output = []
        # Choose the aesthetic based on carbon footprint
        char_set = CLEAN_CHARS if carbon_intensity < 400 else DIRTY_CHARS

        for row in self.grid:
            line = ""
            for val in row:
                # Map 0.0 -> 1.0 to the character index array
                char_idx = int(val * (len(char_set) - 1))
                line += char_set[char_idx]
            output.append(line)
        return "\n".join(output)

# --- MAIN RUNTIME ---
def main():
    ecosystem = EcoSystem(WIDTH, HEIGHT)

    # Simulating a user changing the grid modes manually over time
    modes = [
        {"name": "Hydropower Grid (Norway)", "base_intensity": 40},
        {"name": "Standard Mixed Grid (US-East)", "base_intensity": 350},
        {"name": "Coal-Reliant Grid (Overloaded)", "base_intensity": 780}
    ]

    current_mode_idx = 0
    last_switch_time = time.time()

    try:
        while True:
            clear_screen()

            # Switch grid simulated profiles every 12 seconds automatically
            if time.time() - last_switch_time > 12:
                current_mode_idx = (current_mode_idx + 1) % len(modes)
                last_switch_time = time.time()

            active_grid = modes[current_mode_idx]
            cpu_fluctuation = get_simulated_cpu_load()

            # Final carbon metric calculation
            final_intensity = active_grid["base_intensity"] + (cpu_fluctuation * 1.5)

            # UI Header Display
            print("=" * WIDTH)
            print(f"🌿 ECO-GRID CELLULAR AUTOMATA ENGINE v1.0 | Pure Python Terminal Mode")
            print("=" * WIDTH)
            print(f"📡 Current Energy Profile : {active_grid['name']}")
            print(f"⚡ Simulated AI Model Load: {cpu_fluctuation:.1f}%")
            print(f"📉 Carbon Footprint Proxy : {final_intensity:.1f} gCO2e/kWh")

            if final_intensity < 200:
                print("🟢 STATUS: Clean Runtime. System generating harmonic structures.")
            elif final_intensity < 500:
                print("🟡 STATUS: Balanced Load. System experiencing standard entropy.")
            else:
                print("🔴 ALERT: Dirty Energy Grid! Ecosystem mutating into industrial noise.")
            print("-" * WIDTH)

            # Step and draw the simulation frame
            ecosystem.update(final_intensity)
            print(ecosystem.render(final_intensity))
            print("-" * WIDTH)
            print("Press Ctrl+C inside the terminal window to stop simulation.")

            time.sleep(0.15) # Controls framework animation speed FPS

    except KeyboardInterrupt:
        clear_screen()
        print("\nSimulation safely terminated. Keep building green software! 🌿\n")

if __name__ == "__main__":
    main()
