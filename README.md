# directory-validators
[Directory of UK Exporters validators](https://www.directory.exportingisgreat.gov.uk/)

## Build status

[![CircleCI](https://circleci.com/gh/uktrade/directory-validators/tree/master.svg?style=svg)](https://circleci.com/gh/uktrade/directory-validators/tree/master)

## Coverage

[![codecov](https://codecov.io/gh/uktrade/directory-validators/branch/master/graph/badge.svg)](https://codecov.io/gh/uktrade/directory-validators)

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
