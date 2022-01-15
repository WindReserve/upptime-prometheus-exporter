"""
Models handling Upptime data 
"""

from calendar import prmonth

class ServiceInfo:
    def __init__(self, name, url, icon, slug, status) -> None:
        self._name = name
        self._url = url
        self._icon = icon
        self._slug = slug
        self._status = status

    @property
    def name(self):
        return self._name

    @property
    def url(self):
        return self._url

    @property
    def icon(self):
        return self._icon

    @property
    def slug(self):
        return self._slug

    @property
    def status(self):
        return self._status


class ServiceUptime:
    """
    Class containg uptime data for a service
    """
    def __init__(self, uptime, uptime_day, uptime_week, uptime_month, uptime_year ) -> None:
        self._uptime = uptime
        self._uptime_day = uptime_day
        self._uptime_week = uptime_week
        self._uptime_month = uptime_month
        self._uptime_year = uptime_year

        @property
        def uptime(self):
            return self._uptime

        @uptime.setter
        def uptime(self, uptime):
            self._uptime = uptime

        @property
        def uptime_day(self):
            return self._uptime_day

        @uptime_day.setter
        def uptime_day(self, uptime_day):
            self._uptime_day = uptime_day

        @property
        def uptime_week(self):
            return self._uptime_week

        @uptime_week.setter
        def uptime_week(self, uptime_week):
            self._uptime_week = uptime_week

        @property
        def uptime_month(self):
            return self._uptime_month

        @uptime_month.setter
        def uptime_month(self, uptime_month):
            self._uptime_month = uptime_month

        @property
        def uptime_year(self):
            return self._uptime_year

        @uptime_year.setter
        def uptime_year(self, uptime_year):
            self._uptime_year = uptime_year

class ServiceResponseTime:
    """
    Class containg response time data for a service
    """
    def __init__(self, response_time, response_time_day, response_time_week, response_time_month, response_time_year ) -> None:
        self._response_time = response_time
        self._response_time_day = response_time_day
        self._response_time_week = response_time_week
        self._response_time_month = response_time_month
        self._response_time_year = response_time_year

        @property
        def response_time(self):
            return self._response_time

        @response_time.setter
        def response_time(self, response_time):
            self._response_time = response_time

        @property
        def response_time_day(self):
            return self._response_time_day

        @response_time_day.setter
        def response_time_day(self, response_time_day):
            self._response_time_day = response_time_day

        @property
        def response_time_week(self):
            return self._response_time_week

        @response_time_week.setter
        def response_time_week(self, response_time_week):
            self._response_time_week = response_time_week

        @property
        def response_time_month(self):
            return self._response_time_month

        @response_time_month.setter
        def response_time_month(self, response_time_month):
            self._response_time_month = response_time_month

        @property
        def response_time_year(self):
            return self._response_time_year

        @response_time_year.setter
        def response_time_year(self, response_time_year):
            self._response_time_year = response_time_year


class ServiceDailyMinutesDown:
    def __init__(self, daily_minutes_down) -> None:
        self._daily_minutes_down = daily_minutes_down    
    

class ServiceDetail:
    """
    Class containing the values recorded by Upptime in history/{service_name}.yml

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

class Service:
    def __init__(self, info, uptime, response_time, daily_minutes_down) -> None:
        self._info: ServiceInfo = info
        self._uptime: ServiceUptime = uptime
        self._response_time: ServiceResponseTime = response_time
        self._daily_minutes_down: ServiceDailyMinutesDown = daily_minutes_down

    @property
    def info(self) -> ServiceInfo:
        return self._info

    @property
    def uptime(self) -> ServiceUptime:
        return self._uptime

    @property
    def response_time(self) -> ServiceResponseTime:
        return self._response_time

    @property
    def daily_minutes_down(self) -> ServiceDailyMinutesDown:
        return self._daily_minutes_down
