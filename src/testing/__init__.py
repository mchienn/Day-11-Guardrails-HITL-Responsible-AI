# Lazy imports to avoid RuntimeWarning when running submodules directly
def __getattr__(name):
    if name in ("run_comparison", "print_comparison", "SecurityTestPipeline", "TestResult"):
        from testing.testing import run_comparison, print_comparison, SecurityTestPipeline, TestResult
        return locals()[name]
    raise AttributeError(f"module 'testing' has no attribute {name!r}")