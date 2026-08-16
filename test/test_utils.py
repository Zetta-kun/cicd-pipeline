from app.utils import generate_hash, validate_version, parse_datetime

def test_generate_hash():
    """Hash funksiyası testi"""
    result = generate_hash("hello")
    assert len(result) == 32  # MD5 32 simvol
    assert generate_hash("hello") == generate_hash("hello")  # eyni giriş = eyni çıxış
    assert generate_hash("hello") != generate_hash("world")  # fərqli giriş ≠ eyni çıxış

def test_validate_version():
    """Versiya validasiya testi"""
    assert validate_version("1.0.0") == True
    assert validate_version("2.5.10") == True
    assert validate_version("v1.0.0") == False
    assert validate_version("1.0") == False
    assert validate_version("beta") == False
    assert validate_version("") == False

def test_parse_datetime_valid():
    """Düzgün tarix formatı"""
    result = parse_datetime("2024-01-15T10:30:00")
    assert result is not None
    assert "2024-01-15" in result

def test_parse_datetime_invalid():
    """Səhv tarix formatı"""
    result = parse_datetime("not-a-date")
    assert result is None
    result = parse_datetime("")
    assert result is None