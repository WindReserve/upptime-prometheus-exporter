
from prometheus_client.metrics_core import GaugeMetricFamily
import api
class UpptimeCollector:
    """
    Collects Upptime metrics via the GitHub API
    """

    def collect(self):
        services = api.get_services()
        yield self.metric_no_services(services)
        yield self.metric_services_response_time(services)

    def metric_no_services(self, services):
        no_services = len(services)
        metric = GaugeMetricFamily('upptime_services', "Number of services Upptime is monitoring")
        metric.add_metric([], no_services)
        return metric
    
    def metric_services_response_time(self, services):
        metric = GaugeMetricFamily('upptime_services_response_time', "Response Time of Services monitored by Upptime", labels=["service"])
        for service in services:
            metric.add_metric([service.name], service.response_time)
        
        return metric
        