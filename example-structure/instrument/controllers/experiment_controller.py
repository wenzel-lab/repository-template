"""Experiment controller.

Handles acquisition loops, flow ramps, time series, and other experimental protocols.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from instrument.devices.base import Camera, Pump


@dataclass
class ExperimentParams:
    """Parameters for an experiment."""
    
    flow_rate_ul_min: float
    duration_s: float
    save_path: Path | None = None


class ExperimentController:
    """Controller for running experiments."""
    
    def __init__(self, camera: Camera, pump: Pump) -> None:
        """Initialize experiment controller.
        
        Args:
            camera: Camera device.
            pump: Pump device.
        """
        self._camera = camera
        self._pump = pump
    
    def run_experiment(self, params: ExperimentParams) -> None:
        """Run an experiment with given parameters.
        
        Args:
            params: Experiment parameters.
        """
        # Set flow rate
        self._pump.set_flow_rate(params.flow_rate_ul_min)
        
        # Simple blocking loop for now
        # (Later you can introduce threading or asyncio if needed)
        import time
        
        num_frames = int(params.duration_s)
        for i in range(num_frames):
            frame = self._camera.grab_frame()
            self._save_frame(frame, i, params.save_path)
            time.sleep(1.0)  # 1 second per frame
    
    def _save_frame(self, frame: any, frame_number: int, save_path: Path | None) -> None:
        """Save a frame to disk.
        
        Args:
            frame: Frame data to save.
            frame_number: Frame number.
            save_path: Directory to save frames to.
        """
        if save_path is None:
            return
        
        # Minimal placeholder; real code would write to disk / Zarr / OME-TIFF
        # Example: save as TIFF, or use tifffile, or write to Zarr
        save_path.mkdir(parents=True, exist_ok=True)
        # ... actual saving logic here ...

