# Tool Distribution Decision Tree

**Quick guide for choosing distribution method for tools**

---

## Decision Flow

```
                    ┌─────────────────┐
                    │  New Tool Added  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  Register in    │
                    │  tools-registry │
                    └────────┬─────────┘
                             │
                             ▼
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
   ┌─────────┐        ┌──────────┐        ┌──────────┐
   │  Simple │        │ Complex  │        │  Widely  │
   │   CLI   │        │  Dependencies │   │   Used   │
   └────┬────┘        └─────┬────┘        └─────┬────┘
        │                    │                    │
        │                    │                    │
        ▼                    ▼                    ▼
   ┌─────────┐        ┌──────────┐        ┌──────────┐
   │   Git   │        │  Docker  │        │ Package  │
   │  Only   │        │ Optional │        │  Mgmt    │
   └─────────┘        └──────────┘        └──────────┘
```

---

## Quick Rules

### ✅ Use Git-Based (Current - Always Available)
- **When:** Simple CLI tools, quick iteration, minimal dependencies
- **How:** Clone repo, use directly
- **Example:** `python3 tools/github-badges/update_badges.py`

### 📦 Add Package Publishing (Optional)
- **When:** Tool is widely used, stable API, users prefer package managers
- **How:** Publish to npm/PyPI/etc.
- **Example:** `npm install @dev-toolkit/github-badges`

### 🐳 Add Docker Support (Optional)
- **When:** Complex dependencies, system libraries needed, CI/CD usage
- **How:** Create Dockerfile, publish to container registry
- **Example:** `docker run dev-toolkit/github-badges`

### ❌ Never Use DI Containers
- **Why:** Violates independence, creates coupling, overkill for CLI tools

---

## Examples

### Example 1: Simple Python Tool
```
Tool: github-badges
Dependencies: Python stdlib + jq
Distribution: Git-based ✅
Optional: PyPI package (if widely used)
```

### Example 2: Complex Tool with System Libraries
```
Tool: image-processor
Dependencies: OpenCV, ImageMagick, system libraries
Distribution: Git-based ✅ + Docker 🐳
Optional: Package (if stable)
```

### Example 3: Node.js Tool
```
Tool: markdown-formatter
Dependencies: Node.js packages
Distribution: Git-based ✅ + npm 📦
Optional: Docker (if needed)
```

---

## Registry Schema

```yaml
tools:
  tool-name:
    # ... existing fields
    distribution:
      git:                    # Always present
        url: "https://..."
        method: "clone"
      pypi: "package-name"    # Optional
      npm: "@scope/package"   # Optional
      docker: "registry/image" # Optional
```

---

## Independence Checklist

Before adding any distribution method, verify:

- [ ] Tool remains independent (no shared code)
- [ ] No dependencies on other tools
- [ ] Can be used standalone
- [ ] Distribution method doesn't create coupling
- [ ] Registry entry updated with distribution info

---

**See [Full Analysis](MANAGEMENT_APPROACHES_ANALYSIS.md) for detailed reasoning.**

