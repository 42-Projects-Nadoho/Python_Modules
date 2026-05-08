import importlib
import sys


def load_dependency(module_name: str):
    try:
        return importlib.import_module(module_name)
    except ImportError:
        return None


def module_version(module) -> str:
    return getattr(module, "__version__", "unknown")


def print_dependency_status(modules: dict) -> None:
    print("Checking dependencies:")
    messages = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready",
    }
    for name in messages.keys():
        module = modules.get(name)
        if module is None:
            print(f"[MISSING] {name} - {messages[name]}")
        else:
            print(f"[OK] {name} ({module_version(module)}) - {messages[name]}")


def print_install_help() -> None:
    print("\nMissing required dependencies.")
    print("Install with pip: pip install -r requirements.txt")
    print("Install with Poetry: poetry install")
    print("Run with Poetry: poetry run python loading.py")


def compare_pip_poetry() -> None:
    print("\nDependency manager comparison:")
    print("- pip uses requirements.txt")
    print("- Poetry uses pyproject.toml")
    print(f"- Current Python: {sys.executable}")


def build_matrix_dataset(np, pd, size: int = 1000):
    np.random.seed(42)
    ticks = np.arange(size)
    matrix_load = np.random.normal(loc=50, scale=10, size=size)
    data = pd.DataFrame({
        "tick": ticks,
        "matrix_load": matrix_load,
    })
    return data


def save_visualization(
    df, plt, output_file: str = "matrix_analysis.png"
) -> str:
    plt.subplots(figsize=(10, 5))
    plt.plot(df["tick"], df["matrix_load"], label="matrix_load", alpha=0.5)
    plt.title("Matrix Data Analysis")
    plt.xlabel("Tick")
    plt.ylabel("Load")
    plt.legend()
    plt.grid(True, alpha=0.2)
    plt.savefig(output_file)
    plt.close()
    return output_file


def main() -> None:
    print("\nLOADING STATUS: Loading programs...")

    modules = {
        "pandas": load_dependency("pandas"),
        "numpy": load_dependency("numpy"),
        "matplotlib_pyplot": load_dependency("matplotlib.pyplot"),
        "matplotlib": load_dependency("matplotlib"),
    }

    print_dependency_status(modules)
    compare_pip_poetry()

    required = ["pandas", "numpy", "matplotlib_pyplot"]
    missing = [name for name in required if modules[name] is None]
    if missing:
        print_install_help()
        return

    print("\nAnalyzing Matrix data...")
    dataset = build_matrix_dataset(
        modules["numpy"], modules["pandas"], size=1000
    )
    print(f"Processing {len(dataset)} data points...")
    print("Generating visualization...")
    output_path = save_visualization(dataset, modules["matplotlib_pyplot"])
    print("Analysis complete!")
    print(f"Results saved to: {output_path}")


if __name__ == "__main__":
    main()
