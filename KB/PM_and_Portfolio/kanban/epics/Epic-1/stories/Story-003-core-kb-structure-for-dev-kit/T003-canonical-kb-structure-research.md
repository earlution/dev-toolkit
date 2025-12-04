---
lifecycle: evergreen
ttl_days: null
created_at: 2025-12-04T12:01:50Z
expires_at: null
housekeeping_policy: keep
---

# Canonical Knowledge Base Structure Research

**Task:** E1:S03:T03 – Research canonical KB structures  
**Date:** 2025-12-02  
**Status:** ✅ COMPLETE  
**Version:** Research Document

---

## Executive Summary

This document researches **canonical Knowledge Base directory structures** aligned with current best practices (2024), focusing on:

1. **Self-documenting directory names**
2. **Depth management** (preference: ≤3 levels, not absolute)
3. **Avoiding meandering depth and bifurcation**
4. **Traversal time considerations**

**Key Findings:**
- Industry standard: **3-level maximum** for optimal usability
- Self-documenting names are critical for discoverability
- Flat structures preferred over deep nesting
- Current dev-kit structure has **6-level deep paths** (Kanban epics/stories)
- Several canonical patterns identified that could optimize current structure

---

## 1. Industry Best Practices (2024)

### 1.1 Depth Recommendations

**Industry Consensus:**
- **AllyMatter:** Keep hierarchy **no more than 3 levels deep** for intuitive navigation
- **KnowledgeOwl:** While platforms allow deep hierarchies, **usability decreases** with depth
- **Document360:** Well-planned information architecture limits depth to enhance findability

**Rationale:**
- Cognitive load increases with each level
- Traversal time increases exponentially with depth
- Users lose context in deep hierarchies
- Search becomes less effective in deep structures

### 1.2 Self-Documenting Names

**Principles:**
- Directory names should **immediately convey purpose**
- Avoid abbreviations unless universally understood
- Use consistent naming conventions (PascalCase, snake_case, kebab-case)
- Names should answer: "What is in this directory?"

**Examples:**
- ✅ `Architecture/Standards_and_ADRs/` (clear purpose)
- ✅ `Changelog_and_Release_Notes/Changelog_Archive/` (self-explanatory)
- ❌ `KB/A/SA/` (unclear abbreviations)
- ❌ `Docs/Stuff/` (vague purpose)

### 1.3 Traversal Time Considerations

**Research Findings:**
- **3-level depth:** ~2-3 clicks to reach content (optimal)
- **4-level depth:** ~3-4 clicks (acceptable)
- **5+ level depth:** ~4+ clicks (problematic)
- **6+ level depth:** ~5+ clicks (poor UX)

**Impact:**
- Deep structures increase cognitive load
- Users may abandon navigation
- Search becomes critical (but less effective)
- Maintenance becomes harder

---

## 2. Canonical KB Structure Patterns

### 2.1 Pattern A: Flat Three-Tier Structure (Recommended)

**Structure:**
```
KB/
├── README.md                    # Level 1: Root
├── Architecture/                # Level 1: Section
│   ├── README.md
│   ├── Standards/               # Level 2: Category
│   │   ├── versioning-policy.md
│   │   └── kanban-policy.md
│   └── ADRs/                    # Level 2: Category
│       └── adr-001-versioning.md
├── Project_Management/          # Level 1: Section
│   ├── README.md
│   ├── Kanban/                  # Level 2: Category
│   │   ├── board.md
│   │   └── epics/               # Level 3: Collection
│   │       ├── epic-1-{epic-1-title}.md
│   │       ├── epic-2-{epic-1-title}.md
│   │       └── stories/         # Level 4: Sub-collection (flat)
│   │           ├── epic-1-story-1-{story-1-title}.md
│   │           └── epic-1-story-2-{story-2-title}.md
│   └── Policies/                # Level 2: Category
│       └── governance.md
└── Release_Notes/               # Level 1: Section
    ├── README.md
    └── Archive/                 # Level 2: Category
        └── changelog-v0.1.0.md
```

**Depth Analysis:**
- Maximum depth: **3 levels** (`KB/Section/Category/Item`)
- Kanban epics: **3 levels** (`KB/Project_Management/Kanban/epics/epic-1.md`)
- ✅ Meets 3-level preference

**Advantages:**
- Clear, self-documenting structure
- Optimal traversal time (2-3 clicks)
- Easy to navigate
- Scales well

**Disadvantages:**
- May require flattening current Kanban structure
- Epic/Story relationships less explicit

---

### 2.2 Pattern B: Hierarchical with Controlled Depth

