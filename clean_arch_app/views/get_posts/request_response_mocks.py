

REQUEST_BODY_JSON = """
{
    "offset": 1,
    "length": 1
}
"""


RESPONSE_200_JSON = """
{
    "posts": [
        {
            "post_id": 1,
            "content": "string",
            "created_at": "2099-12-31 00:00:00",
            "created_by": {
                "username": "string",
                "profile_pic_url": "string",
                "user_id": 1
            },
            "comments": [
                {
                    "comment_id": 1,
                    "content": "string",
                    "commented_at": "2099-12-31 00:00:00",
                    "commented_by": {
                        "username": "string",
                        "profile_pic_url": "string",
                        "user_id": 1
                    }
                }
            ]
        }
    ]
}
"""

