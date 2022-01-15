import yaml
from github import Github
from github.ContentFile import ContentFile

import settings

from models import Service

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
    service = Service(name=service_name, **content)
    return service
