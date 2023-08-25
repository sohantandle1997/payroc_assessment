# Weather Data ETL Application

## Description
The Weather Data ETL Application is a simple RESTful tool that performs Extract, Transform, and Load (ETL) operations on forecasted weather data from multiple sources. It extracts weather data, transforms it into a standardized format, and loads it into a database for further analysis.

## Features
1. Extracts weather data from various sources up to 14 days, including JSON and XML.
2. Transforms and normalizes the data to a common format.
3. Loads the transformed data into a SQLite database.
4. Supports updating existing data if records with the same timestamp already exist.

## Data Sources
1. https://open-meteo.com/ - JSON format
2. https://www.weatherapi.com/ - XML format

## Endpoints

### Extract Transform Load

- **HTTP Method:** `GET`
- **Endpoint:** `/extract-transform-load`
- **Parameters:**
    - `lat` (required): Latitude of the location
    - `long` (required): Longitude of the location
    - `forecast-days` (required): Number of days forecast from today
- **Response Messages:**

  | Message            | Code |
  |------|--------------------------|
  | ETL Successful | 200  |
  | Failed to perform ETL    | 500  |
  | Invalid forecast-days, max forecast upto 14 days    | 400  |
  | Invalid request parameters      | 400  |

