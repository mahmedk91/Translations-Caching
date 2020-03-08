from django.http import JsonResponse


class HttpResponseBadRequest(JsonResponse):
    """BadRequest json response with an error message and status 400"""

    status_code = 400

    def __init__(self, error_message: str, **kwargs):
        super().__init__(data={"error": error_message}, **kwargs)


class TranslationResponse(JsonResponse):
    """Translation success response with translated text"""

    status_code = 200

    def __init__(
        self, source: str, target: str, source_text: str, translated_text: str, **kwargs
    ):
        data = {
            "source": source,
            "target": target,
            "source_text": source_text,
            "translated_text": translated_text,
        }
        super().__init__(data=data, **kwargs)
