"""Main application entry point.

Builds devices, controllers, and GUI based on configuration.
"""

from __future__ import annotations

import sys
from pathlib import Path

from qtpy.QtWidgets import QApplication

from instrument.config import InstrumentConfig
from instrument.controllers.experiment_controller import ExperimentController
from instrument.controllers.live_controller import LiveController
from instrument.devices.simulated_ import SimulatedCamera, SimulatedPump
from instrument.gui.main_window import MainWindow


def build_instrument(config: InstrumentConfig) -> tuple[LiveController, ExperimentController]:
    """Build instrument from configuration.
    
    Args:
        config: Instrument configuration.
    
    Returns:
        Tuple of (live_controller, experiment_controller).
    """
    # Build devices based on config
    if config.simulation:
        # Use simulated devices
        camera = SimulatedCamera()
        pump = SimulatedPump("sample_pump")
    else:
        # Build real devices based on config
        # This is where you would instantiate actual camera/pump drivers
        # For now, using simulated as placeholder
        camera = SimulatedCamera()
        pump = SimulatedPump("sample_pump")
    
    # Initialize devices
    camera.initialize()
    pump.initialize()
    
    # Build controllers
    live_controller = LiveController(camera)
    experiment_controller = ExperimentController(camera, pump)
    
    return live_controller, experiment_controller


def main() -> int:
    """Main entry point.
    
    Run with: python -m instrument.main
    Or: python instrument/main.py
    """
    # Load configuration
    config_path = Path("instrument-config.yaml")
    if not config_path.exists():
        print(f"Error: Configuration file not found: {config_path}")
        return 1
    
    config = InstrumentConfig.from_file(config_path)
    
    # Build instrument
    live_controller, experiment_controller = build_instrument(config)
    
    # Create Qt application
    app = QApplication(sys.argv)
    
    # Create main window
    window = MainWindow(live_controller)
    window.show()
    
    # Run event loop
    return app.exec_()


if __name__ == "__main__":
    sys.exit(main())

