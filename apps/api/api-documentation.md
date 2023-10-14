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

## POST `/api/new-customer/`

**Request Body** consists of the following strings:

- `username`
- `password`
- `firstName`
- `lastName`

**Response Data** consists of a `success` boolean and, if false, a `message` string.
