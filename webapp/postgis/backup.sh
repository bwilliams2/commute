docker exec -t postgis_web_1 pg_dumpall -c -U postgres | gzip -c > dump_`date +%d-%m-%Y"_"%H_%M_%S`.gz