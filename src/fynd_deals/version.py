VERSION_RC = 0        # Release candidate (0 = development)
VERSION_EPIC = 3      # Epic number (Epic 3: Numbering & Versioning Framework)
VERSION_STORY = 1     # Story number (Story 1: Dev Kit Alignment with Versioning Framework)
VERSION_TASK = 2      # Task number (Task 2: Ingest versioning findings from fynd.deals Epic 15 work)
VERSION_BUILD = 1     # Build number (bumped by RW)

# Composite version string using RC.EPIC.STORY.TASK+BUILD schema
VERSION_STRING = f"{VERSION_RC}.{VERSION_EPIC}.{VERSION_STORY}.{VERSION_TASK}+{VERSION_BUILD}"


