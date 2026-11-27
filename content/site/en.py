"""Site copy in en. Read by scripts/build.py."""

SUPPORT = """# Support

Have a question or something isn't working? Write to us at **{{EMAIL}}** and we'll reply as soon as we can, usually within two business days. If it's about your subscription, include the anonymous ID shown in the app under Settings › Support, so we can find the right record.

## Subscription

### Cancel your subscription
Open iOS Settings › [your name] › Subscriptions, choose Nodly and tap Cancel Subscription. You can also get there from Settings › Manage Subscription in the app. You keep access until the end of the current period.

### Restore your purchases
On a new device or after reinstalling, sign in with the same Apple Account and tap Restore Purchases on the subscription screen in the app.

### Ask for a refund
Purchases are made through Apple, so refunds are handled by Apple. Request one at [reportaproblem.apple.com](https://reportaproblem.apple.com).

## Frequently asked questions

### Which AirPods work with Nodly?
Nodly needs AirPods with motion sensors: AirPods Pro, AirPods Max and AirPods (3rd generation) or later. When you start an exercise, the app checks whether your connected headphones are supported and tells you if they aren't.

### Can I use Nodly without AirPods?
Yes. Neck exercises can run on a timer without AirPods; Nodly then guides the pace but doesn't measure your movement. Breathing exercises, the eye break and the under-desk exercises never need AirPods.

### Where is my data, and how do I delete it?
Motion data is processed on your device and never leaves it. To delete your exercise history, go to Settings › Delete session history in the app. Deleting the app removes the rest; to delete the iCloud copy too, go to iOS Settings › [your name] › iCloud › Manage Account Storage › Nodly. More in the [Privacy Policy](../privacy/).

### Is Nodly a medical app?
No. Nodly is a wellness app, not a medical device. If you have a neck condition, check with a health professional before you start. See [Health & safety](../health/).
"""

