"""Main application window.

This is the top-level GUI window that contains all widgets and controls.
"""

from __future__ import annotations

from qtpy.QtWidgets import QMainWindow, QTabWidget, QVBoxLayout, QWidget

from instrument.controllers.live_controller import LiveController
from instrument.gui.widgets.camera_widget import CameraWidget
from instrument.gui.widgets.status_widget import StatusWidget


class MainWindow(QMainWindow):
    """Main application window."""
    
    def __init__(self, live_controller: LiveController) -> None:
        """Initialize main window.
        
        Args:
            live_controller: Live view controller.
        """
        super().__init__()
        self._live_controller = live_controller
        self.setWindowTitle("Example Instrument Control")
        self._setup_ui()
    
    def _setup_ui(self) -> None:
        """Set up the user interface."""
        central_widget = QWidget()
        layout = QVBoxLayout()
        
        # Create tabbed interface
        tabs = QTabWidget()
        tabs.addTab(CameraWidget(self._live_controller), "Camera")
        tabs.addTab(StatusWidget(), "Status")
        
        layout.addWidget(tabs)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

