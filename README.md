# E-Commerce Order Processing Service (`ecommerce_service`)

A Python microservice responsible for cart calculations, regional taxation, promotional voucher deduction, logistics route dispatch, and customer onboarding.

---

## 1. Project Structure

```
ecommerce_service/
├── app.py                      # Main pipeline orchestrator
├── requirements.txt            # Microservice dependencies
├── core/
│   ├── pricing_engine.py       # Container volume & packaging calculation
│   ├── discount_calculator.py  # VIP and promotional cart threshold rules
│   └── tax_service.py          # State/regional sales tax engine
├── services/
│   ├── order_processor.py      # High-volume batch ingestion loop
│   ├── shipping_router.py      # Multi-carrier logistics dispatch logic
│   ├── account_manager.py      # Customer profile registration & onboarding
│   └── payment_auditor.py      # Settlement validation & audit trailing
├── utils/
│   ├── network_client.py       # Socket and gateway port parsing
│   ├── config_loader.py        # Settings reader from filesystem
│   └── data_formatter.py       # Data formatting and reporting helper
├── models/
│   ├── customer.py             # Domain customer entity
│   └── address.py              # Address value object
├── refactoring_plan.json       # SCTVA / RDP automated refactoring plan
├── demo_runner.py              # Live demonstration script
└── README.md
```

---

## 2. Refactoring Catalog

| Target File | Detected Smell | Refactoring Action | Confidence | Rollback |
|---|---|---|---|---|
| `core/pricing_engine.py` | `MagicNumber` (`3.14159`) | **Introduce Constant** (`PI_VALUE`) | **0.998** | **No** |
| `core/discount_calculator.py` | `MagicNumber` (`1000`) | **Introduce Constant** (`MIN_DISCOUNT_THRESHOLD`) | **0.997** | **No** |
| `core/tax_service.py` | `MagicNumber` (`0.15`) | **Introduce Constant** (`DEFAULT_TAX_RATE`) | **0.997** | **No** |
| `services/order_processor.py` | `LongMethod` | **Extract Method** (`calculate_order_totals`) | **0.954** | **No** |
| `services/shipping_router.py` | `SwitchStatements` (5 branches) | **Replace Conditional with Polymorphism** | **0.878** | **No** |
| `services/account_manager.py` | `TooManyParameters` (6 params) | **Introduce Parameter Object** (`RegistrationData`) | **0.908** | **No** |
| `services/payment_auditor.py` | `UnreachableCode` (dead print) | **Remove Dead Code** | **1.000** | **No** |
| `utils/network_client.py` | `BareExcept` (broad catch) | **Replace Bare Except with Specific Exception** (`ValueError`) | **1.000** | **No** |
| `utils/config_loader.py` | `BareExcept` (file I/O) | **Replace Bare Except with Specific Exception** (`OSError`) | **1.000** | **No** |
| `utils/data_formatter.py` | Cryptic Method Name (`calc_dat`) | **Rename Method** (`calculate_formatted_data`) | **0.955** | **No** |
| `models/customer.py` | `MessageChains` (Demeter violation) | **Hide Delegate** (`Customer.get_city()` forwarder) | **0.987** | **No** |

---

## 3. Live Demonstration

Run the automated safety verification and transformation demo:

```powershell
python ecommerce_service/demo_runner.py
```

Expected result:
```
TOTAL: 11/11 Transformations Passed with 100% Behavioral Safety & 0 Rollbacks.
```
