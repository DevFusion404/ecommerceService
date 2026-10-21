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

