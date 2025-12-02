VERSION_RC = 0        # Release candidate (0 = development)
VERSION_EPIC = 1      # Epic number (Epic 1: Vibe Dev Kit Core)
VERSION_STORY = 1     # Story number (Story 1: Initial Epic Structure & Versioning Policy)
VERSION_TASK = 1      # Task number (Task 1: Create Epic 1-4 docs and dev-kit versioning policy)
VERSION_BUILD = 1     # Build number (bumped by RW)

# Composite version string using RC.EPIC.STORY.TASK+BUILD schema
VERSION_STRING = f"{VERSION_RC}.{VERSION_EPIC}.{VERSION_STORY}.{VERSION_TASK}+{VERSION_BUILD}"


