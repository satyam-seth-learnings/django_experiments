def custom_context_processor(request):
    return {
        "test_value": "this is test value",
    }