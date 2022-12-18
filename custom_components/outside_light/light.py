"""Platform for light integration"""
from __future__ import annotations
import sys
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from . import DOMAIN

sys.path.append("custom_components/new_light")
from new_light import NewLight


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the light platform."""
    # We only want this platform to be set up via discovery.
    if discovery_info is None:
        return
    ent = OutsideLight()
    add_entities([ent])


class OutsideLight(NewLight):
    """Outside Light."""

    def __init__(self) -> None:
        """Initialize Outside Light."""
        super(OutsideLight, self).__init__(
            "Outside", domain=DOMAIN, debug=False, debug_rl=False
        )

        self.entities["light.outside_group"] = None
        self.switch = "Outside Switch"
