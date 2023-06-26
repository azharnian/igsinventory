user_role_schema = {
    "type": "object",
    "properties" : {
        "role" : {
            "type" : "string", 
            "minLength" : 3, 
            "maxLength" : 60
        },
        "description" : {
            "type" : "string", 
            "maxLength" : 256
        }
    },
    "required" : [
        "role", 
        "description"]
}

user_schema = {
    "type" : "object",
    "properties" : {
        "username" : {
            "type" : "string",
            "minLength" : 3, 
            "maxLength" : 256
        },
        "email" : {
            "type" : "string",
            "minLength" : 8, 
            "maxLength" : 256
        },
        "phone" : {
            "type" : "string",
            "minLength" : 8, 
            "maxLength" : 256
        },
        "password" : {
            "type" : "string",
            "minLength" : 8, 
            "maxLength" : 256
        },
        "first_name" : {
            "type" : "string",
            "minLength" : 1, 
            "maxLength" : 128
        },
        "last_name" : {
            "type" : "string",
            "minLength" : 1, 
            "maxLength" : 128
        },
        "role" : {
            "type" : "integer",
            "minimal" : 1
        },
        "profile_picture" : {
            "type" : "string",
            "minLength" : 8, 
            "maxLength" : 256
        }
    },
    "required" : [
        "username",
        "email",
        "phone",
        "password",
        "first_name",
        "last_name",
        "role"
    ]
}

user_login_schema = {
    "type" : "object",
    "properties" : {
        "username" : {
            "type" : "string",
            "minLength" : 3
        },
        "password" : {
            "type" : "string",
            "minLength" : 8
        }
    },
    "required" : [
        "username", "password"
    ]
}