T = dict(
    lang="en", lang_label="Language",
    title="Nodly: short breaks for your neck, posture and the rest of you",
    description="Short exercises for your neck, breath, eyes, hands, legs and desk yoga. With your AirPods, Nodly measures your neck moves and reminds you when your head stays down. Motion data stays on your device.",
    h1="Gentle breaks for your desk days.",
    lead="Short exercises for your neck, breath, eyes, hands and legs, and desk yoga. With your AirPods, Nodly measures your neck moves, follows your posture and lets you know when your head stays down too long.",
    cta="Download on the App Store", note="For iPhone and iPad · With compatible AirPods, or without",
    nav_links=[("areas", "Exercises"), ("measure", "How it works"), ("posture", "Posture Check"), ("progress", "Progress")],
    gauge=dict(side_r="Right", side_l="Left", back="Back to center", reached="Target reached"),
    screen_alt="Nodly's exercise screen: a turn to the right measured at 51°, rep 1 of 5",
    chips=["Neck", "Posture", "Breathing", "Eye break"],
    areas_e="Not just your neck", areas_h="Six areas, a few minutes each.",
    areas=[("neck", "Neck", "Turns, side tilts, looking down and up, chin tucks. AirPods measure the angle and count reps; without them, Nodly paces you on a timer."),
           ("breath", "Breathing", "Long exhale, box breathing and even breathing, for 1, 2 or 3 minutes, paced by a drawing and a soft tap."),
           ("eyes", "Eyes", "A two-minute break away from the screen: look far away, blink slowly, then rest with your eyes closed."),
           ("hands", "Hands and wrists", "Wrist stretches, wrist circles and opening and closing your hands, for days spent on a keyboard and mouse."),
           ("legs", "Under the desk", "Heel raises, toe raises, knee extensions and seated marching, without leaving your chair."),
           ("yoga", "Desk yoga", "Seated cat-cow, side bend and twist, plus shoulder moves to loosen up between meetings.")],
    areas_note="Only neck tracking uses AirPods. Everything else works without them.",
    measure_e="Measured with your AirPods", measure_h="Nodly tells you when you're there.",
    measure_p="The motion sensors in your earbuds follow your head angle. When you reach the target range, Nodly lets you know with a sound and a tap and counts the rep for you. Targets adapt to your own range of motion.",
    demo_label="Try it: turn your head", demo_hint="Drag to the right until you reach the green range, then come back to center.",
    demo_reps="Reps",
    how=[("Put in your AirPods", "Nodly uses the motion sensors in your earbuds. No camera, no extra device."),
         ("Save your starting point", "Look straight ahead and hold still for a few seconds. Nodly takes this as 0°."),
         ("Move slowly", "When you reach the target range, Nodly lets you know with a sound and a tap, and counts the rep for you.")],
    posture_e="Posture Check", posture_h="A gentle reminder when your head drops.",
    posture=[("desk", "At the desk", "Follows your head while you work, for 30 minutes up to 2 hours, or in Pomodoro rounds of 25 minutes' work and 5 minutes' rest."),
             ("workout", "During a workout", "If your head drops during standing exercises, Nodly lets you know within seconds. For exercises done lying down, just pause it."),
             ("lock", "On the Lock Screen", "Lock your phone and keep working. You see the time left on the Lock Screen and pause or end from there."),
             ("quick", "Start it your way", "With Siri, from Control Center, or with a Focus automation in Shortcuts.")],
    siri="“Start posture check with Nodly”",
    toast="Just lift your gaze straight ahead.",
    today_alt="Nodly's Today screen with Posture Check: At the desk and Working out",
    pomodoro_alt="Posture Check running in Pomodoro mode: 24:58 left in round 1 of 4, your head is upright",
    routines_e="Routines", routines_h="Ready-made routines, or your own order.",
    routines_p="Start with a ready-made routine like Day Opener or Screen Break, or pick moves from the library and put them in your own order. For you on the Today screen suggests one that suits your day and your busiest hours.",
    routine_name="Quick Break", routine_meta="4 exercises · 6 min",
    routine_steps=[("breath", "Long exhale"), ("neck", "Turn Left & Right"), ("neck", "Chin tucks"), ("legs", "Heel raises")],
    suggest=["Day Opener", "Screen Break", "Wrist Break", "Desk Yoga", "Day's End"],
    progress_e="Progress", progress_h="Small steps you can see adding up.",
    progress_p="Your streak, your week, and how your time splits across your neck, breath, eyes, hands and legs, at a glance. And as you practise, a little 3D desk tidies itself up.",
    streak="day streak", week=["M", "T", "W", "T", "F", "S", "S"], areas_title="This week by area",
    bars=[("Neck", 86), ("Breathing", 64), ("Eyes", 42), ("Hands", 30), ("Legs", 52)],
    details_e="The details", details_h="Fits into your day.",
    details=[("cloud", "Synced through iCloud", "Your history and routines sync across your iPhone and iPad through your own iCloud."),
             ("nopods", "Without AirPods, too", "Neck exercises can run on a timer. The other exercises never need AirPods."),
             ("bell", "Reminders you choose", "A daily reminder, desk breaks through your busy hours and a weekly summary, each one optional."),
             ("voice", "Guided by sound", "Spoken cues, sounds and haptics guide you, so your eyes can stay off the screen."),
             ("a11y", "Made for everyone", "Dynamic Type, VoiceOver and Reduce Motion, on iPhone and iPad."),
             ("globe", "12 languages", "English, Turkish, German, Spanish, French, Italian, Portuguese, Dutch, Russian, Japanese, Korean and Chinese (Simplified and Traditional).")],
    trust_e="Privacy and trust", trust_h="Calm, private and honest.",
    trust=[("Stays on your device", "Motion data is processed on your phone and raw motion is never stored. No account needed."),
           ("At your own pace", "Moves should feel slow and comfortable. If something feels off, stop right away. Nodly never pushes you."),
           ("Not a medical device", "Nodly is a wellness app; it doesn't diagnose or treat any condition. If you have a neck condition, check with a health professional before you start.")],
    legal_e="Legal", legal_h="The short version.",
    legal=[("privacy", "Privacy Policy", "No account, and your motion data stays on your device. We collect anonymous usage statistics only if you allow it. No ads, no tracking, no selling of data."),
           ("terms", "Terms of Use", "Nodly is offered as a monthly or yearly subscription, and eligible users get a 7-day free trial. You can cancel any time in your App Store account settings."),
           ("health", "Health & safety", "Move slowly and only within a comfortable range. Stop right away if you feel pain, dizziness or numbness.")],
    more="Read the full text",
    end_h="Take your first break today.", end_s="On the App Store, for iPhone and iPad.",
    disclaimer="Nodly is a wellness app, not a medical device.",
    nav={"privacy": "Privacy", "terms": "Terms", "health": "Health & safety", "support": "Support"},
    home="Home",
    health_title="Health & safety",
)
