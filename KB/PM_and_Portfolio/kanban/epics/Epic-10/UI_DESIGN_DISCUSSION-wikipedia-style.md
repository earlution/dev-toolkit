---
lifecycle: evergreen
ttl_days: null
created_at: 2025-12-11T00:00:00Z
expires_at: null
housekeeping_policy: keep
---

# UI Design Discussion: Wikipedia-Style Interface for Problem-Solution KB

**Epic:** E10 - Knowledge Services Platform (Problem-Solution KB)  
**Story:** E10:S03 - API, UI, and Embeddings Design  
**Created:** 2025-12-11  
**Status:** DISCUSSION

---

## Overview

This document discusses applying Wikipedia-style UI patterns to the human web interface for the Problem-Solution KB Service. **Focus: Functional patterns and open-source technology stack, not visual aesthetics.** Wikipedia's interface excels at presenting structured, versioned, collaboratively-edited knowledge with clear provenance—exactly what we need for problem-solution entries.

---

## Why Wikipedia-Style UI? (Functional, Not Aesthetic)

### Core Alignment
1. **Structured Knowledge**: Wikipedia articles are hierarchical, well-organized, and scannable—perfect for problem statements, solution patterns, and examples.
2. **Provenance & Citations**: Wikipedia's citation model aligns with our requirement for explicit provenance and licensing.
3. **Version History**: Wikipedia's edit history and diff views match our versioning requirements.
4. **Collaborative Editing**: Wikipedia's edit workflow (with moderation) mirrors our submission/review process.
5. **High Information Density**: Wikipedia packs a lot of information into a single page while remaining readable.
6. **Open-Source Foundation**: Wikipedia uses open-source technologies we can leverage or learn from.

### User Mental Models
- **Familiarity**: Most users already understand Wikipedia's navigation and structure.
- **Expectations**: Users expect to find comprehensive, well-organized information with clear sources.
- **Trust Signals**: Quality indicators (verified badges, edit history, citations) build trust.

---

## Wikipedia's Open-Source Technology Stack

### Core Platform: MediaWiki
- **What**: Open-source wiki software (PHP backend)
- **License**: GPL v2+
- **Repository**: https://github.com/wikimedia/mediawiki
- **Use Case**: Full wiki platform with collaborative editing, versioning, moderation
- **Consideration**: Could we use MediaWiki directly, or build our own API-first solution?

### Current UI Framework: OOUI (Object-Oriented User Interface)
- **What**: Open-source JavaScript UI library
- **License**: MIT
- **Repository**: https://github.com/wikimedia/oojs-ui
- **Features**:
  - Responsive widgets, layouts, windows
  - Internationalization (i18n) ready
  - Right-to-left (RTL) language support
  - WCAG accessibility compliance
  - Can be used standalone or with MediaWiki
- **Status**: Still in use, but being phased out in favor of Codex

### New Design System: Codex
- **What**: Modern design system replacing OOUI
- **License**: MIT
- **Repository**: https://github.com/wikimedia/mediawiki-codex
- **Technology**: Vue.js components
- **Features**:
  - Component library (buttons, forms, cards, etc.)
  - Design tokens (colors, spacing, typography)
  - Accessibility built-in
  - Responsive design patterns
- **Status**: Recommended for new Wikimedia projects

### Vector Skin (Default Wikipedia Skin)
- **What**: Default MediaWiki skin (the "Wikipedia look")
- **Focus**: Functional, content-first design
- **Note**: We don't need to replicate this aesthetic—focus on functional patterns

---

## Technical Decision: Build vs. Adopt

### Option 1: Use MediaWiki Directly
**Pros:**
- ✅ Battle-tested, mature platform
- ✅ Built-in versioning, editing, moderation
- ✅ Large community and documentation
- ✅ Extensible via extensions
- ✅ Proven scalability (Wikipedia scale)
- ✅ **Comes with wiki templates** (infoboxes, navigation boxes, etc.)

**Available MediaWiki Templates** (wiki content templates, not UI components):
- Infobox templates (for structured data display)
- Navigation templates (sidebars, navboxes)
- Citation templates (for references)
- Stub templates (for incomplete articles)
- **Note**: These are wiki content templates (server-side), not UI component templates

**Cons:**
- ❌ PHP backend (may not align with our stack)
- ❌ Tightly coupled to wiki model (may not fit our API-first approach)
- ❌ Heavy for our use case (we need API + UI, not full wiki)
- ❌ Customization may be complex
- ❌ Templates are wiki content (server-rendered), not reusable UI components

**Verdict**: Probably not ideal—we need API-first architecture, and MediaWiki is wiki-first. Templates are for wiki content, not UI components.

