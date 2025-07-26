# VS Code Copilot Prompt Crafting Guide

**Source:** [VS Code Copilot Prompt Crafting](https://code.visualstudio.com/docs/copilot/prompt-crafting)

## Introduction

Effective prompt crafting is essential for getting the most value from GitHub Copilot in VS Code. This guide covers techniques for writing prompts that produce relevant, accurate, and useful AI assistance for both inline suggestions and chat interactions.

## Understanding Prompt Engineering

### What is Prompt Engineering?

Prompt engineering involves **strategically structuring your requests** to AI systems to get optimal results. For Copilot, this means:

- **Clear communication** of intent and requirements
- **Providing relevant context** for better understanding
- **Structuring requests** for specific types of responses
- **Iterating and refining** prompts based on results

### Types of Copilot Interactions

**Inline Suggestions:**
- Automatic code completions based on context
- Triggered by comments, function names, and patterns
- Optimized through code structure and naming

**Chat Interactions:**
- Explicit prompts for specific assistance
- Conversational exchanges with follow-up questions
- Context-rich requests with file and symbol references

## Getting the Most from Inline Suggestions

### Provide Context Through Code Structure

**Open related files:**
Having relevant files open helps Copilot understand your project:

```javascript
// If working on user authentication, have these files open:
// - auth.js (current file)
// - user.model.js (data structure)
// - config.js (configuration)
// - middleware/auth.js (related functionality)
```

**Use descriptive top-level comments:**
```javascript
// User authentication service for e-commerce platform
// Handles login, logout, password reset, and session management
// Integrates with JWT tokens and Redis for session storage

class AuthService {
  // Copilot now understands the broader context
}
```

**Include appropriate imports and dependencies:**
```javascript
// Specific imports guide Copilot's suggestions
import bcrypt from 'bcrypt';
import jwt from 'jsonwebtoken';
import { User } from '../models/User.js';
import { logger } from '../utils/logger.js';

// Now Copilot suggests using these specific libraries
function hashPassword(password) {
  // Suggestions will use bcrypt instead of generic hashing
}
```

### Write Meaningful Function Names and Comments

**Descriptive function names:**
```javascript
// Instead of generic names
function fetchData() { }
function processInfo() { }

// Use specific, descriptive names
function getUserProfileById(userId) { }
function validateEmailFormat(email) { }
function calculateShippingCost(weight, distance) { }
```

**Specific and well-scoped comments:**
```javascript
/**
 * Validates user input for registration form
 * Checks email format, password strength, and username availability
 * Returns validation errors or null if valid
 * @param {Object} userData - User registration data
 * @param {string} userData.email - User's email address
 * @param {string} userData.password - Plain text password
 * @param {string} userData.username - Desired username
 * @returns {Object|null} Validation errors or null
 */
function validateRegistrationData(userData) {
  // Copilot now understands exactly what to implement
}
```

### Prime Copilot with Sample Code

**Provide example patterns:**
```javascript
// Include a sample to establish patterns
const userValidation = {
  email: (value) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value),
  password: (value) => value.length >= 8 && /[A-Z]/.test(value)
};

// Now ask for more validators
const productValidation = {
  // Copilot will follow the established pattern
}
```

**Show preferred code style:**
```javascript
// Establish error handling pattern
async function fetchUserData(id) {
  try {
    const response = await api.get(`/users/${id}`);
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }
    return response.data;
  } catch (error) {
    logger.error('Failed to fetch user data:', error);
    throw error;
  }
}

// Now Copilot will use similar error handling patterns
async function fetchProductData(id) {
  // Suggestions will follow the established pattern
}
```

### Maintain Code Quality Standards

**Consistent naming conventions:**
```javascript
// Establish patterns Copilot will follow
class UserService {
  async createUser(userData) { }
  async updateUser(userId, updates) { }
  async deleteUser(userId) { }
  
  // Copilot will suggest consistent naming for new methods
}
```

**Quality code examples:**
```javascript
// High-quality code for Copilot to learn from
const createUser = async (userData) => {
  const validationResult = validateUserData(userData);
  if (!validationResult.isValid) {
    throw new ValidationError('Invalid user data', validationResult.errors);
  }
  
  const hashedPassword = await bcrypt.hash(userData.password, 12);
  const user = await User.create({
    ...userData,
    password: hashedPassword,
    createdAt: new Date()
  });
  
  return user;
};
```

**Disable Copilot during prototyping:**
When writing quick, low-quality code:
1. **Open Copilot status menu** (click Copilot in status bar)
2. **Disable completions** temporarily
3. **Re-enable** when returning to quality code

## Getting the Most from Copilot Chat

### Use Chat Participants and Slash Commands

**Leverage specialized knowledge:**
```
@workspace How is error handling implemented across this project?
@vscode How do I set up debugging for this TypeScript project?
@terminal What's the best way to deploy this Node.js application?
```

**Use slash commands for specific intents:**
```
/explain this authentication middleware
/fix the memory leak in this event handler
/tests Create unit tests for this user service
/doc Generate API documentation for these endpoints
```

**Combine participants and commands:**
```
@workspace /refactor Improve the structure of this React application
@vscode /help Set up ESLint and Prettier for this project
```

### Use Context Variables Effectively

**File references:**
```
#package.json What dependencies should I add for testing?
#src/components/UserForm.jsx How can I improve this form component?
#config/database.js Why might this connection configuration fail?
```

**Symbol references:**
```
#UserService What methods are available in this service?
#validateEmail How can I make this validation more robust?
#API_ENDPOINTS How are these endpoints organized?
```

**Selection context:**
```
// Select code first, then ask:
#selection Refactor this to use modern JavaScript features
#selection What potential security issues do you see?
#selection How can I optimize this for better performance?
```

**Multiple context sources:**
```
#models/User.js #services/auth.js #middleware/validation.js 
How do these files work together for user authentication?
```

### Be Specific and Keep It Simple

**Break down complex requests:**
```
// Instead of one large request:
Create a complete e-commerce system with user auth, product catalog, shopping cart, and payment processing

// Break into focused requests:
1. Create a user authentication system with JWT
2. Add a product catalog with search and filtering
3. Implement shopping cart functionality
4. Integrate payment processing with Stripe
```

**Specify requirements clearly:**
```
// Vague request:
Make this form better

// Specific request:
Add client-side validation to this registration form using Yup schema validation, include real-time feedback, and ensure accessibility compliance
```

**Include technical constraints:**
```
// Generic request:
Add database integration

// Specific with constraints:
Add PostgreSQL integration using Prisma ORM, include connection pooling, and handle migration scripts for deployment
```

### Iterate on Your Solutions

**Progressive refinement workflow:**

**Initial request:**
```
Create a function to calculate shipping costs
```

**First iteration:**
```javascript
function calculateShipping(weight, distance) {
  return weight * 0.5 + distance * 0.1;
}
```

**Refinement request:**
```
Add support for different shipping methods and zones
```

**Second iteration:**
```javascript
function calculateShipping(weight, distance, method = 'standard', zone = 'domestic') {
  const rates = {
    standard: { weight: 0.5, distance: 0.1 },
    express: { weight: 0.8, distance: 0.15 },
    overnight: { weight: 1.2, distance: 0.25 }
  };
  
  const zoneMultiplier = zone === 'international' ? 2.5 : 1;
  const rate = rates[method] || rates.standard;
  
  return (weight * rate.weight + distance * rate.distance) * zoneMultiplier;
}
```

**Further refinement:**
```
Add input validation and error handling
```

**Final iteration with robust implementation:**
```javascript
function calculateShipping(weight, distance, method = 'standard', zone = 'domestic') {
  // Input validation
  if (typeof weight !== 'number' || weight <= 0) {
    throw new Error('Weight must be a positive number');
  }
  if (typeof distance !== 'number' || distance <= 0) {
    throw new Error('Distance must be a positive number');
  }
  
  const rates = {
    standard: { weight: 0.5, distance: 0.1 },
    express: { weight: 0.8, distance: 0.15 },
    overnight: { weight: 1.2, distance: 0.25 }
  };
  
  const validZones = ['domestic', 'international'];
  if (!validZones.includes(zone)) {
    throw new Error(`Invalid zone: ${zone}. Must be one of: ${validZones.join(', ')}`);
  }
  
  if (!rates[method]) {
    throw new Error(`Invalid shipping method: ${method}. Available methods: ${Object.keys(rates).join(', ')}`);
  }
  
  const zoneMultiplier = zone === 'international' ? 2.5 : 1;
  const rate = rates[method];
  
  const cost = (weight * rate.weight + distance * rate.distance) * zoneMultiplier;
  return Math.round(cost * 100) / 100; // Round to 2 decimal places
}
```

## Advanced Prompting Techniques

### Context Layering

**Start broad, get specific:**
```
// Layer 1: Understand the domain
What are best practices for REST API design?

// Layer 2: Apply to project context
#src/api/ How can I improve the API structure in this project?

// Layer 3: Specific implementation
#src/api/users.js Add proper error handling and validation to this user endpoints file
```

### Comparative Analysis

**Request multiple approaches:**
```
Show me three different ways to implement user authentication in Node.js, with pros and cons of each approach
```

**Compare technologies:**
```
Compare Redux, Zustand, and React Context for state management in this #package.json React application
```

### Code Review Prompting

**Security-focused review:**
```
#src/auth/ Review this authentication code for potential security vulnerabilities and recommend improvements
```

**Performance analysis:**
```
#src/components/DataTable.jsx Analyze this component for performance bottlenecks and suggest optimizations
```

**Best practice assessment:**
```
#src/ Review this codebase for adherence to Node.js best practices and suggest improvements
```

### Architecture and Design

**High-level planning:**
```
Design a microservices architecture for this #package.json e-commerce application, including service boundaries and communication patterns
```

**Migration planning:**
```
#src/ Create a plan to migrate this JavaScript codebase to TypeScript incrementally
```

**Scaling considerations:**
```
@workspace What changes would be needed to scale this application to handle 10x more traffic?
```

## Prompt Patterns and Templates

### Learning-Oriented Prompts

**Concept explanation:**
```
Explain [concept] in the context of #file.js
What is [pattern] and how does it apply to this codebase?
How does [technology] work with [another technology]?
```

**Code analysis:**
```
/explain #selection step by step
What design patterns do you see in #file.js?
How does this #function handle edge cases?
```

### Implementation-Oriented Prompts

**Feature requests:**
```
Add [feature] to #component.js with [specific requirements]
Implement [functionality] using [technology/pattern]
Create [component type] that handles [use case]
```

**Improvement requests:**
```
Optimize #selection for [performance/readability/maintainability]
Refactor #file.js to use [pattern/technology]
Add [quality attribute] to this #component
```

### Problem-Solving Prompts

**Debugging assistance:**
```
Why might this #function cause [specific problem]?
How can I fix #selection that's causing [error/issue]?
What's wrong with this #implementation?
```

**Alternative solutions:**
```
What are different ways to solve [problem] in this context?
How else could I implement #selection?
What are the trade-offs between [approach A] and [approach B]?
```

## Common Pitfalls and How to Avoid Them

### Overly Vague Prompts

**Problem:**
```
Make this better
Fix this code
Help with this function
```

**Solution:**
```
Improve error handling and add input validation to this user registration function
Fix the memory leak caused by uncleaned event listeners in this React component
Optimize this database query function for better performance with large datasets
```

### Insufficient Context

**Problem:**
```
How do I implement authentication?
```

**Solution:**
```
#package.json #src/app.js How do I implement JWT-based authentication in this Express.js application?
```

### Too Many Unrelated Requests

**Problem:**
```
Add authentication, implement caching, set up testing, and deploy to AWS
```

**Solution:**
```
// Sequential, focused requests:
1. Add JWT authentication to this Express app
2. Then: Implement Redis caching for user sessions  
3. Then: Set up Jest testing for authentication endpoints
4. Finally: Create AWS deployment configuration
```

### Ignoring Project Conventions

**Problem:**
Not considering existing code patterns and styles.

**Solution:**
```
#src/services/userService.js Following the pattern established in this file, create a productService with CRUD operations
```

## Measuring Prompt Effectiveness

### Quality Indicators

**Good responses include:**
- **Relevant to your specific context** and requirements
- **Follows existing project patterns** and conventions
- **Includes proper error handling** and edge cases
- **Provides working, testable code**
- **Includes helpful explanations** when requested

**Signs to refine your prompt:**
- **Generic, boilerplate responses** not specific to your needs
- **Code that doesn't compile** or has obvious errors
- **Solutions that ignore** project constraints or patterns
- **Overly complex solutions** for simple problems
- **Missing important considerations** like security or performance

### Iterative Improvement

**Track what works:**
- Note which prompt patterns produce the best results
- Save effective prompt templates for reuse
- Build a library of successful context patterns

**Learn from failures:**
- Analyze why certain prompts didn't work
- Identify missing context or unclear requirements
- Refine prompting strategy based on results

## Team Collaboration and Prompt Sharing

### Establishing Team Standards

**Shared prompt patterns:**
```
// Team template for code review requests
#file.js Review this code for [security/performance/maintainability] issues following our [company standards/style guide]
```

**Context conventions:**
```
// Always include relevant files for architecture questions
#src/config/ #src/models/ #src/services/ How should we structure the new feature X?
```

### Documentation Integration

**Link prompts to documentation:**
```
Following the patterns in our #docs/coding-standards.md, implement error handling for this API endpoint
```

**Create prompt libraries:**
- Document effective prompts for common tasks
- Share successful patterns across the team
- Maintain examples for different types of requests

## Related Resources

### Additional Learning

- **[Effective Prompting for GitHub Copilot](https://www.youtube.com/watch?v=ImWfIDTxn7E)** - Video guide
- **[Pragmatic techniques for GitHub Copilot](https://www.youtube.com/watch?v=CwAzIpc4AnA)** - Advanced techniques  
- **[Best practices for prompting](https://www.linkedin.com/pulse/best-practices-prompting-github-copilot-vs-code-pamela-fox)** - LinkedIn article
- **[How to write better prompts](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/)** - GitHub blog

### VS Code Documentation

- **[Chat Overview](../chat/copilot-chat.md)** - Complete chat feature guide
- **[Chat Context Management](../chat/copilot-chat-context.md)** - Advanced context techniques
- **[Getting Started Guide](../chat/getting-started-chat.md)** - Hands-on tutorial
- **[Copilot Overview](../overview.md)** - Understanding all Copilot features

---

*Effective prompt crafting is a skill that improves with practice. Start with clear, specific requests and gradually develop more sophisticated techniques as you learn what works best for your development workflow and projects.*
