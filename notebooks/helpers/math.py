"""Simple first-principles helpers reused across the beginner notebooks."""

from __future__ import annotations


def duty_cycle(ping_width_s: float, inter_ping_interval_s: float) -> float:
    """Return the fraction of time spent transmitting."""
    return ping_width_s / inter_ping_interval_s


def range_from_delay(sound_speed_m_s: float, delay_s: float) -> float:
    """Convert round-trip delay into one-way range."""
    return sound_speed_m_s * delay_s / 2.0


def delay_samples_for_range(
    sound_speed_m_s: float, target_range_m: float, sample_rate_hz: float
) -> int:
    """Return the rounded sample delay for a target at range."""
    delay_s = 2.0 * target_range_m / sound_speed_m_s
    return int(round(delay_s * sample_rate_hz))
