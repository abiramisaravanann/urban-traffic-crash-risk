# 🚦 Urban Traffic Crash Risk & Public Intelligence System

An end-to-end data engineering and analytics project designed to analyze **urban traffic crashes, identify high-risk areas, understand accident patterns, and generate actionable insights for road-safety analysis**.

The project uses real-world traffic crash data from the **Chicago Data Portal through the Socrata API** and processes the data through a **Bronze–Silver–Gold data pipeline** using Apache Spark and Databricks.

---

## 📌 Project Overview

Urban traffic accidents are influenced by several factors such as location, time, road conditions, weather, traffic conditions, and vehicle or crash characteristics.

This project aims to transform raw traffic crash data into meaningful information by:

* Collecting real-world traffic crash data through an API
* Storing and organizing raw data using a **Bronze layer**
* Cleaning and transforming the data in the **Silver layer**
* Creating analytics-ready datasets in the **Gold layer**
* Identifying accident frequency and severity patterns
* Analyzing fatality and injury-related trends
* Identifying high-risk locations and zones
* Generating structured traffic safety reports
* Supporting data-driven urban road-safety decisions

---

## 🎯 Objectives

The main objectives of the project are:

1. **Collect** real-world urban traffic crash data.
2. **Build** a scalable data ingestion pipeline.
3. **Clean and transform** raw crash data.
4. **Analyze** accident frequency and severity.
5. **Identify** high-risk locations.
6. **Analyze** temporal and regional accident patterns.
7. **Generate** meaningful traffic safety insights.
8. **Provide** analytics-ready data for visualization and reporting.

---

## 🏗️ System Architecture

```text
                    ┌─────────────────────────┐
                    │   Chicago Data Portal   │
                    │      Socrata API        │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │     Data Ingestion       │
                    │       Python / API       │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │      BRONZE LAYER       │
                    │       Raw Data           │
                    │    Delta / Data Lake     │
                    └────────────┬────────────┘
                                 │
                         Data Cleaning
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │      SILVER LAYER       │
                    │ Cleaned & Transformed   │
                    │         Data             │
                    └────────────┬────────────┘
                                 │
                       Aggregation / Analysis
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │       GOLD LAYER        │
                    │ Analytics-Ready Data    │
                    └────────────┬────────────┘
                                 │
                ┌────────────────┼────────────────┐
                │                │                │
                ▼                ▼                ▼
          Risk Analysis     Trend Analysis    Location Analysis
                │                │                │
                └────────────────┼────────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │   Reports / Dashboard   │
                    │     Power BI / BI       │
                    └─────────────────────────┘
```

---

# 🔄 Data Pipeline

## 1. Data Source

The project uses real-world **Chicago traffic crash data** obtained through the **Socrata API**.

The API provides structured information related to traffic crashes, including attributes associated with:

* Crash location
* Crash date and time
* Injuries
* Fatalities
* Crash circumstances
* Roadway/location information
* Vehicle-related information
* Other crash characteristics

The API-based approach makes it possible to retrieve data programmatically rather than manually downloading datasets.

---

## 2. Data Ingestion

The first stage of the pipeline retrieves traffic crash data from the Socrata API.

### Ingestion process

```text
API Request
     ↓
Retrieve JSON Data
     ↓
Convert to Structured Data
     ↓
Store Raw Dataset
     ↓
Bronze Layer
```

Python is used for API interaction and initial data handling.

---

# 🥉 Bronze Layer

The **Bronze layer** contains the raw data collected directly from the source.

The main purpose of this layer is to preserve the original dataset before applying transformations.

### Responsibilities

* Store raw API data
* Preserve original information
* Maintain data traceability
* Provide a reliable source for downstream processing

```text
Socrata API
     ↓
Raw JSON / Data
     ↓
Bronze Delta Table
```

No major business transformations are applied at this stage.

---

# 🥈 Silver Layer

The Silver layer contains **cleaned and transformed data**.

The raw crash dataset may contain:

* Missing values
* Duplicate records
* Inconsistent formats
* Unnecessary columns
* Incorrect data types
* Invalid or incomplete records

These issues are handled during the transformation stage.

### Silver-layer operations

* Data cleaning
* Null-value handling
* Duplicate removal
* Data-type conversion
* Column selection
* Date/time transformation
* Standardization of values
* Data validation

```text
Bronze Data
     ↓
Cleaning
     ↓
Transformation
     ↓
Validation
     ↓
Silver Data
```

Apache Spark / PySpark is used to perform scalable data processing.

---

# 🥇 Gold Layer

The Gold layer contains **business-ready and analytics-ready datasets**.

Instead of working directly with individual crash records, the Gold layer creates meaningful aggregated information.

### Example analytics

#### Accident Frequency

Analyze:

* Number of crashes
* Crashes by year
* Crashes by month
* Crashes by day
* Crashes by time period

#### Injury Analysis

Analyze:

* Total injuries
* Injury trends
* Injury severity
* Injuries by location

#### Fatality Analysis

Analyze:

* Number of fatal crashes
* Fatality trends
* Fatalities by region
* High-fatality areas

#### Location Risk Analysis

Identify:

* High-crash locations
* High-injury locations
* High-fatality locations
* Geographical accident patterns

---

# 📊 Risk Analysis

