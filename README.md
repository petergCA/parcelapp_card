# ParcelApp Card

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)

A Lovelace card for Home Assistant that displays your [Parcel App](https://parcelapp.net) deliveries with carrier icons, delivery timeline, and tap-to-expand event history.

## Features

- Carrier icons for UPS, USPS, FedEx, Amazon, OnTrac, and more
- Tap a row to expand the full tracking event timeline
- Long-press to open the carrier's tracking page in a new tab
- Delivered items dim and sort to the bottom automatically
- Today's deliveries highlighted with a colored border
- Compact mode, sort options, and per-field visibility toggles

## Requirements

Install the companion [Parcel App Delivery Tracker](https://github.com/peterlgray/ha-parcelapp) integration first — this card reads from the `sensor.parcel_deliveries` entity it creates.

## Installation via HACS

1. Add this repository as a **Custom Repository** in HACS (Category: Integration)
2. Install **ParcelApp Card**
3. Restart Home Assistant
4. Add `parcelapp_card:` to your `configuration.yaml` and restart again

## Card Configuration

```yaml
type: custom:parcelapp-card
entity: sensor.parcel_deliveries
```

### Full options

```yaml
type: custom:parcelapp-card
entity: sensor.parcel_deliveries
title: My Packages          # card header (default: "Parcel Deliveries")
hide_delivered: true        # hide delivered items (default: false)
show_today_only: false      # show only items arriving today (default: false)
show_icon: true             # show carrier icon (default: true)
show_description: true      # show package description (default: true)
show_status: true           # show latest tracking event (default: true)
show_timing: true           # show days-until-delivery line (default: true)
show_events: true           # enable tap-to-expand timeline (default: true)
highlight_today: true       # outline today's deliveries (default: true)
max_items: 10               # limit number of rows shown (default: no limit)
sort: soonest               # soonest | today | carrier (default: soonest)
compact: false              # compact row height (default: false)
```
