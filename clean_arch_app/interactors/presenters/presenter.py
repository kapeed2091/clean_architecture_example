"""
Created on 2019-07-18

@author: kapeed2091
"""
import abc
from clean_arch_app.interactors.storages.post_storage import PostDTO


class Presenter:

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def create_post(self, post_dto: PostDTO):
        pass
