# The PSB Workflow System for Claude Code Projects

## Video Summary
**Source:** [YouTube Video](https://www.youtube.com/watch?v=aQvpqlSiUIQ)  
**Date Summarized:** December 30, 2025  
**Duration:** ~34 minutes  
**Content:** Claude Code project workflow methodology  
**LLM Model:** Claude Opus 4.5  

---

## Overview

This document outlines the **PSB System** (Plan, Setup, Build) — a structured three-phase workflow for effectively starting and developing projects with Claude Code. The system emphasizes upfront planning, proper configuration, and organized development workflows to maximize productivity and reduce iteration cycles.

---

## The PSB System: Three-Phase Workflow

### Phase 1: Plan
Set up your project for success before writing any code.

### Phase 2: Setup  
Configure Claude Code with everything it needs to build effectively.

### Phase 3: Build
Execute development using structured workflows and best practices.

---

## Phase 1: Planning

### Two Critical Questions Before Building

| Question | Purpose |
|----------|---------|
| **What are you actually trying to do?** | Determines scope, quality requirements, and what can be skipped |
| **What are the milestones of functionality?** | Breaks project into clear phases (MVP → v2 → v3) |

### Project Goal Types

- **Learning a new technology** — Move fast, skip edge cases
- **Validating an idea** — Focus on core functionality
- **Building an alpha product** — Consider security, error handling, polish
- **Prototyping** — Quick iteration, can "move fast and break things"

### Using AI for Planning

**Pro Tip:** Ask AI to ask you questions:
> "Hey Claude, I want to build this project. What are the three most important questions I need to answer to build an MVP successfully?"

**Voice Mode Planning:** Talk through ideas using Claude assistant or ChatGPT voice mode, then ask for a markdown summary.

---

## The Project Spec Document

The main deliverable of the planning phase — contains both product and engineering requirements.

### Part 1: Product Requirements (PRD)

Answers three key questions:
1. **Who is the product for?**
2. **What problems does it solve?**
3. **What should the product do?**

**Best Practices:**
- Be specific about user interactions (not just "users can create entries" — describe the workflow)
- Break into clear capability milestones
- Define what "done" looks like for each milestone
- Iterate on requirements as you build

### Part 2: Technical/Engineering Requirements

#### Tech Stack Decisions

| Category | Example Choices |
|----------|-----------------|
| Frontend Hosting | Vercel |
| Framework | Next.js |
| Styling | Tailwind CSS |
| Components | shadcn/ui |
| Database | MongoDB, Supabase |
| Authentication | Clerk |
| Payments | Stripe |
| Email | Resend |
| Backend Hosting | Digital Ocean |
| Object Storage | Cloudflare R2 |
| AI Models | Anthropic, Google Gemini |

**Why specify your stack:** If you don't, Claude may inject random technology choices.

#### Technical Architecture

- System design overview
- Key components and interactions
- Database schema
- API design
- **Provision infrastructure early** — Create databases, set up hosting, generate API keys

---

## Phase 2: Setup (7-Step Checklist)

### Step 1: Set Up GitHub Repository

**Benefits:**
- Use Claude Code on web and mobile
- Access GitHub CLI and Claude Code GitHub Action
- Automated PR reviews
- Deploy previews via providers like Vercel
- Issue-based development workflow
- Multi-agent development support

**Workflow:** Create new branch per feature → merge/PR to main when done.

---

### Step 2: Create Environment Variable File

1. Ask Claude to create an example `.env` file based on project spec
2. Create a copy with real credentials and API keys
3. Claude can build without stopping to ask for credentials

---

### Step 3: Set Up `CLAUDE.md` File

**Purpose:** Project memory, always included in context for every chat.

**Key Principle:** Keep it focused and finite — don't bloat it.

#### What to Include:

| Section | Purpose |
|---------|---------|
| **Project Goals & Architecture Overview** | Big picture grounding |
| **Design Style Guide & UX Guidelines** | Keep generated code aligned |
| **Constraints & Policies** | Prevent unsafe actions |
| **Repository Etiquette** | PRs vs merges, branch naming, Git workflows |
| **Frequently Used Commands** | Build, test commands Claude can run |
| **Testing Instructions** | Rules Claude should follow |

**Pro Tip:** Link to other files instead of repeating info:
```markdown
For full architecture details, see architecture.md
For project spec, see docs/project-spec.md
```

---

### Step 4: Set Up Automated Documentation

Four core documents to maintain alongside `CLAUDE.md`:

#### 1. `architecture.md`
- System design
- App structure  
- Component interactions
- Update after adding big features

#### 2. `changelog.md`
- List of changes over time
- Helps track work done
- Gives Claude project evolution context

#### 3. `project-status.md`
- Project milestones
- Accomplished items
- Where you left off last time
- **Essential for burst-style work patterns**

#### 4. Feature Reference Docs
- High-level overview of key features
- Examples: onboarding, push notifications, payments, time zones
- Useful for planning improvements and fixing bugs

**Keeping Docs Updated:** 
- Instruction in `CLAUDE.md` to update automatically
- Custom `/command` Claude runs after finishing features

---

### Step 5: Set Up Plugins

**Plugins extend Claude Code with:**
- Slash commands
- Sub-agents
- MCP servers
- Hooks
- Skills

#### Recommended Plugins:

| Plugin | Purpose |
|--------|---------|
| **Anthropic Frontend Plugin** | Better UIs, avoids "purple gradient" |
| **Anthropic Feature Dev Plugin** | Streamlines feature development |
| **Every Compound Engineering Plugin** | Suite of commands/sub-agents for continuous improvement |

**Management:** Use `/plugins` command in Claude Code

---

### Step 6: Set Up MCPs (Model Context Protocol Servers)

MCPs connect Claude Code to external tools and services.

#### Recommended MCPs by Category:

| Category | MCP |
|----------|-----|
| **Database** | MongoDB MCP, Supabase MCP |
| **Web Testing** | Playwright MCP, Puppeteer MCP |
| **Deployment** | Vercel MCP |
| **Analytics** | Mixpanel MCP |
| **Project Management** | Linear MCP |

**Installation:** Usually one-line install per MCP.

---

### Step 7: Set Up Slash Commands & Sub-Agents

#### Understanding the Difference:

| Type | Context | Best For |
|------|---------|----------|
| **Slash Command** | Uses same context window as main conversation | Quick shortcuts to prompts/tasks |
| **Sub-Agent** | Uses forked context (isolated) | Parallel work, specialized focused tasks |

#### Recommended Custom Sub-Agents:

1. **Changelog Sub-Agent** — Creates/updates changelog after features
2. **Frontend Testing Sub-Agent** — Runs Playwright tests automatically
3. **Retro Agent** — Reflects on improvements, updates `CLAUDE.md`, prompts, commands

#### Recommended Slash Commands:

- `/commit` and `/prit` — Committing changes
- `/feature-dev` — Feature development workflow
- Custom: Update all project docs
- Custom: Create GitHub issues from project spec

---

### Bonus Setup Tips

#### Bonus 1: Preconfigure Permissions

Pre-approve or pre-block commands so Claude doesn't wait for permission:
- Allow git commands without asking
- Allow file edits without asking
- **Prevents "coffee break → stuck waiting" problem**

#### Bonus 2: Set Up Hooks

Scripts that run automatically at lifecycle points:

**Example Hooks:**
- **Stop Hook:** Checks if tests pass when Claude finishes → tells Claude to fix if not
- **Notification Hook:** Pings Slack when Claude needs permission

---

## Phase 3: Build

### Building Your MVP

1. Reference your project spec doc and milestones
2. Ask Claude to build milestone one
3. **Pro Tip:** Ask Claude to use parallel sub-agents during implementation
4. **Always use Plan Mode first** — Claude translates spec into implementation plan

---

## Three Development Workflows

### Workflow 1: General Workflow (Single Feature)

**Four Parts:**

```
Research → Plan → Implement → Test
```

| Step | Description |
|------|-------------|
| **Research** | Create research report, use external research (optional but helpful for big features) |
| **Plan** | **Most important!** Use Plan Mode — Claude thinks through task, breaks into steps, asks clarifying questions |
| **Implement** | Claude uses plugins, sub-agents, MCPs, commands from setup phase |
| **Test** | Automated testing with configured tools |

**Common Mistake:** Not using Plan Mode enough.

---

### Workflow 2: Issue-Based Development

**GitHub Issues become source of truth** for features, bugs, and tasks.

**Benefits:**
- Project stays tidy (no scattered to-do files)
- Can ask Claude to tackle multiple issues with sub-agents
- Multiple Claude Code instances can work issues in parallel

**Process:**
1. Ask Claude to turn project spec/milestones into GitHub issues
2. Create issues manually as needed
3. Automate with slash command that outputs issues from file/folder

---

### Workflow 3: Multi-Agent Development

**Most advanced workflow** — work on multiple features simultaneously.

#### How It Works:

1. Run multiple Claude Code instances
2. Each session works on a different feature
3. Use **Git Worktrees** for isolation

#### Git Worktrees:
- Multiple working copies of repo in different directories
- Each on a different branch
- Isolated files, shared git history
- Merge worktrees together when done

**Use Cases:**
- Fix multiple bugs quickly in parallel
- Add multiple larger features simultaneously

---

## Four Productivity Tips for Build Phase

### Tip 1: Use the Best Models

| Task Type | Recommended Model |
|-----------|-------------------|
| Planning, complex tasks | Opus 4.5 |
| Implementation workhorse | Sonnet |
| Simple tasks, bug fixes | Haiku |

**Rationale:** Time saved with fewer mistakes > money saved with cheaper model.

---

### Tip 2: Periodically Update `CLAUDE.md`

- Update as you add features or reach milestones
- **Pro Tip:** Create custom command that updates `CLAUDE.md` then creates git commit
- Keeps documentation and code in sync

---

### Tip 3: Regression Prevention

When Claude makes a mistake:
1. Don't just fix and move on
2. Type `#` (hashtag/pound) to give Claude an instruction
3. Instruction automatically incorporates into relevant `CLAUDE.md`
4. Quick on-the-fly updates without manual edits

---

### Tip 4: Don't Be Afraid to Throw Away Work

- **Code is cheap** — especially in prototype stages
- Undo or throw away features and start fresh
- Use Claude Code's **Checkpoints and Rewind** for session-level recovery
- Combined with Git for project-level version control

---

## Quick Reference: Key Files Summary

| File | Purpose | Update Frequency |
|------|---------|------------------|
| `CLAUDE.md` | Project memory, always in context | Periodically/per milestone |
| `project-spec.md` | Product + engineering requirements | Start of project |
| `architecture.md` | System design, component interactions | After big features |
| `changelog.md` | Track changes over time | Per release/feature |
| `project-status.md` | Milestones, progress, last session | Per session |
| `.env.example` | Template for environment variables | When new vars added |
| `.env` | Actual credentials (gitignored) | As needed |
| Feature reference docs | High-level feature overviews | Per major feature |

---

## Implementation Checklist for Teams

### Before Starting a New Project:

- [ ] Answer the two critical questions (goal + milestones)
- [ ] Create project spec doc (product + engineering requirements)
- [ ] Define tech stack
- [ ] Provision infrastructure
- [ ] Set up GitHub repository
- [ ] Create `.env` files
- [ ] Create initial `CLAUDE.md`
- [ ] Set up automated documentation files
- [ ] Install relevant plugins
- [ ] Configure MCPs for tech stack
- [ ] Create custom slash commands/sub-agents
- [ ] Configure permissions
- [ ] Set up hooks (optional)

### During Development:

- [ ] Use Plan Mode before implementation
- [ ] Use feature branches
- [ ] Update documentation as you go
- [ ] Practice regression prevention (#)
- [ ] Use appropriate model for task complexity
- [ ] Leverage parallel sub-agents when possible

---

## Key Takeaways for Developer Presentation

1. **Plan before coding** — 15 minutes of planning saves hours/days of frustration
2. **Project spec doc is essential** — Combines PRD + engineering design
3. **`CLAUDE.md` is your project's memory** — Keep it focused, link to other docs
4. **Automated documentation** — Four core docs that Claude maintains
5. **MCPs extend capabilities** — Database, testing, deployment integrations
6. **Three workflows** — General (single feature), Issue-based, Multi-agent
7. **Plan Mode is critical** — Most common mistake is not using it enough
8. **Git Worktrees enable parallel development** — Isolated branches, shared history
9. **Use best models for quality** — Time saved > money saved
10. **Code is cheap** — Don't be afraid to throw away and restart
