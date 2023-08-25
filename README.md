# Weather Data ETL Application

## Description
The Weather Data ETL Application is a simple RESTful tool that performs Extract, Transform, and Load (ETL) operations on forecasted weather data from multiple sources. It extracts weather data, transforms it into a standardized format, and loads it into a database for further analysis.

## Features
1. Extracts weather data from various sources up to 14 days, including JSON and XML.
2. Transforms and normalizes the data to a common format.
3. Aggregates the transformed data by averaging the weather parameters.
4. Loads the transformed data into a SQLite database.
5. Supports updating existing data if records with the same timestamp already exist.

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

#### Sample Response
```json
{
"message": "ETL Successful"
}
```

### Query Weather Data

- **HTTP Method:** `GET`
- **Endpoint:** `/extract-transform-load`
- **Parameters:**
  - `lat` (required): Latitude of the location
  - `long` (required): Longitude of the location
  - `date` (required): Date in YYYY-MM-DD format
  - **Response Messages:**

    | Message                      | Code |
    |------|--------------------------|
    | Successfully queried weather data                  | 200  |
    | Failed to query weather data | 500  |
    | Invalid request parameters   | 400  |

#### Sample Response
```json
{
  "date": "2023-08-25",
  "hourly_data": {
    "00:00": {
      "precipitation": 0.0,
      "temperature": 21.65,
      "wind_direction": 81.9,
      "wind_speed": 7.55
    },
    "01:00": {
      "precipitation": 0.15,
      "temperature": 21.4,
      "wind_direction": 60.8,
      "wind_speed": 8.5
    },
    "02:00": {
      "precipitation": 0.0,
      "temperature": 21.15,
      "wind_direction": 61.8,
      "wind_speed": 7.6
    },
    .
    .
    .
    .
    "23:00": {
      "precipitation": 0.0,
      "temperature": 21.75,
      "wind_direction": 105.8,
      "wind_speed": 9.25
    }
  },
  "latitude": 52.52,
  "longitude": 13.42
}
```

