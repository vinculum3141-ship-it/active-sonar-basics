"""Shared baseline parameters for the beginner active sonar track."""

BASELINE_SCENE = {
    "sound_speed_m_s": 1500.0,
    "carrier_hz": 15_000.0,
    "bandwidth_hz": 1_000.0,
    "ping_width_s": 0.05,
    "inter_ping_interval_s": 0.2,
    "sample_rate_hz": 10_000.0,
    "pings_per_cpi": 64,
    "target_range_m": 75.0,
    "target_velocity_m_s": 0.1,
    "target_bearing_deg": 20.0,
    "interferer_bearing_deg": -30.0,
}
