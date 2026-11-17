import lib8relind

FULL_NAME = "Eight Relays"
LINK = (
    "https://sequentmicrosystems.com/products/8-relays-stackable-card-for-raspberry-pi"
)
API = lib8relind
DOMAIN = "sm8relind"
NAME_PREFIX = "sm4ri"
SM_MAP = {
    "switch": {
        "relay": {
            "chan_no": 8,
            "com": {"get": "get", "set": "set"},
        }
    },
}
