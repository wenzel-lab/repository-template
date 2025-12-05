"""Tests for controllers."""

from instrument.controllers.experiment_controller import ExperimentController, ExperimentParams
from instrument.devices.simulated_ import SimulatedCamera, SimulatedPump


def test_experiment_controller():
    """Test experiment controller."""
    camera = SimulatedCamera()
    pump = SimulatedPump("test_pump")
    
    camera.initialize()
    pump.initialize()
    
    controller = ExperimentController(camera, pump)
    
    # Test that controller can be instantiated
    assert controller is not None
    
    camera.close()
    pump.close()

