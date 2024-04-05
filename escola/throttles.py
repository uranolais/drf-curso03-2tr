from rest_framework.throttling import AnonRateThrottle 

class MatriculaThrottleAnon(AnonRateThrottle):
    rate = '2/day'