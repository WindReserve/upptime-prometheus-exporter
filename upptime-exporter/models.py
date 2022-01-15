
class Service:
    """
    Class containing the values recorded by Upptime

    url: https://cloud.windreserve.de
    status: up
    code: 200
    responseTime: 864
    lastUpdated: 2022-01-14T23:08:36.001Z
    startTime: Sun Jan 09 2022 22:29:05 GMT+0000 (Coordinated Universal Time)
    generator: Upptime <https://github.com/upptime/upptime>
    """
    def __init__(self, name=None, url=None, status=None, code=None, responseTime=None, lastUpdated=None, startTime=None, generator=None) -> None:
        self._name = name
        self._url = url
        self._status = status
        self._code = code
        self._response_time = responseTime
        self._last_updated = lastUpdated
        self._start_time = startTime
        self._generator = generator

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        self._url = url
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, status):
        # TODO: check if status value is oen of up, down, degraded
        self._status = status

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        # TODO: check if value is valid HTTP response code
        self._code = code
    
    @property
    def response_time(self):
        return self._response_time
    
    @response_time.setter
    def response_time(self, response_time):
        # TODO: check if value is int
        self._response_time = response_time
    
    @property
    def last_updated(self):
        return self._last_updated
    
    @last_updated.setter
    def last_updated(self, last_updated):
        # TODO: Check if value is valid datetime string
        self._last_updated = last_updated

    @property
    def start_time(self):
        return self._start_time
    
    @start_time.setter
    def start_time(self, start_time):
        # TODO: Check if value is valid datetime string, but different than last_updated
        self._start_time = start_time