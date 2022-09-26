# Hacker News Miniblog Project

This project is aimed at synchronizing with the live hacker news api to provide a smooth interactive space for a user to search all the news content based on their preferred text keywords or possibly by the news type.

Below are the avaialable Restful endpoints from this flask application;

## Fetch All News Items From Database

Used to fetch all the data avaialable in the database in order of the newest entries being at the top.

**URL** : `/api/v1/news`
**METHOD** : `GET`

### Success Response

**Code** : `200 OK`

**Content example**

```json
{
  "message": "Fetch successfull",
  "data": [], // Data in a list
  "code": 200
}
```

## Fetch All News Items By Filter (by text or type )

Used to fetch data avaialable in the database based on text search or by the news type (story, job or poll).

**URL** : `/api/v1/news`
**METHOD** : `POST`

### Success Response

**Code** : `200 OK`

**Content example**

```json
{
  "message": "Fetch successfull",
  "data": [], // Data in a list
  "code": 200
}
```

## Fetch Single Item From Database

Used to fetch a single news data from the database.

`<news_id> is unique news id`

**URL** : `/api/v1/news/<news_id>`
**METHOD** : `GET`

### Success Response

**Code** : `200 OK`

**Content example**

```json
{
  "message": "Item Fetch Success",
  "data": item, // Data object
  "code": 200
}
```

## Create New Item To Database

Used to create/write a new data into database with a new unique id.

`<news_id> is not neccessarily valid`

**URL** : `/api/v1/news/<news_id>`
**METHOD** : `POST`

### Success Response

**Code** : `200 OK`

**Content example**

```json
{
  "message": "New Item Created",
  "data": true, // (Bool) created data
  "code": 200
}
```

## RUN ALL TESTS

This command run all the three (3) scripts to validate all the app functions to be working fine.

**COMMAND** : `python -m unittest tests`

## Creator

Codefred - https://codefred.me
