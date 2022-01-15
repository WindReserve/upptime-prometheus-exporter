from github import Github

import settings

g = Github(settings.GH_ACCESS_TOKEN)
repo = g.get_repo(settings.UPPTIME_REPO_NAME)

def get_services():
    services = repo.get_dir_contents('/api')
    return services
    print(services)
    for service in services:

        print(service.name)