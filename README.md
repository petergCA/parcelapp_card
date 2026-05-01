# ParcelApp Card

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)

A Lovelace dashboard card for Home Assistant that displays your [Parcel App](https://parcelapp.net) deliveries with carrier icons, delivery timeline, and tap-to-expand event history.

## Requirements

Install the companion [Parcel App Delivery Tracker](https://github.com/petergCA/parcelapp) integration first — this card reads from the `sensor.parcel_deliveries` entity it creates.

## Features

- Carrier icons for UPS, USPS, FedEx, Amazon, OnTrac, ABF, SpeedX, UniUni, GLS, YunExpress, and more
- Tap a row to expand the full tracking event timeline
- Long-press to open the carrier's tracking page in a new tab
- Delivered items dim and sort to the bottom automatically
- Today's deliveries highlighted with a colored border
- Compact mode, sort options, and per-field visibility toggles

## Installation via HACS

1. In HACS, go to the three-dot menu → **Custom repositories**
2. Add `https://github.com/petergCA/parcelapp_card` with category **Dashboard**
3. Click **Install** on the ParcelApp Card entry
4. Verify that the `parcel_app_images` folder and its contents were created at `/config/www/community/parcelapp_card/parcel_app_images/`. If the folder is missing, create it manually and copy the images from the [`parcel_app_images/`](https://github.com/petergCA/parcelapp_card/tree/main/parcel_app_images) folder in this repository into it.
5. Add the card to your dashboard (no restart required)

## Manual Installation

1. Download `parcelapp_card.js` from the [latest release](https://github.com/petergCA/parcelapp_card/releases/latest)
2. Copy it to `/config/www/parcelapp_card/parcelapp_card.js`
3. In Home Assistant go to **Settings → Dashboards → Resources** and add:
   - URL: `/local/parcelapp_card/parcelapp_card.js`
   - Type: **JavaScript module**
4. Copy the `parcel_app_images/` folder from this repository to `/config/www/parcelapp_card/parcel_app_images/`. Verify the folder and its image files exist at that path — if not, create the `parcel_app_images` folder inside `/config/www/parcelapp_card/` and copy the images into it.

## Card Configuration

```yaml
type: custom:parcelapp-card
entity: sensor.parcel_deliveries
```

### All options

| Option | Default | Description |
|---|---|---|
| `entity` | *(required)* | The `sensor.parcel_deliveries` entity from the integration |
| `title` | `"Parcel Deliveries"` | Card header text |
| `hide_delivered` | `false` | Hide delivered items entirely |
| `show_today_only` | `false` | Show only items arriving today |
| `show_icon` | `true` | Show carrier icon |
| `show_description` | `true` | Show package description |
| `show_status` | `true` | Show latest tracking event text |
| `show_timing` | `true` | Show days-until-delivery line |
| `show_events` | `true` | Enable tap-to-expand event timeline |
| `highlight_today` | `true` | Highlight today's deliveries with a colored border |
| `max_items` | *(no limit)* | Maximum number of rows to display |
| `sort` | `"soonest"` | Sort order: `soonest`, `today`, or `carrier` |
| `compact` | `false` | Use compact row height |

### Full example

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
max_items: 10
sort: soonest
compact: false
```
