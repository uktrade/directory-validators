# Changelog

## [6.0.2](https://pypi.org/project/directory-validators/6.0.2/) (2020-05-11)
[Full Changelog](https://github.com/uktrade/directory-validators/pull/62/files)

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