One of the major objectives of the project is to identify **high-risk traffic zones**.

A location can be considered high-risk based on factors such as:

```text
Crash Frequency
       +
Injury Count
       +
Fatality Count
       +
Historical Crash Patterns
       ↓
Traffic Risk Insights
```

This allows the processed data to highlight areas that may require additional traffic-safety attention.

---

# ⏰ Temporal Analysis

Traffic crashes are also analyzed according to time.

The project can identify patterns such as:

* Peak crash hours
* Day-wise crash frequency
* Monthly trends
* Yearly trends
* Weekday vs weekend patterns

This helps understand **when traffic crashes occur most frequently**.

---

# 📍 Geographical Analysis

Location-based analysis is used to understand the spatial distribution of crashes.

The analysis focuses on:

* Crash hotspots
* High-risk areas
* Areas with repeated crashes
* Injury-prone regions
* Fatality-prone regions

These insights can support urban traffic planning and road-safety analysis.

---

# 🧠 Public Intelligence / Sentiment Component

The project also includes a public-intelligence component intended to complement crash statistics with public-facing information.

The purpose is to provide a broader understanding of traffic-related concerns rather than relying only on numerical accident statistics.

This can help combine:

```text
Traffic Crash Data
        +
Public Information / Sentiment
        ↓
Public Intelligence
        ↓
Better Traffic Safety Insights
```

---

# 🛠️ Technologies Used

| Technology                 | Purpose                                 |
| -------------------------- | --------------------------------------- |
| **Python**                 | API ingestion and data processing       |
| **PySpark**                | Large-scale data transformation         |
| **Apache Spark**           | Distributed data processing             |
| **Databricks**             | Data engineering and Spark execution    |
| **Delta Lake**             | Reliable storage and table management   |
| **Socrata API**            | Real-world traffic crash data source    |
| **Data Lake Architecture** | Layered data storage                    |
| **Power BI**               | Data visualization and reporting        |
| **GitHub**                 | Source-code and project version control |

---

# 🗂️ Project Structure

```text
Urban-Traffic-Crash-Risk-System/
│
├── README.md
│
├── data/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── notebooks/
│   ├── data_ingestion
│   ├── data_cleaning
│   ├── data_transformation
│   └── data_analysis
│
├── src/
│   ├── ingestion/
│   ├── transformation/
│   └── analysis/
│
├── dashboards/
│   └── traffic_crash_dashboard
│
├── reports/
│   └── traffic_risk_reports
│
└── requirements.txt
```

---

# 🔍 Key Data Engineering Concepts Demonstrated

This project demonstrates practical knowledge of:

* REST API data ingestion
* JSON data processing
* ETL pipeline development
* Data Lake architecture
* Medallion architecture
* Bronze–Silver–Gold architecture
* Distributed data processing
* PySpark DataFrames
* Data cleaning
* Data transformation
* Data aggregation
* Delta Lake
* Databricks
* Data quality handling
* Analytics-ready dataset creation
* Business intelligence and visualization

---

# 📈 Expected Insights

The processed data can be used to answer questions such as:

* Which locations experience the highest number of crashes?
* Which areas have the highest injury rates?
* Which locations have more fatal crashes?
* During which hours do crashes occur most frequently?
* Which months have higher crash frequencies?
* Are crashes concentrated in particular geographical areas?
* Which locations should be considered high-risk?
* What patterns can be observed from historical crash data?

---

# 🌍 Real-World Applications

The insights generated from this project can potentially support:

* Urban traffic planning
* Road-safety analysis
* Identification of accident hotspots
* Emergency response planning
* Infrastructure improvement
* Traffic management
* Public safety decision-making
* Data-driven city planning

The project is intended as an **analytical decision-support system**, not as a replacement for official traffic-safety assessments.

---

# 🚀 Future Enhancements

Possible future improvements include:

* Real-time crash data ingestion
* Kafka-based streaming pipeline
* Automated scheduled API ingestion
* Advanced geospatial analysis
* Machine-learning-based crash-risk prediction
* Weather-data integration
* Traffic-density integration
* Real-time risk dashboards
* Automated alerts for high-risk areas
* More advanced public sentiment analysis
* Cloud deployment and orchestration

---

# 💡 Project Highlights

### Data Engineering

Built a layered data pipeline to transform raw API data into structured, analytics-ready datasets.

### Big Data Processing

Used PySpark and Databricks to process and transform large-scale traffic crash data efficiently.

### Data Analytics

Analyzed crash frequency, injuries, fatalities, temporal patterns, and geographical risk.

### Decision Support

Converted raw traffic data into meaningful insights that can support urban road-safety analysis.

---

# 👩‍💻 Author

**Abirami S**

B.Tech – Artificial Intelligence & Data Science
JJ College of Engineering and Technology, Trichy

GitHub: `abiramisaravanann`

---

## ⭐ Conclusion

The **Urban Traffic Crash Risk & Public Intelligence System** demonstrates how real-world public datasets can be transformed into useful insights using modern data engineering and analytics technologies.

The project follows a structured:

**API → Bronze → Silver → Gold → Analytics → Visualization**

architecture to convert raw traffic crash records into meaningful information about **accident trends, injuries, fatalities, and high-risk urban areas**.
