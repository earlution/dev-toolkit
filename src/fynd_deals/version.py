VERSION_RC = 0        # Release candidate (0 = development)
VERSION_EPIC = 4      # Epic number (Epic 4: Kanban Framework)
VERSION_STORY = 1     # Story number (Story 1: Dev Kit Kanban Implementation)
VERSION_TASK = 1      # Task number (Task 1: Review existing dev-kit Kanban policies and templates)
VERSION_BUILD = 1     # Build number (bumped by RW)

# Composite version string using RC.EPIC.STORY.TASK+BUILD schema
VERSION_STRING = f"{VERSION_RC}.{VERSION_EPIC}.{VERSION_STORY}.{VERSION_TASK}+{VERSION_BUILD}"


