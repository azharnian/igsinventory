user_role_schema = {
    "type": "object",
    "properties" : {
        "role" : {"type" : "string", "minLength" : 3, "maxLength" : 60},
        "description" : {"type" : "string", "maxLength" : 256}
    },
    "required" : ["role", "description"]
}