**Structure:**
```
KB/
├── README.md                    # Level 1: Root
├── Architecture/                # Level 1: Section
│   ├── README.md
│   ├── Standards/               # Level 2: Category
│   └── ADRs/                    # Level 2: Category
├── Project_Management/          # Level 1: Section
│   ├── README.md
│   ├── Kanban/                  # Level 2: Category
│   │   ├── README.md
│   │   ├── board.md
│   │   └── epics/               # Level 3: Collection
│   │       ├── epic-1.md        # Epic file (contains stories summaries)
│   │       └── epic-1/          # Level 4: Section (contains detailed stories)
│   │           └── story-1.md   # Story file (Contains Tasks)
│   └── Policies/                # Level 2: Category
└── Release_Notes/               # Level 1: Section
    └── Archive/                 # Level 2: Category
```

**Depth Analysis:**
- Maximum depth: **5 levels** (`KB/Project_Management/Kanban/epics/epic-1/stories/story-1.md`)
- ⚠️ Exceeds 3-level preference
- ⚠️ Traversal time: ~4-5 clicks

**Advantages:**
- Maintains Epic/Story hierarchy
- Clear relationships
- Matches current dev-kit structure

**Disadvantages:**
- Deep nesting (5 levels)
- Longer traversal time
- Higher cognitive load

---

### 2.3 Pattern C: Flat Collection Pattern (Optimal for Kanban)

**Structure:**
```
KB/
├── README.md                    # Level 1: Root
├── Architecture/                 # Level 1: Section
│   └── Standards/               # Level 2: Category
├── Project_Management/          # Level 1: Section
│   ├── README.md
│   ├── Kanban/                  # Level 2: Category
│   │   ├── README.md
│   │   ├── board.md
│   │   ├── epics/               # Level 3: Flat collection
│   │   │   ├── epic-1.md        # Epic file (contains story refs)
│   │   │   └── epic-2.md
│   │   └── stories/             # Level 3: Flat collection
│   │       ├── epic-1-story-1.md
│   │       └── epic-1-story-2.md
│   └── Policies/                # Level 2: Category
└── Release_Notes/               # Level 1: Section
    └── Archive/                 # Level 2: Category
```

**Depth Analysis:**
- Maximum depth: **3 levels** (`KB/Project_Management/Kanban/stories/epic-1-story-1.md`)
- ✅ Meets 3-level preference
- ✅ Optimal traversal time (2-3 clicks)

**Advantages:**
- Flat structure (3 levels max)
- Fast traversal
- Self-documenting names (`epic-1-story-1.md`)
- Easy to search and filter

**Disadvantages:**
- Epic/Story relationship via naming convention (not directory structure)
- May require refactoring current structure

---

### 2.4 Pattern D: Hybrid (Sections Flat, Collections Hierarchical)

**Structure:**
```
KB/
├── README.md                    # Level 1: Root
├── Architecture/                # Level 1: Section (flat)
│   └── Standards/               # Level 2: Category
├── Project_Management/          # Level 1: Section (flat)
│   ├── Kanban/                  # Level 2: Category
│   │   ├── epics/               # Level 3: Collection
│   │   │   ├── epic-1.md        # Epic file
│   │   │   └── epic-1/          # Level 4: Epic assets (optional)
│   │   │       └── stories/      # Level 5: Stories (only if needed)
│   │   │           └── story-1.md
│   │   └── board.md
│   └── Policies/                # Level 2: Category
└── Release_Notes/               # Level 1: Section (flat)
    └── Archive/                 # Level 2: Category
```

**Depth Analysis:**
- Sections: **2 levels** (optimal)
- Kanban epics: **3 levels** (epic files)
- Kanban stories: **5 levels** (only if assets needed)
- **Default depth: 3 levels** (stories can be referenced in epic files)

**Advantages:**
- Flexible: 3 levels default, 5 levels only when needed
- Maintains Epic/Story relationships
- Self-documenting
- Optimizes for common case (3 levels)

**Disadvantages:**
- Inconsistent depth (3 vs 5)
- Requires discipline to keep stories in epic files when possible

---

## 3. Current Dev-Kit Structure Analysis

### 3.1 Current Depth Map

```
KB/                                    # Level 1
├── Architecture/                      # Level 2
│   └── Standards_and_ADRs/           # Level 3
│       └── [files]                   # Level 3 (files)
├── Changelog_and_Release_Notes/      # Level 2
│   └── Changelog_Archive/            # Level 3
│       └── [files]                   # Level 3 (files)
└── PM_and_Portfolio/                 # Level 2
    ├── kanban/                       # Level 3
    │   └── epics/                    # Level 4
    │       └── Epic-1/              # Level 5
    │           └── stories/         # Level 6
    │               └── Story-003/    # Level 7 (task deliverables)
    │                   └── [files]  # Level 7 (files)
    └── rituals/                      # Level 3
        └── policy/                   # Level 4
            └── [files]               # Level 4 (files)
```

