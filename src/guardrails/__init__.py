# Lazy imports to avoid RuntimeWarning when running submodules directly
def __getattr__(name):
    if name in ("detect_injection", "topic_filter", "InputGuardrailPlugin"):
        from guardrails.input_guardrails import detect_injection, topic_filter, InputGuardrailPlugin
        return locals()[name]
    if name in ("content_filter", "llm_safety_check", "OutputGuardrailPlugin"):
        from guardrails.output_guardrails import content_filter, llm_safety_check, OutputGuardrailPlugin
        return locals()[name]
    raise AttributeError(f"module 'guardrails' has no attribute {name!r}")