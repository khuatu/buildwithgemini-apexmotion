# My agent: Calisthenics & Sport Strength Coach (ApexMotion)
One-liner: A conversational coach that helps athletes, calisthenics practitioners, and sport enthusiasts (climbing, volleyball, bulking, leaning) build custom training plans, log workouts with muscle-specific RPE exhaustion tracking, and dynamically compute next-day training splits and accessory routines.

Tool coverage:
- Memory: User profile (fitness goal e.g. climbing/volleyball/bulking/leaning, target calisthenics skills like planche/front lever/v-sit, historical PRs/hold times, injury history, fatigue recovery rates, accessory preferences like yoga/stretching/abs).
- Tools: Log workout sets with RPE, calculate muscle recovery status (chest, anterior/lateral/rear delts, lats, biceps, triceps, lower back, core, quads, hamstrings/glutes), query available workouts/exercises filtered by fresh muscle groups, generate next-day routine recommendations.
- Catalog/UI: Exercise & skill library (push/pull/legs splits, planche progressions, front/back lever, v-sit, and cooldown accessories like yoga/stretching/abs/handstand practice) rendered as structured A2UI cards and readiness tables.
- Image gen: Infographics and visual cues of exercise technique, posture checks (e.g. scapular protraction in planche, hollow body positioning, lever alignment), or motivation milestone art.
- Sandbox: Mathematical recovery decay model calculating residual fatigue from session volume * RPE to optimize the next day's training split.

Recommended for every project: memory, storage, tools, image generation, A2UI
Agent-specific / stretch (pick what fits): code sandbox for recovery decay algorithms & muscle fatigue scoring, Cloud Trace for tool execution observability.
