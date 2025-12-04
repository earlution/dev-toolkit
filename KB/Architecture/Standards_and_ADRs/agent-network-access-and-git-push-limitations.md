---
lifecycle: evergreen
ttl_days: null
created_at: 2025-12-04T12:10:00Z
expires_at: null
housekeeping_policy: keep
---

# Agent Network Access and Git Push Limitations

**Version:** 1.0.0  
**Last Updated:** 2025-12-04  
**Status:** Active  
**Related:** [Release Workflow Agent Execution](../../../packages/frameworks/workflow%20mgt/KB/Documentation/Developer_Docs/vwmp/release-workflow-agent-execution.md) | [Workflow Hardening Guide](./workflow-hardening-guide.md)

---

## 📋 Overview

AI agents executing workflows (particularly the Release Workflow) may encounter network access limitations in sandbox environments that prevent direct `git push` operations. This document describes the issue, its impact, and recommended solutions.

**Problem Statement:**
- Agents cannot push to remote repositories due to sandbox network restrictions
- Release Workflow (RW) Step 11 (Push to Remote) fails or requires manual intervention
- This breaks the automated workflow pattern and requires user action

**Impact:**
- Workflow automation is incomplete
- User must manually execute `git push origin main --tags` after each release
- Breaks the "hands-off" agent-driven workflow pattern
- Creates friction in the release process

---

## 🎯 Problem Description

### Current Behavior

When executing Release Workflow Step 11 (Push to Remote), agents encounter:

```
Error: Network access restricted in sandbox environment
Error: Cannot push to remote repository
```

**Workaround:** User must manually execute:
```bash
git push origin main --tags
```

### Root Cause

