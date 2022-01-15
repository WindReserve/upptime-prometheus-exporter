
from prometheus_client.metrics_core import GaugeMetricFamily
import api
class UpptimeCollector:
    """
    Collects Upptime metrics via the GitHub API
    """

    def collect(self):
        services = api.get_services()
        yield self.metric_no_services(services)

    def metric_no_services(self, services):
        no_services = len(services)
        metric = GaugeMetricFamily('upptime_services', "Number of services Upptime is monitoring")
        metric.add_metric([], no_services)
        return metric