from __future__ import annotations


def get_weather(city: str) -> str:
    """Get a simple weather string for a given city.

    Args:
        city: City name, e.g., "sf".

    Returns:
        A short, human-readable weather text.
    """

    return f"It's always sunny in {city}!"


