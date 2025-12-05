"""Simulated device implementations.

These devices maintain internal state and return plausible values without
requiring actual hardware. Useful for testing and development.
"""

from __future__ import annotations

import time
import numpy as np
from .base import Camera, Pump, Sensor, Valve


class SimulatedCamera(Camera):
    """Simulated camera that generates synthetic images."""
    
    def __init__(self, width: int = 1024, height: int = 1024) -> None:
        self._width = width
        self._height = height
        self._exposure_ms = 20.0
        self._initialized = False
    
    def initialize(self) -> None:
        """Initialize simulated camera."""
        self._initialized = True
        print("[SimulatedCamera] Initialized")
    
    def close(self) -> None:
        """Close simulated camera."""
        self._initialized = False
        print("[SimulatedCamera] Closed")
    
    def grab_frame(self) -> np.ndarray:
        """Generate a synthetic frame."""
        if not self._initialized:
            raise RuntimeError("Camera not initialized")
        
        # Generate a simple synthetic image
        frame = np.random.randint(0, 4095, (self._height, self._width), dtype=np.uint16)
        return frame
    
    def set_exposure_time(self, exposure_ms: float) -> None:
        """Set exposure time (simulated)."""
        self._exposure_ms = exposure_ms
        print(f"[SimulatedCamera] Exposure set to {exposure_ms} ms")


class SimulatedPump(Pump):
    """Simulated pump that maintains flow rate state."""
    
    def __init__(self, name: str) -> None:
        self._name = name
        self._current_rate = 0.0
        self._initialized = False
    
    def initialize(self) -> None:
        """Initialize simulated pump."""
        self._initialized = True
        print(f"[SimulatedPump {self._name}] Initialized")
    
    def close(self) -> None:
        """Close simulated pump."""
        self._initialized = False
        print(f"[SimulatedPump {self._name}] Closed")
    
    def set_flow_rate(self, rate_ul_min: float) -> None:
        """Set flow rate (simulated)."""
        if not self._initialized:
            raise RuntimeError("Pump not initialized")
        self._current_rate = rate_ul_min
        print(f"[SimulatedPump {self._name}] Flow rate set to {rate_ul_min} uL/min")
    
    def get_flow_rate(self) -> float:
        """Get current flow rate."""
        return self._current_rate


class SimulatedValve(Valve):
    """Simulated valve that maintains channel state."""
    
    def __init__(self, name: str, num_channels: int = 2) -> None:
        self._name = name
        self._num_channels = num_channels
        self._current_channel = 0
        self._initialized = False
    
    def initialize(self) -> None:
        """Initialize simulated valve."""
        self._initialized = True
        print(f"[SimulatedValve {self._name}] Initialized")
    
    def close(self) -> None:
        """Close simulated valve."""
        self._initialized = False
        print(f"[SimulatedValve {self._name}] Closed")
    
    def switch_channel(self, channel: int) -> None:
        """Switch to channel (simulated)."""
        if not self._initialized:
            raise RuntimeError("Valve not initialized")
        if channel < 0 or channel >= self._num_channels:
            raise ValueError(f"Invalid channel: {channel}")
        self._current_channel = channel
        print(f"[SimulatedValve {self._name}] Switched to channel {channel}")
    
    def get_current_channel(self) -> int:
        """Get current channel."""
        return self._current_channel


class SimulatedSensor(Sensor):
    """Simulated sensor that returns random values."""
    
    def __init__(self, name: str, unit: str = "units") -> None:
        self._name = name
        self._unit = unit
        self._initialized = False
    
    def initialize(self) -> None:
        """Initialize simulated sensor."""
        self._initialized = True
        print(f"[SimulatedSensor {self._name}] Initialized")
    
    def close(self) -> None:
        """Close simulated sensor."""
        self._initialized = False
        print(f"[SimulatedSensor {self._name}] Closed")
    
    def read_value(self) -> float:
        """Read sensor value (simulated)."""
        if not self._initialized:
            raise RuntimeError("Sensor not initialized")
        # Return a random value in a plausible range
        value = np.random.uniform(0.0, 100.0)
        return value