### Option 2: Use Codex Components (Vue.js)
**Pros:**
- ✅ Modern, accessible component library
- ✅ Open-source, MIT licensed
- ✅ Built for Wikimedia's needs (similar to ours)
- ✅ Can use standalone (don't need MediaWiki)
- ✅ Vue.js ecosystem (if we choose Vue)
- ✅ **Comes with pre-built components** (buttons, forms, cards, etc.)

**Available Codex Components** (from https://design.wikimedia.org/codex/):
- **Buttons**: Button, ButtonGroup
- **Forms**: Checkbox, Combobox, Field, Label, Radio, Select, TextInput, Textarea, ToggleSwitch
- **Layout**: Card, Grid, Stack
- **Navigation**: Menu, Tabs, TabsBar
- **Feedback**: Message, ProgressBar, Thumbnail
- **Data Display**: Table, TypeaheadSearch
- **Overlays**: Dialog, Menu, Popup
- **Design Tokens**: Colors, spacing, typography, icons

**Cons:**
- ❌ Vue.js dependency (need to commit to Vue)
- ❌ Still relatively new (less mature than OOUI)
- ❌ May need customization for our use case
- ❌ **No article/infobox templates** - need to compose from components

**Verdict**: **Strong candidate** if we choose Vue.js stack. Components available, but need to compose article pages ourselves.

### Option 3: Use OOUI (Standalone)
**Pros:**
- ✅ Mature, battle-tested
- ✅ Framework-agnostic (vanilla JS)
- ✅ Can use standalone
- ✅ Excellent accessibility
- ✅ **Comes with pre-built widgets** (buttons, forms, layouts, windows)

**Available OOUI Widgets** (from https://doc.wikimedia.org/oojs-ui/master/js/):
- **Buttons**: Button, ButtonGroup, ButtonWidget, IconButton
- **Forms**: CheckboxInput, DropdownInput, RadioInput, TextInput, TextInputWidget
- **Layouts**: HorizontalLayout, VerticalLayout, StackLayout, PanelLayout, MenuLayout
- **Windows**: Dialog, ProcessDialog, MessageDialog
- **Menus**: MenuSelectWidget, MenuOptionWidget, DropdownWidget
- **Lists**: SelectWidget, OptionWidget, OutlineSelectWidget
- **Toolbars**: Toolbar, ToolGroup
- **Other**: PopupWidget, PopupButtonWidget, IndexLayout, BookletLayout

**Cons:**
- ❌ Being phased out (Codex is future)
- ❌ Less modern than Codex
- ❌ May not align with modern frontend practices
- ❌ **No article/infobox templates** - need to compose from widgets

**Verdict**: **Possible** but not ideal—Codex is the future. Widgets available, but need to compose article pages ourselves.

### Option 4: Build Custom (Inspired by Patterns)
**Pros:**
- ✅ Full control over stack (React, Vue, Svelte, etc.)
- ✅ Optimized for our specific needs
- ✅ API-first architecture
- ✅ Can adopt functional patterns without framework lock-in

**Cons:**
- ❌ More development effort
- ❌ Need to build accessibility features
- ❌ Need to implement versioning/editing UI

**Verdict**: **Most likely**—we can adopt functional patterns while using our preferred stack.

---

## Practical Example: Composing Article Pages from Components

### Example: Problem Entry Page Using Codex (Vue.js)

Here's how you'd compose a Wikipedia-style problem entry page using Codex components:

#### Component Structure
```vue
<template>
  <div class="problem-entry-page">
    <!-- Header with Quality Badge -->
    <div class="page-header">
      <h1>{{ problem.title }}</h1>
      <cdx-badge :type="qualityBadgeType">{{ qualityStatus }}</cdx-badge>
    </div>

    <!-- Main Layout: Sidebar + Content -->
    <cdx-grid>
      <!-- Infobox Sidebar (using Card component) -->
      <cdx-grid-col :span="3">
        <cdx-card class="infobox">
          <template #title>Problem Details</template>
          <cdx-field>
            <cdx-label>Domain:</cdx-label>
            <span>{{ problem.domain }}</span>
          </cdx-field>
          <cdx-field>
            <cdx-label>Scale:</cdx-label>
            <span>{{ problem.scale }}</span>
          </cdx-field>
          <cdx-field>
            <cdx-label>Constraints:</cdx-label>
            <span>{{ problem.constraints }}</span>
          </cdx-field>
          <cdx-field>
            <cdx-label>Tags:</cdx-label>
            <cdx-chip-group>
              <cdx-chip v-for="tag in problem.tags" :key="tag">{{ tag }}</cdx-chip>
            </cdx-chip-group>
          </cdx-field>
          <cdx-field>
            <cdx-label>Status:</cdx-label>
            <span>{{ problem.status }}</span>
          </cdx-field>
          <cdx-field>
            <cdx-label>Last Updated:</cdx-label>
            <span>{{ problem.lastUpdated }}</span>
          </cdx-field>
          <cdx-field>
            <cdx-label>Version:</cdx-label>
            <span>{{ problem.version }}</span>
          </cdx-field>
        </cdx-card>
      </cdx-grid-col>

      <!-- Main Content Area -->
      <cdx-grid-col :span="9">
        <!-- Abstract/Summary -->
        <cdx-message type="notice" class="abstract">
          {{ problem.abstract }}
        </cdx-message>

        <!-- Table of Contents (auto-generated) -->
        <nav class="table-of-contents" v-if="hasMultipleSections">
          <h2>Contents</h2>
          <ul>
            <li v-for="section in sections" :key="section.id">
              <a :href="`#${section.id}`">{{ section.title }}</a>
            </li>
          </ul>
        </nav>

        <!-- Problem Statement Section -->
        <section id="problem-statement">
          <h2>Problem Statement</h2>
          <div class="content" v-html="problem.statement"></div>
        </section>

        <!-- Context & Constraints Section -->
        <section id="context">
          <h2>Context & Constraints</h2>
          <div class="content" v-html="problem.context"></div>
        </section>

        <!-- Solution Patterns Section -->
        <section id="solutions">
          <h2>Solution Patterns</h2>
          <cdx-card v-for="solution in problem.solutions" :key="solution.id" class="solution-card">
            <template #title>
              <router-link :to="`/solutions/${solution.id}`">
                {{ solution.title }}
              </router-link>
            </template>
            <p>{{ solution.summary }}</p>
            <cdx-field>
              <cdx-label>Applicability:</cdx-label>
              <span>{{ solution.applicability }}</span>
            </cdx-field>
          </cdx-card>
        </section>

        <!-- Examples Section -->
        <section id="examples">
          <h2>Examples</h2>
          <div v-for="example in problem.examples" :key="example.id" class="example-block">
            <cdx-card>
              <template #title>{{ example.title }}</template>
              <!-- Code Block Component (custom, using syntax highlighter) -->
              <code-block 
                :code="example.code" 
                :language="example.language"
                :provenance="example.provenance"
                :license="example.license"
              />
            </cdx-card>
          </div>
        </section>

        <!-- References & Provenance Section -->
        <section id="references">
          <h2>References & Provenance</h2>
          <ol class="references-list">
            <li v-for="(ref, index) in problem.references" :key="index">
              <a :href="ref.url" target="_blank" rel="noopener">
                {{ ref.title }}
              </a>
              <span class="license-badge">{{ ref.license }}</span>
              <span class="retrieved">Retrieved: {{ ref.retrieved }}</span>
            </li>
          </ol>
        </section>

        <!-- Action Buttons -->
        <div class="page-actions">
          <cdx-button action="progressive">Edit</cdx-button>
          <cdx-button action="quiet">View History</cdx-button>
          <cdx-button action="quiet">Discuss</cdx-button>
          <cdx-button action="quiet">Flag</cdx-button>
        </div>
      </cdx-grid-col>
    </cdx-grid>
  </div>
</template>

<script setup>
import { CdxCard, CdxGrid, CdxGridCol, CdxField, CdxLabel, CdxBadge, CdxChip, CdxChipGroup, CdxMessage, CdxButton } from '@wikimedia/codex'
import CodeBlock from '@/components/CodeBlock.vue' // Custom component

const props = defineProps({
  problem: {
    type: Object,
    required: true
  }
})

const qualityBadgeType = computed(() => {
  const statusMap = {
    'verified': 'success',
    'draft': 'warning',
    'deprecated': 'error'
  }
  return statusMap[props.problem.status] || 'notice'
})
</script>
```

#### Custom Components Needed
```vue
<!-- CodeBlock.vue - Syntax-highlighted code with provenance -->
<template>
  <div class="code-block">
    <div class="code-header">
      <span class="language-badge">{{ language }}</span>
      <cdx-button action="quiet" @click="copyCode">Copy</cdx-button>
    </div>
    <pre><code :class="`language-${language}`">{{ code }}</code></pre>
    <div class="code-footer">
      <a :href="provenance.url" target="_blank" rel="noopener">
        Source: {{ provenance.title }}
      </a>
      <span class="license-badge">{{ license }}</span>
    </div>
  </div>
</template>
```

### Example: Same Page Using React + shadcn/ui

For comparison, here's how it would look with React:

```tsx
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { Button } from '@/components/ui/button'
import { Grid, GridCol } from '@/components/ui/grid'
import CodeBlock from '@/components/CodeBlock'

export function ProblemEntryPage({ problem }) {
  return (
    <div className="problem-entry-page">
      {/* Header */}
      <div className="page-header">
        <h1>{problem.title}</h1>
        <Badge variant={getQualityVariant(problem.status)}>
          {problem.status}
        </Badge>
      </div>

      {/* Main Layout */}
      <Grid>
        {/* Infobox Sidebar */}
        <GridCol span={3}>
          <Card className="infobox">
            <CardHeader>
              <CardTitle>Problem Details</CardTitle>
            </CardHeader>
            <CardContent>
              <Field label="Domain">{problem.domain}</Field>
              <Field label="Scale">{problem.scale}</Field>
              <Field label="Constraints">{problem.constraints}</Field>
              <Field label="Tags">
                {problem.tags.map(tag => (
                  <Badge key={tag}>{tag}</Badge>
                ))}
              </Field>
              <Field label="Status">{problem.status}</Field>
              <Field label="Last Updated">{problem.lastUpdated}</Field>
              <Field label="Version">{problem.version}</Field>
            </CardContent>
          </Card>
        </GridCol>

        {/* Main Content */}
        <GridCol span={9}>
          {/* Abstract */}
          <Alert className="abstract">{problem.abstract}</Alert>

          {/* Table of Contents */}
          {sections.length > 1 && (
            <nav className="table-of-contents">
              <h2>Contents</h2>
              <ul>
                {sections.map(section => (
                  <li key={section.id}>
                    <a href={`#${section.id}`}>{section.title}</a>
                  </li>
                ))}
              </ul>
            </nav>
          )}

          {/* Problem Statement */}
          <section id="problem-statement">
            <h2>Problem Statement</h2>
            <div dangerouslySetInnerHTML={{ __html: problem.statement }} />
          </section>

          {/* Solution Patterns */}
          <section id="solutions">
            <h2>Solution Patterns</h2>
            {problem.solutions.map(solution => (
              <Card key={solution.id} className="solution-card">
                <CardHeader>
                  <CardTitle>
                    <Link to={`/solutions/${solution.id}`}>
                      {solution.title}
                    </Link>
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <p>{solution.summary}</p>
                  <Field label="Applicability">{solution.applicability}</Field>
                </CardContent>
              </Card>
            ))}
          </section>

          {/* Examples */}
          <section id="examples">
            <h2>Examples</h2>
            {problem.examples.map(example => (
              <Card key={example.id}>
                <CardHeader>
                  <CardTitle>{example.title}</CardTitle>
                </CardHeader>
                <CardContent>
                  <CodeBlock
                    code={example.code}
                    language={example.language}
                    provenance={example.provenance}
                    license={example.license}
                  />
                </CardContent>
              </Card>
            ))}
          </section>

          {/* References */}
          <section id="references">
            <h2>References & Provenance</h2>
            <ol className="references-list">
              {problem.references.map((ref, index) => (
                <li key={index}>
                  <a href={ref.url} target="_blank" rel="noopener">
                    {ref.title}
                  </a>
                  <Badge>{ref.license}</Badge>
                  <span>Retrieved: {ref.retrieved}</span>
                </li>
              ))}
            </ol>
          </section>

          {/* Actions */}
          <div className="page-actions">
            <Button variant="default">Edit</Button>
            <Button variant="ghost">View History</Button>
            <Button variant="ghost">Discuss</Button>
            <Button variant="ghost">Flag</Button>
          </div>
        </GridCol>
      </Grid>
    </div>
  )
}
```

### Key Takeaways from Examples

1. **Components are building blocks**: Codex/React components provide buttons, cards, grids, forms
2. **You compose templates**: Article pages are composed from these components
3. **Custom components needed**: Code blocks, citation systems, version history need custom implementation
4. **Pattern is framework-agnostic**: Same structure works with Vue (Codex), React (shadcn/ui), or Svelte
5. **Accessibility built-in**: Codex and modern component libraries include accessibility features

### What You Get vs. What You Build

| Component Type | Provided by Framework | You Build |
|----------------|---------------------|-----------|
| Buttons | ✅ Yes | ❌ No |
| Forms (inputs, selects) | ✅ Yes | ❌ No |
| Cards | ✅ Yes | ❌ No |
| Grid/Layout | ✅ Yes | ❌ No |
| Badges | ✅ Yes | ❌ No |
| **Article Page Template** | ❌ No | ✅ Yes (compose from components) |
| **Infobox Component** | ❌ No | ✅ Yes (Card + Fields) |
| **Code Block** | ❌ No | ✅ Yes (custom with syntax highlighter) |
| **Citation System** | ❌ No | ✅ Yes (custom list + links) |
| **Version History UI** | ❌ No | ✅ Yes (custom timeline/diff view) |
| **Table of Contents** | ❌ No | ✅ Yes (auto-generate from sections) |

---

## Functional Patterns to Adopt (Framework-Agnostic)

Regardless of which framework we choose, these are the functional patterns we should adopt:

### 1. **Article/Entry Page Structure**
- Infobox sidebar (metadata)
- Table of contents (auto-generated)
- Structured sections
- References/citations section
- Edit/view history links

### 2. **Navigation Patterns**
- Prominent search bar
- Sidebar navigation (collapsible on mobile)
- Breadcrumbs
- Related content links
- Category/tag browsing

### 3. **Editing Workflow**
- Edit button → Edit form → Preview → Save
- Draft saving (work-in-progress)
- Conflict resolution (multiple editors)
- Change summary (required)

### 4. **Version History**
- List of versions (timeline)
- Diff view (compare versions)
- Revert capability (for stewards)
- Version metadata (timestamp, editor, summary)

### 5. **Citation/Provenance System**
- Inline citations `[1]` `[2]`
- References section at bottom
- License badges
- Source URLs (clickable)

### 6. **Quality Indicators**
- Visual badges (verified/draft/deprecated)
- Status indicators
- Moderation queue
- Flagging system

### 7. **Accessibility Patterns**
- Keyboard navigation
- Screen reader support
- High contrast mode
- Focus indicators
- ARIA labels

---

## Component/Template Availability Summary

### What Comes with Each Framework

| Framework | UI Components | Article Templates | Notes |
|-----------|--------------|-------------------|-------|
| **MediaWiki** | ❌ No | ✅ Yes (wiki templates) | Templates are server-side wiki content, not reusable UI components |
| **Codex (Vue)** | ✅ Yes (buttons, forms, cards, etc.) | ❌ No | Need to compose article pages from components |
| **OOUI (JS)** | ✅ Yes (widgets, layouts, windows) | ❌ No | Need to compose article pages from widgets |
| **Custom (React/Svelte)** | ❌ No | ❌ No | Need to build everything or use third-party component libraries |

### Key Insight
**None of these frameworks provide ready-made article/infobox templates** - they provide **UI components** that you compose into article pages. This means:

- ✅ **Codex/OOUI**: Give you building blocks (buttons, forms, cards, layouts)
- ❌ **No templates**: You still need to compose article pages, infoboxes, citation systems yourself
- ✅ **Patterns available**: You can study Wikipedia's structure and recreate it using the components

### What This Means for Our Project

1. **If using Codex (Vue)**:
   - Get: Buttons, forms, cards, tables, menus, dialogs
   - Build: Article page layout, infobox component, citation system, version history UI

2. **If using OOUI (JS)**:
   - Get: Widgets, layouts, windows, menus
   - Build: Article page layout, infobox component, citation system, version history UI

3. **If building custom (React/Svelte)**:
   - Get: Nothing (or use third-party component libraries like shadcn/ui, Chakra UI)
   - Build: Everything, but can adopt Wikipedia's functional patterns

---

## Recommended Approach

### Stack Suggestion
1. **Backend**: API-first (REST/GraphQL) - language agnostic
2. **Frontend**: Modern framework (React/Vue/Svelte) with:
   - **If Vue**: Codex component library (buttons, forms, cards, etc.)
   - **If React**: shadcn/ui or Chakra UI (similar component libraries)
   - **If Svelte**: Custom components or Svelte Material UI
   - Accessibility-first design
   - Responsive layout system

### Functional Patterns to Implement
1. **Adopt Wikipedia's information architecture** (not visual design)
2. **Use Codex components** (if Vue) or similar component libraries (if React/Svelte)
3. **Build article/infobox templates** using available components (compose from building blocks)
4. **Focus on accessibility** (WCAG 2.1 AA compliance)
5. **API-first design** (UI renders API data)

### Key Principles
- ✅ **Functional over aesthetic**: Focus on usability, not visual mimicry
- ✅ **Open-source components**: Use Codex (Vue) or similar (React/Svelte) for building blocks
- ✅ **Compose templates**: Build article/infobox templates from components
- ✅ **Accessibility first**: WCAG compliance, keyboard navigation
- ✅ **API-first**: UI is a client of our API
- ✅ **Framework flexibility**: Choose stack that fits our needs

---

## Wikipedia UI Patterns to Adopt

### 1. **Article/Entry Page Structure**

#### Problem Entry Page
```
┌─────────────────────────────────────────────────────────┐
│ [Problem Title]                                         │
│                                                         │
│ [Quality Badge: Verified/Draft/Deprecated]             │
│                                                         │
│ ┌─────────────────┐  ┌──────────────────────────────┐ │
│ │   Infobox       │  │  Abstract/Summary            │ │
│ │                 │  │  (2-3 sentence overview)      │ │
│ │ Domain:         │  │                              │ │
│ │ Scale:          │  │  [Table of Contents]        │ │
│ │ Constraints:    │  │  • Problem Statement        │ │
│ │ Tags:           │  │  • Context                  │ │
│ │ Status:         │  │  • Solution Patterns        │ │
│ │ Last Updated:   │  │  • Examples                  │ │
│ │ Version:        │  │  • Related Problems        │ │
│ └─────────────────┘  └──────────────────────────────┘ │
│                                                         │
│ ## Problem Statement                                   │
│ [Detailed description with context]                    │
│                                                         │
│ ## Context & Constraints                                │
│ [Domain, scale, constraints, expected outcomes]        │
│                                                         │
│ ## Solution Patterns                                   │
│ [List of linked solution pattern pages]                │
│                                                         │
│ ## Examples                                            │
│ [Code snippets with provenance links]                  │
│                                                         │
│ ## Related Problems                                    │
│ [Links to similar/related problems]                    │
│                                                         │
│ ┌─────────────────────────────────────────────────┐  │
│ │ References & Provenance                          │  │
│ │ • [1] Source URL (License: MIT)                  │  │
│ │ • [2] Example Repository (License: Apache 2.0)   │  │
│ └─────────────────────────────────────────────────┘  │
│                                                         │
│ [Edit] [View History] [Discuss] [Flag]                │
└─────────────────────────────────────────────────────────┘
```

#### Solution Pattern Entry Page
```
┌─────────────────────────────────────────────────────────┐
│ [Solution Pattern Title]                                │
│                                                         │
│ ┌─────────────────┐  ┌──────────────────────────────┐ │
│ │   Infobox       │  │  Summary                     │ │
│ │                 │  │  (When to use this pattern)  │ │
│ │ Applicability:  │  │                              │ │
│ │ Complexity:     │  │  [Table of Contents]         │ │
│ │ Trade-offs:     │  │  • Overview                 │ │
│ │ Related:        │  │  • Applicability            │ │
│ │ Status:         │  │  • Trade-offs               │ │
│ └─────────────────┘  │  • Pros & Cons             │ │
│                       │  • Anti-patterns            │ │
│                       │  • Examples                │ │
│                       └──────────────────────────────┘ │
│                                                         │
│ ## Overview                                            │
│ [Pattern description]                                  │
│                                                         │
│ ## Applicability                                       │
│ [When to use, constraints, prerequisites]              │
│                                                         │
│ ## Trade-offs                                          │
│ [Performance, complexity, maintainability, etc.]      │
│                                                         │
│ ## Pros & Cons                                         │
│ [Structured comparison]                                 │
│                                                         │
│ ## Anti-patterns                                       │
│ [What NOT to do, common mistakes]                      │
│                                                         │
│ ## Examples                                            │
│ [Code examples with provenance]                        │
│                                                         │
│ ## Related Patterns                                    │
│ [Links to alternative/complementary patterns]          │
└─────────────────────────────────────────────────────────┘
```

### 2. **Navigation & Discovery**

#### Top Navigation Bar
```
┌─────────────────────────────────────────────────────────────┐
│ [Logo] Problem-Solution KB    [Search Box]  [Submit] [Login]│
└─────────────────────────────────────────────────────────────┘
```

#### Sidebar Navigation
```
┌─────────────────┐
│ Navigation      │
│                 │
│ • Main Page     │
│ • Browse        │
│   - Problems    │
│   - Solutions   │
│   - Examples    │
│ • Categories    │
│ • Recent Changes│
│ • Random Entry  │
│                 │
│ Tools           │
│ • What links    │
│   here          │
│ • Related       │
│   changes       │
│ • Special pages │
└─────────────────┘
```

#### Search Interface
- **Prominent search bar** (top center, like Wikipedia)
- **Autocomplete** with suggestions (problems, solutions, tags)
- **Advanced search** with filters:
  - Domain/technology tags
  - Quality status (verified/draft)
  - License type
  - Date range
  - Provenance source

### 3. **Content Sections**

#### Table of Contents (Auto-generated)
- Automatically generated from H2/H3 headings
- Sticky sidebar for long pages
- Jump-to-section links

#### Infobox (Metadata Sidebar)
- **Problem entries**: Domain, scale, constraints, tags, status, version, last updated
- **Solution entries**: Applicability, complexity, trade-offs, related patterns
- **Example entries**: Language, framework, license, provenance link, code snippet preview

#### Code Examples Section
- Syntax-highlighted code blocks
- Language/framework badges
- Copy-to-clipboard button
- Provenance link (GitHub, documentation, etc.)
- License badge
- "View Full Example" link (if truncated)

### 4. **Provenance & Citations**

#### Citation Style
- Inline citations `[1]` `[2]` `[3]`
- References section at bottom:
  ```
  ## References & Provenance
  
  1. ^ [Source Name](URL) - License: MIT - Retrieved: 2025-12-11
  2. ^ [Example Repository](URL) - License: Apache 2.0 - Commit: abc123
  3. ^ [Documentation](URL) - License: CC-BY-SA
  ```

#### Provenance Display
- **Every example** must show:
  - Source URL (clickable)
  - License (badge + text)
  - Last verified date
  - Attribution (if required by license)

#### License Badges
- Visual badges (MIT, Apache 2.0, CC-BY-SA, etc.)
- Color-coded for quick scanning
- Hover tooltip with full license text

### 5. **Version History & Editing**

#### View History Page
- List of all versions (like Wikipedia)
- Compare versions (diff view)
- Revert to previous version (for stewards)
- Version metadata:
  - Timestamp
  - Editor (username or "API")
  - Change summary
  - Quality state at that version

#### Edit Interface
- **Visual editor** (like Wikipedia's VisualEditor) for non-technical users
- **Markdown editor** for technical content
- **Code editor** for code examples
- **Preview** before saving
- **Draft save** (for work-in-progress)
- **Required fields** validation:
  - Problem: title, abstract, context, constraints
  - Solution: summary, applicability, trade-offs
  - Example: code, provenance URL, license

#### Edit Conflict Resolution
- Show conflicts when multiple users edit simultaneously
- Merge interface (like Wikipedia)
- Conflict markers for manual resolution

### 6. **Quality Indicators & Moderation**

#### Quality Badges
- **Verified** (green badge): Steward-reviewed, high quality
- **Draft** (yellow badge): Submitted, pending review
- **Deprecated** (red badge): Outdated, replaced by newer solution
- **Needs Review** (orange badge): Flagged for quality issues

#### Moderation Queue
- **Steward dashboard** showing:
  - Pending submissions
  - Flagged entries
  - Recent changes requiring review
  - Quality metrics

#### Flagging System
- **Flag reasons**:
  - Outdated information
  - License violation
  - Missing provenance
  - Quality issues
  - Duplicate entry
- **Flag workflow**: User flags → Steward reviews → Action taken

### 7. **Related Content & Discovery**

#### "See Also" Section
- Related problems
- Alternative solutions
- Complementary patterns
- Related examples

#### Category/Tag Pages
- Browse by category (like Wikipedia categories)
- Tag clouds
- Filtered views (e.g., "All verified solutions for Python")

#### "What Links Here"
- Show all entries that link to current entry
- Useful for understanding dependencies and relationships

---

## Adaptations for Problem-Solution KB

### Differences from Wikipedia

1. **Structured Data Model**
   - Wikipedia: Free-form articles
   - Our KB: Structured entries (Problem → Solutions → Examples)
   - **Solution**: Use infoboxes and structured sections, but allow flexibility

2. **Code Examples**
   - Wikipedia: Minimal code (usually in examples)
   - Our KB: Code is primary content
   - **Solution**: Syntax-highlighted code blocks with copy buttons, runnable examples (if applicable)

3. **Provenance Requirements**
   - Wikipedia: Citations are important but not always enforced
   - Our KB: Provenance is mandatory
   - **Solution**: Required fields, validation, prominent display

4. **Quality Gates**
   - Wikipedia: Anyone can edit, community moderates
   - Our KB: Submission → Review → Verified workflow
   - **Solution**: Clear quality states, moderation queue, steward approval

5. **API-First Design**
   - Wikipedia: Web-first, API secondary
   - Our KB: Dual-mode (web + API)
   - **Solution**: UI renders API data, API-first architecture

---

## UI Components & Technical Considerations

### Component Library
- **Article Page Component**: Main entry display
- **Infobox Component**: Metadata sidebar
- **Code Block Component**: Syntax-highlighted, copyable code
- **Citation Component**: Inline citations with tooltips
- **References Section**: Bottom-of-page citations
- **Edit Form Component**: Structured editing interface
- **History Viewer**: Version comparison
- **Search Component**: Autocomplete, filters, results
- **Quality Badge Component**: Visual status indicators

### Responsive Design
- **Desktop**: Full Wikipedia-style layout (sidebar + main content)
- **Tablet**: Collapsible sidebar, stacked layout
- **Mobile**: Bottom navigation, simplified infobox, full-width content

### Accessibility
- **WCAG 2.1 AA compliance**
- **Keyboard navigation** (like Wikipedia)
- **Screen reader support**
- **High contrast mode**
- **Focus indicators**

### Performance
- **Lazy loading** for code examples
- **Progressive enhancement** (works without JS)
- **CDN** for static assets
- **Caching** for frequently accessed entries

---

## User Flows

### 1. **Browse & Discover**
```
Home → Browse Categories → Problem Entry → Solution Pattern → Example
                                                              ↓
                                                         Related Problems
```

### 2. **Search**
```
Search Query → Results Page → Entry Page → Related Content
```

### 3. **Submit Entry**
```
Submit Button → Choose Type (Problem/Solution/Example) → Fill Form → 
Preview → Submit → Moderation Queue → Steward Review → Verified
```

### 4. **Edit Entry**
```
Entry Page → Edit Button → Edit Form → Preview → Save Draft/Submit → 
Version Created → History Updated
```

### 5. **Review & Moderate**
```
Steward Dashboard → Moderation Queue → Review Entry → Approve/Reject/Request Changes
```

---

## Design Principles

1. **Familiarity First**: Leverage Wikipedia's familiar patterns
2. **Provenance Prominence**: Make citations and licenses highly visible
3. **Quality Transparency**: Show quality states and review history
4. **Structured Flexibility**: Enforce structure but allow rich content
5. **Mobile-Friendly**: Responsive design for all devices
6. **Accessibility**: WCAG compliance, keyboard navigation
7. **Performance**: Fast load times, efficient rendering

---

## Open Questions & Decisions Needed

1. **Frontend Stack**
   - Vue.js + Codex (Wikipedia's stack) vs React + custom vs Svelte?
   - What are our team's preferences and existing expertise?

2. **Code Examples**
   - Should code blocks be collapsible/expandable?
   - Should we support "run" buttons for certain languages (e.g., Python, JavaScript)?
   - How to handle very long code examples (pagination, lazy loading)?

3. **Editing Experience**
   - Visual editor vs. Markdown editor vs. Both?
   - Should we support collaborative real-time editing (like Google Docs)?
   - How to handle code editing (Monaco editor, CodeMirror, etc.)?

4. **Moderation UI**
   - Should moderation happen inline (like Wikipedia) or in separate dashboard?
   - How to show moderation history to users?
   - What information should be visible to non-stewards?

5. **Search & Discovery**
   - Should we have a "random entry" feature (like Wikipedia)?
   - How to surface related content algorithmically (semantic similarity, tags, etc.)?
   - What search backend (Elasticsearch, Algolia, custom)?

6. **Mobile Experience**
   - Should mobile have a simplified view or full feature parity?
   - How to handle code examples on small screens (horizontal scroll, expandable, etc.)?

7. **API Integration**
   - How should UI consume API (REST vs GraphQL)?
   - Real-time updates (WebSockets, polling, SSE)?
   - Caching strategy (client-side, CDN, service worker)?

---

## Next Steps

1. **Create wireframes** for key pages (Problem entry, Solution entry, Search)
2. **Design component library** (infobox, code blocks, citations)
3. **Prototype** key user flows (browse, search, submit, edit)
4. **User testing** with target users (developers, architects, agents)
5. **Iterate** based on feedback

---

## Technical Stack Recommendations

### Option A: Vue.js + Codex (Wikipedia's New Stack)
- **Frontend**: Vue.js 3 + Codex components
- **Backend**: API-first (REST/GraphQL) - language agnostic
- **Pros**: Use Wikipedia's actual UI framework, proven patterns, accessibility built-in
- **Cons**: Commits to Vue.js ecosystem

### Option B: React + Custom Components (Inspired by Patterns)
- **Frontend**: React + shadcn/ui or Chakra UI
- **Backend**: API-first (REST/GraphQL)
- **Pros**: Popular stack, full control, can adopt functional patterns
- **Cons**: Need to build accessibility features ourselves

### Option C: SvelteKit + Custom Components
- **Frontend**: SvelteKit
- **Backend**: API-first (REST/GraphQL)
- **Pros**: Modern, performant, lightweight
- **Cons**: Smaller ecosystem, less mature

### Recommendation: **Option B (React)** or **Option A (Vue + Codex)**
- **If we want Wikipedia's proven components**: Choose Vue + Codex
- **If we want flexibility and popular stack**: Choose React + custom components inspired by Wikipedia patterns

---

## Key Takeaways

1. **Wikipedia uses open-source frameworks**: MediaWiki (PHP), OOUI (JS), Codex (Vue.js)
2. **Focus on functional patterns, not aesthetics**: Information architecture, navigation, editing workflow
3. **Accessibility is non-negotiable**: WCAG 2.1 AA compliance, keyboard navigation
4. **API-first architecture**: UI is a client of our API, not tightly coupled to backend
5. **Framework choice**: Can use Codex (Vue) or build custom (React/Svelte) with same patterns

---

## References

- **MediaWiki**: https://www.mediawiki.org/
- **Codex Design System**: https://www.mediawiki.org/wiki/Design_Systems_Team/Codex
- **OOUI Framework**: https://www.mediawiki.org/wiki/OOUI
- **Wikipedia UI/UX patterns**: https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style
- **MediaWiki interface**: https://www.mediawiki.org/wiki/Manual:Interface
- **Citation styles**: https://en.wikipedia.org/wiki/Wikipedia:Citing_sources
- **Wikipedia's design principles**: https://www.mediawiki.org/wiki/Design

### Code Repositories
- **MediaWiki**: https://github.com/wikimedia/mediawiki
- **Codex**: https://github.com/wikimedia/mediawiki-codex
- **OOUI**: https://github.com/wikimedia/oojs-ui

---

## Next Steps

1. **Decide on frontend stack** (Vue + Codex vs React + custom vs Svelte)
2. **Review Codex components** (if choosing Vue) to see what we can reuse
3. **Design component library** based on functional patterns (infobox, citations, version history)
4. **Create wireframes** focusing on information architecture (not visual design)
5. **Prototype** key user flows (browse, search, submit, edit)

---

**Discussion Notes:**
- [Add notes from team discussion here]
- [Add decisions made]
- [Add follow-up actions]

