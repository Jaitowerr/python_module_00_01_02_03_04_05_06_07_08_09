#!/usr/bin/env python3
"""
Helper file for Growing Code - AUTO-CLEAN + AUTO-CHECK VERSION.
Run from the root folder: python3 main.py
"""

import sys
import os
import shutil
import io
import contextlib

EXERCISES = [
    ("0", "ft_hello_garden", "ex0", "Say hello"),
    ("1", "ft_plot_area", "ex1", "Calculate area"),
    ("2", "ft_harvest_total", "ex2", "Add up weights"),
    ("3", "ft_plant_age", "ex3", "Check if ready"),
    ("4", "ft_water_reminder", "ex4", "Water check"),
    ("5i", "ft_count_harvest_iterative", "ex5", "Count (iterative)"),
    ("5r", "ft_count_harvest_recursive", "ex5", "Count (recursive)"),
    ("6", "ft_garden_summary", "ex6", "Garden info"),
    ("7", "ft_seed_inventory", "ex7", "Seed inventory"),
]


def clean_folder(folder):
    """Remove __pycache__ and .pyc files to keep the workspace clean."""
    folder_path = os.path.join(os.path.dirname(__file__), folder)
    pycache = os.path.join(folder_path, "__pycache__")

    if os.path.exists(pycache):
        shutil.rmtree(pycache)

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".pyc"):
                os.remove(os.path.join(root, file))


def test_seed_inventory(ft_function):
    """Test ft_seed_inventory against expected outputs."""
    tests = [
        (("tomato", 15, "packets"), "Tomato seeds: 15 packets available"),
        (("carrot", 8, "grams"),    "Carrot seeds: 8 grams total"),
        (("lettuce", 12, "area"),   "Lettuce seeds: covers 12 square meters"),
        (("basil", 5, "unknown"),   "Unknown unit type"),
    ]
    all_ok = True
    for args, expected in tests:
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            ft_function(*args)
        output = buffer.getvalue().strip()
        if output == expected:
            print(f"  ✅ {args} → '{output}'")
        else:
            print(f"  ❌ {args}")
            print(f"     Expected : '{expected}'")
            print(f"     Got      : '{output}'")
            all_ok = False

    if all_ok:
        print("\n✅ ft_seed_inventory: ALL TESTS PASSED!")
    else:
        print("\n❌ ft_seed_inventory: SOME TESTS FAILED")


def test_ft_exercise(exercise_file_name, folder):
    """Import and run an exercise from its folder and then clean up."""
    print(f"\n=== Testing {exercise_file_name} ===")

    folder_path = os.path.join(os.path.dirname(__file__), folder)
    if folder_path not in sys.path:
        sys.path.insert(0, folder_path)

    try:
        if exercise_file_name in sys.modules:
            del sys.modules[exercise_file_name]

        ft_module = __import__(exercise_file_name)
        ft_function = getattr(ft_module, exercise_file_name)

        if exercise_file_name == "ft_seed_inventory":
            test_seed_inventory(ft_function)
        else:
            ft_function()
            print(f"\n✅ {exercise_file_name} completed!")

        clean_folder(folder)
        return True

    except ImportError:
        print(f"❌ Could not find {exercise_file_name}.py in {folder}/")
        clean_folder(folder)
        return False
    except AttributeError:
        print(f"❌ Could not find function {exercise_file_name}()")
        clean_folder(folder)
        return False
    except Exception as error:
        print(f"❌ Error: {error}")
        clean_folder(folder)
        return False


def main():
    """Main loop with menu."""
    while True:
        print("\n🌱 Growing Code Tester (Auto-Clean) 🌱")
        print("─" * 45)
        for key, name, _, desc in EXERCISES:
            print(f"  {key:3} - {name:35} | {desc}")
        print(f"  {'a':3} - Run all")
        print(f"  {'q':3} - Quit")
        print("─" * 45)

        choice = input("\nEnter choice: ").strip().lower()

        if choice == "q":
            break
        elif choice == "a":
            for _, name, folder, _ in EXERCISES:
                test_ft_exercise(name, folder)
        else:
            found = False
            for key, name, folder, _ in EXERCISES:
                if choice == key:
                    test_ft_exercise(name, folder)
                    found = True
                    break
            if not found:
                print("❌ Invalid choice!")

        if input("\n▶ Press Enter to continue (or 'q' to quit): ").lower() == "q":
            break

    print("\n👋 Workspace clean. Goodbye! 🌱")


if __name__ == "__main__":
    main()