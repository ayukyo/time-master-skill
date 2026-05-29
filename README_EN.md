# LiuYage.skill - HaiWang Mode - Time Master

> Multi-context parallel automation Skill for OpenClaw

---

## Origin Story

This skill is inspired by a real social incident — the **"Luoyang Queen of Polyamory"** (Liu Yage) case.

> Liu Yage, a law school graduate from a university in Wuhan, working in Luoyang's public sector, maintained simultaneous romantic/engagement relationships with **three men for over two years** — achieving:
> - Three parallel timelines with **zero overlap or collision**
> - Each partner unaware of the others (**perfect context isolation**)
> - Weekdays with Partner-A, weekends with B/C (**time-slice scheduling**)
> - Custom persona and vocabulary for each partner (**template×variable output**)
> - On-demand context switching when anyone checks in (**priority scheduling**)
> - A holiday perfectly partitioned among three people (**conflict detection**)
> - Even her mother was aware and coordinated (**supervisor mode**)

Morality aside, the operational pattern — **multi-line parallelism, context isolation, zero-conflict switching** — is exactly what AI automation needs for multi-task scheduling.

---

## Capabilities

| Yage's Move | OpenClaw Automation |
|-------------|---------------------|
| Two WeChat accounts isolating three relationships | Multi-account login with fully isolated contexts |
| Weekdays with one partner, weekends with the other two | Time-sliced task scheduling |
| All three in the same city | Collocate similar tasks to reduce switching cost |
| Custom talk tracks per partner | Same data -> template×variable multi-format output |
| Whoever checks in first gets priority | Interrupt handling: snapshot -> handle -> restore |
| Holiday split into segments for each | Cron job conflict detection and rebalancing |
| "Feeling down / in a meeting" excuses | Graceful fallback on task blockage |
| Timeline reconstructed afterward | Full audit trail with second-level precision |
| Mom knew everything | Supervisor agent monitoring sub-agents |

---

## Core Concepts

### Context Isolation (Two-WeChat Mode)

```
[Session-A: Partner A]
  Main account | Weekday mode
  -> House buying talk, meeting parents

[Session-B: Partner B]
  Secondary account | Weekend mode
  -> Daily life, cohabitation

[Session-C: Partner C]
  Main account | Weekend + Holiday mode
  -> Engagement, betrothal gifts, apartment hunting
```

In OpenClaw: Each context maintains independent state, credentials, and session info. Switching to Context-B never leaks data from Context-A.

### Time-Slice Scheduling (Weekday/Weekend Mode)

```
Mon-Fri (Workdays):  Partner A (living together)
Sat-Sun (Weekends):  Partner B (hometown) + Partner C (another place)

Holiday masterpiece:
  Days 1-3 -- Partner B (trip)
  Days 4-6 -- Partner C (meet parents + trip)
  Days 7-9 -- Partner A (workdays + short trip)
```

In OpenClaw: Tasks assigned to fixed time slices with forced snapshot/restore between slices.

### Priority Interrupt Handling

```
Scenario: Partner A calls unexpectedly
  1. Hang up on B's call (snapshot current context)
  2. Switch to "Partner A mode" (tone, environment)
  3. Say "feeling down, just got out of shower" (blocking excuse)
  4. Pacify (task complete)
  5. Resume Partner B (restore context)
```

In OpenClaw: High-priority task arrives -> snapshot -> handle -> restore seamlessly.

### Conflict Detection

```
Input:
  Partner-A: Days 1-3 trip
  Partner-B: Days 4-6 trip
  Partner-C: Days 7-9 trip + outing

Output:
  [OK] No overlap!
  [WARN] Day 7 is a workday but also with C
      Suggest taking annual leave
```

In OpenClaw: Cron jobs auto-check for time overlap and suggest rebalancing.

---

## Usage Examples

### Example 1: Multi-Channel Notification

```
User: Send this notice to 3 channels using time-master mode

[Context-A: WeChat Work] -> Formal notice @everyone
[Context-B: DingTalk]    -> Group announcement with progress table
[Context-C: Email]       -> Full email with attachments
────────────────────────────────
Time-slice:
  |- 09:00 WeChat Work (priority channel first)
  |- 09:15 DingTalk (copy + format adapt)
  └─ 09:30 Email (needs attachment, standalone)
────────────────────────────────
Summary:
  [OK] WeChat -> sent, 3 read receipts
  [OK] DingTalk -> sent, pinned to group
  [OK] Email -> sent, 12 recipients
```

### Example 2: Multi-Project Status Report

```
User: Generate weekly reports for Project A, B, C simultaneously

[Context-A: Project Alpha] -> v2.1 80% done, no risks
[Context-B: Project Beta]  -> perf optimization 60%, blocked: QA env
[Context-C: Project Gamma] -> refactoring 30%, risk: understaffed
────────────────────────────────
Template×Variable:
  "This week {project} {progress}, risks: {risks}, next: {plan}"
────────────────────────────────
Summary:
  [OK] Alpha -> 80%, next: QA handover
  [WAIT] Beta  -> blocked (Plan-B: run unit tests meanwhile)
  [OK] Gamma -> 30%, reinforcement requested
```

### Example 3: Cron Conflict Detection

```
User: Schedule this week's cron jobs
  Job 1: Daily 9:00 DB backup (~20min)
  Job 2: Daily 9:00 report generation (~10min)
  Job 3: Tue 9:30 weekly standup reminder

[WARN] 9:00-9:20 backup overlaps report!
  Suggest: backup -> 8:30, report -> 9:30
[WARN] Tue 9:30 standup conflicts with rescheduled report!
  Suggest: Tue report -> 10:00
```

---

## File Structure

```
time-master-skill/
├── SKILL.md          # Core skill definition (OpenClaw entry)
├── README.md         # Chinese documentation
├── README_EN.md      # English documentation (this file)
└── scripts/
    └── conflict-detector.py  # Conflict detection script
```

## Installation

```bash
# Method 1: Symlink into OpenClaw skills directory
ln -s /path/to/time-master-skill ~/.openclaw/skills/time-master

# Method 2: Copy
cp -r /path/to/time-master-skill ~/.openclaw/skills/time-master

# Verify
openclaw skills list | grep time-master
```

## Disclaimer

- The skill name and case references are drawn from publicly available social incident materials
- **For technical demonstration and entertainment purposes only** — no judgment is made on any real person's moral character
- The case mapping is purely to help illustrate abstract concepts; any resemblance is incidental
- Use responsibly and within legal boundaries

---

> Remember: Technology is neutral. Yage used it to date three guys — you can use it to manage three projects. Stay classy.
