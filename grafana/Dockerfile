FROM grafana/grafana-enterprise

COPY dhtdashboard.yml /etc/grafana/provisioning/dashboards/dhtdashboard.yml
COPY dashboard.json /var/lib/grafana/dashboards/dashboard.json
COPY postgres.yml /etc/grafana/provisioning/datasources/postgres.yml