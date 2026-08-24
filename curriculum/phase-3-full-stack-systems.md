# Phase 3: Full-Stack Systems

**Days 21–30 · Outcome:** build a secure, database-backed web application and understand the contracts connecting browser, API, worker, cache, and database.

Create a `phase-3` branch. Keep the backend under `apps/api`, the frontend under `apps/web`, and preserve the ingestion package as an independently tested component.

## Day 21: HTTP and API contracts

**Learn:** Resources, request methods, status codes, headers, JSON, idempotency, pagination, filtering, error bodies, API versioning, CORS, and the difference between transport and domain models.

**Build:** Design the document API before implementing it. Specify create/list/get/delete endpoints, pagination, validation errors, request IDs, and asynchronous ingestion status. Write example requests and responses in `docs/api-contract.md`.

**Ship:** Review the contract as a client: identify retry-safe operations, bounded collections, and every place user-controlled input crosses a boundary.

**Check:** Each endpoint has a clear success code, predictable error shape, and stated authentication rule.

**Resources:** [MDN HTTP methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods) · [Microsoft REST API Guidelines](https://github.com/microsoft/api-guidelines) · [OpenAPI specification](https://spec.openapis.org/oas/latest.html)

## Day 22: FastAPI and boundary validation

**Learn:** ASGI, routing, dependency injection, request/response schemas, middleware, generated OpenAPI, sync versus async handlers, and why validation belongs at system boundaries.

**Build:** Implement `/health`, `/ready`, and the first document routes in FastAPI using in-memory storage. Add centralized error responses and request-ID middleware. Keep domain logic outside route functions.

**Ship:** API tests for valid and invalid requests plus a checked-in OpenAPI snapshot or documented generated schema command.

**Check:** `/health` reports that the process runs; `/ready` reports whether dependencies are usable. Neither exposes secrets or stack traces.

**Resources:** [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) · [FastAPI testing](https://fastapi.tiangolo.com/tutorial/testing/) · [ASGI specification](https://asgi.readthedocs.io/en/latest/)

## Day 23: Relational data and SQL

**Learn:** Tables, rows, keys, constraints, normalization, joins, aggregates, indexes, query plans, and parameterized queries. Model data around invariants, not around the current screen.

**Build:** Design tables for users, collections, documents, chunks, ingestion jobs, and queries. Draw relationships, choose primary/foreign keys, add uniqueness and nullability rules, and create a small database in PostgreSQL or SQLite for SQL practice.

**Ship:** Write SQL for insert, update, pagination, document/chunk joins, aggregate counts, and safe deletion. Save it under `docs/sql-practice.sql` with expected results.

**Check:** Explain which invalid states the database prevents even if application validation is bypassed.

**Resources:** [SQLBolt](https://sqlbolt.com/) · [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html) · [PostgreSQL constraints](https://www.postgresql.org/docs/current/ddl-constraints.html)

## Day 24: PostgreSQL, migrations, and transactions

**Learn:** Database processes and connections, transactions, isolation basics, connection pooling, schema migrations, forward/backward compatibility, backups, and indexes as measured tradeoffs.

**Build:** Run PostgreSQL locally, preferably through a temporary container. Create the initial schema through Alembic or another migration tool—not manual production steps. Wrap multi-table document creation in a transaction and add only indexes justified by a query.

**Ship:** Apply migrations from an empty database and roll back the latest safe migration. Record the commands and expected schema version.

**Check:** Force a failure halfway through an insert and prove no partial document remains.

**Resources:** [PostgreSQL transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html) · [PostgreSQL indexes](https://www.postgresql.org/docs/current/indexes.html) · [Alembic tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)

## Day 25: Data access and integration tests

**Learn:** Connection lifecycle, ORM benefits and traps, repository boundaries, N+1 queries, unit versus integration tests, test databases, fixtures, and deterministic cleanup.

**Build:** Implement document persistence with SQLAlchemy. Keep transaction ownership in the application/service layer. Add integration tests against a real disposable PostgreSQL database for constraints, transactions, and representative queries.

**Ship:** Capture an `EXPLAIN` plan for the document list query before and after an appropriate index. Explain the difference rather than chasing arbitrary speed.

**Check:** Route tests do not need to know SQL, and domain tests do not need a database.

**Resources:** [SQLAlchemy unified tutorial](https://docs.sqlalchemy.org/en/20/tutorial/) · [PostgreSQL `EXPLAIN`](https://www.postgresql.org/docs/current/using-explain.html) · [Testcontainers for Python](https://testcontainers-python.readthedocs.io/)

## Day 26: Authentication and web security

**Learn:** Authentication versus authorization, sessions and tokens, password hashing, secure cookies, CSRF, CORS, input validation, injection, broken access control, rate limiting, and threat modeling. Do not invent cryptography or a production identity provider.

**Build:** For learning, add a simple authenticated user flow using a maintained library or external identity-provider mock. Protect collection routes and enforce ownership in the service/data query—not only in the UI. Configure exact CORS origins and redact credentials from logs.

**Ship:** Create `docs/threat-model.md` listing assets, actors, trust boundaries, likely abuse cases, mitigations, and accepted risks.

**Check:** Test unauthenticated access, cross-user access, malformed tokens, and login throttling. If your practice auth is not production-ready, label it clearly.

**Resources:** [OWASP Top 10](https://owasp.org/www-project-top-ten/) · [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) · [FastAPI security](https://fastapi.tiangolo.com/tutorial/security/)

## Day 27: TypeScript and React foundations

**Learn:** TypeScript primitives, unions, interfaces, modules, promises, browser events, React components, props, state, effects, forms, and component composition.

**Build:** Create a Vite React/TypeScript app. Implement typed components to list documents, show status, and submit a document form using local fixture data. Keep data-fetching types and UI types explicit.

**Ship:** Component tests for loading, empty, populated, validation-error, and unexpected-error states.

**Check:** The page remains understandable with JavaScript errors and usable by keyboard; no component assumes that network data is automatically valid.

**Resources:** [TypeScript handbook](https://www.typescriptlang.org/docs/handbook/intro.html) · [React Learn](https://react.dev/learn) · [Vite guide](https://vite.dev/guide/)

## Day 28: Full-stack integration

**Learn:** Browser fetch, asynchronous state, cancellation, optimistic versus pessimistic updates, cache invalidation, error boundaries, accessibility, responsive design, and client/server contract drift.

**Build:** Connect the React app to the API. Generate or hand-maintain a narrow typed client from the OpenAPI contract. Show explicit loading, retry, empty, success, and error states. Add a correlation/request ID to user-visible error details.

**Ship:** One browser-level test that creates a document and observes it in the list, plus an API contract test that catches incompatible schema changes.

**Check:** A slow request, offline API, duplicate submission, and server validation error each produce useful behavior.

**Resources:** [MDN Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) · [web.dev accessibility](https://web.dev/learn/accessibility/) · [Playwright intro](https://playwright.dev/docs/intro)

## Day 29: Caching, queues, and background work

**Learn:** Latency versus throughput, synchronous versus asynchronous work, caching, TTLs, cache invalidation, queues, retries, dead-letter handling, idempotency keys, delivery semantics, and backpressure.

**Build:** Move ingestion out of the request path. The API creates a job and returns `202`; a worker claims it and records progress. A repeated idempotency key must not create duplicate work. Use Redis if practical, but keep the job interface independent of the queue technology.

**Ship:** A state diagram for queued → running → succeeded/failed, including retry limits and crash recovery. Test duplicate delivery and a worker crash.

**Check:** The UI can poll boundedly or receive status without holding the upload request open.

**Resources:** [Redis data types](https://redis.io/docs/latest/develop/data-types/) · [Celery tasks](https://docs.celeryq.dev/en/stable/userguide/tasks.html) · [AWS Builders' Library: retries and backoff](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/)

## Day 30: Milestone production-shaped CRUD

**Build:** Deliver a vertical slice where an authenticated user can create a collection, submit a document, watch ingestion status, browse stored documents, and delete owned data. Run the API, worker, database, and optional cache with documented local commands.

**Required quality:** Database migrations, ownership checks, boundary validation, timeouts, structured errors, integration tests, one browser test, request IDs, health/readiness endpoints, and no credentials in source.

**Ship:** Open a milestone PR with an architecture diagram, API examples, test evidence, threat-model update, screenshots, and known limitations. Merge and tag `day-30`.

**Demo:** Start from an empty database, apply migrations, ingest a file, find it in the UI, demonstrate a rejected cross-user request, and trace an error by request ID.

**Resources:** [C4 model for architecture diagrams](https://c4model.com/) · [The Twelve-Factor App](https://12factor.net/) · [OWASP API Security Top 10](https://owasp.org/API-Security/)

## Phase 3 exit ticket

Explain the complete request path and where authentication, authorization, validation, transactions, idempotency, and error translation occur. Rebuild the database from migrations and run the browser flow from a clean checkout.
