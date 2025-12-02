# Vibe Coding For Dummies: Part/Chapter Outline and Sample Section

**Working Title:** Vibe Coding For Dummies  
**Author Background:** First-class CompSci degree, former developer/teacher/head of department, now full-time vibe coder  
**Audience:** Non-technical founders, junior engineers, teachers, solo creators, aspiring entrepreneurs, aspiring start-up founders  
**Approach:** Tool-agnostic framework/guide based on real-world experience building 4 projects (2 games, 1 commercial product ~200K lines, 1 EdTech product ~160K lines near MVP)

---

## Part/Chapter Outline

### Part I: Getting Started with Vibe Coding

**Chapter 1: What Is Vibe Coding, Anyway?**  
- The shift from traditional coding to AI-assisted development
- What vibe coding is (and what it isn't)
- Why now? The tools that made this possible
- Who this book is for (and who it's not for)
- What you'll build by the end of this book

**Chapter 2: What You Need to Know (And What You Don't)**  
- The CompSci fundamentals that still matter
- What you can skip (for now)
- The mindset shift: from "I code" to "we code"
- Your role: architect, reviewer, and collaborator
- Setting realistic expectations

**Chapter 3: Setting Up Your Vibe Coding Environment**  
- Choosing your AI coding assistant (overview, not deep dive)
- Essential tools beyond the AI assistant
- Your first project structure
- Version control basics (you'll need this)
- Creating your first "vibe coding" project

**Chapter 4: Your First Conversation with AI**  
- How to talk to an AI coding assistant
- Writing prompts that get results
- The back-and-forth rhythm
- Common mistakes and how to avoid them
- Building your first tiny feature together

---

### Part II: Doing the Core Stuff

**Chapter 5: Writing Prompts That Actually Work**  
- The anatomy of a good prompt
- Context: how much is enough?
- Being specific without being prescriptive
- Iterating and refining
- When to start over vs. when to fix

**Chapter 6: Building Features, One Step at a Time**  
- Breaking big ideas into small prompts
- The feature → prompt → code → test cycle
- Managing complexity as features grow
- Keeping your codebase coherent
- Real example: building a user authentication flow

**Chapter 7: Working with Existing Code**  
- Reading code with AI help
- Making changes without breaking things
- Refactoring safely
- Understanding code you didn't write
- The "explain this to me" prompt pattern

**Chapter 8: Debugging Together**  
- When things go wrong (they will)
- Using AI to understand error messages
- Systematic debugging approaches
- Reading logs and stack traces with AI
- Fixing bugs without creating new ones

**Chapter 9: Managing Context and Complexity**  
- Why context matters (and why it's limited)
- Organizing your code for clarity
- Documentation that helps AI help you
- When to split files, modules, or projects
- Keeping your mental model aligned with AI's understanding

---

### Part III: Digging Deeper

**Chapter 10: Working on Larger Projects**  
- Scaling from prototype to production
- Managing multiple features simultaneously
- Code organization patterns that work
- Maintaining consistency across thousands of lines
- Real example: lessons from a 200K-line project

**Chapter 11: Managing Multiple Projects**  
- Context switching between projects
- Shared code and reusable patterns
- Keeping projects separate but consistent
- Time management and prioritization
- Building your personal "dev kit"

**Chapter 12: Testing and Quality Assurance**  
- Why testing matters (even with AI)
- Writing tests with AI assistance
- What to test and what to skip
- Manual testing workflows
- Catching bugs before users do

**Chapter 13: Working with Others**  
- Code reviews when AI wrote the code
- Explaining your codebase to teammates
- Collaboration patterns
- Documentation for humans (not just AI)
- Version control workflows that make sense

**Chapter 14: Advanced Prompting Techniques**  
- Multi-step reasoning prompts
- Using examples and patterns
- Teaching AI your preferences
- Complex refactoring prompts
- When to be explicit vs. when to trust AI

---

### Part IV: The Part of Tens

**Chapter 15: Ten Common Mistakes (And How to Avoid Them)**  
1. Over-relying on AI without understanding
2. Not testing enough
3. Ignoring error messages
4. Writing prompts that are too vague
5. Writing prompts that are too prescriptive
6. Not managing context effectively
7. Skipping version control
8. Not documenting your decisions
9. Trying to build everything at once
10. Forgetting you're still the architect

**Chapter 16: Ten Productivity Tips**  
1. Build a library of reusable prompts
2. Create project templates
3. Use consistent naming conventions
4. Document as you go
5. Test incrementally
6. Keep a "lessons learned" log
7. Automate repetitive tasks
8. Use version control branches effectively
9. Take breaks and review your code
10. Build your personal framework

**Chapter 17: Ten Tools and Resources**  
1. AI coding assistants (overview)
2. Version control (Git basics)
3. Code editors and IDEs
4. Testing frameworks
5. Project management tools
6. Documentation tools
7. Deployment platforms
8. Monitoring and analytics
9. Community resources
10. Learning resources for deepening your understanding

**Chapter 18: Ten Things You Should Know About Software Engineering**  
1. Separation of concerns
2. DRY (Don't Repeat Yourself)
3. Version control fundamentals
4. Testing basics
5. Error handling
6. Security basics
7. Performance considerations
8. Maintainability
9. Documentation importance
10. The software lifecycle

---

## Sample Section: Chapter 5, Section 2 — "Context: How Much Is Enough?"

This sample demonstrates the For Dummies style, voice, and structure guidelines.

---

### Context: How Much Is Enough?

One of the biggest questions you'll face as a vibe coder is this: how much information should you give your AI assistant? Too little, and it makes wild guesses. Too much, and you overwhelm it (or hit context limits). Getting this right is the difference between smooth collaboration and frustrating back-and-forth.

**What context actually means**

When we talk about "context" in vibe coding, we mean all the information your AI assistant needs to understand what you're asking for. This includes:

- What file or files you're working on
- What the code is supposed to do
- What similar code looks like in your project
- What constraints or requirements you have
- What went wrong (if you're debugging)

Think of it like explaining a problem to a colleague. You wouldn't just say "fix the login button" without showing them the code, right? But you also wouldn't read them your entire codebase. Context is about finding that sweet spot.

**Why context matters**

Your AI assistant doesn't have magical knowledge of your project. It only knows what you tell it (and what it can see in the files you've shared). If you ask it to "add a user profile page" without any context, it might:

- Use a completely different framework than you're using
- Create a design that doesn't match your existing pages
- Put files in the wrong place
- Use naming conventions that clash with your codebase

Give it good context, and it can match your existing patterns, use your preferred libraries, and create code that fits seamlessly into what you've already built.

**The context sweet spot**

Here's a practical rule of thumb: include enough context for the AI to make informed decisions, but not so much that you're pasting entire files unnecessarily.

**Good context includes:**

- The specific file(s) you're modifying
- Relevant functions or classes it needs to understand
- Examples of similar code from your project (1–2 examples is usually enough)
- Any constraints ("must work with our existing authentication system")
- The goal ("add a settings page that matches the style of our dashboard")

**Too little context looks like:**

```
Add a delete button to the user page.
```

**Too much context looks like:**

```
[Pastes entire 500-line file]
Add a delete button somewhere in here.
```

**Just right looks like:**

```
I'm working on user-management.js. Here's the relevant function:

[Shows the renderUserPage function, about 20 lines]

I want to add a delete button next to the "Edit" button. It should:
- Match the style of the Edit button
- Show a confirmation dialog before deleting
- Call our existing deleteUser API function (which I've shown below)

[Shows deleteUser function, about 5 lines]
```

**A practical example**

Let's say you want to add email validation to a signup form. Here's how you'd provide good context:

1. **Show the relevant code:**
   ```
   Here's my signup form component:
   [Paste the form component, maybe 30–40 lines]
   ```

2. **Explain what you want:**
   ```
   I need to add email validation. The email field should:
   - Check that it contains an @ symbol
   - Check that it has a valid domain (not just @gmail)
   - Show an error message below the field if invalid
   - Match the style of our existing password validation
   ```

3. **Show a similar example:**
   ```
   Here's how we do password validation in the same form:
   [Paste the password validation code, maybe 10–15 lines]
   ```

4. **Mention any constraints:**
   ```
   We're using React and our existing validation library is Yup.
   ```

This gives your AI assistant everything it needs to create code that fits your project perfectly.

TIP: Keep a "context template" file in each project. List the key files, patterns, and conventions. When starting a new feature, copy relevant sections from this template into your prompt. It saves time and ensures consistency.

**When to include more context**

Sometimes you'll need to provide more context than usual:

- **Refactoring across multiple files:** Show all the files that interact
- **Debugging complex issues:** Include error messages, logs, and the code paths involved
- **Matching existing patterns:** Show 2–3 examples of similar code so AI can identify the pattern
- **Working with unfamiliar code:** If you're modifying code you didn't write, include more surrounding context so AI understands the structure

REMEMBER: It's better to include a bit too much context than too little. You can always refine your prompts later, but starting with insufficient context wastes time on back-and-forth.

**When to include less context**

You can be more minimal when:

- **Working in a single, small file:** If the file is under 100 lines, you might not need to explain much
- **Following an established pattern:** If you've already shown AI your patterns, you can reference them briefly
- **Simple, isolated changes:** Adding a single function to a well-structured file often needs minimal context

WARNING: Don't assume AI remembers context from previous conversations. If you're continuing work from yesterday, briefly recap the key points. AI assistants typically don't retain memory across separate sessions unless explicitly configured to do so.

**Building your context intuition**

Like any skill, knowing how much context to provide gets easier with practice. Start by erring on the side of more context. As you work with your AI assistant, you'll learn:

- What level of detail it needs for different types of tasks
- Which patterns you can reference briefly vs. which need full examples
- When to paste entire files vs. when snippets are enough

Keep notes on what works. After a few weeks, you'll have a feel for the right amount of context for your project and your AI assistant.

TECHNICAL STUFF: Different AI assistants have different context window sizes (the maximum amount of text they can process at once). Most modern assistants can handle several thousand words, but very large codebases might require you to be selective. If you hit context limits, focus on the most relevant files and summarize the rest.

**What's next**

Now that you understand how to provide good context, let's look at how to be specific in your prompts without being overly prescriptive. That's the topic of the next section.

---

## Notes on This Sample

This sample section demonstrates:

- **Second-person voice** ("you'll face", "you're working on")
- **Short paragraphs** (2–5 sentences)
- **Plain language** with jargon defined ("context", "context window")
- **Active voice** ("Give it good context" vs. "Good context should be given")
- **Concrete examples** (the signup form example)
- **Callouts** (TIP, REMEMBER, WARNING, TECHNICAL STUFF)
- **Numbered lists** for procedures/examples
- **Bulleted lists** for options and characteristics
- **Outcome-based headings** ("Context: How Much Is Enough?")
- **Practical focus** over theory
- **Encouraging tone** ("Like any skill, this gets easier")

The section is "dippable" — a reader could jump here without reading earlier chapters and still understand the core concept, though reading Chapter 5's intro would help.

