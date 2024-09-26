=========
Databases
=========

.. figure:: images/database_types.png
   :alt: Database types
   
   `Source <https://unihost.com/blog/database-server/>`_

SQLite
======
SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. 
SQLite is the most used database engine in the world. SQLite is built into all mobile phones and most computers and comes 
bundled inside countless other applications that people use every day.

`Official Website <https://www.sqlite.org/>`_

Commands
--------

*  ``sqlite3 <database_file>`` - Open a database file (e.g. ``sqllite3 test.db``)
* ``.help`` - Show help
* ``.tables`` - Show all tables
* ``.quit`` - Quit


InfluxDB
========
InfluxDB is an open-source time series database developed by InfluxData. It is written in Go and optimized for fast, 
high-availability storage and retrieval of time series data in fields such as operations monitoring, 
application metrics, Internet of Things sensor data, and real-time analytics.

`Official Website <https://www.influxdata.com/>`_


DuckDB
======
DuckDB is an open-source **column-oriented relational database** management system. Is a fast in-process analytical database.
Unlike other embedded databases (for example, SQLite) DuckDB is not focusing on transactional (OLTP) applications and 
instead is specialized for online analytical processing **(OLAP) workloads**

DuckDB in its OLAP niche does not compete with the traditional DBMS like MSSQL, PostgreSQL and Oracle database. 
While using SQL for queries, DuckDB targets the serverless applications and provides extremely **fast responses using 
Apache Parquet files for storage**. These attributes make it a popular choice for large dataset analysis in interactive mode, 
but match poorly the requirements of the enterprise data storage.

DuckDB also deviates from the traditional client–server model by **running inside a host process** (it has bindings, for example, 
for a Python interpreter with the ability to directly place data into NumPy arrays).

`Official Website <https://www.duckdb.org/>`_