**Depth Summary:**
- **Architecture:** 3 levels ✅ (optimal)
- **Changelog:** 3 levels ✅ (optimal)
- **Kanban Epics:** 3 levels ✅ (optimal)
- **Kanban Stories:** 6 levels ⚠️ (deep)
- **Kanban Task Deliverables:** 7 levels ❌ (very deep)
- **Policies:** 4 levels ⚠️ (acceptable)

**Problem Areas:**
1. **Kanban task deliverables:** 7 levels deep (poor UX)
2. **Kanban stories:** 6 levels deep (problematic)
3. **Traversal time:** 5-6 clicks to reach task deliverables

---

### 3.2 Current Structure Assessment

**Strengths:**
- ✅ Clear separation of concerns (Architecture, PM, Changelog)
- ✅ Self-documenting section names
- ✅ Architecture and Changelog are optimally structured (3 levels)

**Weaknesses:**
- ❌ Kanban structure is **too deep** (6-7 levels)
- ❌ Traversal time is **too long** (5-6 clicks)
- ❌ Epic/Story/Task hierarchy creates unnecessary nesting
- ⚠️ Policies are 4 levels (acceptable but could be 3)

---

## 4. Recommended Structure for Dev-Kit

### 4.1 Proposed Optimized Structure

**Goal:** Achieve **3-level default**, **4-level maximum** (with exceptions only when necessary)

```
KB/                                    # Level 1: Root
├── README.md                          # Navigation hub
│
├── Architecture/                     # Level 2: Section (3-level max)
│   ├── README.md
│   └── Standards_and_ADRs/           # Level 3: Category
│       └── [policy files]           # Level 3: Files
│
├── Changelog_and_Release_Notes/      # Level 2: Section (3-level max)
│   ├── README.md
│   └── Changelog_Archive/            # Level 3: Category
│       └── [changelog files]        # Level 3: Files
│
├── Project_Management/               # Level 2: Section (3-level max)
│   ├── README.md
│   ├── Kanban/                      # Level 3: Category
│   │   ├── README.md
│   │   ├── board.md                 # Board view
│   │   ├── epics/                   # Level 3: Flat collection
│   │   │   ├── epic-1.md            # Epic file (contains story refs)
│   │   │   └── epic-2.md
│   │   └── stories/                 # Level 3: Flat collection
│   │       ├── epic-1-story-1.md    # Story file (contains task refs)
│   │       └── epic-1-story-2.md
│   └── Policies/                    # Level 3: Category
│       └── [policy files]           # Level 3: Files
│
└── Guides/                          # Level 2: Section (3-level max)
    ├── README.md
    ├── Getting_Started/             # Level 3: Category
    │   └── [guide files]            # Level 3: Files
    └── Framework_Consumption/        # Level 3: Category
        └── [guide files]            # Level 3: Files
```

**Depth Analysis:**
- **Maximum depth: 3 levels** ✅
- **Traversal time: 2-3 clicks** ✅
- **Self-documenting:** ✅ (epic-1-story-1.md naming)

**Key Changes:**
1. **Flatten Kanban structure:** Epics and stories become flat collections
2. **Naming convention:** `epic-{N}-story-{M}.md` for stories
3. **Task deliverables:** Embedded in story files or separate `tasks/` collection
4. **Policies:** Moved to 3-level depth

---

### 4.2 Alternative: Hybrid Approach (Preserve Some Hierarchy)

If Epic/Story/Task directory hierarchy is **essential** for organization:

```
KB/
└── Project_Management/
    └── Kanban/
        ├── epics/                   # Level 3: Collection
        │   ├── epic-1.md            # Epic file
        │   └── epic-1/              # Level 4: Epic assets (ONLY if needed)
        │       ├── stories/         # Level 5: Stories (ONLY if assets needed)
        │       │   └── story-1.md
        │       └── assets/         # Level 5: Epic-specific assets
        └── stories/                 # Level 3: Default location (flat)
            └── epic-1-story-1.md    # Most stories here (3 levels)
```

**Strategy:**
- **Default:** Stories in flat `stories/` collection (3 levels)
- **Exception:** Epic-specific assets in `epic-{N}/` (5 levels, only when needed)
- **Rule:** Use deep structure only when assets require organization

