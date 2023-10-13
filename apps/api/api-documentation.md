# API Documentation

## GET `/api/drone-statuses/`

Returns array of drone status objects which consist of a text value.

example json:

```
{"droneStatuses":
  [
    {"text": "idle"},
    {"text": "delivering"},
    {"text": "owner"}
  ]
}
```
