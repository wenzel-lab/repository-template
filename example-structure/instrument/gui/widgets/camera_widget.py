"""Camera control widget.

Provides UI for camera settings and live view.
"""

from __future__ import annotations

from qtpy.QtWidgets import QPushButton, QVBoxLayout, QWidget

from instrument.controllers.live_controller import LiveController


class CameraWidget(QWidget):
    """Widget for camera control."""
    
    def __init__(self, live_controller: LiveController) -> None:
        """Initialize camera widget.
        
        Args:
            live_controller: Live view controller.
        """
        super().__init__()
        self._live_controller = live_controller
        self._setup_ui()
    
    def _setup_ui(self) -> None:
        """Set up the widget UI."""
        layout = QVBoxLayout()
        
        # Example: Add live view toggle button
        self._live_button = QPushButton("Start Live")
        self._live_button.clicked.connect(self._toggle_live)
        layout.addWidget(self._live_button)
        
        # Add more camera controls here (exposure, gain, etc.)
        
        self.setLayout(layout)
    
    def _toggle_live(self) -> None:
        """Toggle live view on/off."""
        if self._live_controller.is_live:
            self._live_controller.stop_live()
            self._live_button.setText("Start Live")
        else:
            self._live_controller.start_live()
            self._live_button.setText("Stop Live")