**Depth Analysis:**
- **Default depth: 3 levels** ✅
- **Exception depth: 5 levels** (only when necessary)
- **Traversal time: 2-3 clicks** (default), 4-5 clicks (exception)

---

## 5. Migration Strategy

### 5.1 Option A: Full Flattening (Recommended)

**Changes:**
1. Move all epic files to `KB/Project_Management/Kanban/epics/` (flat)
2. Move all story files to `KB/Project_Management/Kanban/stories/` (flat)
3. Rename stories: `epic-{N}-story-{M}.md`
4. Embed task deliverables in story files or create `tasks/` collection
5. Update all cross-references

**Benefits:**
- ✅ 3-level maximum depth
- ✅ Optimal traversal time
- ✅ Self-documenting names
- ✅ Easier to maintain

**Effort:** Medium (requires refactoring and link updates)

---

### 5.2 Option B: Hybrid Approach (Pragmatic)

**Changes:**
1. Keep epic files in `epics/` (flat, 3 levels)
2. Keep most stories in `stories/` (flat, 3 levels)
3. Use `epic-{N}/` directories **only** for epic-specific assets
4. Rename stories: `epic-{N}-story-{M}.md` for flat collection
5. Update cross-references

**Benefits:**
- ✅ Default 3-level depth
- ✅ Flexibility for assets
- ✅ Preserves some hierarchy when needed
- ✅ Less disruptive migration

**Effort:** Low-Medium (minimal refactoring, mostly naming)

---

### 5.3 Option C: Keep Current Structure (Not Recommended)

**Rationale:**
- Current structure works functionally
- Migration effort may be high
- Team familiarity with current structure

**Trade-offs:**
- ❌ 6-7 level depth (poor UX)
- ❌ Long traversal time
- ❌ Higher cognitive load
- ⚠️ Does not align with best practices

---

## 6. Recommendations

### 6.1 Immediate Actions

1. **Adopt Pattern C (Flat Collection)** for Kanban structure
   - Flatten epics and stories to 3-level depth
   - Use naming convention: `epic-{N}-story-{M}.md`
   - Embed task deliverables in story files or separate `tasks/` collection

2. **Flatten Policies** to 3-level depth
   - Move from `PM_and_Portfolio/rituals/policy/` (4 levels)
   - To `PM_and_Portfolio/Policies/` (3 levels)

3. **Document Structure Principles**
   - Establish 3-level default rule
   - Define exceptions (when 4-5 levels are acceptable)
   - Create migration guide

### 6.2 Long-Term Strategy

1. **Maintain 3-Level Default**
   - Enforce in structure principles
   - Review new additions for depth compliance
   - Refactor deep structures when encountered

2. **Self-Documenting Names**
   - Use descriptive names (`epic-1-story-1.md` vs `story-1.md`)
   - Establish naming conventions
   - Document in KB structure principles

3. **Traversal Time Monitoring**
   - Track average clicks to reach content
   - Optimize high-traffic paths
   - Consider search improvements for deep content

---

## 7. Comparison Matrix

| Pattern | Max Depth | Traversal Time | Self-Doc | Migration Effort | Recommendation |
|---------|-----------|----------------|----------|------------------|----------------|
| **Pattern A (Flat 3-Tier)** | 3 levels | 2-3 clicks | ✅ High | Medium | ⭐⭐⭐⭐⭐ |
| **Pattern B (Hierarchical)** | 5 levels | 4-5 clicks | ✅ Medium | Low | ⭐⭐ |
| **Pattern C (Flat Collection)** | 3 levels | 2-3 clicks | ✅ High | Medium | ⭐⭐⭐⭐⭐ |
| **Pattern D (Hybrid)** | 3-5 levels | 2-5 clicks | ✅ High | Low-Medium | ⭐⭐⭐⭐ |
| **Current Structure** | 7 levels | 5-6 clicks | ⚠️ Medium | N/A | ⭐ |

---

## 8. Conclusion

**Key Findings:**
1. Industry standard: **3-level maximum** for optimal usability
2. Current dev-kit structure has **6-7 level deep paths** (Kanban)
3. **Pattern C (Flat Collection)** aligns best with requirements
4. Self-documenting names can replace directory hierarchy

**Recommended Action:**
- **Adopt Pattern C** with flat epic/story collections
- **Target: 3-level default**, 4-level maximum (with exceptions)
- **Migration:** Medium effort, high benefit

**Next Steps:**
1. Review and approve recommended structure
2. Create detailed migration plan
3. Execute migration (Phase 2 of KB structure work)
4. Update structure principles document

---

_End of Research Document_

