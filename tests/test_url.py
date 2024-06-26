import pytest

from django import forms

from directory_validators import url

# https://github.com/django/django/blob/1.10/tests/validators/valid_urls.txt
urls = [
    "http://www.djangoproject.com/",
    "HTTP://WWW.DJANGOPROJECT.COM/",
    "http://localhost/",
    "http://example.com/",
    "http://example.com./",
    "http://www.example.com/",
    "http://www.example.com:8000/test",
    "http://valid-with-hyphens.com/",
    "http://subdomain.example.com/",
    "http://a.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "http://200.8.9.10/",
    "http://200.8.9.10:8000/test",
    "http://su--b.valid-----hyphens.com/",
    "http://example.com?something=value",
    "http://example.com/index.php?something=value&another=value2",
    "https://example.com/",
    "ftp://example.com/",
    "ftps://example.com/",
    "http://foo.com/blah_blah",
    "http://foo.com/blah_blah/",
    "http://foo.com/blah_blah_(wikipedia)",
    "http://foo.com/blah_blah_(wikipedia)_(again)",
    "http://www.example.com/wpstyle/?p=364",
    "https://www.example.com/foo/?bar=baz&inga=42&quux",
    "http://✪df.ws/123",
    "http://userid:password@example.com:8080",
    "http://userid:password@example.com:8080/",
    "http://userid@example.com",
    "http://userid@example.com/",
    "http://userid@example.com:8080",
    "http://userid@example.com:8080/",
    "http://userid:password@example.com",
    "http://userid:password@example.com/",
    "http://142.42.1.1/",
    "http://142.42.1.1:8080/",
    "http://➡.ws/䨹",
    "http://⌘.ws",
    "http://⌘.ws/",
    "http://foo.com/blah_(wikipedia)#cite-1",
    "http://foo.com/blah_(wikipedia)_blah#cite-1",
    "http://foo.com/unicode_(✪)_in_parens",
    "http://foo.com/(something)?after=parens",
    "http://☺.damowmow.com/",
    "http://djangoproject.com/events/#&product=browser",
    "http://j.mp",
    "ftp://foo.bar/baz",
    "http://foo.bar/?q=Test%20URL-encoded%20stuff",
    "http://مثال.إختبار",
    "http://例子.测试",
    "http://उदाहरण.परीक्षा",
    "http://-.~_!$&'()*+,;=:%40:80%2f::::::@example.com",
    "http://xn--7sbb4ac0ad0be6cf.xn--p1ai",
    "http://1337.net",
    "http://a.b-c.de",
    "http://223.255.255.254",
    "ftps://foo.bar/",
    "http://10.1.1.254",
    "http://[FEDC:BA98:7654:3210:FEDC:BA98:7654:3210]:80/index.html",
    "http://[::192.9.5.5]/ipng",
    "http://[::ffff:192.9.5.5]/ipng",
    "http://[::1]:8080/",
    "http://0.0.0.0/",
    "http://255.255.255.255",
    "http://224.0.0.0",
    "http://224.1.1.1",
    (
        "http://aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        "aaa.example.com"
    ),
    (
        "http://example.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        "aaaaaaaaaaa.com"
    ),
    (
        "http://example.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        "aaaaaaaaaaa"
    ),
    (
        "http://aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.aaaaaaaaaaaaaaaaaaaaaaaaaa"
        "a.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        ".aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa."
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.aaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    ),
    "http://dashintld.c-m",
    "http://multipledashintld.a-b-c",
    "http://evenmoredashintld.a---c",
    "http://dashinpunytld.xn---c",
    "www.djangoproject.com/",
    "WWW.DJANGOPROJECT.COM/",
    "localhost/",
    "example.com/",
    "example.com./",
    "www.example.com/",
    "www.example.com:8000/test",
    "valid-with-hyphens.com/",
    "subdomain.example.com/",
    "a.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "200.8.9.10/",
    "200.8.9.10:8000/test",
    "su--b.valid-----hyphens.com/",
    "example.com?something=value",
    "example.com/index.php?something=value&another=value2",
    "https://example.com/",
    "ftp://example.com/",
    "ftps://example.com/",
    "foo.com/blah_blah",
    "foo.com/blah_blah/",
    "foo.com/blah_blah_(wikipedia)",
    "foo.com/blah_blah_(wikipedia)_(again)",
    "www.example.com/wpstyle/?p=364",
    "https://www.example.com/foo/?bar=baz&inga=42&quux",
    "✪df.ws/123",
    "userid:password@example.com:8080",
    "userid:password@example.com:8080/",
    "userid@example.com",
    "userid@example.com/",
    "userid@example.com:8080",
    "userid@example.com:8080/",
    "userid:password@example.com",
    "userid:password@example.com/",
    "142.42.1.1/",
    "142.42.1.1:8080/",
    "➡.ws/䨹",
    "⌘.ws",
    "⌘.ws/",
    "foo.com/blah_(wikipedia)#cite-1",
    "foo.com/blah_(wikipedia)_blah#cite-1",
    "foo.com/unicode_(✪)_in_parens",
    "foo.com/(something)?after=parens",
    "☺.damowmow.com/",
    "djangoproject.com/events/#&product=browser",
    "j.mp",
    "ftp://foo.bar/baz",
    "foo.bar/?q=Test%20URL-encoded%20stuff",
    "مثال.إختبار",
    "例子.测试",
    "उदाहरण.परीक्षा",
    "-.~_!$&'()*+,;=:%40:80%2f::::::@example.com",
    "xn--7sbb4ac0ad0be6cf.xn--p1ai",
    "1337.net",
    "a.b-c.de",
    "223.255.255.254",
    "ftps://foo.bar/",
    "10.1.1.254",
    "[FEDC:BA98:7654:3210:FEDC:BA98:7654:3210]:80/index.html",
    "[::192.9.5.5]/ipng",
    "[::ffff:192.9.5.5]/ipng",
    "[::1]:8080/",
    "0.0.0.0/",
    "255.255.255.255",
    "224.0.0.0",
    "224.1.1.1",
    (
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        "aaa.example.com"
    ),
    (
        "example.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        "aaaaaaaaaaa.com"
    ),
    (
        "example.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        "aaaaaaaaaaa"
    ),
    (
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.aaaaaaaaaaaaaaaaaaaaaaaaaa"
        "a.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        ".aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa."
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.aaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    ),
    "dashintld.c-m",
    "multipledashintld.a-b-c",
    "evenmoredashintld.a---c",
    "dashinpunytld.xn---c",
    "www.www.djangoproject.com/",
    "www.WWW.DJANGOPROJECT.COM/",
    "www.localhost/",
    "www.example.com/",
    "www.example.com./",
    "www.www.example.com/",
    "www.www.example.com:8000/test",
    "www.valid-with-hyphens.com/",
    "www.subdomain.example.com/",
    "www.a.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "www.200.8.9.10/",
    "www.200.8.9.10:8000/test",
    "www.su--b.valid-----hyphens.com/",
    "www.example.com?something=value",
    "www.example.com/index.php?something=value&another=value2",
    "https://example.com/",
    "ftp://example.com/",
    "ftps://example.com/",
    "www.foo.com/blah_blah",
    "www.foo.com/blah_blah/",
    "www.foo.com/blah_blah_(wikipedia)",
    "www.foo.com/blah_blah_(wikipedia)_(again)",
    "www.www.example.com/wpstyle/?p=364",
    "https://www.example.com/foo/?bar=baz&inga=42&quux",
    "www.✪df.ws/123",
    "www.userid:password@example.com:8080",
    "www.userid:password@example.com:8080/",
    "www.userid@example.com",
    "www.userid@example.com/",
    "www.userid@example.com:8080",
    "www.userid@example.com:8080/",
    "www.userid:password@example.com",
    "www.userid:password@example.com/",
    "www.142.42.1.1/",
    "www.142.42.1.1:8080/",
    "www.➡.ws/䨹",
    "www.⌘.ws",
    "www.⌘.ws/",
    "www.foo.com/blah_(wikipedia)#cite-1",
    "www.foo.com/blah_(wikipedia)_blah#cite-1",
    "www.foo.com/unicode_(✪)_in_parens",
    "www.foo.com/(something)?after=parens",
    "www.☺.damowmow.com/",
    "www.djangoproject.com/events/#&product=browser",
    "www.j.mp",
    "ftp://foo.bar/baz",
    "www.foo.bar/?q=Test%20URL-encoded%20stuff",
    "www.مثال.إختبار",
    "www.例子.测试",
    "www.उदाहरण.परीक्षा",
    "www.-.~_!$&'()*+,;=:%40:80%2f::::::@example.com",
    "www.xn--7sbb4ac0ad0be6cf.xn--p1ai",
    "www.1337.net",
    "www.a.b-c.de",
    "www.223.255.255.254",
    "ftps://foo.bar/",
    "www.10.1.1.254",
    "www.[FEDC:BA98:7654:3210:FEDC:BA98:7654:3210]:80/index.html",
    "www.[::192.9.5.5]/ipng",
    "www.[::ffff:192.9.5.5]/ipng",
    "www.[::1]:8080/",
    "www.0.0.0.0/",
    "www.255.255.255.255",
    "www.224.0.0.0",
    "www.224.1.1.1",
    (
        "www.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        "aaa.example.com"
    ),
    (
        "www.example.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        "aaaaaaaaaaa.com"
    ),
    (
        "www.example.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        "aaaaaaaaaaa"
    ),
    (
        "www.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.aaaaaaaaaaaaaaaaaaaaaaaaaa"
        "a.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        ".aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa."
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.aaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    ),
    "www.dashintld.c-m",
    "www.multipledashintld.a-b-c",
    "www.evenmoredashintld.a---c",
    "www.dashinpunytld.xn---c",
]


