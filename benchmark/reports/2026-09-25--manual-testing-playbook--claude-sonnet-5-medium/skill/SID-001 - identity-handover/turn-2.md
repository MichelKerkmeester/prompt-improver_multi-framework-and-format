Saved: `export/002 - enhanced-gym-app-onboarding-welcome-email-prompt.md`

CLEAR 45/50 | Gate: passed | Energy: Standard | Framework: COSTAR

**What changed:**
- **Context:** The prompt now says the email is one step in your app's onboarding flow, sent right after someone joins. It adds an `[APP_NAME]` placeholder and a line explaining why that first message matters.
- **Placeholders:** The trial and schedule placeholders now ask where each lives in the app, for example how to activate the trial or where to find the schedule.
- **Guardrails:** The AI is told not to invent app features, and the 120-word limit still covers the whole email.

**Assumptions:**
- [Assumes: the email goes out right after sign-up, as the first onboarding message]
- [Assumes: it stays an email, not an in-app or push message]
- [Assumes: the trial and schedule can be reached through the app, but I left the details as placeholders because I don't know your features]

If you want a different channel, such as a push notification or in-app card, tell me and I'll rework it for that.