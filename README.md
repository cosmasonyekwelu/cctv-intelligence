# cctv-intelligence

Local-first CCTV intelligence platform foundation for Stuch Beddings.

## Current status
This repository currently contains Phase 1 foundation scaffolding:
- Python package structure
- Environment-driven configuration
- Structured logging bootstrap
- SQLite connection and migration bootstrap
- Minimal health endpoint
- Baseline unit tests

## Quick start
1. Copy environment template:
   - `cp .env.example .env`
2. Run tests:
   - `python -m unittest discover -s tests -v`
3. Run local API:
   - `python scripts/run_api.py`
4. Health check:
   - `curl http://127.0.0.1:8000/health`