Sandbox environments (like Cursor's AI agent execution environment) often have:
- **Network restrictions** for security reasons
- **Limited outbound connectivity** to prevent unauthorized access
- **Git credential limitations** preventing authentication
- **Firewall rules** blocking git protocol ports

---

## 🔧 Solutions and Workarounds

### Solution 1: Environment Configuration (Recommended)

**Approach:** Configure the sandbox/execution environment to allow git push operations.

**Steps:**

1. **Check Network Access:**
   ```bash
   # Test connectivity to git remote
   git ls-remote origin
   ```

2. **Configure Git Credentials:**
   ```bash
   # Use credential helper or SSH keys
   git config --global credential.helper store
   # OR
   git config --global credential.helper cache
   ```

3. **Use SSH Instead of HTTPS:**
   ```bash
   # Change remote URL to SSH
   git remote set-url origin git@github.com:user/repo.git
   ```

4. **Configure SSH Keys:**
   ```bash
   # Generate SSH key if needed
   ssh-keygen -t ed25519 -C "agent@vibe-dev-kit"
   # Add to SSH agent
   eval "$(ssh-agent -s)"
   ssh-add ~/.ssh/id_ed25519
   ```

5. **Test Push:**
   ```bash
   git push origin main --tags --dry-run
   ```

**Pros:**
- ✅ Enables full automation
- ✅ No manual intervention required
- ✅ Maintains workflow integrity

**Cons:**
- ❌ Requires environment configuration
- ❌ May require security policy changes
- ❌ SSH key management overhead

---

### Solution 2: Workflow Adaptation (Current Approach)

**Approach:** Adapt the Release Workflow to handle push failures gracefully and provide clear instructions.

**Implementation:**

Update RW Step 11 to:
1. Attempt push operation
2. Catch network/authentication errors
3. Provide clear user instructions if push fails
4. Mark workflow as "complete pending push"

**Example RW Step 11 Update:**

```python
# Step 11: Push to Remote
try:
    subprocess.run(['git', 'push', 'origin', 'main', '--tags'], check=True)
    print("✅ Successfully pushed to remote")
except subprocess.CalledProcessError as e:
    print("⚠️  Push failed due to network/authentication restrictions")
    print("\n📋 Manual Push Required:")
    print("   Please run the following command locally:")
    print("   git push origin main --tags")
    print("\n   This is a known limitation in sandbox environments.")
    print("   See: KB/Architecture/Standards_and_ADRs/agent-network-access-and-git-push-limitations.md")
    # Don't fail the workflow - mark as complete pending push
    return "complete_pending_push"
```

**Pros:**
- ✅ Works in restricted environments
- ✅ Provides clear user guidance
- ✅ Doesn't break workflow execution

**Cons:**
- ❌ Requires manual user action
- ❌ Not fully automated
- ❌ Creates workflow friction

---

### Solution 3: Post-Release Hook Pattern

**Approach:** Create a post-release hook that can be executed locally or in CI/CD.

**Implementation:**

1. **Create Post-Release Script:**
   ```bash
   # scripts/post-release-push.sh
   #!/bin/bash
   # Post-release push hook
   
   LATEST_TAG=$(git describe --tags --abbrev=0)
   echo "Pushing release $LATEST_TAG..."
   
   git push origin main --tags
   echo "✅ Release pushed successfully"
   ```

2. **Update RW to Generate Hook:**
   ```python
   # After Step 10 (Create Git Tag)
   hook_script = f"""#!/bin/bash
   # Auto-generated post-release push hook
   # Created: {datetime.now()}
   # Release: {version_string}
   
   git push origin main --tags
   """
   
   Path("scripts/post-release-push.sh").write_text(hook_script)
   Path("scripts/post-release-push.sh").chmod(0o755)
   ```

3. **User Executes Hook:**
   ```bash
   ./scripts/post-release-push.sh
   ```

**Pros:**
- ✅ Separates release from push
- ✅ Can be automated in CI/CD
- ✅ Provides audit trail

**Cons:**
- ❌ Still requires separate execution
- ❌ Additional script management

---

### Solution 4: CI/CD Integration

**Approach:** Move push operation to CI/CD pipeline triggered by release commit.

**Implementation:**

1. **RW Creates Release Commit (No Push):**
   ```python
   # Step 9: Commit Changes
   subprocess.run(['git', 'commit', '-m', commit_message], check=True)
   # Step 10: Create Git Tag
   subprocess.run(['git', 'tag', '-a', tag, '-m', tag_message], check=True)
   # Step 11: Skip push (will be done by CI/CD)
   ```

2. **CI/CD Pipeline Pushes:**
   ```yaml
   # .github/workflows/release-push.yml
   name: Release Push
   on:
     push:
       branches: [main]
       tags: ['v*']
   
   jobs:
     push-release:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         - name: Push tags
           run: git push origin main --tags
   ```

**Pros:**
- ✅ Full automation in CI/CD
- ✅ No sandbox restrictions
- ✅ Centralized push control

**Cons:**
- ❌ Requires CI/CD setup
- ❌ Additional infrastructure
- ❌ Delayed push (until CI runs)

---

## 📊 Comparison of Solutions

| Solution | Automation Level | Setup Complexity | User Friction | Recommended For |
|-----------|------------------|------------------|---------------|-----------------|
| **Environment Config** | ✅ Full | Medium | None | Production environments |
| **Workflow Adaptation** | ⚠️ Partial | Low | Low | Sandbox/development |
| **Post-Release Hook** | ⚠️ Partial | Low | Medium | Hybrid workflows |
| **CI/CD Integration** | ✅ Full | High | None | CI/CD-enabled projects |

---

## 🎯 Recommended Approach

### For Development/Sandbox Environments

**Use Solution 2 (Workflow Adaptation):**
- Update RW Step 11 to handle push failures gracefully
- Provide clear user instructions
- Document the limitation
- Don't fail the workflow

### For Production Environments

**Use Solution 1 (Environment Configuration):**
- Configure SSH keys or credential helpers
- Enable network access for git operations
- Test push operations
- Achieve full automation

### For CI/CD-Enabled Projects

**Use Solution 4 (CI/CD Integration):**
- Move push to CI/CD pipeline
- RW creates commit and tag locally
- CI/CD handles push automatically
- Best separation of concerns

---

## 🔄 Workflow Updates Required

### Release Workflow Step 11 Update

Update `packages/frameworks/workflow mgt/KB/Documentation/Developer_Docs/vwmp/release-workflow-agent-execution.md`:

```markdown
### Step 11: Push to Remote

**Objective:** Push committed changes and tags to remote repository.

**Agent Execution:**

1. **Attempt Push:**
   ```python
   try:
       subprocess.run(['git', 'push', 'origin', 'main', '--tags'], check=True)
       print("✅ Successfully pushed to remote")
   except subprocess.CalledProcessError as e:
       # Handle network/authentication errors
       print("⚠️  Push failed - see manual push instructions below")
   ```

2. **Handle Push Failures:**
   - If push fails due to network restrictions:
     - Print clear user instructions
     - Provide exact command to run
     - Link to this document
     - Mark workflow as "complete pending push"
   - Don't fail the entire workflow

3. **User Instructions (if push fails):**
   ```markdown
   📋 Manual Push Required:
   
   Due to sandbox environment network restrictions, please run:
   
   ```bash
   git push origin main --tags
   ```
   
   See: KB/Architecture/Standards_and_ADRs/agent-network-access-and-git-push-limitations.md
   ```

**Validation:**
- ✅ Push succeeds OR clear instructions provided
- ✅ Workflow completes successfully
- ✅ User knows what action is required
```

---

## 📝 Agent Requirements

Agents executing Release Workflow **MUST**:

1. **Attempt push operation** (don't skip it)
2. **Handle push failures gracefully** (catch exceptions)
3. **Provide clear user instructions** if push fails
4. **Link to this document** for context
5. **Don't fail the workflow** if push fails (mark as "complete pending push")

**Agent Rule:**
```markdown
When executing RW Step 11:
- Always attempt git push
- If push fails, provide user instructions
- Link to agent-network-access-and-git-push-limitations.md
- Mark workflow as complete (pending push)
- Never fail the workflow due to push restrictions
```

---

## 🔗 Related Documents

- **Release Workflow Agent Execution:** [`packages/frameworks/workflow mgt/KB/Documentation/Developer_Docs/vwmp/release-workflow-agent-execution.md`](../../../packages/frameworks/workflow%20mgt/KB/Documentation/Developer_Docs/vwmp/release-workflow-agent-execution.md)
- **Workflow Hardening Guide:** [`workflow-hardening-guide.md`](./workflow-hardening-guide.md)
- **Release Workflow Reference:** [`packages/frameworks/workflow mgt/KB/Documentation/Developer_Docs/vwmp/release-workflow-reference.md`](../../../packages/frameworks/workflow%20mgt/KB/Documentation/Developer_Docs/vwmp/release-workflow-reference.md)

---

## 📚 References

- **Git Credential Helpers:** https://git-scm.com/docs/git-credential
- **SSH Keys for Git:** https://docs.github.com/en/authentication/connecting-to-github-with-ssh
- **CI/CD Integration:** https://docs.github.com/en/actions

---

## 🎯 Success Criteria

**This issue is resolved when:**

1. ✅ Agents can push to remote OR provide clear instructions
2. ✅ Workflow doesn't fail due to push restrictions
3. ✅ Users understand why manual push is needed
4. ✅ Documentation exists for all solutions
5. ✅ Workflow adaptation implemented (Solution 2)

---

**Last Updated:** 2025-12-04  
**Status:** Active — Issue documented, solutions provided

