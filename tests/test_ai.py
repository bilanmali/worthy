from services.ai import get_verdict

def test_get_verdict_returns_text():
    # ask for a verdict and check we get some text back, not empty
    verdict = get_verdict("Netflix", days_since_last_used=5)
    assert isinstance(verdict, str)
    assert len(verdict) > 0