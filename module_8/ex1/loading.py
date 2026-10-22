import importlib
import sys


DEPENDENCIES: dict[str, str] = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready",
}


def check_dependencies() -> bool:
    print("Checking dependencies:")
    all_available = True

    for package, description in DEPENDENCIES.items():
        try:
            module = importlib.import_module(package)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {package} ({version}) - {description}")
        except ModuleNotFoundError:
            print(f"[MISSING] {package} - not installed")
            all_available = False

    return (all_available)


def show_package_management() -> None:
    print("Package management:")
    print("pip: installs dependencies listed in requirements.txt")
    print("Poetry: manages dependencies and project metadata in pyproject.toml")


def show_install_instructions() -> None:
    print("Missing dependencies detected.")
    print("Install with pip:")
    print("pip install -r requirements.txt")
    print("Or install with Poetry:")
    print("poetry install")
    print("Then run this program again.")


def analyze_matrix_data() -> None:
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    print("Analyzing Matrix data...")

    generator = np.random.default_rng(42)
    signal = generator.normal(loc=50.0, scale=15.0, size=1000)
    stability = generator.uniform(low=0.0, high=100.0, size=1000)

    frame = pd.DataFrame({
        "signal": signal,
        "stability": stability,
    })
    frame["signal_smoothed"] = frame["signal"].rolling(
        window=25,
        min_periods=1,
    ).mean()

    print(f"Processing {len(frame)} data points...")
    print("Generating visualization...")

    plt.figure(figsize=(10, 5))
    plt.plot(frame.index, frame["signal_smoothed"])
    plt.xlabel("Matrix data point")
    plt.ylabel("Signal level")
    plt.title("Matrix Signal Analysis")
    plt.tight_layout()
    plt.savefig("matrix_analysis.png")
    plt.close()

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    available = check_dependencies()
    show_package_management()

    if not available:
        show_install_instructions()
        sys.exit(1)

    analyze_matrix_data()


if __name__ == "__main__":
    main()
