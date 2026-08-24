# Phase 5: Production Readiness

**Days 41–50 · Outcome:** turn the working AI feature into a measured, observable, secure, cost-aware, containerized release candidate.

Create a `phase-5` branch. A feature is not production-ready merely because its happy-path demo works.

## Day 41: Evaluation strategy and datasets

**Learn:** Offline versus online evaluation, golden datasets, representative sampling, slice metrics, regression thresholds, annotation guidance, inter-rater disagreement, dataset versioning, and contamination.

**Build:** Create a versioned evaluation set with at least 30 questions: answerable, unanswerable, ambiguous, multi-document, conflicting, adversarial, and permission-sensitive. Store expected sources and acceptable answer criteria—not one brittle exact sentence.

**Ship:** Add an evaluation card documenting purpose, collection method, sensitive-data policy, important slices, limitations, and change process.

**Check:** Keep the set separate from prompt examples and development fixtures. Each item has an ID and reason for inclusion.

**Resources:** [OpenAI evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices) · [Google ML test and monitor guidance](https://developers.google.com/machine-learning/testing-debugging) · [Hugging Face dataset cards](https://huggingface.co/docs/hub/datasets-cards)

## Day 42: Automated AI evaluations

**Learn:** Deterministic checks, retrieval metrics, groundedness, answer relevance, citation correctness, model-graded evaluation, calibration, repeated trials, confidence intervals, and why human review remains necessary.

**Build:** Write an evaluation runner that records retrieval hit-rate, abstention correctness, citation validity, latency, token usage, and estimated cost. Add an optional judge behind a documented rubric, blind it to irrelevant metadata, and spot-check its disagreements with humans.

**Ship:** Produce a machine-readable result and a Markdown summary. Set an initial regression budget based on the measured baseline rather than an arbitrary perfect score.

**Check:** A deliberately broken retriever fails the gate; repeated stochastic runs reveal variance instead of overwriting it.

**Resources:** [OpenAI evals guide](https://developers.openai.com/api/docs/guides/evals) · [OpenAI graders](https://developers.openai.com/api/docs/guides/graders) · [Evidently: LLM evaluation](https://www.evidentlyai.com/llm-guide/llm-evaluation)

## Day 43: Safety, hallucination, and prompt injection

**Learn:** Prompt injection, indirect injection in retrieved content, insecure output handling, excessive agency, data exfiltration, hallucination, unsafe content, denial-of-wallet, red teaming, and layered defenses.

**Build:** Threat-model the AI-specific flow. Add adversarial documents and questions to the evaluation set. Clearly delimit untrusted text, minimize tool permissions, validate citations and outputs, cap input/output/tool steps, and require approval for side effects.

**Ship:** A red-team report with attacks attempted, observed outcomes, mitigations, residual risk, and a release-blocking severity definition.

**Check:** Retrieved instructions cannot override the application policy or reveal another user's content; output rendered in the browser is safely escaped.

**Resources:** [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) · [OpenAI safety best practices](https://developers.openai.com/api/docs/guides/safety-best-practices) · [NIST Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)

## Day 44: Observability for AI systems

**Learn:** Structured logs, metrics, traces, spans, correlation IDs, RED metrics, semantic conventions, cardinality, sampling, privacy-aware telemetry, dashboards, and the difference between observability and dumping raw prompts.

**Build:** Trace browser → API → retrieval → model → response. Record stage latency, result count, model/prompt version, token usage, status, and stable error class. Add request/job/run IDs. Export through OpenTelemetry or a local compatible collector.

**Ship:** A dashboard or saved query answering: Is it failing? Where is it slow? Which version is affected? What does it cost? Add one screenshot with synthetic data only.

**Check:** No secrets or raw private documents appear in telemetry; user-provided values are not metric labels with unbounded cardinality.

**Resources:** [OpenTelemetry Python](https://opentelemetry.io/docs/languages/python/) · [OpenTelemetry concepts](https://opentelemetry.io/docs/concepts/) · [Google SRE: monitoring distributed systems](https://sre.google/sre-book/monitoring-distributed-systems/)

## Day 45: Latency, reliability, and cost

**Learn:** Latency percentiles, timeouts, retry budgets, exponential backoff with jitter, rate limits, circuit breaking, concurrency limits, caching, batching, streaming, token budgets, fallbacks, and cost per successful task.

**Build:** Benchmark at least 30 representative requests. Allocate an end-to-end latency budget across retrieval and generation. Add request timeouts, bounded retries for transient/idempotent calls, concurrency control, and safe caching where identity and prompt/model versions are part of the key.

**Ship:** A before/after report with p50/p95 latency, success rate, tokens, estimated cost, quality score, and the tradeoff you chose.

**Check:** A retry storm cannot multiply indefinitely; a cache cannot return one user's answer to another.

**Resources:** [OpenAI latency optimization](https://developers.openai.com/api/docs/guides/latency-optimization) · [OpenAI cost optimization](https://developers.openai.com/api/docs/guides/cost-optimization) · [AWS Builders' Library: avoiding overload](https://aws.amazon.com/builders-library/avoiding-insurmountable-queue-backlogs/)

## Day 46: Security, privacy, and data governance

**Learn:** Asset inventory, data classification, least privilege, encryption in transit/at rest, secret rotation, retention and deletion, dependency risk, software bills of materials, log redaction, tenant isolation, and incident response.

**Build:** Draw a data-flow diagram from upload through storage, embeddings, model provider, telemetry, backups, and deletion. Classify each data element. Minimize what leaves the service, define retention, implement collection deletion, and verify provider settings match the intended privacy posture.

**Ship:** Update the threat model and add a security checklist, dependency scan, secret scan, and documented credential-rotation procedure using dummy values.

**Check:** A deletion test proves documents, chunks, vectors, cached results, and accessible references disappear according to policy; backups have a documented expiry limitation.

**Resources:** [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [GitHub secret scanning](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning) · [OpenSSF Scorecard](https://scorecard.dev/)

## Day 47: Production Docker images

**Learn:** Images, layers, build context, registries, containers, volumes, networks, tags versus digests, multi-stage builds, caching, PID 1, signals, health checks, non-root users, and image scanning.

**Build:** Write Dockerfiles for the API, worker, and web app. Use small trusted base images, pinned runtime versions, deterministic dependency installation, multi-stage builds, a non-root user, `.dockerignore`, and an exec-form entrypoint. Do not bake credentials into layers.

**Ship:** Build, inspect, run, stop gracefully, and scan the images. Record size, start time, user, exposed port, health behavior, and accepted scan findings.

**Check:** The service starts from environment configuration, writes mutable data outside the image, and handles `SIGTERM` within the platform grace period.

**Resources:** [Docker get started](https://docs.docker.com/get-started/) · [Dockerfile best practices](https://docs.docker.com/build/building/best-practices/) · [Docker build secrets](https://docs.docker.com/build/building/secrets/)

## Day 48: Local systems with Docker Compose

**Learn:** Container networking, service discovery, volumes, environment interpolation, dependency readiness versus startup order, profiles, resource limits, and the boundary between development orchestration and production scheduling.

**Build:** Compose the web app, API, worker, PostgreSQL/pgvector, Redis, and optional telemetry collector. Add persistent named volumes, health checks, explicit networks, sensible resource limits, and a one-shot migration service. Keep secrets outside the Compose file.

**Ship:** Document `start`, `migrate`, `seed`, `test`, `logs`, `stop`, and safe reset commands. Test on a clean machine or clean Docker state without relying on host-installed runtimes.

**Check:** Application readiness waits for usable dependencies; restarting a worker does not lose persisted documents or duplicate completed jobs.

**Resources:** [Docker Compose overview](https://docs.docker.com/compose/) · [Compose networking](https://docs.docker.com/compose/how-tos/networking/) · [Compose startup order](https://docs.docker.com/compose/how-tos/startup-order/)

## Day 49: Cloud and deployment architecture

**Learn:** Regions and availability zones, compute, managed databases/caches, object storage, container registries, DNS, TLS, load balancers, IAM, firewalls, secret managers, horizontal scaling, infrastructure as code, and the shared-responsibility model.

**Build:** Choose one affordable deployment target—such as a container platform/PaaS plus managed PostgreSQL—and write an ADR. Diagram network and trust boundaries, public/private components, secret flow, storage, backups, scaling, observability, and estimated monthly cost.

**Ship:** Provision a minimal disposable sandbox manually or with infrastructure as code, but do not deploy the app yet. Set a budget alert and teardown procedure before creating paid resources.

**Check:** No database or cache is unnecessarily public; workloads use service identity where available instead of long-lived embedded keys.

**Resources:** [AWS cloud essentials](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html) · [Azure architecture fundamentals](https://learn.microsoft.com/en-us/azure/architecture/guide/) · [Google Cloud architecture framework](https://cloud.google.com/architecture/framework)

## Day 50: Milestone release candidate

**Build:** Produce a release candidate that runs as a complete Compose stack, passes conventional tests and the AI evaluation gate, emits usable telemetry, survives transient provider failure, and has documented security/privacy behavior.

**Required quality:** Hardened images, exact config contract, health/readiness checks, migrations, no critical known vulnerabilities, dataset and prompt/model versions, latency/cost report, red-team results, deletion path, architecture and data-flow diagrams.

**Ship:** Open a milestone PR with a release checklist, generated evaluation summary, image digests, scan results, demo evidence, accepted risks, and deployment ADR. Merge and tag `v0.1.0-rc.1` and `day-50`.

**Demo:** Start from a clean clone with one documented command sequence, run a question, trace it, show the evaluation result, simulate provider failure, and shut everything down cleanly.

**Resources:** [SLSA supply-chain levels](https://slsa.dev/) · [CIS Docker Benchmark overview](https://www.cisecurity.org/benchmark/docker) · [OpenAI deployment checklist](https://developers.openai.com/api/docs/guides/deployment-checklist)

## Phase 5 exit ticket

Show evidence—not confidence—for quality, safety, latency, cost, tenant isolation, deletion, reproducibility, and recoverability. Explain every remaining release risk and who owns it.
