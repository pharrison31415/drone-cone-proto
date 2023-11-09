# API Documentation
**All requests and responses are in JSON**
## GET `/api/cone-types/`,`/api/ice-cream-types`,`/api/topping-types`

**Response Data** consists of a `success` boolean and a `coneTypes`, `iceCreamTypes`, or `toppingTypes` array of those inventory objects with public data (no unit costs or stock count). Example below.

```
{
  "success": true,
  "coneTypes": [
    {
      "name": "Waffle",
      "imageUrl": "#"
    },
    ...
  ],
}
```

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

## POST `/api/new-customer/`, `/api/new-owner`

**Request Body** consists of the following strings:

- `username`
- `password`
- `firstName`
- `lastName`

**Response Data** consists of a `success` boolean and, if false, a `message` string. If the request body is bad, there will be an error because I don't want to fix that yet.

## POST `/api/customer-login/`, `/api/manager-login`, `/api/owner-login`

**Request Body** consits of the following strings:

- `username`
- `password`

**Response Data** consists of a `success` boolean and, if false, a `message` string.

**Response Headers** has a `customer-token`, `manager-token`, or `owner-token` string 128 characters in length if `success` on the response data is true. If the request body is bad, there will be an error because I don't want to fix that yet.

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
    },
    ...
  ]
}
```

## POST `/api/add-drone/`

**Cookie Required**: `owner-token`

**Request Body** consists of the following strings:

- `name`
- `status` (`"idle"`, `"delivering"`, `"owner"`)
- `droneType` (`"light"`, `"medium"`, `"heavy"`)

**Response Data** consists of a `success` boolean and an `id` integer of the new drone. If the request body is bad, there will be an error because I don't want to fix that yet.

## GET `/api/my-drones/`

**Cookie Required**: `owner-token`

**Response Data** consists of a `success` boolean and a `drones` array. Example below.

```
{
  "success": true,
  "drones": [
    {
      "id": 1,
      "name": "Obama's favorite toy",
      "status": {
        "text": "idle"
      },
      "droneType": {
        "text": "heavy",
        "capacity": 8
      },
      "owner": {
        "username": "paul",
        "firstName": "Paul",
        "lastName": "Harrison",
        "created": "2023-10-31T02:55:37.309Z"
      },
      "lastUse": "1970-01-01T00:00:00Z",
      "created": "2023-10-31T02:55:54.393Z"
    },
    ...
  ]
}
```

## PATCH `/api/update-drone`

**Cookie Required**: `owner-token`

**Request Body** must contain the integer `id` of the drone to update. The following properties are optional to include for updating. If they are not included.

- `name`
- `status` (`"idle"`, `"delivering"`, `"owner"`)
- `droneType` (`"light"`, `"medium"`, `"heavy"`)

Note that if a drone's status is set to `"delivering"`, the status is unable to be changed. This is reflected in the response datea.

**Response Data** consists of a `success` boolean and a drone `id`. If the request body is bad, there will be an error because I don't want to fix that yet.

## PATCh `/api/update_inventory`

**Cookie Required**: `manager-token`

**Request Body** must contain the integer `id` of the inventory item to update. The following are properties that can be included for updating.
- `name`
- `amountChange` (positive or negative int. This is how much of the item to add or subtract to the total inventory amount)
- `price` (postive float. the new unit price for the item)

**Response Data** consists of a `success` boolean.

## GET `/api/inventory/`

**Cookie Required**: `manager-token`

**Response Data** consists of a `success` boolean and an `inventory` object consisting of `coneTypes`, `iceCreamTypes`, and `toppingTypes`. Example below.

```
{
  "success": true,
  "inventory": {
    "coneTypes": [
      {
        "name": "Waffle",
        "quantity": 500,
        "unitCost": 48,
        "imageUrl": "#"
      },
      ...
    ],
    ...
  }
}
```

## POST `/api/new-order/`

**Cookie Optional**: `customer-token`

**Request Body** must contain a non-empty array of `cones`, each of which is an object with a valid `coneType`, `iceCreamType`, and `toppingType`. If a valid `customer-token` cookie is provided, the `addressId` must be specified. If no valid `customer-token` cookie is provided, a `guestAddress` must be provided. The guest address's format is in the same format as used in `/api/add-address/`.

**Response Data** will contain a `success` boolean. If false, a `message` string will be provided. If true, an `orderId` integer and `created` date will be provided. If the request body is bad, there will be an error because I don't want to fix that yet.

**Response Headers** has a `order-token` string 128 characters in length if `success` on the response data is true. If the request body is bad, there will be an error because I don't want to fix that yet.

## POST `/api/order-delivered/`

**Reason:** This operation marks the drones used for the order as being available for another delivery. We haven't figured out a way to make them automatically available after 10 minutes. We are still working on it. :(

**Cookie Required** `order-token`

**Response Data** will contain a `success` boolean of true.

## POST `/api/new-message/`

**Request Body** must contain a `content` string (max length 1024 characters), and an `email` string (max length 128 characters).

**Response Data** will contain a `success` boolean. If the request body is bad, there will be an error because I don't want to fix that yet.
