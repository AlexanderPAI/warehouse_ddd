import pytest

from tests.unit.domain.fixtures import dto_fixtures


@pytest.mark.parametrize("dto, expected", dto_fixtures)
def test_dto_to_dict(dto, expected):
    assert dto.as_dict() == expected
