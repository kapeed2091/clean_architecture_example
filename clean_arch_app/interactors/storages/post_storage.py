"""
Created on 2019-07-18

@author: kapeed2091
"""
import abc
import datetime
from dataclasses import dataclass


@dataclass
class PostDTO:
    post_id: int
    content: str
    created_at: datetime.datetime
    created_by_id: int


class PostStorage:

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def create_post(self, content: str, created_by_id: int) -> PostDTO:
        pass
