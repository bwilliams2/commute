FROM postgis/postgis:13-3.1-alpine
COPY dump_25-02-2021_23_13_40.sql.gz /tmp/sql_backup.sql.gz
COPY restore_database.sh /docker-entrypoint-initdb.d/
# COPY restore_database.sh ./restore_database.sh
# RUN chmod +x ./restore_database.sh
EXPOSE 5432
