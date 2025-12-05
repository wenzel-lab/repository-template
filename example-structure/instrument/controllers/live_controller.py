"""Live view controller.

Handles streaming camera previews, toggling illumination, and simple focus controls.
"""

from __future__ import annotations

from instrument.devices.base import Camera


class LiveController:
    """Controller for live camera view and basic controls."""
    
    def __init__(self, camera: Camera) -> None:
        """Initialize live controller.
        
        Args:
            camera: Camera device to control.
        """
        self._camera = camera
        self._is_live = False
    
    def start_live(self) -> None:
        """Start live view streaming."""
        self._is_live = True
        # Implementation: start camera streaming, set up callbacks, etc.
    
    def stop_live(self) -> None:
        """Stop live view streaming."""
        self._is_live = False
        # Implementation: stop camera streaming
    
    def grab_frame(self) -> any:  # Use np.ndarray in real code
        """Grab a frame from the camera.
        
        Returns:
            Camera frame.
        """
        return self._camera.grab_frame()
    
    @property
    def is_live(self) -> bool:
        """Check if live view is active."""
        return self._is_live

