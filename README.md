# data_collector_agent 
Collects data from SQL database and send them over HTTPS to NiFi server. 
NiFi is orchestrating all events, ETL to receipients.
Collector works as a reverse proxy agent at the remote SQL database server allowing data to be pushed back to NiFi instead of pulling. 

The periodic process:

Step 1. Sen heartbeat to NiFi and check response for change in synchronisation parameters:
- heartbeat period
- database connectivity and authentication params
- synchronisation period
- data transfer payload format and mode (e.g. segmentation)
Updates changes if required

Step 2. Collector requests NiFi for the SQL and execute it
Step 4. Collector sends results to NiFi 

