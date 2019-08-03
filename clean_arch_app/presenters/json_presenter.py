"""
Created on 2019-07-18

@author: kapeed2091
"""

from clean_arch_app.interactors.storages.post_storage import PostDTO
from clean_arch_app.interactors.presenters.presenter import Presenter


class JsonPresenter(Presenter):
    def create_post(self, post_dto: PostDTO):
        return {
            'post_id': post_dto.post_id
        }
