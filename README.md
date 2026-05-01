# Flights Analytics Dashboard

## Project Overview

This is a Streamlit web application for flight search and basic analytics. The app allows users to search flights between cities and view visual insights about airlines and airport traffic using data stored in a MySQL database.

## Features

### Check Flights
- Select Source and Destination cities
- Search and view list of flights with details:
  - Airline
  - Route
  - Departure Time
  - Duration
  - Price

### Analytics
- **Airline Frequency**: Pie chart showing the number of flights operated by each airline
- **Busiest Airports**: Bar chart displaying the busiest airports based on total flight traffic (Source + Destination)

## Technologies Used

- Streamlit
- Plotly (for interactive charts)
- MySQL (via mysql.connector)
- Python

## Database Helper

The `DB` class in `dbhelper.py` handles all database operations:
- Fetching unique city names (Source & Destination)
- Searching flights between selected cities
- Getting airline-wise flight frequency
- Finding busiest airports using combined Source and Destination data

## Conclusion

This project successfully demonstrates how to build a simple yet functional flight analytics dashboard by integrating Streamlit with a MySQL database. It provides users an easy interface to search flights and visualize key insights such as airline distribution and airport traffic.

---

**Project Purpose**: Learning Streamlit, Plotly visualization, and MySQL integration in a web application.
