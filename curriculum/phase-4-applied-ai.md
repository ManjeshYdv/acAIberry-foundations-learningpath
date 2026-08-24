# Phase 4: Applied AI Systems

**Days 31–40 · Outcome:** build a grounded AI feature with explicit contracts, measurable retrieval, controlled tool use, source citations, and provider boundaries.

Create a `phase-4` branch. Keep a non-AI baseline and deterministic fixtures so development and tests do not require paid API calls.

## Day 31: Machine-learning mental models

**Learn:** Features and labels, training/validation/test splits, supervised versus unsupervised learning, inference, generalization, overfitting, data leakage, distribution shift, classification/regression, and precision/recall/F1. Understand that a metric encodes a product tradeoff.

**Build:** Take a small labeled dataset such as support-topic examples. Write a rule-based baseline, split the data before tuning it, and calculate a confusion matrix, precision, and recall. Identify the cost of false positives and false negatives for your scenario.

**Ship:** `docs/ml-baseline.md` with the data assumptions, metric choice, result, error examples, and one leakage risk.

**Check:** You can explain why “accuracy” may be misleading and why a test set is not repeatedly used for tuning.

**Resources:** [Google Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course) · [scikit-learn model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html) · [Rules of Machine Learning](https://developers.google.com/machine-learning/guides/rules-of-ml)

## Day 32: How LLMs behave

**Learn:** Tokens, embeddings, transformer attention at a conceptual level, pretraining, post-training, context windows, next-token generation, sampling, temperature, hallucination, and why fluent output is not verified truth.

**Build:** Using an approved model playground or a local model, vary prompt wording, context, temperature, and output constraints across a fixed question set. Record output quality, consistency, token use, and failure cases. Do not send private data.

**Ship:** `experiments/llm-behavior.md` with hypotheses, setup, observations, and conclusions rather than a collection of screenshots.

**Check:** Explain the difference between model parameters, request parameters, context, retrieved evidence, and generated output.

**Resources:** [Hugging Face LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) · [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) · [OpenAI token counting guide](https://developers.openai.com/api/docs/guides/token-counting)

## Day 33: Model APIs and structured output

**Learn:** Provider SDKs, authentication, model selection, messages and roles, structured outputs, streaming, rate limits, retries, timeouts, usage accounting, and the difference between transient and permanent errors.

**Build:** Define an application-owned `ModelClient` interface. Implement one real provider adapter and one deterministic fake. Request a typed answer containing text, citations, and confidence notes; validate every response before use. Bound retries and respect provider retry hints.

**Ship:** Contract tests that run against the fake by default, plus an explicitly enabled smoke test for the real service. Record model and prompt versions with latency and token usage.

**Check:** The app starts without a model key in local fake mode and fails safely—not mysteriously—when live mode lacks credentials.

**Resources:** [OpenAI API quickstart](https://developers.openai.com/api/docs/quickstart) · [OpenAI structured outputs](https://developers.openai.com/api/docs/guides/structured-outputs) · [Anthropic API getting started](https://docs.anthropic.com/en/api/getting-started)

## Day 34: Prompt design as code

**Learn:** Clear instructions, context delimiters, examples, output contracts, decomposition, prompt injection boundaries, and the interaction between model behavior and evaluation. Prompts are versioned application logic, not magic prose.

**Build:** Create a prompt module for grounded question answering. State the task, allowed evidence, abstention behavior, citation format, and untrusted-content boundaries. Add several few-shot examples only if an evaluation shows they help.

**Ship:** Version the prompt, render it with test fixtures, snapshot or assert its stable sections, and write a small change log explaining why each revision exists.

**Check:** Prompt inputs are escaped or delimited, token budget is visible, and changing the prompt triggers relevant evaluations.

**Resources:** [OpenAI prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering) · [Anthropic prompting overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) · [Prompt injection defenses](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)

## Day 35: Tool calling and control flow

**Learn:** Tool schemas, model-selected arguments, validation, authorization, confirmation, timeouts, bounded loops, idempotency, and why the application—not the model—owns execution and policy.

**Build:** Add read-only tools for listing collections and retrieving document metadata. Validate arguments, derive user identity from trusted application state, enforce ownership again in the tool, limit calls, and return compact structured results. Keep write/destructive tools out for now.

**Ship:** Tests for unknown tools, invalid arguments, unauthorized access, tool errors, repeated calls, and maximum-step termination.

**Check:** No model-produced string is executed as shell, SQL, or code; logs distinguish model decisions from application executions.

**Resources:** [OpenAI function calling](https://developers.openai.com/api/docs/guides/function-calling) · [Anthropic tool use](https://docs.anthropic.com/en/docs/build-with-claude/tool-use/overview) · [OWASP LLM Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/)

## Day 36: Embeddings and vector search

**Learn:** Dense vector representations, distance metrics, chunking, metadata filters, top-k retrieval, approximate nearest neighbors, indexing, and why retrieval quality depends heavily on the corpus and query—not only the embedding model.

**Build:** Generate embeddings for your chunks using a provider or local model and store them with content hashes and embedding-version metadata. Implement similarity search with collection/owner filters. Create 15 representative queries with expected relevant chunks.

**Ship:** A retrieval report containing recall@k or hit-rate@k, latency, index size, misses, and two chunking experiments.

**Check:** Re-ingestion does not embed unchanged chunks; a model/version change cannot silently mix incompatible vectors.

**Resources:** [OpenAI embeddings guide](https://developers.openai.com/api/docs/guides/embeddings) · [pgvector](https://github.com/pgvector/pgvector) · [Pinecone: chunking strategies](https://www.pinecone.io/learn/chunking-strategies/)

## Day 37: Build a RAG pipeline

**Learn:** Retrieval-augmented generation stages: query preparation, filtering, retrieval, optional reranking, context assembly, answer generation, citation mapping, and abstention. Retrieval and generation must be evaluated separately.

**Build:** Implement query → retrieve → build bounded context → generate → validate citations. Return stable source identifiers and quoted supporting spans. If no evidence clears a documented threshold, return “I don't have enough evidence” rather than improvise.

**Ship:** Integration tests for answerable, unanswerable, ambiguous, cross-tenant, and conflicting-source questions.

**Check:** Every claim that your product presents as sourced maps to content the user is authorized to read.

**Resources:** [OpenAI retrieval guide](https://developers.openai.com/api/docs/guides/retrieval) · [Azure advanced RAG guidance](https://learn.microsoft.com/en-us/azure/developer/ai/advanced-retrieval-augmented-generation) · [OWASP Vector and Embedding Weaknesses](https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/)

## Day 38: Agents, workflows, and state

**Learn:** Deterministic workflows versus agentic loops, state machines, planning, tool selection, memory, checkpoints, human approval, maximum steps, and compensation after partial failure. Use an agent only when fixed control flow is insufficient.

**Build:** Draw the question-answering flow as states and transitions. Implement a bounded orchestration loop that can retrieve, request clarification, answer, abstain, or fail. Require explicit human confirmation before any future side effect.

**Ship:** Persist enough state to resume or diagnose a run, with a trace containing decisions, tool calls, and outcomes but not hidden reasoning or secrets.

**Check:** Simulate tool failure, repeated model requests, malformed output, and maximum steps; every run reaches a terminal state.

**Resources:** [OpenAI agents guide](https://developers.openai.com/api/docs/guides/agents) · [Anthropic: building effective agents](https://www.anthropic.com/research/building-effective-agents) · [Statecharts introduction](https://statecharts.dev/what-is-a-state-machine.html)

## Day 39: Repository-aware coding agents

**Learn:** Repository instructions, scoped context, plan/implement/review loops, permission modes, automated checks, worktrees or isolated branches, and the risks of secrets, untrusted instructions, excessive autonomy, and unreviewed bulk edits.

**Build:** Add a concise `AGENTS.md` to the capstone describing repository layout, commands, conventions, boundaries, and definition of done. If your selected tool uses another instruction file, keep shared rules in one source and avoid contradictory copies. Ask the assistant to investigate one real issue, propose a plan, implement it, run checks, and self-review.

**Ship:** A human-reviewed PR containing the issue, plan, focused diff, test evidence, and your written review of the agent's decisions.

**Check:** The agent received no production secrets, used the narrowest permissions, changed only intended files, and left the tree understandable.

**Resources:** [Codex prompting](https://learn.chatgpt.com/codex/prompting) · [Codex `AGENTS.md`](https://learn.chatgpt.com/codex/agent-configuration/agents-md) · [Claude Code memory](https://docs.anthropic.com/en/docs/claude-code/memory)

## Day 40: Milestone source-citing assistant

**Build:** Complete a UI flow where an authenticated user asks a question about an owned collection and receives a streamed or progressively displayed answer with clickable citations. The pipeline must retrieve authorized chunks, bound context, validate model output, abstain without evidence, and expose a request ID.

**Required quality:** Provider abstraction and fake, versioned prompt, embedding-version metadata, retrieval benchmark, tool/loop limits, citation validation, cross-tenant tests, timeout/retry behavior, and basic token/latency accounting.

**Ship:** Open a milestone PR containing the updated architecture diagram, retrieval report, recorded demo, limitations, and cost estimate for 100 representative questions. Merge and tag `day-40`.

**Demo:** Ask an answerable question, an unanswerable one, an adversarial one, and a question targeting another user's data. Explain each outcome from logs and retrieved evidence.

**Resources:** [OpenAI production best practices](https://developers.openai.com/api/docs/guides/production-best-practices) · [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) · [Model Cards for Model Reporting](https://arxiv.org/abs/1810.03993)

## Phase 4 exit ticket

Explain where probabilistic behavior enters the system, what remains deterministic, how retrieval and generation are measured separately, how access control survives model/tool calls, and when the system must abstain.
