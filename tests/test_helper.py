

from directory_validators.helper import validate_social_media_url

facebook_legal_urls = [
        'https://facebook.com/thing',
        'http://facebook.com/thing',
        'http://thing.facebook.com/thing',
        'http://www.facebook.com/thing',
    ]

twitter_legal_urls = [
        'https://twitter.com/thing',
        'http://twitter.com/thing',
        'http://thing.twitter.com/thing',
        'http://www.twitter.com/thing',
    ]
linkedin_legal_urls = [
        'https://linkedin.com/thing',
        'http://linkedin.com/thing',
        'http://thing.linkedin.com/thing',
        'http://www.linkedin.com/thing',
    ]


def test_valid_facebook_social_media_url():
    allowed_list = ['facebook.com', '*.facebook.com']
    for value in facebook_legal_urls:
        assert validate_social_media_url(value, allowed_list, 'Please provide a link to Facebook.') is True


def test_valid_twitter_social_media_url():
    allowed_list = ['twitter.com', '*.twitter.com']
    for value in twitter_legal_urls:
        assert validate_social_media_url(value, allowed_list, 'Please provide a link to Twitter.') is True


def test_valid_linkedin_social_media_url():
    allowed_list = ['linkedin.com', '*.linkedin.com']
    for value in linkedin_legal_urls:
        assert validate_social_media_url(value, allowed_list, 'Please provide a link to LinkedIn.') is True
