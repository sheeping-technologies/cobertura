from django.http import HttpResponse

def custom_exception_handler(get_response):
    def middleware(request):
        response = get_response(request)
        if response.status_code == 401:
             # Devuelve la plantilla HTML personalizada con código de estado 401
            with open('templates/provider/401.html', 'r') as file:
                content = file.read()
            return HttpResponse(content, status=401)
        return response

    return middleware