"""Pump control widget.

Provides UI for pump flow rate control.
"""

from __future__ import annotations

from qtpy.QtWidgets import QDoubleSpinBox, QLabel, QVBoxLayout, QWidget

from instrument.devices.base import Pump


class PumpWidget(QWidget):
    """Widget for pump control."""
    
    def __init__(self, pump: Pump) -> None:
        """Initialize pump widget.
        
        Args:
            pump: Pump device to control.
        """
        super().__init__()
        self._pump = pump
        self._setup_ui()
    
    def _setup_ui(self) -> None:
        """Set up the widget UI."""
        layout = QVBoxLayout()
        
        # Example: Add flow rate control
        layout.addWidget(QLabel("Flow Rate (uL/min):"))
        self._flow_rate_spinbox = QDoubleSpinBox()
        self._flow_rate_spinbox.setRange(0.0, 10000.0)
        self._flow_rate_spinbox.setValue(self._pump.get_flow_rate())
        self._flow_rate_spinbox.valueChanged.connect(self._on_flow_rate_changed)
        layout.addWidget(self._flow_rate_spinbox)
        
        # Add more pump controls here
        
        self.setLayout(layout)
    
    def _on_flow_rate_changed(self, value: float) -> None:
        """Handle flow rate change.
        
        Args:
            value: New flow rate value.
        """
        self._pump.set_flow_rate(value)

