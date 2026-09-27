**Saved:** `export/001 - enhanced-hybrid-work-policy-announcement-prompt.yaml`

CLEAR 44/50 | Gate: passed | Framework: COSTAR | Perspectives: 4 (Prompt Engineering, AI Interpretation, End-User Experience, Framework Architecture)

The prompt locks the HR assistant to only the four confirmed policy facts (1 March Tue/Thu office days, two exceptions per quarter via team lead, flat €60/month allowance, no other confirmed changes), and structures the three required outputs — ~300-word announcement, exactly six-question FAQ, two-line Slack teaser — with explicit must-include/must-not-include lists so it can't promise beyond the policy text or slip into corporate spin.

`[Assumes: "1 March" is the next upcoming date — confirm exact year; warehouse crew keep the flat allowance despite already being on-site full time; exceptions run through the existing team-lead conversation, no new tool]` — three placeholders (`${COMPANY_NAME}`, `${HR_CONTACT_CHANNEL}`, `${INTRANET_ANNOUNCEMENT_LINK}`) are left for you to fill in before use.