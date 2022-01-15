from typing import Dict, List
import json
import yaml
from github import Github
from github.ContentFile import ContentFile

import settings

from models import Service, ServiceInfo, ServiceUptime, ServiceResponseTime, ServiceDailyMinutesDown, ServiceDetail

g = Github(settings.GH_ACCESS_TOKEN)
repo = g.get_repo(settings.UPPTIME_REPO_NAME)

def get_services():
    service_files = repo.get_dir_contents('/history')
    services = []

    for i, service_file in enumerate(service_files):

        # Remove LICENSE and summary.json files from service_files list
        # TODO: make use of summary.json
        if service_file.name == 'LICENSE' or service_file.name == 'summary.json':
            service_files.pop(i)
            del service_file
            continue

        # Get service details from file
        service = get_service_details(service_file)
        services.append(service)



    
    return services

def get_service_details(service):
    service_name = service.name.replace(".yml", "")
    print(f"Getting details for {service_name}")
    contents: ContentFile = repo.get_contents(service.path)
    content = yaml.safe_load(contents.decoded_content)
    service = ServiceDetail(name=service_name, **content)
    return service


def get_summary():
    summary_file = repo.get_contents('/history/summary.json')
    summary = json.loads(summary_file.decoded_content)

    services = []

    for service_dict in summary:
        service_uptime = {
            "uptime": service_dict["uptime"],
            "uptime_day": service_dict["uptimeDay"],
            "uptime_week": service_dict["uptimeWeek"],
            "uptime_month": service_dict["uptimeMonth"],
            "uptime_year": service_dict["uptimeYear"],
        }

        service_response_time = {
            "response_time": service_dict["time"],
            "response_time_day": service_dict["timeDay"],
            "response_time_week": service_dict["timeWeek"],
            "response_time_month": service_dict["timeMonth"],
            "response_time_year": service_dict["timeYear"],
        }

        service_daily_minutes_down = service_dict["dailyMinutesDown"]

        service_general = {
            "name": service_dict["name"],
            "url": service_dict["url"],
            "icon": service_dict["icon"],
            "slug": service_dict["slug"],
            "status": service_dict["status"],
        }
        info = ServiceInfo(**service_general)
        uptime = ServiceUptime(service_uptime)
        response_time = ServiceResponseTime(service_response_time)
        daily_minutes_down = ServiceDailyMinutesDown(service_daily_minutes_down)
        service = Service(info, uptime, response_time, daily_minutes_down)
        services.append(service)
    
    return services

