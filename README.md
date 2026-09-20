# active-sonar-basics

Notebook-driven course teaching active sonar from first principles: pings, FM
sweeps, the sonar equation, matched filtering, Doppler, Kalman tracking, and
beamforming, capped by a synthetic-aperture imaging project that images the
seafloor using the same building blocks. Every concept is built by hand first,
then packaged into reusable helpers.

The source training course is reference material, not a template to duplicate.
This repository is being built to stand on its own, with notebook boundaries,
ordering, and supporting documents chosen by the physics and the learner's path
rather than by inheritance from the earlier course.

## Current layout

- `notebooks/` holds the learner notebooks.
- `docs/physics/` holds standalone companion markdown documents that define and
	explain the physics independently of the notebooks.
- `notebooks/helpers/` holds the reusable helper code introduced only after
	each idea is first shown directly in a notebook.
- Root planning documents remain available while the notebook series is being
	built out.

## Quickstart

```bash
cd notebooks
jupyter notebook
```

The notebooks import helpers locally from `helpers/` in the same folder.
