"""Smoke tests for GUI components.

These are minimal tests to ensure GUI components can be instantiated
without errors. Full GUI testing would require pytest-qt.
"""

def test_gui_imports():
    """Test that GUI modules can be imported."""
    from instrument.gui.main_window import MainWindow
    from instrument.gui.widgets.camera_widget import CameraWidget
    from instrument.gui.widgets.pump_widget import PumpWidget
    from instrument.gui.widgets.status_widget import StatusWidget
    
    # If we get here, imports worked
    assert True

