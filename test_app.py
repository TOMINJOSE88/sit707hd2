import app

def log_test(name, description, passed):
    print(f"\n[Test Case] {name}")
    print(f"Description: {description}")
    print(f"Result: {'✅ PASSED' if passed else '❌ FAILED'}")

def test_home():
    name = "Home Page Access"
    desc = "Check if the home page loads successfully and contains the correct heading."
    try:
        client = app.app.test_client()
        response = client.get('/')
        assert response.status_code == 200
        assert b"Simple BMI Calculator" in response.data
        log_test(name, desc, True)
    except AssertionError:
        log_test(name, desc, False)
        raise

def test_bmi_underweight():
    name = "BMI Category - Underweight"
    desc = "Input: weight=40, height=1.75 (Expected Category: Underweight)"
    try:
        client = app.app.test_client()
        response = client.post('/bmi', data={"weight": "40", "height": "1.75"})
        assert response.status_code == 200
        assert b"Underweight" in response.data
        log_test(name, desc, True)
    except AssertionError:
        log_test(name, desc, False)
        raise

def test_bmi_normal():
    name = "BMI Category - Normal weight"
    desc = "Input: weight=70, height=1.75 (Expected Category: Normal weight)"
    try:
        client = app.app.test_client()
        response = client.post('/bmi', data={"weight": "70", "height": "1.75"})
        assert response.status_code == 200
        assert b"Normal weight" in response.data
        log_test(name, desc, True)
    except AssertionError:
        log_test(name, desc, False)
        raise

def test_bmi_overweight():
    name = "BMI Category - Overweight"
    desc = "Input: weight=85, height=1.75 (Expected Category: Overweight)"
    try:
        client = app.app.test_client()
        response = client.post('/bmi', data={"weight": "85", "height": "1.75"})
        assert response.status_code == 200
        assert b"Overweight" in response.data
        log_test(name, desc, True)
    except AssertionError:
        log_test(name, desc, False)
        raise

def test_bmi_obese():
    name = "BMI Category - Obese"
    desc = "Input: weight=110, height=1.75 (Expected Category: Obese)"
    try:
        client = app.app.test_client()
        response = client.post('/bmi', data={"weight": "110", "height": "1.75"})
        assert response.status_code == 200
        assert b"Obese" in response.data
        log_test(name, desc, True)
    except AssertionError:
        log_test(name, desc, False)
        raise

def test_invalid_input():
    name = "Invalid Input - Text Instead of Numbers"
    desc = "Input: weight=abc, height=xyz (Expected: Error message)"
    try:
        client = app.app.test_client()
        response = client.post('/bmi', data={"weight": "abc", "height": "xyz"})
        assert response.status_code == 200
        assert b"Invalid input" in response.data
        log_test(name, desc, True)
    except AssertionError:
        log_test(name, desc, False)
        raise

def test_zero_height():
    name = "Invalid Input - Height Zero"
    desc = "Input: weight=70, height=0 (Expected: Height must be greater than zero)"
    try:
        client = app.app.test_client()
        response = client.post('/bmi', data={"weight": "70", "height": "0"})
        assert response.status_code == 200
        assert b"Height must be greater than zero" in response.data
        log_test(name, desc, True)
    except AssertionError:
        log_test(name, desc, False)
        raise
def test_bmi_failing_case():
    name = "Intentional Fail Case - Wrong BMI Category"
    desc = "Input: weight=70, height=1.75 (Expecting 'Obese' instead of correct 'Normal weight')"
    try:
        client = app.app.test_client()
        response = client.post('/bmi', data={"weight": "70", "height": "1.75"})
        assert b"Obese" in response.data  # This will fail intentionally
        log_test(name, desc, True)
    except AssertionError:
        log_test(name, desc, False)
        raise