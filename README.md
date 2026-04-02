# 📦 Parcel App — Lovelace Card

> A custom Lovelace card for Home Assistant that displays your [Parcel App](https://parcelapp.net) deliveries with carrier icons, tracking timelines, and tap-to-expand event history.

This card works alongside the [Parcel App integration](../parcelapp/) and reads directly from the `sensor.parcel_deliveries` entity.

---

## Features

- Per-delivery rows with carrier icon, description, latest status, and timing
- Tap to expand a full tracking event timeline with staggered animation
- Long-press to open the carrier's tracking page in a new tab
- Today's deliveries highlighted with a colored outline
- Delivered packages dimmed and sorted to the bottom automatically
- Compact mode for dense dashboards
- Fully isolated with Shadow DOM — no style bleed

---

## Installation

### Manual

1. Copy `parcelapp-card.js` and the `www/` folder (carrier images) into:
   ```
   config/custom_components/parcelapp_card/
   ```
2. Add `parcelapp_card` to your `configuration.yaml`:
   ```yaml
   parcelapp_card:
   ```
3. Restart Home Assistant — the card JS is registered and served automatically via `__init__.py`

> **Note:** Unlike most custom cards, this one does **not** need to be added to Lovelace resources manually. The integration registers it via `add_extra_js_url` on startup.

---

## Basic Usage

```yaml
type: custom:parcelapp-card
entity: sensor.parcel_deliveries
```

That's all you need. Everything else has sensible defaults.

---

## Full Configuration Example

```yaml
type: custom:parcelapp-card
entity: sensor.parcel_deliveries
title: My Packages
hide_delivered: true
show_today_only: false
show_icon: true
show_description: true
show_status: true
show_timing: true
show_events: true
highlight_today: true
sort: soonest
max_items: 10
compact: false
```

---

## Configuration Options

### Required

| Option | Type | Description |
|---|---|---|
| `entity` | `string` | **Required.** The entity ID of your Parcel App sensor — typically `sensor.parcel_deliveries` |

---

### Display Options

| Option | Type | Default | Description |
|---|---|---|---|
| `title` | `string` | `"Parcel Deliveries"` | Card header text. Set to an empty string `""` to hide the header |
| `show_icon` | `boolean` | `true` | Show the carrier logo icon on each row |
| `show_description` | `boolean` | `true` | Show the package description (label you set in Parcel App) |
| `show_status` | `boolean` | `true` | Show the latest tracking event text below the description |
| `show_timing` | `boolean` | `true` | Show the delivery timing line (e.g. *"2 Days until Delivery"*, *"Today is Delivery Day"*, *"Delivered"*) |
| `show_events` | `boolean` | `true` | Enable tap-to-expand full event timeline. When `false`, tapping a row does nothing |
| `highlight_today` | `boolean` | `true` | Adds a colored outline (using `--primary-color`) to packages arriving today |
| `compact` | `boolean` | `false` | Reduces row padding and icon size for a denser layout |

---

### Filtering Options

| Option | Type | Default | Description |
|---|---|---|---|
| `hide_delivered` | `boolean` | `false` | Hides packages marked as delivered from the list entirely |
| `show_today_only` | `boolean` | `false` | Shows only packages with `days_to_delivery === 0` that are not yet delivered — useful for a focused "arriving today" card |

> **Note:** `show_today_only` takes precedence over `hide_delivered`. If both are `true`, only undelivered same-day packages will appear.

---

### Sorting & Limiting

| Option | Type | Default | Options | Description |
|---|---|---|---|---|
| `sort` | `string` | `"soonest"` | `soonest` `today` `carrier` | Controls how deliveries are sorted. Delivered packages always sort to the bottom regardless of mode |
| `max_items` | `number` | `null` | Any positive integer | Limits the number of rows shown. Applied after filtering and sorting. `null` shows all |

#### Sort Mode Details

| Value | Behaviour |
|---|---|
| `soonest` | Sorts by `days_to_delivery` ascending — closest delivery date first |
| `today` | Puts today's arrivals at the very top, then falls back to soonest order |
| `carrier` | Sorts alphabetically by carrier code (e.g. `amzlus`, `fedex`, `ups`, `usps`) |

---

## Interactions

| Gesture | Action |
|---|---|
| **Tap** | Expands / collapses the tracking event timeline for that package |
| **Long press** (≥ 900ms) | Opens the carrier's tracking page in a new browser tab |

Long-press tracking links are supported for: **UPS, USPS, FedEx, OnTrac, UniUni, GSO/GLS, Amazon Logistics**.

---

## Supported Carriers

The card automatically displays the correct logo based on the `carrier_code` returned by the Parcel App API.

| Carrier Code | Carrier |
|---|---|
| `ups` | UPS |
| `usps` | USPS |
| `fedex` | FedEx |
| `amzlus` | Amazon Logistics |
| `gofous` | GoFor |
| `abf` | ABF Freight |
| `speedx` | SpeedX |
| `uniuni` | UniUni |
| `ontrac` | OnTrac |
| `gso` | GSO / GLS |
| `yun` / `yunexpress` | Yun Express |
| *(anything else)* | Generic package icon |

When a package is delivered, the icon switches to a delivered checkmark regardless of carrier.

---

## Example Configurations

### Minimal — no header, hide delivered

```yaml
type: custom:parcelapp-card
entity: sensor.parcel_deliveries
title: ""
hide_delivered: true
```

---

### Arriving Today dashboard tile

```yaml
type: custom:parcelapp-card
entity: sensor.parcel_deliveries
title: Arriving Today
show_today_only: true
compact: true
show_events: false
```

---

### Compact full list, sorted by carrier

```yaml
type: custom:parcelapp-card
entity: sensor.parcel_deliveries
title: All Packages
sort: carrier
compact: true
max_items: 20
```

---

### Status-only view (no icons, no timeline)

```yaml
type: custom:parcelapp-card
entity: sensor.parcel_deliveries
show_icon: false
show_events: false
highlight_today: true
```

---

## File Structure

```
custom_components/parcelapp_card/
├── __init__.py              # Registers the JS resource and static path
├── manifest.json            # Integration metadata
├── parcelapp-card.js        # The custom card element
└── www/
    └── parcel_app_images/
        ├── ups.png
        ├── usps.jpg
        ├── fedex.png
        ├── amazon_orange_v3.png
        ├── gofous.png
        ├── abf.png
        ├── speedx_v2.png
        ├── uniuni.png
        ├── ontrac.png
        ├── gls.png
        ├── yunexpress.png
        ├── delivered.png
        └── package.png
```

---

## Troubleshooting

**Card shows "Entity not found"**
- Confirm the `entity` value matches exactly, including the `sensor.` prefix
- Ensure the Parcel App integration is set up and the sensor has loaded

**Carrier icon is a generic box**
- The `carrier_code` from the API doesn't match a known carrier code
- Check the `carrier_code` value in `Developer Tools → States → sensor.parcel_deliveries` attributes

**Long-press tracking link doesn't open**
- The carrier may not have a supported tracking URL (see supported carriers table above)
- Some browsers block `window.open` from non-user-initiated events — try a different browser

**Card JS not loading after install**
- Restart Home Assistant fully (not just a config reload) so `__init__.py` can register the static path and JS URL
- Check your browser console for 404 errors on `/parcelapp_card/parcelapp-card.js`
