---
lifecycle: evergreen
ttl_days: null
created_at: 2025-12-11T00:00:00Z
expires_at: null
housekeeping_policy: keep
---

# ADR: E10 UI Framework Selection - Codex (Vue.js)

**Decision ID:** ADR-E10-UI-001  
**Status:** ✅ APPROVED  
**Date:** 2025-12-11  
**Decision Maker:** Project Maintainer (via AI Agent)  
**Epic:** E10 - Knowledge Services Platform (Problem-Solution KB)  
**Story:** E10:S03 - API, UI, and Embeddings Design  
**Related Documents:**
- `KB/PM_and_Portfolio/kanban/epics/Epic-10/UI_DESIGN_DISCUSSION-wikipedia-style.md`
- `KB/PM_and_Portfolio/kanban/epics/Epic-10/DESIGN_DECISION-codex-vs-alternatives.md`
- `KB/PM_and_Portfolio/kanban/fr-br/FR-009-problem-solution-kb-service.md`

---

## Decision

**We will use Codex (Vue.js) as the UI framework for the Problem-Solution KB Service human web interface.**

### Decision Statement

The Problem-Solution KB Service will use **Codex**, Wikimedia's open-source Vue.js component library, as the foundation for its human web interface. This decision prioritizes development path of least resistance, leveraging Wikipedia's proven UI patterns and component library to accelerate development while ensuring accessibility and maintainability.

---

## Context

### Problem Statement

The Problem-Solution KB Service requires a human web interface that:
- Presents structured, versioned, collaboratively-edited knowledge (problems, solutions, examples)
- Displays provenance and citations prominently
- Supports editing, version history, and moderation workflows
- Maintains high accessibility standards (WCAG 2.1 AA compliance)
- Provides familiar navigation patterns for users
- Enables rapid development with minimal custom component creation

### Requirements

1. **Functional Requirements:**
   - Article/entry page templates (problem entries, solution patterns, examples)
   - Infobox components for metadata display
   - Citation/provenance system
   - Version history UI
   - Code block components with syntax highlighting
   - Search and browse interfaces
   - Edit and moderation workflows

2. **Non-Functional Requirements:**
   - Accessibility: WCAG 2.1 AA compliance
   - Performance: Fast load times, efficient rendering
   - Maintainability: Long-term sustainability
   - Developer Experience: Path of least resistance

3. **Constraints:**
   - Open-source project (must use open-source frameworks)
   - Aesthetic is not a factor (beyond elegance, simplicity, familiarity)
   - API-first architecture (UI is a client of the API)

### Decision Criteria

The decision was evaluated against the following criteria (in order of importance):

1. **Development Path of Least Resistance**
   - Time to productivity
   - Component availability
   - Pattern familiarity
   - Documentation quality

2. **Accessibility**
   - Built-in WCAG compliance
   - Keyboard navigation support
   - Screen reader compatibility

3. **Maintainability**
   - Framework maturity and stability
   - Community support
   - Long-term sustainability

4. **Ecosystem**
   - Component library availability
   - Tooling and developer experience
   - Integration capabilities

---

## Decision Drivers

### Primary Driver: Wikipedia Familiarity

**Rationale:** The project maintainer has extensive familiarity with Wikipedia's UI patterns. This familiarity provides:

1. **Instant Pattern Recognition**
   - Every design decision can reference Wikipedia: "How does Wikipedia do citations?" → Instant answer
   - No need for extensive design research or iteration
   - **Time Saved:** 1-2 weeks of design iteration

2. **Living Reference**
   - Wikipedia itself serves as documentation and examples
   - Can inspect Wikipedia's implementation directly
   - **Time Saved:** Hours of research per feature

3. **Proven Patterns**
   - Wikipedia's UI patterns are battle-tested at massive scale
   - Patterns are optimized for knowledge presentation
   - **Risk Reduction:** Lower risk of design mistakes

### Secondary Driver: Component Availability

**Rationale:** Codex provides ready-to-use components designed for Wikipedia's exact use case:

1. **Pre-Built Components**
   - Buttons, forms, cards, grids, badges, menus, dialogs
   - Components designed for article pages, citations, versioning
   - **Time Saved:** 2-3 weeks of component development

2. **Accessibility Built-In**
   - WCAG 2.1 AA compliance baked into components
   - Keyboard navigation, screen reader support included
   - **Time Saved:** 2-3 weeks of accessibility work

