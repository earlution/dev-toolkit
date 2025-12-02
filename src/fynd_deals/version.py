VERSION_RC = 0        # Release candidate (0 = development)
VERSION_EPIC = 3      # Epic number (Epic 3: Numbering & Versioning Framework)
VERSION_STORY = 1     # Story number (Story 1: Dev Kit Alignment with Versioning Framework)
VERSION_TASK = 3      # Task number (Task 3: Update dev-kit versioning policy as canonical SoT)
VERSION_BUILD = 1     # Build number (bumped by RW)

# Composite version string using RC.EPIC.STORY.TASK+BUILD schema
VERSION_STRING = f"{VERSION_RC}.{VERSION_EPIC}.{VERSION_STORY}.{VERSION_TASK}+{VERSION_BUILD}"


