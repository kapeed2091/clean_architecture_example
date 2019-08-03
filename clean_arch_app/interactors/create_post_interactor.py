from clean_arch_app.interactors.storages.post_storage import PostStorage
from clean_arch_app.interactors.presenters.presenter import Presenter


class CreatePostInteractor:
    def __init__(self, post_storage: PostStorage, presenter: Presenter):
        self.post_storage = post_storage
        self.presenter = presenter

    def create_post(self, post_content: str, created_by_id: int):
        post_dto = self.post_storage.create_post(post_content, created_by_id)
        response = self.presenter.create_post(post_dto)
        return response
