"""
Created on 2019-07-18

@author: kapeed2091
"""
from clean_arch_app.interactors.storages.post_storage import PostDTO
from clean_arch_app.interactors.storages.post_storage import PostStorage


class PostStorageImpl(PostStorage):

    def create_post(self, content: str, created_by_id: int) -> PostDTO:
        from clean_arch_app.models import Post
        post_obj = Post.objects.create(content=content,
                                       created_by_id=created_by_id)
        post_dto = PostDTO(
            post_obj.id, post_obj.content, post_obj.created_at,
            post_obj.created_by_id
        )
        return post_dto
