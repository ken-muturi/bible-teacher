// Bible Teacher — plugin build / validation pipeline (fan-out → fan-in).
//
// Run from Claude Code with:  Workflow({ name: 'build-plugin' })
//
// Fan-out: one researcher validates each skill in parallel (frontmatter,
// trigger uniqueness, argument-hint, prerequisites, portable references).
// Barrier. Fan-in: a coordinator builds the dependency/order graph, detects
// trigger collisions, and runs `claude plugin validate` as the release gate.
// Read-only except for the validate commands — it reports, it does not ship.
//
// Paths are relative to the repo root (the project cwd), so it is portable
// across clones.

export const meta = {
  name: 'build-plugin',
  description: 'Validate & prep the Bible Teacher plugin: a researcher validates each skill in parallel (fan-out), then a coordinator builds the dependency graph, detects trigger conflicts, and runs the validate gate (fan-in)',
  phases: [
    { title: 'Prepare', detail: 'one Sonnet researcher per skill' },
    { title: 'Synthesize', detail: 'dependency graph + conflicts + validate gate (Opus)' },
  ],
}

const SKILLS = ['teacher-foundation','passage-study','book-overview','book-overview-infographic','discussion-guide','bible-timeline','video-outline']

const PREP_SCHEMA = {
  type: 'object',
  properties: {
    skill: { type: 'string' },
    hasFrontmatter: { type: 'boolean' },
    name: { type: 'string' },
    description: { type: 'string' },
    argumentHint: { type: 'string' },
    trigger: { type: 'string' },
    prerequisites: { type: 'array', items: { type: 'string' } },
    issues: { type: 'array', items: { type: 'string' } },
    ok: { type: 'boolean' },
  },
  required: ['skill','hasFrontmatter','trigger','prerequisites','issues','ok'],
}

const RELEASE_SCHEMA = {
  type: 'object',
  properties: {
    ready: { type: 'boolean' },
    validatePassed: { type: 'boolean' },
    dependencyOrder: { type: 'array', items: { type: 'string' } },
    conflicts: { type: 'array', items: { type: 'string' } },
    blocking: { type: 'array', items: { type: 'string' } },
    warnings: { type: 'array', items: { type: 'string' } },
    bundleInSync: { type: 'boolean' },
    summary: { type: 'string' },
  },
  required: ['ready','validatePassed','blocking','warnings','summary'],
}

phase('Prepare')
const reports = (await parallel(SKILLS.map((s) => () =>
  agent(
    'Read plugins/bible-teacher/skills/' + s + '/SKILL.md and validate it as a Claude Code plugin skill. Return structured data: hasFrontmatter (true if there is a YAML --- block with at least name and description); the name; the description; the argument-hint (or "" if none); the exact trigger phrase the description tells the user to type (e.g. "book-overview <Book>" or "passage-study <reference>"); prerequisites = any skills it names under "Prerequisite"; and issues[] listing problems (missing frontmatter; description longer than ~1024 characters; missing argument-hint; internal/relative file references that would break outside the repo; a documented trigger phrase identical to another skill\'s). Set ok=true only if there are no blocking issues. Set skill="' + s + '". Read-only — do not modify anything.',
    { label: 'check:' + s, phase: 'Prepare', model: 'sonnet', agentType: 'general-purpose', schema: PREP_SCHEMA }
  )
))).filter(Boolean)

phase('Synthesize')
const verdict = await agent(
  'You are the release coordinator for the Bible Teacher Claude Code plugin (repo root is the current working directory). Below are per-skill validation reports as JSON:\n\n' + JSON.stringify(reports, null, 2) + '\n\nProduce the structured release verdict:\n1. dependencyOrder = a topological order of the skills from their declared prerequisites (teacher-foundation first; book-overview before book-overview-infographic and before video-outline).\n2. conflicts[] = any case where two skills document the SAME trigger phrase (report the phrase and the two skill names).\n3. Run these two commands with Bash and read their output: `claude plugin validate .` and `claude plugin validate ./plugins/bible-teacher`. Set validatePassed = true only if both succeed; put any validation errors into blocking[].\n4. Check that mobile/bible-teacher-project.md exists and mentions each of: teacher-foundation, passage-study, book-overview-infographic, discussion-guide, bible-timeline. Set bundleInSync accordingly; note any missing ones in warnings[].\n5. blocking[] = anything that MUST be fixed before release (failed validate, malformed skill, an unresolved trigger collision). warnings[] = non-blocking observations. ready = (blocking is empty) AND validatePassed. Write a one-paragraph summary. Read-only except for running the validate commands.',
  { label: 'coordinator', phase: 'Synthesize', agentType: 'general-purpose', schema: RELEASE_SCHEMA }
)

log('Release ready: ' + verdict.ready + ' · validate passed: ' + verdict.validatePassed + ' · blocking: ' + (verdict.blocking || []).length + ' · conflicts: ' + (verdict.conflicts || []).length)
return verdict
