"""Configuration loading and validation.

Loads instrument-config.yaml and validates it using Pydantic models.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, Field


class CameraConfig(BaseModel):
    """Camera configuration."""
    
    type: str
    serial_number: str | None = None
    exposure_ms: float = 20.0
    pixel_format: str = "MONO12"


class PumpConfig(BaseModel):
    """Pump configuration."""
    
    name: str
    backend: str  # "pyvisa", "serial", "gpio"
    flow_unit: str = "uL/min"
    max_flow_rate: float | None = None
    
    # Backend-specific fields
    resource: str | None = None  # For pyvisa
    port: str | None = None  # For serial
    baudrate: int | None = None  # For serial
    channel: int | None = None  # For gpio


class ValveConfig(BaseModel):
    """Valve configuration."""
    
    name: str
    backend: str  # "gpio", "serial"
    type: str | None = None  # "solenoid", etc.
    
    # Backend-specific fields
    channel: int | None = None  # For gpio
    port: str | None = None  # For serial
    baudrate: int | None = None  # For serial


class SensorConfig(BaseModel):
    """Sensor configuration."""
    
    name: str
    backend: str
    unit: str | None = None
    
    # Backend-specific fields
    port: str | None = None
    baudrate: int | None = None


class PathsConfig(BaseModel):
    """Path configuration."""
    
    data_root: str = "/data/experiments"
    log_dir: str = "/data/logs"


class ExperimentConfig(BaseModel):
    """Experiment default configuration."""
    
    default_duration_s: float = 60.0
    auto_save: bool = True
    file_format: str = "ome-tiff"


class InstrumentConfig(BaseModel):
    """Complete instrument configuration."""
    
    instrument_name: str
    simulation: bool = False
    
    camera: CameraConfig | None = None
    pumps: list[PumpConfig] = Field(default_factory=list)
    valves: list[ValveConfig] = Field(default_factory=list)
    sensors: list[SensorConfig] = Field(default_factory=list)
    paths: PathsConfig = Field(default_factory=PathsConfig)
    experiment: ExperimentConfig = Field(default_factory=ExperimentConfig)
    
    @classmethod
    def from_file(cls, path: Path | str) -> InstrumentConfig:
        """Load configuration from YAML file."""
        path = Path(path)
        if not path.exists():
            raise FileNotFoundError(f"Config file not found: {path}")
        
        with open(path, "r") as f:
            data = yaml.safe_load(f)
        
        return cls.model_validate(data)
    
    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        return self.model_dump()

