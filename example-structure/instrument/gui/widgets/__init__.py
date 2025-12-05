"""GUI widgets.

One widget per file - not monolithic. Each widget handles a specific
aspect of the user interface.
"""

from .camera_widget import CameraWidget
from .pump_widget import PumpWidget
from .status_widget import StatusWidget

__all__ = ["CameraWidget", "PumpWidget", "StatusWidget"]

