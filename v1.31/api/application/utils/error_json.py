
"""Error validating schema in request json"""
error_model_json = lambda e : {
        "errors" : e.message
    }