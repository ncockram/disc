# Building Effective Agents - Summary

- https://www.anthropic.com/engineering/building-effective-agents

## Overview
This Anthropic engineering article provides practical guidance for building effective LLM agents based on real-world experience with dozens of customer implementations across industries. The key finding is that successful agent implementations rely on simple, composable patterns rather than complex frameworks.

## Key Architectural Distinctions

**Workflows vs Agents:**
- **Workflows**: LLMs and tools orchestrated through predefined code paths
- **Agents**: LLMs dynamically direct their own processes and tool usage, maintaining autonomous control

## Core Principles

1. **Start Simple**: Find the simplest solution possible, only increasing complexity when needed
2. **Performance Trade-offs**: Agentic systems often trade latency and cost for better task performance
3. **Framework Caution**: Use LLM APIs directly first; frameworks can obscure underlying prompts and add unnecessary complexity

## Building Block Patterns

### 1. Augmented LLM (Foundation)
Base building block enhanced with retrieval, tools, and memory capabilities.

### 2. Workflow Patterns
- **Prompt Chaining**: Sequential steps where each LLM call processes previous output
- **Routing**: Classifies input and directs to specialized follow-up tasks
- **Parallelization**: Breaks tasks into independent subtasks (sectioning) or runs same task multiple times (voting)
- **Orchestrator-Workers**: Central LLM dynamically breaks down tasks and delegates to worker LLMs
- **Evaluator-Optimizer**: One LLM generates response while another provides feedback in iterative loop

### 3. Autonomous Agents
- Operate independently with tool usage based on environmental feedback
- Handle open-ended problems with unpredictable step requirements
- Require careful tool design and documentation
- Higher costs and potential for compounding errors

## Successful Use Cases

**Customer Support**: Natural conversation flow with tool integration for data access and programmatic actions
