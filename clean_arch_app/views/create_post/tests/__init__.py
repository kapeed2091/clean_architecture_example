# pylint: disable=wrong-import-position

APP_NAME = "clean_arch_app"
OPERATION_NAME = "create_post"
REQUEST_METHOD = "post"
URL_SUFFIX = "posts/create/"

from .test_case_01 import TestCase01CreatePostAPITestCase

__all__ = [
    "TestCase01CreatePostAPITestCase"
]
