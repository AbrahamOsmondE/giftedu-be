# API

Roughly follows [REST API](https://restfulapi.net/).
HTTP Method used:

| HTTP Method | CRUD Equivalent |
| ----------- | --------------- |
| POST        | Create          |
| GET         | Read            |
| PUT         | Update          |
| DELETE      | Delete          |

## Message Format

```json
{
  "error_code": 0,
  "message": "success",
  "data": {
    "id": 1,
    "title": "Exam Wishes",
    "open_date": "4 March 2021",
    "closed_date": "10 March 2021",
    "delivery_date": "12 March 2021",
    "is_closed": true
  }
}
```

## API List

### Donator

#### `GET /donator_api`

Request Parameter

null

Response Data

```json
[
    {
        "id": 1,
        "name": "Irvin",
        "phone_number": "12345678",
        "photo": "photo_1"
    },
    {
        "id": 2,
        "name": "Ferlita",
        "phone_number": "12345679",
        "photo": "photo_2"
    },
```

#### `POST /donator_api`

Request Parameter

```json
{
  "name": "Irvin",
  "phone_number": "12345678",
  "photo": "base64string"
}
```

Response Data

```json
{
  "id": 1
}
```

### `GET /donator_api/get_id/<username>`

Request Parameter

null

Response Data

```json
{
  "id": 1,
  "name": "Irvin",
  "phone_number": "12345678",
  "photo": "base64string"
}
```

#### `GET /donator_api/<donator_id>`

Request Parameter

null

Response Data

```json
{
  "id": 1,
  "name": "Irvin",
  "phone_number": "12345678",
  "photo": "base64string"
}
```

### Donee

#### `POST /donee_api`

Request Parameter

```json
{
  "name": "Ferlita Child Care",
  "phone_number": "12345679",
  "photo": "base64string",
  "description": "Jurong-based Toddler Care Centre, built in 2023."
}
```

Response Data

```json
{
  "id": 1
}
```

#### `GET /donee_api`

Request Parameter

null

Response Data

```json
[
  {
    "id": 1,
    "name": "Ferlita Child Care",
    "description": "Jurong-based Toddler Care Centre, built in 2023.",
    "phone_number": "12345679",
    "photo": "base64string"
  },
  {
    "id": 2,
    "name": "Vin Child Care",
    "description": "Tampines-based Toddler Care Centre, built in 2023.",
    "phone_number": "12345679",
    "photo": "base64string"
  }
]
```

#### `GET /donee_api/get_id/<donee_name>`

Request Parameter

null

Response Data

```json
{
  "id": 1,
  "name": "Ferlita Child Care",
  "phone_number": "12345679",
  "photo": "base64string",
  "description": "Jurong-based Toddler Care Centre, built in 2023."
}
```

#### `GET /donee_api/<donee_id>`

Request Parameter

null

Response Data

```json
{
  "id": 1,
  "name": "Ferlita Child Care",
  "phone_number": "12345679",
  "photo": "base64string",
  "description": "Jurong-based Toddler Care Centre, built in 2023.",
  "children": [
    {
      "id": 1,
      "name": "Bram",
      "description": "5-year-old boy from Johor Bahru",
      "photo": "base64string"
    },
    {
      "id": 2,
      "name": "Brem",
      "description": "6-year-old girl from Tekong Island",
      "photo": "base64string"
    }
  ]
}
```

#### `GET /donee_api/fund/<donee_id>`

Request Parameter

null

Response Data

```json
{
  "fund": 300
}
```

### Child

#### `POST /child_api`

Request Parameter

```json
{
  "name": "Bram",
  "description": "5-year-old boy from Johor Bahru",
  "photo": "base64string",
  "subscription_cost": 10,
  "donee_id": 1
}
```

Response Data

```json
{
  "id": 1
}
```

#### `GET /child_api`

Request Parameter

null

Response Data

```json
[
  {
    "id": 1,
    "name": "Bram",
    "description": "5-year-old boy from Johor Bahru",
    "photo": "base64string",
    "subscription_cost": 10,
    "donee": "Ferlita Child Care"
  },
  {
    "id": 2,
    "name": "Fer",
    "description": "6-year-old boy from Johor Bahru",
    "photo": "base64string",
    "subscription_cost": 12,
    "donee": "Ferlita Child Care"
  }
]
```

#### `GET /child_api/<child_id>`

Request Parameter

null

Response Data

```json
{
  "id": 1,
  "name": "Bram",
  "description": "5-year-old boy from Johor Bahru",
  "photo": "base64string",
  "subcription_cost": 10,
  "fund": 200,
  "donee": "Ferlita Child Care",
  "posts": [
    {
      "id": 1,
      "created": "2022-05-12T15:47:15.799693Z",
      "title": "Hello World",
      "text": "I just attended my first day at Nanyang Primary School."
    },
    {
      "id": 2,
      "created": "2022-05-12T15:47:15.799693Z",
      "title": "Hello Sunshine",
      "text": "I got an A+ for my math test today."
    }
  ]
}
```

#### `GET /child_api/subscription/<child_id>`

Request Parameter

null

Response Data

```json
{
  "fund": 200,
  "subscription": [
    {
      "id": 1,
      "name": "Irvin",
      "created": "2022-05-12T15:47:15.799693Z"
    },
    {
      "id": 2,
      "name": "Ferlita",
      "created": "2022-05-12T15:47:15.799693Z"
    }
  ]
}
```

### Post

#### `POST /post_api`

Request Parameter

```json
{
  "title": "Hello World",
  "text": "I just attended my first day at Nanyang Primary School.",
  "child_id": 1
}
```

Response Data

```json
{
  "id": 1,
  "date_created": "2022-05-12T15:47:15.799693Z"
}
```

#### `GET /post_api`

Request Parameter

null

Response Data

```json
[
  {
    "id": 1,
    "title": "Hello World",
    "text": "I just attended my first day at Nanyang Primary School.",
    "created": "2022-05-12T15:45:38.437490Z"
  },
  {
    "id": 2,
    "title": "Hello Sunshine",
    "text": "I got an A+ for my math test today.",
    "created": "2022-05-12T15:46:22.544806Z"
  }
]
```

#### `GET /post_api/<post_id>`

Request Parameter

null

Response Data

```json
{
  "id": 1,
  "title": "Hello World",
  "text": "I just attended my first day at Nanyang Primary School.",
  "created": "2022-05-12T15:47:15.799693Z"
}
```

### Subscription

#### `GET /subscription_api`

Request Parameter

| Parameter Name | Type | Required | Description               |
| -------------- | ---- | -------- | ------------------------- |
| `donator_id`   | int  | Depends  | User ID to filter against |
| `donee_id`     | int  | Depends  | User ID to filter against |

Response Data

```json
{
  "connected": true
}
```

#### `POST /subscription_api`

Request Parameter

```json
{
  "donator_id": 1,
  "donee_id": 1
}
```

Response Data

```json
{
  "id": 1,
  "date_created": "2022-05-12T15:47:15.799693Z"
}
```

#### `GET /subscription_api/donator/<donator_id>`

Request Parameter

null

Response Data

```json
[
  {
    "id": 1,
    "name": "Bram",
    "created": "2022-05-12T15:53:01.170111Z"
  },
  {
    "id": 2,
    "name": "Fer",
    "created": "2022-05-12T15:53:04.982439Z"
  }
]
```

#### `GET /subscription_api/child/<child_id>`

Request Parameter

null

Response Data

```json
[
  {
    "id": 1,
    "name": "Irvin",
    "created": "2022-05-12T15:53:01.170111Z"
  }
]
```

#### `GET /subscription_api/donee/<donee_id>`

Request Parameter

null

Response Data

```json
[
  {
    "id": 1,
    "name": "Irvin",
    "created": "2022-05-12T15:53:01.170111Z"
  },
  {
    "id": 2,
    "name": "Ferlita",
    "created": "2022-05-12T15:53:04.982439Z"
  }
]
```
