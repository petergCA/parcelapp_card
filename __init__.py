from homeassistant.core import HomeAssistant
from homeassistant.components.frontend import add_extra_js_url
from homeassistant.components.http import StaticPathConfig

URL_BASE = "/parcelapp_card"

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    await hass.http.async_register_static_paths([
        StaticPathConfig(
            URL_BASE,
            hass.config.path("custom_components/parcelapp_card/www"),
            cache_headers=False,
        )
    ])
    add_extra_js_url(hass, f"{URL_BASE}/parcelapp-card.js")
    return True
