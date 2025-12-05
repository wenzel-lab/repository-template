"""Status display widget.

Shows instrument status, logs, and system information.
"""

from __future__ import annotations

from qtpy.QtWidgets import QLabel, QVBoxLayout, QWidget


class StatusWidget(QWidget):
    """Widget for displaying instrument status."""
    
    def __init__(self) -> None:
        """Initialize status widget."""
        super().__init__()
        self._setup_ui()
    
    def _setup_ui(self) -> None:
        """Set up the widget UI."""
        layout = QVBoxLayout()
        
        # Example: Add status label
        status_label = QLabel("Status: Ready")
        layout.addWidget(status_label)
        
        # Add more status information here (logs, system info, etc.)
        
        self.setLayout(layout)

