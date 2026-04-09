# Engineering Setup

## Prerequisites

- Go 1.25+
- Node.js LTS + pnpm
- Docker + Docker Compose
- PostgreSQL 18 (via Docker)

## Quick Start

```bash
make quickstart   # interactive setup
make up-full      # start all services
make health-check # verify services
```

## Environment

Copy `.env.example` to `.env` and fill in:
- `JWT_SIGNING_SECRET`
- `GITHUB_APP_ID` + `GITHUB_APP_PRIVATE_KEY`
- `DATABASE_URL`
