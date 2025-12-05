"""Tests for device implementations."""

from instrument.devices.simulated_ import SimulatedCamera, SimulatedPump, SimulatedValve


def test_simulated_camera():
    """Test simulated camera."""
    camera = SimulatedCamera()
    camera.initialize()
    
    frame = camera.grab_frame()
    assert frame is not None
    assert frame.shape == (1024, 1024)
    
    camera.close()


def test_simulated_pump():
    """Test simulated pump."""
    pump = SimulatedPump("test_pump")
    pump.initialize()
    
    pump.set_flow_rate(100.0)
    assert pump.get_flow_rate() == 100.0
    
    pump.close()


def test_simulated_valve():
    """Test simulated valve."""
    valve = SimulatedValve("test_valve", num_channels=4)
    valve.initialize()
    
    valve.switch_channel(2)
    assert valve.get_current_channel() == 2
    
    valve.close()

