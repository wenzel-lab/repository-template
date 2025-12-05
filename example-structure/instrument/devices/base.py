"""Abstract base classes for all devices.

This module defines the interfaces that all device drivers must implement.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class Device(ABC):
    """Base class for all devices."""
    
    @abstractmethod
    def initialize(self) -> None:
        """Initialize the device.
        
        This should be called before using the device. It may open connections,
        configure settings, or perform other setup tasks.
        """
        ...
    
    @abstractmethod
    def close(self) -> None:
        """Close the device and release resources.
        
        This should be called when done with the device to ensure proper cleanup.
        """
        ...


class Camera(Device):
    """Abstract camera interface."""
    
    @abstractmethod
    def grab_frame(self) -> Any:  # In real code, use np.ndarray
        """Grab a single frame from the camera.
        
        Returns:
            Frame data (typically numpy array).
        """
        ...
    
    @abstractmethod
    def set_exposure_time(self, exposure_ms: float) -> None:
        """Set camera exposure time.
        
        Args:
            exposure_ms: Exposure time in milliseconds.
        """
        ...


class Pump(Device):
    """Abstract pump interface."""
    
    @abstractmethod
    def set_flow_rate(self, rate_ul_min: float) -> None:
        """Set the pump flow rate.
        
        Args:
            rate_ul_min: Flow rate in microliters per minute.
        """
        ...
    
    @abstractmethod
    def get_flow_rate(self) -> float:
        """Get the current flow rate.
        
        Returns:
            Current flow rate in microliters per minute.
        """
        ...


class Valve(Device):
    """Abstract valve interface."""
    
    @abstractmethod
    def switch_channel(self, channel: int) -> None:
        """Switch valve to specified channel.
        
        Args:
            channel: Channel number to switch to.
        """
        ...
    
    @abstractmethod
    def get_current_channel(self) -> int:
        """Get the current valve channel.
        
        Returns:
            Current channel number.
        """
        ...


class Sensor(Device):
    """Abstract sensor interface."""
    
    @abstractmethod
    def read_value(self) -> float:
        """Read current sensor value.
        
        Returns:
            Sensor reading (units depend on sensor type).
        """
        ...

