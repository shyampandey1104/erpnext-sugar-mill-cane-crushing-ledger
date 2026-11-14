# ERPNext Sugar Mill Cane Crushing & FRP Payment Engine

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Sugar](https://img.shields.io/badge/Agri--Manufacturing-Sugar%20Mills-olive.svg)](https://dfpd.gov.in)

Sugar mill pit-head cane weighment, laboratory pol/brix recovery adjustment, and Statutory Fair & Remunerative Price (FRP) fortnightly farmer ledger engine.

## Features
- **Statutory Central FRP Formula:** Automated base FRP rate calculation plus recovery premium increments above 10.25%.
- **By-Product Mass Balance:** Yield calculation for molasses and bagasse cogeneration feedstock.
- **Farmer Direct Benefit Ledger:** Fortnightly payment advice generation ready for PFMS / NEFT bank integration.

## Tests
```bash
python3 -m unittest discover tests
```
