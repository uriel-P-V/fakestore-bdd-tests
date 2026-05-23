# fakestore-bdd-tests

![CI](https://github.com/uriel-P-V/fakestore-bdd-tests/actions/workflows/tests.yml/badge.svg)

A BDD-based test suite for the FakeStore API —
demonstrates advanced mocking techniques with Behave and Gherkin,
including patch.object, MagicMock spec, side_effect exceptions,
and a modular mock architecture separated by domain.

---

## Project Structure

```
fakestore-bdd-tests/
├── .github/
│   └── workflows/
│       └── tests.yml                  ← GitHub Actions CI
├── features/
│   ├── mocks/
│   │   ├── __init__.py
│   │   ├── products_mock.py           ← Mock data and GET handler for products
│   │   ├── cart_mock.py               ← Mock data and POST handler for cart
│   │   └── users_mock.py              ← Mock data and GET handler for users
│   ├── steps/
│   │   ├── common_steps.py            ← Shared steps across features
│   │   ├── products_steps.py          ← Products feature steps
│   │   ├── cart_steps.py              ← Cart feature steps
│   │   └── users_steps.py             ← Users feature steps
│   ├── environment.py                 ← Hooks and unified mock orchestration
│   ├── cart_client.py                 ← CartClient class wrapping POST /carts
│   ├── products.feature               ← List and get products
│   ├── cart.feature                   ← Create cart, validate fields, timeout
│   └── users.feature                  ← Get user, validate fields
└── requirements.txt
```

---

## Features

- **Multi-feature BDD** — three independent Gherkin feature files by domain
- **Modular mock architecture** — `features/mocks/` folder with one file per domain
- **Unified mock dispatcher** — `environment.py` routes by URL to the right mock
- **4 advanced mocking techniques** — see below
- **Tag-driven execution** — `@smoke` hits real API, `@regression` fully mocked
- **GitHub Actions CI** — smoke runs first, regression only if smoke passes

---

## Mocking Techniques

### 1 — `patch("requests.get")` with URL discrimination
Routes GET requests to different mock handlers based on the URL path.
```python
def unified_mock_get(url, **kwargs):
    if "/products" in url:
        return mock_products_get(url, **kwargs)
    elif "/users" in url:
        return mock_users_get(url, **kwargs)
```

### 2 — `patch.object` on a class instance
Patches a specific method on a specific instance — does not affect other callers.
```python
with patch.object(client, "create_cart", side_effect=requests.exceptions.Timeout):
    try:
        client.create_cart(VALID_CART_DATA)
    except requests.exceptions.Timeout:
        context.timeout_raised = True
```

### 3 — `MagicMock(spec=dict)`
Enforces that the mock only allows attributes that exist on a real `dict`.
Catches typos and contract violations at test time.
```python
mock_validator = MagicMock(spec=dict)
mock_validator.__contains__ = MagicMock(return_value=True)
assert isinstance(data, dict)
```

### 4 — `side_effect=Exception` for network failures
Simulates timeouts and network errors without hitting the real API.
```python
patch("requests.post", side_effect=requests.exceptions.Timeout)
```

---

## Setup

```bash
git clone https://github.com/uriel-P-V/fakestore-bdd-tests.git
cd fakestore-bdd-tests
pip install -r requirements.txt
behave
```

---

## Running Tests

```bash
# All scenarios
behave

# Smoke only — hits real API, fast critical check
behave --tags=smoke

# Regression only — fully mocked, no internet required
behave --tags=regression

# Single feature
behave features/products.feature
behave features/cart.feature
behave features/users.feature
```

---

## CI/CD Pipeline
Two dependent jobs run on every push and pull request to `main`:
If `smoke` fails, `regression` is skipped automatically.

> **Note:** FakeStore API blocks requests from CI/CD datacenter IPs (403 Forbidden).
> Smoke tests are configured with `continue-on-error: true` in CI.
> Run `behave --tags=smoke` locally to validate against the real API.

```
push / PR → smoke (3 scenarios) → regression (6 scenarios) 
```

If `smoke` fails, `regression` is skipped automatically.

---

## API Under Test

**FakeStore API** — `https://fakestoreapi.com`  
Public REST API for e-commerce testing. No authentication required.

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/products` | GET | List all products |
| `/products/{id}` | GET | Get product by ID |
| `/carts` | POST | Create cart |
| `/users/{id}` | GET | Get user by ID |

---

## Tech Stack

- **Python 3.11+**
- **Behave** — BDD framework with Gherkin support
- **Requests** — HTTP client for API calls
- **unittest.mock** — patch, patch.object, MagicMock, side_effect

- **GitHub Actions** — CI/CD pipeline

---




## Author

**Uriel Alejandro Pérez Valdovinos**  
[github.com/uriel-P-V](https://github.com/uriel-P-V) · [linkedin.com/in/uriel-pv](https://linkedin.com/in/uriel-pv)