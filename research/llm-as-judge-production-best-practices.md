# LLM Evals in the Real World (Router Evals, Arize Phoenix)

## Video Summary
**Source:** [YouTube Video](https://www.youtube.com/watch?v=nbZzSC5A6hs)  
**Date Summarized:** 8/7/25
**Duration:** ~18:51  
**Content:** Talk + demo on task-level LLM evals, LM-as-a-judge, router/function-call evaluation, and research on context placement and prompting.  
**LLM Model:** GitHub Copilot/GPT-5 (Preview)

## Overview
The speaker (Arize cofounder) explains how “LM as a judge” and task-focused evaluations work in production LLM apps. Beyond leaderboard model evals, real systems need multi-level task evals—especially around routing (intent classification and function selection) and parameter extraction. A Phoenix demo shows how a misrouted function call throws an entire workflow off, underscoring why granular traces, evals, and explanations matter for debugging and iteration.

## Why task evals (vs model evals)
- Model evals (e.g., leaderboards, MMLU) help select a base model.
- Task evals measure whether your application behaves correctly end-to-end for real user intents.
- In production, routing accuracy and parameter extraction often dominate failure modes.

## Anatomy of a production app and where to evaluate
- Common pattern: router → LLM calls → app/tool calls → optional classic ML → response.
- Place evals at multiple levels:
  - Router-level: Did it choose the right branch/function?
  - Component-level: Did parameter extraction produce correct arguments?
  - Trace/session-level: Did the multi-turn flow achieve the task?

## Demo highlights (Phoenix)
- User asks for current promotions on a specific phone.
- System incorrectly calls a generic product search function instead of the promotions/discounts function.
- Result: downstream branch is wrong; the entire interaction degrades.
- Takeaway: Router/function-call evals with explanations pinpoint the fix (update function descriptions, prompts, or routing logic).

## Best practices from the field
- Run evals with explanations: a bare pass/fail or score isn’t actionable; explanations guide fixes.
- Maintain datasets of failures; add new misses and run experiments to validate improvements.
- Iterate continuously: trace → evaluate → explain → fix → re-run.
- Use multi-level eval coverage: session, trace, and span/component.

## Research findings mentioned
1) Numeric vs categorical scores
- Numeric LM-judge scores often collapse to near-binary (e.g., 1 or 10) and miss granularity.
- Don’t rely solely on numeric scores; prefer categorical/multiclass outcomes and explanations.

2) Needle-in-a-haystack and context placement
- Retrieval success depends on where facts appear in the context window.
- Models struggled more when the key fact was early in long contexts; placement within the window matters.

3) Retrieval vs generation performance and prompting
- A model that retrieved well underperformed on generation-type tasks.
- Prompting to “explain your reasoning, then answer” significantly improved generation accuracy.

## Practical checklist
- Define router-level evals: correct branch/function for each user intent.
- Evaluate parameter extraction: right arguments for the selected function.
- Include explanations in all evals to drive fixes.
- Track failures in a dataset; run controlled experiments after changes (prompts, function schemas, model choice).
- Measure at session/trace/span levels; watch compound failures across steps.
- For RAG, test context placement sensitivity, not just chunking/recall.
- Prefer categorical/multiclass judgments over raw numeric scores alone.

## Key takeaways
- Production LLM quality hinges on multi-level task evals, not just model leaderboards.
- Explanations make evals actionable and accelerate iteration.
- Routing and parameter extraction are high-leverage eval targets.
- Context placement and “explain-then-answer” prompting can materially shift results.