def test_not_contain_url_does_contains_urls():
    value_templates = [
        '{url} Thing', '{url}Thing',  # at the start
        'Thing {url} Thing', 'Thing{url}Thing', 'Thing{url} Thing',  # middle
        'Thing{url}', 'Thing {url}',  # at the end
    ]
    for item in urls:
        for value_template in value_templates:
            value = value_template.format(url=item)
            with pytest.raises(forms.ValidationError) as excinfo:
                url.not_contains_url_or_email(value)
            assert url.MESSAGE_REMOVE_URL in str(excinfo.value)


def test_not_contain_url_does_not_contain_url():
    assert url.not_contains_url_or_email('Thing') is None
    assert url.not_contains_url_or_email('') is None


def test_is_facebook_accepts_schemes():
    expected_legal_urls = [
        'https://facebook.com/thing',
        'http://facebook.com/thing',
    ]
    for value in expected_legal_urls:
        assert url.is_facebook(value) is True


def test_is_facebook_accepts_subdomains():
    expected_legal_urls = [
        'http://thing.facebook.com/thing',
        'http://www.facebook.com/thing',
    ]
    for value in expected_legal_urls:
        assert url.is_facebook(value) is True


def test_is_facebook_rejects_wrong_service():
    value = 'http://google.com'
    expected_message = url.MESSAGE_NOT_FACEBOOK
    with pytest.raises(forms.ValidationError) as excinfo:
        url.is_facebook(value)
    assert expected_message in str(excinfo.value)


