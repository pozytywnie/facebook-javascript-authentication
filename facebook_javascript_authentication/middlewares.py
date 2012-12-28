class P3PMiddleware():
    def process_request(self, request):
        if not request.session.items():
            request.session.modified = True # force create session

    def process_response(self, request, response):
        if hasattr(request, 'session'):
            request.session['foo'] = 'bar'
        response['P3P'] = 'CP="IDC DSP COR CURa ADMa OUR IND PHY ONL COM STA"'
        return response
