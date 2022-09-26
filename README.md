# Hacker News Miniblog Project

This project is aimed at synchronizing with the live hacker news api to provide a smooth interactive space for a user to search all the news content based on their preferred text keywords or possibly by the news type.

Below are the avaialable Restful endpoints from this flask application;

## Fetch All News Items From Database

Used to fetch all the data avaialable in the database in order of the newest entries being at the top.

**URL** : `/api/v1/news`
**METHOD** : `GET`

## Success Response

**Code** : `200 OK`

**Content example**

```json
{
  "message": "93144b288eb1fdccbe46d6fc0f241a51766ecd3d",
  "data": [],
  "code": 200
}
```

## Error Response

**Condition** : Invalid request

**Code** : `400 BAD REQUEST`

```

Test Command - `python -m unittest tests`
```
