import time


class StatsMiddleware(object):
    """A middleware to measure response time"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # time before start processing request
        request.start_time = time.time()

        # process request
        response = self.get_response(request)

        # time elapsed in processing request
        total = time.time() - request.start_time

        print("Request completed in {0} seconds".format(total))

        return response
