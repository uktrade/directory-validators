# directory-validators
[Directory of UK Exporters validators](https://www.directory.exportingisgreat.gov.uk/)

[![code-climate-image]][code-climate]
[![circle-ci-image]][circle-ci]
[![codecov-image]][codecov]
[![gemnasium-image]][gemnasium]

---

## Requirements

## Installation

```shell
pip install -e git+https://github.com/uktrade/directory-validators.git@<branch>#egg=directory_validators

```

## Usage

```python
from directory_validators import enrolment

enrolment.validate_company_number('12345678')
enrolment.validate_email('test@example.com')
```


## Development

    $ git clone https://github.com/uktrade/directory-validators
    $ cd directory-validators
    $ make


## Testing
	$ py.test .

[code-climate-image]: https://codeclimate.com/github/uktrade/directory-validators/badges/issue_count.svg
[code-climate]: https://codeclimate.com/github/uktrade/directory-validators

[circle-ci-image]: https://circleci.com/gh/uktrade/directory-validators/tree/master.svg?style=svg
[circle-ci]: https://circleci.com/gh/uktrade/directory-validators/tree/master

[codecov-image]: https://codecov.io/gh/uktrade/directory-validators/branch/master/graph/badge.svg
[codecov]: https://codecov.io/gh/uktrade/directory-validators

[gemnasium-image]: https://gemnasium.com/badges/github.com/uktrade/directory-validators.svg
[gemnasium]: https://gemnasium.com/github.com/uktrade/directory-validators