3. **Design Tokens**
   - Colors, spacing, typography, icons provided
   - Consistent design system out of the box
   - **Time Saved:** 1 week of design system creation

### Tertiary Driver: Development Speed

**Rationale:** Codex enables rapid development through:

1. **Composition Over Creation**
   - Compose article pages from existing components
   - Minimal custom component development needed
   - **Time Saved:** 1-2 weeks of custom development

2. **Vue.js Ecosystem**
   - Rich ecosystem (Vue Router, Pinia, VueUse)
   - Excellent tooling and TypeScript support
   - **Time Saved:** Days of integration work

3. **Documentation Quality**
   - Codex has good documentation
   - Large Vue.js community for support
   - **Time Saved:** Hours of troubleshooting

---

## Options Considered

### Option 1: Codex (Vue.js) ✅ SELECTED

**Description:** Wikimedia's open-source Vue.js component library, designed for Wikipedia and other Wikimedia projects.

**Pros:**
- ✅ Wikipedia familiarity = instant pattern recognition
- ✅ Components designed for article pages, citations, versioning
- ✅ Accessibility built-in (WCAG 2.1 AA compliance)
- ✅ Living reference (Wikipedia itself)
- ✅ Proven at scale (Wikipedia uses it)
- ✅ Open-source (MIT license)
- ✅ Actively maintained by Wikimedia
- ✅ Vue.js ecosystem support

**Cons:**
- ⚠️ Vue.js commitment (framework lock-in)
- ⚠️ Learning curve if team doesn't know Vue.js (1-2 weeks)
- ⚠️ Codex still evolving (may have gaps, but can fill with custom components)

**Development Time Estimate:** ~6 weeks  
**Path of Least Resistance Score:** 9/10

### Option 2: React + shadcn/ui (or Chakra UI)

**Description:** React framework with popular component libraries (shadcn/ui or Chakra UI).

**Pros:**
- ✅ Popular stack (large community, many developers know React)
- ✅ Rich ecosystem (massive npm ecosystem)
- ✅ Good component libraries available
- ✅ TypeScript support

