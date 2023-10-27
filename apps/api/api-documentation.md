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

## GET `/api/drone-types/`

**Response Data** consists of a `droneTypes` array of drone type objects which consist of a `text` string and a `capacity` integer. Example below.

```
{"droneTypes":
  [
    {
      "text": "light",
      "capacity": 1
    },
    ...
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

## POST `/api/customer-login/`

**Request Body** consits of the following strings:

- `username`
- `password`

**Response Data** consists of a `success` boolean and, if false, a `message` string.

**Response Headers** has a `customer-token` string 128 characters in length if `success` on the response data is true.

## POST `/api/add-address/`

**Cookie Required**: `customer-token`

**Request Body** consists of the following strings:

- `lineOne`
- `lineTwo`
- `city`
- `state`
- `zipCode`

**Response Data** consists of a `success` boolean and an `id` integer of the new address. If the request body is bad, there will be an error because I don't want to fix that yet.

## GET `/api/my-addresses/`

**Cookie Required**: `customer-token`

**Response Data** consists of a `success` boolean and an `addresses` array. Example below.

```
{
	"success": true,
	"addresses": [
		{
			"id": 1,
			"lineOne": "1234 Champ Dr.",
			"lineTwo": "",
			"city": "Logan",
			"state": "UT",
			"zipCode": "84321",
			"customer": {
				"username": "paul",
				"firstName": "Paul",
				"lastName": "Harrison",
				"created": "2023-10-27T18:20:20.190Z"
			}
		}
	]
}
```
