from wagtail.core import hooks


@hooks.register('register_rich_text_features')
def register_my_feature(features):
    extra_features = ['code', 'superscript', 'subscript', 'strikethrough', 'blockquote', 'h5', 'h6']
    features.default_features.extend(extra_features)