**Cons:**
- ❌ No Wikipedia pattern alignment (need to figure out patterns yourself)
- ❌ Accessibility not guaranteed (need to audit and ensure)
- ❌ Component mismatch (components designed for different use cases)
- ❌ No living reference (can't look at Wikipedia as reference)
- ❌ More design iteration needed

**Development Time Estimate:** ~10-12 weeks (+6-7 weeks vs. Codex)  
**Path of Least Resistance Score:** 6/10

### Option 3: SvelteKit + Custom Components

**Description:** SvelteKit framework with custom component development.

**Pros:**
- ✅ Modern and performant
- ✅ Simple syntax
- ✅ Fast, lightweight

**Cons:**
- ❌ Smaller ecosystem (fewer libraries, less community support)
- ❌ No Wikipedia pattern alignment
- ❌ Limited component libraries
- ❌ Less developer familiarity
- ❌ More custom development needed

**Development Time Estimate:** ~12-15 weeks (+8-10 weeks vs. Codex)  
**Path of Least Resistance Score:** 4/10

### Option 4: OOUI (Vanilla JavaScript)

**Description:** Wikimedia's older JavaScript UI library (being phased out in favor of Codex).

**Pros:**
- ✅ Framework-agnostic
- ✅ Mature and battle-tested
- ✅ Wikipedia pattern alignment
- ✅ Accessibility built-in

**Cons:**
- ❌ Being phased out (Codex is the future)
- ❌ No modern framework benefits (no reactive updates, manual DOM manipulation)
- ❌ Less modern development experience (no TypeScript, no component composition)
- ❌ Higher maintenance burden (manual DOM manipulation)

**Development Time Estimate:** ~7-9 weeks (+2-4 weeks vs. Codex)  
**Path of Least Resistance Score:** 5/10

---

## Decision Rationale

### Quantitative Analysis

| Factor | Codex | React | SvelteKit | OOUI |
|--------|-------|-------|-----------|------|
| **Development Time** | 6 weeks | 10-12 weeks | 12-15 weeks | 7-9 weeks |
| **Time Saved vs. Codex** | Baseline | +6-7 weeks | +8-10 weeks | +2-4 weeks |
| **Component Availability** | High | Medium | Low | Medium |
| **Pattern Familiarity** | Perfect | Low | Low | Perfect |
| **Accessibility** | Built-in | Needs audit | Needs audit | Built-in |
| **Maintenance Burden** | Low | Medium | Medium | High |
| **Ecosystem Maturity** | High | Very High | Medium | Medium |

### Qualitative Analysis

#### Why Codex Wins on "Path of Least Resistance"

1. **Familiarity Multiplier (1-2 weeks saved)**
   - Wikipedia familiarity eliminates design iteration
   - Every design question has an instant answer: "Like Wikipedia"
   - No need for extensive UX research or pattern exploration

2. **Component Availability (2-3 weeks saved)**
   - Ready-to-use components for article pages, citations, versioning
   - No need to design and build components from scratch
   - Components are designed for Wikipedia's exact use case

3. **Accessibility Built-In (2-3 weeks saved)**
   - WCAG 2.1 AA compliance baked into components
   - No need for accessibility audit or fixes
   - Keyboard navigation and screen reader support included

4. **Living Reference (Hours per feature saved)**
   - Wikipedia itself serves as documentation
   - Can inspect Wikipedia's implementation directly
   - No need for extensive research or pattern libraries

5. **Proven at Scale (Risk reduction)**
   - Wikipedia uses Codex at massive scale
   - Battle-tested patterns reduce risk of design mistakes
   - Lower risk of needing major refactoring

**Total Time Savings: 6-7 weeks** compared to alternatives

### Risk Assessment

#### Risks with Codex

1. **Vue.js Commitment (Low Risk)**
   - **Risk:** Locked into Vue.js ecosystem
   - **Mitigation:** Vue.js is mature, widely adopted, unlikely to disappear
   - **Impact:** Low risk, but worth noting

2. **Learning Curve (Low Risk)**
   - **Risk:** Team may not know Vue.js
   - **Mitigation:** Vue.js has gentle learning curve, excellent docs (1-2 weeks for experienced developers)
   - **Impact:** Low risk, manageable learning curve

3. **Codex Gaps (Low Risk)**
   - **Risk:** Codex may have gaps for our specific needs
   - **Mitigation:** Can build custom components using Vue.js patterns, Vue.js ecosystem fills gaps
   - **Impact:** Low risk, gaps can be filled

#### Risk Comparison

| Risk | Codex | React | SvelteKit | OOUI |
|------|-------|-------|-----------|------|
| **Framework Abandonment** | Low | Very Low | Medium | High (being phased out) |
| **Learning Curve** | Low | Low | Medium | Medium |
| **Component Gaps** | Low | Medium | High | Medium |
| **Maintenance Burden** | Low | Medium | Medium | High |
| **Overall Risk** | **Low** | Low-Medium | Medium | Medium-High |

### Trade-offs Accepted

1. **Vue.js Commitment**
   - **Trade-off:** Locked into Vue.js ecosystem
   - **Justification:** Vue.js is mature, widely adopted, unlikely to disappear. The benefits outweigh the risk.

2. **Codex Still Evolving**
   - **Trade-off:** May need to build some custom components
   - **Justification:** Codex provides most components needed. Custom components can be built using Vue.js patterns. The time saved (6-7 weeks) outweighs the cost of building a few custom components.

3. **Not the Most Popular Stack**
   - **Trade-off:** React is more popular, easier to hire for
   - **Justification:** The familiarity advantage and time savings (6-7 weeks) outweigh the hiring advantage. Vue.js is still widely known and used.

---

## Consequences

### Positive Consequences

1. **Faster Development**
   - 6-7 weeks faster than alternatives
   - Earlier delivery to users
   - Lower development costs

2. **Higher Quality**
   - Accessibility built-in
   - Proven patterns reduce design mistakes
   - Battle-tested at Wikipedia scale

3. **Lower Maintenance Burden**
   - Components maintained by Wikimedia
   - Less custom code to maintain
   - Easier to keep up with accessibility standards

4. **Better Developer Experience**
   - Familiar patterns reduce cognitive load
   - Living reference (Wikipedia) for examples
   - Faster decision-making

### Negative Consequences

1. **Vue.js Commitment**
   - Locked into Vue.js ecosystem
   - Need to learn Vue.js if team doesn't know it
   - **Mitigation:** Vue.js is gentle to learn, excellent docs

2. **Codex Gaps**
   - May need to build some custom components
   - **Mitigation:** Can use Vue.js ecosystem, custom components follow Vue.js patterns

3. **Less Popular Than React**
   - Harder to hire Vue.js developers (though still widely available)
   - **Mitigation:** Vue.js is still popular, learning curve is gentle

### Neutral Consequences

1. **Aesthetic Independence**
   - We're not tied to Wikipedia's visual design
   - Can customize appearance while keeping functional patterns
   - **Note:** Aesthetic is not a factor per requirements

---

## Implementation Strategy

### Phase 1: Setup (Week 1)
- Install Vue.js + Codex
- Set up project structure
- Create basic article page template
- Test component composition

### Phase 2: Core Components (Weeks 2-3)
- Build article page template
- Create infobox component (Card + Fields)
- Build citation system
- Create code block component

### Phase 3: Advanced Features (Weeks 4-5)
- Version history UI
- Edit interface
- Search/browse interface
- Moderation queue

### Phase 4: Polish (Week 6)
- Accessibility audit
- Performance optimization
- Documentation
- Testing

**Total Estimated Time: 6 weeks** (vs. 10-12 weeks for alternatives)

---

## Validation

### Success Criteria

1. **Development Speed**
   - ✅ Article page template completed in Week 2-3
   - ✅ Core components functional by Week 3
   - ✅ Full UI functional by Week 6

2. **Accessibility**
   - ✅ WCAG 2.1 AA compliance verified
   - ✅ Keyboard navigation works
   - ✅ Screen reader compatibility confirmed

3. **Pattern Familiarity**
   - ✅ UI patterns match Wikipedia's functional patterns
   - ✅ Users find interface familiar and intuitive

4. **Component Reuse**
   - ✅ 80%+ of UI built from Codex components
   - ✅ Minimal custom component development

### Validation Plan

1. **Week 2:** Review article page template, validate component composition
2. **Week 4:** Accessibility audit, validate WCAG compliance
3. **Week 6:** User testing, validate pattern familiarity
4. **Ongoing:** Monitor component reuse, track custom component count

---

## Traceability

### Related Decisions

- **E10:S03:** API, UI, and Embeddings Design (this decision is part of)
- **FR-009:** Problem-Solution KB Service (requirements source)

### Related Documents

- `KB/PM_and_Portfolio/kanban/epics/Epic-10/UI_DESIGN_DISCUSSION-wikipedia-style.md` - Initial discussion
- `KB/PM_and_Portfolio/kanban/epics/Epic-10/DESIGN_DECISION-codex-vs-alternatives.md` - Detailed analysis
- `KB/PM_and_Portfolio/kanban/fr-br/FR-009-problem-solution-kb-service.md` - Requirements

### Decision History

- **2025-12-11:** Initial analysis and decision
- **2025-12-11:** Decision approved

### Future Reviews

- **Review Date:** 2026-06-11 (6 months)
- **Review Criteria:**
  - Development speed achieved
  - Accessibility compliance maintained
  - Component reuse percentage
  - Maintenance burden assessment

---

## Accountability

### Decision Maker

- **Role:** Project Maintainer
- **Method:** AI Agent acting on behalf of project maintainer
- **Rationale:** User preference (Wikipedia familiarity) + quantitative analysis

### Stakeholders

- **Primary:** Project Maintainer (decision maker)
- **Secondary:** Future developers (affected by framework choice)
- **Tertiary:** End users (affected by UI patterns and accessibility)

### Approval

- **Status:** ✅ APPROVED
- **Date:** 2025-12-11
- **Method:** Analysis-driven decision based on path of least resistance criteria

---

## References

### External References

- **Codex Documentation:** https://design.wikimedia.org/codex/
- **Codex Repository:** https://github.com/wikimedia/mediawiki-codex
- **Vue.js Documentation:** https://vuejs.org/
- **Wikipedia:** https://en.wikipedia.org/ (living reference)

### Internal References

- `KB/PM_and_Portfolio/kanban/epics/Epic-10/UI_DESIGN_DISCUSSION-wikipedia-style.md`
- `KB/PM_and_Portfolio/kanban/epics/Epic-10/DESIGN_DECISION-codex-vs-alternatives.md`
- `KB/PM_and_Portfolio/kanban/fr-br/FR-009-problem-solution-kb-service.md`

---

## Appendix: Detailed Analysis

See `KB/PM_and_Portfolio/kanban/epics/Epic-10/DESIGN_DECISION-codex-vs-alternatives.md` for:
- Detailed development effort estimates
- Component availability comparison
- Risk assessment details
- Mitigation strategies

---

**Document Status:** ✅ APPROVED  
**Last Updated:** 2025-12-11  
**Next Review:** 2026-06-11

