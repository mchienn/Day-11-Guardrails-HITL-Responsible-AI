# Lazy imports to avoid RuntimeWarning when running submodules directly
def __getattr__(name):
    if name in ("ConfidenceRouter", "RoutingDecision", "hitl_decision_points", "HIGH_RISK_ACTIONS"):
        from hitl.hitl import ConfidenceRouter, RoutingDecision, hitl_decision_points, HIGH_RISK_ACTIONS
        return locals()[name]
    raise AttributeError(f"module 'hitl' has no attribute {name!r}")