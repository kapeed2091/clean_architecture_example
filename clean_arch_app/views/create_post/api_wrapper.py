from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user = kwargs['user']
    request_data = kwargs['request_data']

    content = request_data['content']
    created_by_id = user.id

    from clean_arch_app.interactors.create_post_interactor import CreatePostInteractor
    from clean_arch_app.storages.post_storage_impl import PostStorageImpl
    from clean_arch_app.presenters.json_presenter import JsonPresenter

    post_storage = PostStorageImpl()
    json_presenter = JsonPresenter()

    interactor = CreatePostInteractor(post_storage=post_storage,
                                      presenter=json_presenter)
    response = interactor.create_post(post_content=content,
                                      created_by_id=created_by_id)

    return response
