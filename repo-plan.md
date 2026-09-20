# Sonar Repository Plan

This document records the intended setup for creating a standalone git
repository for the sonar work. It is a plan to be executed later; it captures
the suggested name, description, layout, and rationale.

Note: the project is inherently **underwater sonar**. Everything in the track
is built around sensing through water — sound travelling at ~1500 m/s, seawater
absorption, ambient noise and reverberation, hydrophone (underwater
microphone) arrays, target bearings, and Doppler. There is no non-underwater
sonar in this project.

## Suggested name

**Recommended: `active-sonar-basics`**

- Clear, discoverable, mirrors the repo it grew from
  (`active-radar-tracker-basics`) while standing fully on its own.
- The "active" prefix signals active sonar (send a ping, listen for the echo)
  rather than passive listening.
- Alternatives, in preference order:
  - `sonar-tracking-basics` — if tracking is the selling point
  - `underwater-ping-basics` — playful, water-themed
  - `sonar-beginners` — short and explicit

## Suggested description

> A beginner-friendly, notebook-driven course introducing active sonar from
> first principles: the ping, FM sweeps, the sonar equation, matched filtering,
> Doppler and range–Doppler maps, Kalman contact tracking, hydrophone-array
> beamforming with adaptive nulling — and a synthetic aperture imaging capstone
> that forms an image of the seafloor from the same building blocks. Each
> concept is taught by hand first, then packaged into small reusable helpers
> across notebooks 00–11.

## Suggested repo layout

The layout below reflects the updated beginner-first sonar structure agreed for
this repository. It keeps the learner path obvious (`notebooks/`) and groups
written companions under `docs/`.

```
active-sonar-basics/
├── README.md                    # one-paragraph pitch + quickstart + links
├── LICENSE
├── notebooks/                   # 00–11 lesson notebooks (.ipynb, 11 = capstone)
│   └── helpers/                 # notebook-local helper package (constants, waveforms, equation,
│                                #   channel, math, doppler, kalman, array, doa, steering, plotting)
├── docs/
│   ├── physics/                 # notebook companion explanations and derivations
│   └── publishing/              # (future) docs publishing notes
├── 00-intro-story.md            # standalone narrative
├── notebook-playbook.md         # build plan
├── notebook-compliance-checklist.md
├── presentations/
│   ├── 00-intro/                # Act 1 deck (one deck per act)
│   ├── 01-waves-and-ranging/
│   ├── …
│   └── 05-capstone-sas/         # final deck: the synthetic aperture image
└── output/                      # (optional, later) exported artifacts if needed
```

## Rationale for the key choices

- **`notebooks/` at the root** — the whole repo is the beginner track, so the
  learner path should be immediately visible.
- **`docs/physics/`** — keeps physics companions near future written material
  without cluttering the root.
- **`presentations/` one folder per act** — keeps slide decks aligned with the
  five acts, and gives each deck a build of its own.
- **`.gitignore`** — add up front: `output/*.png`, `__pycache__/`, `.venv/`,
  `.ipynb_checkpoints/`.

## Steps to execute later

1. `mkdir active-sonar-basics` and `git init`.
2. Create `notebooks/` and `notebooks/helpers/`.
3. Create `docs/physics/` and move companion write-ups there.
4. Add `README.md`, `LICENSE`, `.gitignore`.
5. Keep `presentations/` as the future deck workspace.
6. Commit the skeleton, then build notebooks 00–01 first (see
   `notebook-playbook.md`).