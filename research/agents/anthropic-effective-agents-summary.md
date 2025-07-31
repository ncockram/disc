# Building Effective Agents - Summary

**Source URL**: https://www.anthropic.com/engineering/building-effective-agents  
**Summary Date**: July 31, 2025

## Overview

Based on Anthropic's work with dozens of teams building LLM agents across industries, this comprehensive guide reveals that the most successful agent implementations use simple, composable patterns rather than complex frameworks. The article provides practical guidance for developers on building effective agentic systems.

## Core Definitions

**Workflows vs Agents - Key Architectural Distinction:**
- **Workflows**: Systems where LLMs and tools are orchestrated through predefined code paths
- **Agents**: Systems where LLMs dynamically direct their own processes and tool usage, maintaining autonomous control over task accomplishment

## Fundamental Principles

1. **Start Simple**: Find the simplest solution possible, only adding complexity when demonstrably needed
2. **Performance Trade-offs**: Agentic systems often trade latency and cost for better task performance - consider when this makes sense
3. **Framework Caution**: Start with LLM APIs directly; frameworks can obscure underlying prompts and add unnecessary complexity
4. **Measure and Iterate**: Success comes from measuring performance and iterating on implementations

## Building Blocks and Patterns

### Foundation: The Augmented LLM
The basic building block enhanced with:
- **Retrieval**: Generating search queries and accessing information
- **Tools**: Selecting and using appropriate tools
- **Memory**: Determining what information to retain
- Implementation can leverage Model Context Protocol (MCP) for tool integration

### Workflow Patterns

#### 1. Prompt Chaining
**Structure**: Sequential steps where each LLM call processes the previous output
**When to Use**: Tasks that can be cleanly decomposed into fixed subtasks
**Benefits**: Trades latency for higher accuracy by making each call easier
**Examples**: 
- Generate marketing copy → translate to different language
- Write outline → check criteria → write full document

#### 2. Routing  
**Structure**: Classifies input and directs to specialized follow-up tasks
**When to Use**: Complex tasks with distinct categories better handled separately
**Benefits**: Separation of concerns, specialized prompts
**Examples**:
- Customer service queries (general/refund/technical) → different processes
- Easy questions → smaller models, hard questions → capable models

#### 3. Parallelization
**Two Variations**:
- **Sectioning**: Breaking tasks into independent subtasks run in parallel
- **Voting**: Running same task multiple times for diverse outputs

**When to Use**: When subtasks can be parallelized for speed or multiple perspectives needed
**Examples**:
- Sectioning: Guardrails (one model processes queries, another screens content)
- Voting: Code vulnerability reviews, content appropriateness evaluation

#### 4. Orchestrator-Workers
**Structure**: Central LLM dynamically breaks down tasks and delegates to worker LLMs
**When to Use**: Complex tasks where subtasks can't be predicted (dynamic decomposition)
**Examples**:
- Coding products making complex multi-file changes
- Search tasks requiring analysis from multiple sources

#### 5. Evaluator-Optimizer
**Structure**: One LLM generates response while another provides evaluation and feedback in iterative loop
**When to Use**: Clear evaluation criteria exist and iterative refinement provides measurable value
**Examples**:
- Literary translation with nuanced feedback
- Complex search requiring multiple rounds of analysis

### Autonomous Agents

**Characteristics**:
- Operate independently with tool usage based on environmental feedback
- Handle open-ended problems with unpredictable step requirements
- Begin with command/discussion from user, then plan and operate independently
- Gain "ground truth" from environment at each step
- Include stopping conditions for control

**When to Use**: Open-ended problems where steps can't be predicted and fixed paths can't be hardcoded

**Considerations**:
- Higher costs and potential for compounding errors
- Require extensive testing in sandboxed environments
- Need appropriate guardrails
- Crucial to design toolsets and documentation clearly

**Examples**:
- SWE-bench coding tasks (editing multiple files based on task description)
- Computer use implementations where Claude accomplishes tasks via computer interface

## Practical Applications

### Customer Support
**Why Effective**:
- Natural conversation flow with tool integration
- Access to customer data, order history, knowledge base
- Programmatic actions (refunds, ticket updates)
- Clear success measurement through user-defined resolutions
- Companies use usage-based pricing models charging only for successful resolutions

### Coding Agents
**Why Effective**:
- Code solutions are verifiable through automated tests
- Agents can iterate using test results as feedback
- Well-defined, structured problem space
- Objective quality measurement
- Can solve real GitHub issues based on pull request descriptions alone

## Tool Design Best Practices (Agent-Computer Interface)

**Core Principles**:
- Give model enough tokens to "think" before writing
- Keep format close to naturally occurring text on internet
- Avoid formatting "overhead" (line counting, string escaping)

**Design Guidelines**:
- Put yourself in model's shoes - is tool usage obvious?
- Write clear descriptions like docstrings for junior developers
- Include example usage, edge cases, input requirements, boundaries
- Test extensively with many example inputs
- "Poka-yoke" tools to prevent mistakes (e.g., require absolute filepaths)

## Framework Recommendations

**Available Frameworks**: LangGraph, Amazon Bedrock AI Agent framework, Rivet, Vellum

**Guidance**:
- Start with LLM APIs directly - many patterns can be implemented in few lines
- Frameworks help with standard tasks but create abstraction layers
- Can obscure underlying prompts and responses, making debugging harder
- If using frameworks, ensure you understand the underlying code
- Consider reducing abstraction layers when moving to production

## Success Principles

1. **Maintain Simplicity**: In agent design and implementation
2. **Prioritize Transparency**: Explicitly show agent's planning steps
3. **Craft Agent-Computer Interface**: Through thorough tool documentation and testing

## Key Takeaways

- Success isn't about building the most sophisticated system, but the right system for your needs
- Start with simple prompts, optimize with comprehensive evaluation
- Add multi-step agentic systems only when simpler solutions fall short
- Combine and customize patterns rather than following prescriptive implementations
- Invest as much effort in agent-computer interfaces (ACI) as human-computer interfaces (HCI)
- Extensive tool optimization often matters more than overall prompt optimization
