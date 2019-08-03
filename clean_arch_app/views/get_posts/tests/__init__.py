# pylint: disable=wrong-import-position

APP_NAME = "clean_arch_app"
OPERATION_NAME = "get_posts"
REQUEST_METHOD = "get"
URL_SUFFIX = "posts/"

from .test_case_01 import TestCase01GetPostsAPITestCase

__all__ = [
    "TestCase01GetPostsAPITestCase"
]
