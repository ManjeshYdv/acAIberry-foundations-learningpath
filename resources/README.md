# Curated Resource Library

Use this page as a reference desk, not a second syllabus. Each curriculum day already links to the smallest useful reading. Start with primary documentation, build the exercise, and consult a deeper resource when a specific question appears.

Resource links were selected for technical quality, practical examples, stable ownership, and free access where possible. A resource appearing here is not an instruction to complete it end to end.

## Core foundations

| Area | Start here | Go deeper |
| --- | --- | --- |
| Linux and shell | [The Missing Semester](https://missing.csail.mit.edu/) | [Linux Journey](https://linuxjourney.com/) · [GNU manuals](https://www.gnu.org/manual/manual.html) |
| Networking and HTTP | [MDN: how the web works](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works) | [Cloudflare Learning Center](https://www.cloudflare.com/learning/) · [HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110) |
| Git | [Pro Git](https://git-scm.com/book/en/v2) | [Learn Git Branching](https://learngitbranching.js.org/) · [Git reference](https://git-scm.com/docs) |
| GitHub collaboration | [GitHub Skills](https://skills.github.com/) | [GitHub pull-request docs](https://docs.github.com/en/pull-requests) · [Google code review guide](https://google.github.io/eng-practices/review/) |

## Software engineering

| Area | Start here | Go deeper |
| --- | --- | --- |
| Python | [Official Python tutorial](https://docs.python.org/3/tutorial/) | [Python Packaging User Guide](https://packaging.python.org/) · [Architecture Patterns with Python](https://www.cosmicpython.com/book/preface.html) |
| Testing | [pytest documentation](https://docs.pytest.org/) | [Testcontainers](https://testcontainers.com/) · [Testing Library principles](https://testing-library.com/docs/guiding-principles/) |
| TypeScript | [TypeScript handbook](https://www.typescriptlang.org/docs/handbook/intro.html) | [TypeScript for JavaScript programmers](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html) |
| React | [React Learn](https://react.dev/learn) | [web.dev accessibility](https://web.dev/learn/accessibility/) · [Playwright](https://playwright.dev/docs/intro) |
| API development | [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/) | [OpenAPI specification](https://spec.openapis.org/oas/latest.html) · [OWASP API Security](https://owasp.org/API-Security/) |
| Architecture | [C4 model](https://c4model.com/) | [Architecture Decision Records](https://adr.github.io/) · [The Twelve-Factor App](https://12factor.net/) |

## Data systems

| Area | Start here | Go deeper |
| --- | --- | --- |
| SQL | [SQLBolt](https://sqlbolt.com/) | [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html) |
| Database internals | [PostgreSQL documentation](https://www.postgresql.org/docs/current/) | [Use The Index, Luke](https://use-the-index-luke.com/) |
| Python persistence | [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/20/tutorial/) | [Alembic](https://alembic.sqlalchemy.org/) |
| Redis and queues | [Redis data types](https://redis.io/docs/latest/develop/data-types/) | [Celery user guide](https://docs.celeryq.dev/en/stable/userguide/) |
| Vector search | [pgvector](https://github.com/pgvector/pgvector) | [FAISS](https://faiss.ai/) |

## AI engineering

| Area | Start here | Go deeper |
| --- | --- | --- |
| ML fundamentals | [Google ML Crash Course](https://developers.google.com/machine-learning/crash-course) | [scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html) |
| LLM concepts | [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/) | [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) |
| OpenAI platform | [API quickstart](https://developers.openai.com/api/docs/quickstart) | [Prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering) · [Function calling](https://developers.openai.com/api/docs/guides/function-calling) · [Embeddings](https://developers.openai.com/api/docs/guides/embeddings) |
| Anthropic platform | [API getting started](https://docs.anthropic.com/en/api/getting-started) | [Prompt engineering](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) · [Tool use](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview) |
| Retrieval and RAG | [OpenAI retrieval](https://developers.openai.com/api/docs/guides/retrieval) | [Azure advanced RAG](https://learn.microsoft.com/en-us/azure/developer/ai/advanced-retrieval-augmented-generation) |
| Agents | [OpenAI agents](https://developers.openai.com/api/docs/guides/agents) | [Anthropic: Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) |
| Evaluation | [OpenAI evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices) | [OpenAI evals](https://developers.openai.com/api/docs/guides/evals) · [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) |
| AI security | [OWASP GenAI Security](https://genai.owasp.org/) | [OpenAI safety best practices](https://developers.openai.com/api/docs/guides/safety-best-practices) |

## AI coding tools

Choose one assistant for the exercises. Learning the workflow transfers better than memorizing a product interface.

- **Codex:** [quickstart](https://learn.chatgpt.com/codex/quickstart), [prompting](https://learn.chatgpt.com/codex/prompting), [`AGENTS.md`](https://learn.chatgpt.com/codex/agent-configuration/agents-md), and [permissions](https://learn.chatgpt.com/codex/permissions).
- **Claude Code:** [overview](https://docs.anthropic.com/en/docs/claude-code/overview), [common workflows](https://docs.anthropic.com/en/docs/claude-code/common-workflows), and [security](https://docs.anthropic.com/en/docs/claude-code/security).
- **GitHub Copilot:** [documentation](https://docs.github.com/en/copilot) and [responsible use](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features).

Model names, product features, pricing, limits, and interfaces change quickly. Follow the current official documentation and pin important behavior with tests instead of copying old screenshots or commands.

## Containers, delivery, and operations

| Area | Start here | Go deeper |
| --- | --- | --- |
| Docker | [Docker get started](https://docs.docker.com/get-started/) | [Build best practices](https://docs.docker.com/build/building/best-practices/) · [Compose](https://docs.docker.com/compose/) |
| GitHub Actions | [Actions quickstart](https://docs.github.com/en/actions/writing-workflows/quickstart) | [Security hardening](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions) |
| Observability | [OpenTelemetry](https://opentelemetry.io/docs/) | [Prometheus](https://prometheus.io/docs/introduction/overview/) · [Grafana](https://grafana.com/docs/) |
| Reliability | [Google SRE book](https://sre.google/sre-book/table-of-contents/) | [Google SRE workbook](https://sre.google/workbook/table-of-contents/) |
| Supply chain | [OpenSSF Scorecard](https://scorecard.dev/) | [SLSA](https://slsa.dev/) · [GitHub artifact attestations](https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations) |
| Load testing | [k6](https://grafana.com/docs/k6/latest/) | [Locust](https://docs.locust.io/) |

## Cloud platform choices

The path is vendor-neutral. Pick the least expensive option that supports a containerized web service, worker, managed PostgreSQL, secrets, HTTPS, logs, and budget alerts.

- **AWS:** [Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
- **Microsoft Azure:** [Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/)
- **Google Cloud:** [Architecture Framework](https://cloud.google.com/architecture/framework)
- **Simple container platforms:** Render, Railway, Fly.io, Cloud Run, Azure Container Apps, or an equivalent may reduce setup time. Read the current official pricing and limits before provisioning.

Kubernetes is intentionally optional in this foundation. Learn it after you can deploy and operate one service well; it adds operational machinery but does not replace application reliability practices.

## Books worth keeping nearby

These are optional and may not be free:

- *Designing Data-Intensive Applications* — Martin Kleppmann
- *Release It!* — Michael T. Nygard
- *Designing Machine Learning Systems* — Chip Huyen
- *Building Machine Learning Powered Applications* — Emmanuel Ameisen
- *Site Reliability Engineering* — Betsy Beyer et al. ([free online edition](https://sre.google/sre-book/table-of-contents/))

## How to judge a new resource

Before adding a link, ask:

1. Does it support a specific learning objective or unblock a build?
2. Is the author authoritative and is the material maintained?
3. Does it teach reasoning and tradeoffs rather than copy/paste only?
4. Can a learner access it without surrendering unnecessary personal data or paying unexpectedly?
5. Is it better than a resource already listed?

