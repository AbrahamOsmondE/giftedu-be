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
{
    "donees": [
    {
        "id": 1,
        "name": "Ferlita Child Care",
        "photo": "base64string",
        "description": "Jurong-based Toddler Care Centre, built in 2023.",
    },
    {
        "id": 2,
        "name": "Fer Child Care",
        "photo": "base64string",
        "description": "Tampines-based Toddler Care Centre, built in 2024.",
    }
    ]
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
  "subcription_cost": 10,
  "donee_id": 1
}
```

Response Data
```json
{
  "id": 1
}
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
  "posts": [
      {
          "id": 1,
          "created": "01/01/2022",
          "title": "Hello World",
          "text": "I just attended my first day at Nanyang Primary School."
      },
      {
          "id": 2,
          "created": "02/01/2022",
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
      "created": "01/01/2022"
    },
    {
      "id": 2,
      "name": "Ferlita",
      "created": "02/01/2022"
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
  "date_created": "01/01/2022"
}
```

#### `GET /post_api/<post_id>`

Request Parameter

null

Response Data

```json
{
    "id": 1,
    "created": "01/01/2022",
    "title": "Hello World",
    "text": "I just attended my first day at Nanyang Primary School."
}
```

### Subscription

#### `GET /subscription_api`

Request Parameter

| Parameter Name    | Type | Required | Description               |
| ----------------- | ---- | -------- | ------------------------- |
| `donator_id`      | int  | Depends  | User ID to filter against |
| `donee_id`      | int  | Depends  | User ID to filter against |

Response Data

```json
{
    "connected": true
}
```