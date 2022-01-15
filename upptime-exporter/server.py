from collector import UpptimeCollector

from prometheus_client import start_http_server, REGISTRY

from time import sleep

import settings

if __name__ == "__main__":

    collector = UpptimeCollector()

    start_http_server(settings.PORT, addr=settings.BIND_IP)

    REGISTRY.register(collector)

    while True:
        sleep(1)