# API Documentation

## GET `/api/drone-statuses/`

**Response Data** consists of a `droneStatuses` array of drone status objects which consist of a `text` string. Example below.

```
{"droneStatuses":
  [
    {"text": "idle"},
    {"text": "delivering"},
    {"text": "owner"}
  ]
}
```