def test_is_twitter_accepts_schemes():
    expected_legal_urls = [
        'https://twitter.com/thing',
        'http://twitter.com/thing',
    ]
    for value in expected_legal_urls:
        assert url.is_twitter(value) is True


def test_is_twitter_accepts_subdomains():
    expected_legal_urls = [
        'http://thing.twitter.com/thing',
        'http://www.twitter.com/thing',
    ]
    for value in expected_legal_urls:
        assert url.is_twitter(value) is True


def test_is_twitter_rejects_wrong_service():
    value = 'http://google.com'
    expected_message = url.MESSAGE_NOT_TWITTER
    with pytest.raises(forms.ValidationError) as excinfo:
        url.is_twitter(value)
    assert expected_message in str(excinfo.value)


def test_is_linkedin_accepts_schemes():
    expected_legal_urls = [
        'https://linkedin.com/thing',
        'http://linkedin.com/thing',
    ]
    for value in expected_legal_urls:
        assert url.is_linkedin(value) is True


def test_is_linkedin_accepts_subdomains():
    expected_legal_urls = [
        'http://thing.linkedin.com/thing',
        'http://www.linkedin.com/thing',
    ]
    for value in expected_legal_urls:
        assert url.is_linkedin(value) is True


def test_is_linkedin_rejects_wrong_service():
    value = 'http://google.com'
    expected_message = url.MESSAGE_NOT_LINKEDIN
    with pytest.raises(forms.ValidationError) as excinfo:
        url.is_linkedin(value)
    assert expected_message in str(excinfo.value)
