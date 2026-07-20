# ParcelApp Card

> [!IMPORTANT]
> **⚠️ DEPRECATED — this card is now bundled with the [Parcel App Delivery Tracker](https://github.com/petergCA/parcelapp) integration (v0.2.0+).**
>
> The integration serves the card and registers the dashboard resource automatically. A separate card install is no longer needed, and this repository is archived and will receive no further updates.

## Migrating

1. Update the [Parcel App Delivery Tracker](https://github.com/petergCA/parcelapp) integration to **v0.2.1 or later** in HACS
2. Restart Home Assistant
3. Remove **ParcelApp Card** from HACS (this also removes its dashboard resource entry)
4. Hard-refresh your browser (Ctrl/Cmd+Shift+R)

Your existing dashboard configuration keeps working unchanged — the bundled card uses the same `custom:parcelapp-card` element and the same options:

```yaml
type: custom:parcelapp-card
entity: sensor.parcel_deliveries
```

## Documentation

All card documentation — configuration options, features, and troubleshooting — now lives in the [integration README](https://github.com/petergCA/parcelapp#bundled-dashboard-card).

## About

This was a Lovelace dashboard card for Home Assistant displaying [Parcel App](https://parcelapp.net) deliveries with carrier icons, a delivery timeline, and tap-to-expand event history. It lives on inside the integration.
