"""Top-level Prismatic package exports.

Keep the root package lightweight so importing nested modules like
``prismatic.extern.hf.configuration_prismatic`` does not eagerly pull in the
full model stack and its training-time dependencies.
"""

from importlib import import_module

__all__ = ["available_model_names", "available_models", "get_model_description", "load", "load_vla"]


def __getattr__(name):
	if name in __all__:
		return getattr(import_module("prismatic.models"), name)
	raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
