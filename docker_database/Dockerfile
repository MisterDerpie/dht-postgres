FROM postgres
COPY create_database.sh /docker-entrypoint-initdb.d/create_database.sh
EXPOSE 5432
ENV POSTGRES_PASSWORD=test