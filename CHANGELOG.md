# Changelog

## [9.3.3](https://pypi.org/project/directory-validators/9.3.3/) (2024-02-20)
- KLS-1307 - Bump Django to 4.2.10 minimum

## [9.3.1](https://pypi.org/project/directory-validators/9.3.1/) (2023-10-19)
- KLS-1307 - upgrade pillow library

## [9.3.0](https://github.com/uktrade/directory-validators/pull/77) (2023-05-22)
- KLS-622 - Bump Django to 4.2

## [9.2.1](https://pypi.org/project/directory-validators/9.2.1/) (2022-09-20)
- GLS-410 - django patch (small fix)

## [9.2.0](https://pypi.org/project/directory-validators/9.2.0/) (2022-09-05)
- GLS-410 - django patch

## [9.1.0](https://pypi.org/project/directory-validators/9.1.0/) (2022-09-05)
- GLS-410 - django patch

## [9.0.0](https://pypi.org/project/directory-validators/9.0.0/) (2022-08-17)
- GLS-382 - django 3 upgrade

## [8.0.1](https://pypi.org/project/directory-validators/8.0.1/) (2022-03-14)
- GLS-149 - upgrade pillow library.

## [8.0.0](https://pypi.org/project/directory-validators/8.0.0/) (2022-01-13)
- no ticket - upgrade pillow library. Python 3.6 no longer supported.

## [7.0.1](https://pypi.org/project/directory-validators/7.0.1/) (2021-06-24)
- no ticket - dependencies update

## [7.0.0](https://pypi.org/project/directory-validators/7.0.0/) (2021-06-24)
- no ticket - dependencies update


## [6.0.6](https://pypi.org/project/directory-validators/6.0.6/) (2021-06-09)
- no ticket - upgrade pillow lib

## [6.0.5](https://pypi.org/project/directory-validators/6.0.5/) (2021-03-19)
- no ticket - upgrade pillow lib

## [6.0.4](https://pypi.org/project/directory-validators/6.0.4/) (2020-11-05)
- no ticket - upgrade pytz lib


## [6.0.3](https://pypi.org/project/directory-validators/6.0.3/) (2020-08-04)
- no ticket - pillow lib upgrade for security vulnerability fix
- no ticket - codecov lib upgrade

## [6.0.2](https://pypi.org/project/directory-validators/6.0.2/) (2020-05-11)
[Full Changelog](https://github.com/uktrade/directory-validators/pull/63/files)
### Implemented enhancements
- no ticket - Incrased the range of pytz versions

## [6.0.1](https://pypi.org/project/directory-validators/6.0.1/) (2020-04-06)
[Full Changelog](https://github.com/uktrade/directory-validators/pull/61/files)

### Implemented enhancements
- no ticket - Upgrade Pillow

## [6.0.0](https://pypi.org/project/directory-validators/6.0.0/) (2019-11-20)
[Full Changelog](https://github.com/uktrade/directory-validators/pull/60/files)

### Implemented enhancements
- no ticket - Upgrade Pillow

### Breaking Change
- the following methods have been moved

| old name                         | new name                      |
| -------------------------------- | ----------------------------- |
| common.not_contains_url_or_email | url.not_contains_url_or_email |
| company.keywords_word_limit | string.word_limit (it's not a curried function) |
| company.keywords_special_characters | string.no_special_characters |
| company.image_format | file.image_format |
| company.case_study_image_filesize | file.case_study_image_filesize |
| company.case_study_social_link_facebook | url.is_facebook |
| company.case_study_social_link_twitter | url.is_twitter |
| company.case_study_social_link_linkedin | url.is_linkedin |
| company.no_html | string.no_html |
| enrolment.logo_filesize | file.logo_filesize |
| helpers.tokenize_keywords | string.tokenize_words |
| password_validation.AlphabeticPasswordValidator | password.AlphabeticPasswordValidator |
| password_validation.PasswordWordPasswordValidator | password.PasswordWordPasswordValidator |

- the following methods have been deleted:
| -------------------------------- |
| company.no_company_with_insufficient_companies_house_data |
| company.case_study_video_filesize |
| enrolment.company_number |
| enrolment.email_domain_free |
| enrolment.email_domain_disposable |
| enrolment.domestic_mobile_phone_number |

## [5.2.0](https://pypi.org/project/directory-validators/5.2.0/) (2019-07-17)
[Full Changelog](https://github.com/uktrade/directory-validators/pull/58/files)

### Breaking Change
- no ticket - Add support for django 2

## [5.1.1](https://pypi.org/project/directory-validators/5.1.1/) (2019-05-29)
[Full Changelog](https://github.com/uktrade/directory-validators/pull/55/files)

### Implemented enhancements
- no ticket - PyPI now renders the markdown readme

### Fixed bugs:
- Upgraded minimum supported django to avoid security vulnerability
- Upgraded minimum supported urllib3 to avoid security vulnerability

