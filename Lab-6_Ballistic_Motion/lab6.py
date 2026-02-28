# Programming Lab 6 - Blindfolded Archer
# PHYS 2511 - Spring 2026

import math

def simulate(v0, angle_deg, b, g=9.8, y0=1.8, dt=0.001):
    """
    Simulate 2D ballistic motion with Stokes drag.
    Returns final x position when projectile hits ground (y=0).
    Optionally returns full trajectory if store=True.
    """
    angle = math.radians(angle_deg)
    vx = v0 * math.cos(angle)
    vy = v0 * math.sin(angle)
    x = 0.0
    y = y0

    while y >= 0:
        ax = -b * vx
        ay = -g - b * vy
        vx = vx + ax * dt
        vy = vy + ay * dt
        x = x + vx * dt
        y = y + vy * dt

    return x

def simulate_full(v0, angle_deg, b, g=9.8, y0=1.8, dt=0.001):
    """Returns full trajectory as lists of (x, y) points."""
    angle = math.radians(angle_deg)
    vx = v0 * math.cos(angle)
    vy = v0 * math.sin(angle)
    x = 0.0
    y = y0
    xs, ys = [x], [y]

    while y >= 0:
        ax = -b * vx
        ay = -g - b * vy
        vx = vx + ax * dt
        vy = vy + ay * dt
        x = x + vx * dt
        y = y + vy * dt
        xs.append(x)
        ys.append(y)

    return xs, ys

def compare_air_resistance(v0=30.0, angle_deg=45.0, g=9.8, b=0.1):
    """Show difference in final position with and without air resistance."""
    x_no_drag = simulate(v0, angle_deg, b=0.0, g=g)
    x_drag    = simulate(v0, angle_deg, b=b,   g=g)
    print("\n--- Air Resistance Comparison ---")
    print(f"  Initial speed : {v0} m/s at {angle_deg} degrees")
    print(f"  b = 0   (no drag) : landing x = {x_no_drag:.3f} m")
    print(f"  b = {b} (drag)    : landing x = {x_drag:.3f} m")
    print(f"  Difference        : {abs(x_no_drag - x_drag):.3f} m")

def auto_aim(target_x, b, g=9.8, tol=0.5, max_shots=200):
    """
    Automated archer: binary-search on speed (fixed 45 deg) to hit target.
    Each 'shot' is informed by the miss distance from the previous shot.
    Returns (winning_v0, winning_angle, shots_taken) or None if not found.
    """
    angle = 45.0
    v_low, v_high = 1.0, 500.0

    for shot in range(1, max_shots + 1):
        v_mid = (v_low + v_high) / 2.0
        x_land = simulate(v_mid, angle, b, g)
        delta = x_land - target_x
        print(f"  Shot {shot:3d}: speed={v_mid:.3f} m/s, angle={angle:.1f} deg, "
              f"landed at x={x_land:.3f} m, miss={delta:+.3f} m")

        if abs(delta) <= tol:
            print(f"\n  *** HIT! Shot lands within {tol} m of target. ***")
            return v_mid, angle, shot

        if delta < 0:        # fell short -> need more speed
            v_low = v_mid
        else:                # overshot -> need less speed
            v_high = v_mid

    return None

def main():
    print("=" * 55)
    print("        PHYS 2511 Lab 6 - Blindfolded Archer")
    print("=" * 55)

    # --- User inputs ---
    v0        = float(input("\nInitial velocity magnitude (m/s): "))
    angle_deg = float(input("Launch angle (degrees above horizontal): "))
    b         = float(input("Drag coefficient b (0 = no air resistance): "))

    # Optional gravitational constant
    g_in = input("Gravitational constant g (press Enter for 9.8 m/s^2): ").strip()
    g = float(g_in) if g_in else 9.8

    # --- Single shot simulation ---
    x_final = simulate(v0, angle_deg, b, g)
    print(f"\nFinal landing position: x = {x_final:.4f} m from the archer.")

    # --- Air resistance comparison (standalone example) ---
    compare_air_resistance(v0, angle_deg, g=g, b=b if b != 0 else 0.1)

    # --- Target and miss distance ---
    target_x = float(input("\nEnter target distance from archer (m): "))
    delta_x = x_final - target_x
    print(f"\nShot missed the target by: |Δx| = {abs(delta_x):.4f} m")
    if abs(delta_x) <= 0.5:
        print("Direct hit on the first shot!")
    else:
        print("Shot did not hit the target (need within 0.5 m).")

    # --- Auto-aim algorithm ---
    print("\n--- Auto-Aim Algorithm (binary search on launch speed) ---")
    result = auto_aim(target_x, b, g)
    if result:
        win_v, win_ang, n_shots = result
        print(f"\nWinning parameters:")
        print(f"  Initial speed : {win_v:.4f} m/s")
        print(f"  Launch angle  : {win_ang:.1f} degrees")
        print(f"  Shots taken   : {n_shots}")
    else:
        print("Could not find a winning shot within the attempt limit.")

if __name__ == "__main__":
    main()