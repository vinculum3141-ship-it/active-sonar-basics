# Sonar Track — Notebook Build Plan (Playbook)

This document is the step-by-step build guide for the beginner sonar notebooks
under `notebooks/`. It defines the educational standard used across
the sonar track and applies it notebook by notebook, so every chapter can be
written quickly, consistently, and in the right order.

The rule is simple: build the notebooks around the physics and learning goals
first, and use code only as the demonstration vehicle. Shared notebook
functionality lives under `notebooks/helpers/`.

---

## 1. The compliance standard this track follows

Every sonar notebook is only complete when it meets the following standard:

1. **Readable for a beginner.**
   - Clear chapter titles.
   - Short explanatory paragraphs.
   - Concrete examples before abstractions.
   - No unexplained jargon (define *ping*, *contact*, *bearing*, *target
     strength*, *reverberation* the first time they appear).
2. **Necessary math and physics.**
   - The relevant equation must be shown explicitly (`R = c·τ_delay / 2`,
     `RL = SL − 2·TL + TS`, `f_d = 2v/λ`, …).
   - The equation must be explained in plain language.
   - The lesson must connect the equation to a physical interpretation.
3. **Calculations in explicit cells.**
   - At least one cell computes the core quantity by hand, with the variables
     visible so the student can see the arithmetic.
   - The student should see the same formula in code and in prose.
4. **Implementation in beginner-friendly cells.**
   - A worked example must appear before any helper is used.
   - The first occurrence of a concept shows the direct implementation in the
     notebook itself, followed by the helper as a clean, reusable repetition —
     never a mystery shortcut.
   - Each notebook opens the hands-on part by moving naturally from the story
     to the equations, then into code, printed results, and finally the same
     calculation in reusable helper form.
5. **Shared helpers for later reuse.**
   - Shared functionality belongs in the notebook-local helper package
     (`notebooks/helpers/`); later notebooks call the helper API instead of
     duplicating logic.
6. **Final summary and learning checkpoint.**
   - The notebook ends by recalling the key equations and the main physical
     idea, closes the loop on the opening questions, and finishes with a short
     set of learner checks plus a stretch exercise.
   - The notebook also provides a student-facing answer section that explains
     the checkpoint questions, corrects the common mistakes in detail, and
     gives the stretch exercise as a runnable code snippet with explanation.

### Notebook and companion pairing

Each notebook should have a matching physics companion in `docs/physics/`.
The companion is read first and should set up the story, the symbols, and the
physical interpretation the notebook will then work through in code. Keep the
two aligned in sequence, but do not duplicate the same bridge sentence in both
places.

### Required ordering inside every sonar notebook

1. Chapter title and learning goals ("What this notebook teaches").
2. Short narrative framing ("Where we are in the story").
3. Setup and baseline values.
4. Story-to-equation transition before the first calculation.
5. Core model or physical idea (with the governing equation, explained).
6. Explicit code calculations with printed results.
7. Reusable helper form of the same calculation.
8. Output and interpretation (plots that reinforce the lesson).
9. "Checkpoint", "Common mistake", "Why the helpers exist", "Stretch".
10. "Closing the loop" answers + "Summary" that connects back to the sonar
    story and to earlier notebooks in the track.
11. "Answers and corrections" that explain the checkpoint questions,
  the common mistakes, and the stretch exercise in detail.
12. A runnable stretch snippet, when appropriate, with a short explanation of
  what it demonstrates and why it matters.

---

## 2. Baseline sonar scene (shared by all notebooks)

One fixed teaching scenario, chosen so the numbers behave cleanly and remain
verifiable across every chapter. It is deliberately a **short-range sonar**
scene — this keeps the ping rate high enough that per-ping Doppler stays
unambiguous (see the physics note in §3).

| Quantity | Value | What it controls |
|---|---|---|
| Sound speed `c` | 1500 m/s | The "c" in every delay and wavelength formula |
| Carrier `f_c` | 15 kHz | Sets wavelength `λ = c / f_c = 0.1 m` and Doppler |
| Bandwidth `B` | 1 kHz | Range resolution via pulse compression |
| Ping width `τ` | 50 ms | Duration of each transmitted sound burst |
| Inter-ping interval `T` | 0.2 s | Ping rate (PRF) = 5 Hz; the "listen window" |
| Sampling rate `f_s` | 10 kHz | Samples per second in fast time |
| Pings per CPI `N` | 64 | Slow-time samples for the Doppler FFT |
| Target range `R` | 75 m | Round-trip delay = 0.100 s = 1000 samples |
| Target velocity `v` | 0.1 m/s (~0.2 kn) | Inside the unambiguous band on purpose |
| Target bearing | +20° from broadside | Used by the array notebooks |
| Interferer bearing | −30° from broadside | 30 dB stronger than the target |

Numbers worth locking in, because later notebooks reuse them:

- `τ_delay = 2R / c = 0.1 s`, which at `f_s = 10 kHz` is 1000 samples.
- Ping length in samples: `f_s·τ = 500`. The 0.15 s listen window fits the
  echo comfortably.
- Range resolution: `c / (2B) = 0.75 m` after compression.
- Time–bandwidth product: `B·τ = 50`.
- Wavelength: `λ = 0.1 m`; array spacing `d = λ/2 = 5 cm`.
- Doppler: `f_d = 2v/λ = 2 Hz` for the 0.1 m/s target.
- Unambiguous velocity: `±λ·PRF/4 = ±0.125 m/s`; velocity resolution
  `λ/(2·N·T) ≈ 0.004 m/s`.
- CPI duration: `N·T = 12.8 s` (a fresh contact every ~13 s for the tracker).
- Transmission loss at baseline range: `TL = 20·log10(75) + α·75` dB (with a
  small textbook absorption `α`, e.g. ≈ 1 dB/km at 15 kHz) — the value the
  channel model turns into an attenuation in dB.

---

## 3. Physics notes — sonar-specific teaching points

These are the physical realities that shape every notebook in this track.
They should appear as deliberate teaching points, not hidden changes or
caveats:

1. **Sound is slow.** `c ≈ 1500 m/s` is orders of magnitude slower than
   electromagnetic waves, so delays are long and ranges are short. Express
   all "delay → range" examples with `c = 1500`, and let the student feel
   how different that is.
2. **Absorption.** Water absorbs sound, and loss grows steeply with frequency.
   This is the defining trade-off of sonar: high frequency buys resolution,
   low frequency buys range. The frequency trade-off belongs in Notebook 02.
3. **Noise is ambient, not thermal.** The corrupting background is wind, waves,
   shipping, and marine life (ambient noise), plus **reverberation** — echoes
   off the water, the surface, and the floor. Model it as AWGN for the
   beginner track and mention reverberation explicitly.
4. **Doppler needs a fast ping rate.** Per-ping Doppler (FFT across pings) only
   works when the ping rate exceeds the highest Doppler shift that can appear.
   This is why the baseline scene is deliberately short-range with a 5 Hz ping
   rate. The trainer should teach this constraint in Notebook 05 (it is a
   *feature* of sonar, not a limitation) and mention intra-ping Doppler on a
   long CW ping as the common alternative — a stretch discussion, not a
   requirement.
5. **Terminology.** Sonar carries its own established words: ping, contact,
   bearing, target strength, transmission loss, reverberation, hydrophone.
   The underlying mathematical framework is the same one described in the
   compliance standard; only the labels change.

---

## 4. Build order

Build in this sequence to move fastest:

1. Lock the notebook spine and titles (00–11).
2. Define the sonar helper structure and import rules (`notebooks/helpers/`).
3. Write the shared notebook template and teaching style (§1).
4. Draft trainer notes per notebook before writing code cells.
5. Build Notebook 00 and 01 first to establish the pattern.
6. Build the remaining notebooks in dependency order (02 → 03 → 04 → 05 → 06 →
   07 → 08 → 09 → 10 → 11).
7. Add checkpoint questions and stretch exercises after each notebook.
8. Run the quality pass (review gate in §8) once the spine is complete.

---

## 5. Notebook-by-notebook plan

Each plan lists the learner goal, the required content, the code cells in
order, and the trainer companion notes, mapped to the checklist's required
ordering. For every notebook the narrative should flow from the story to the
equations, then to the code, the printed results, and finally the reusable
helper form of the same calculation.

### Notebook 00 — Sonar intuition and baseline parameters

**Learner goal:** understand what active sonar is and why the baseline
parameters were chosen.

**Must contain:**

- Active vs passive sonar, and why active sonar *pings then listens*.
- The transmit–listen rhythm: ping width `τ`, inter-ping interval `T`
  (inter-ping time), ping rate, and duty cycle `D = τ/T`.
- The quiet-listen principle and the round-trip relation `R = c·τ_delay / 2`
  with `c = 1500 m/s`.
- Baseline parameter table (from §2) with every number explained.
- One simple calculation each for duty cycle and round-trip delay → samples.

**Code cells should show:**

- Importing baseline constants from the local `helpers` package under
  `notebooks/helpers/`.
- Duty-cycle calculation in code with printed explanation.
- Delay-to-range calculation `R = c·τ_delay / 2` in code with printed explanation.
- Delay in samples: 0.1 s at 10 kHz = 1000 samples.
- A ping/listen timing diagram (narrow transmit bar, wide listening bar).

**Trainer companion notes:**

- Lead with the "shout into a canyon, then listen for the echo" analogy.
- Emphasise every baseline number is intentional, not arbitrary — especially
  the deliberately slow 0.1 m/s target chosen for later Doppler discussion.
- Emphasise that the choice of sound as the carrier — not radio, not light —
  is what makes underwater sensing possible.
- Plant the first seed for the capstone: in practice the sonar platform is
  moving, so each ping is transmitted from a slightly different position. That
  motion will be used to build a long virtual array in the capstone chapter.

### Notebook 01 — Ping generation and FM sweep intuition

**Learner goal:** see how a plain tone burst becomes an FM sweep and why the
sweep improves range resolution in water.

**Must contain:**

- The tonal burst (CW): a short block of a single 15 kHz tone.
- The LFM (FM) sweep: same length, frequency rises linearly across `B`.
  `s(t) = exp(j·π·(B/τ)·t²)`.
- The frequency-ramp plot that separates sweep from tone.
- Range resolution: `ΔR = cτ/2` for the tone burst vs `ΔR = c/(2B)` for the
  swept ping — `37.5 m` vs `0.75 m`.
- Time–bandwidth product `TBP = B·τ = 50` and what it promises.

**Code cells should show:**

- Tone burst and FM sweep waveforms in time (real/imaginary).
- Instantaneous frequency sweep plot.
- TBP and resolution arithmetic by hand, then via a `fm_sweep` helper.
- A matched-filter compression preview (tone stays wide, sweep collapses).

**Trainer companion notes:**

- Keep it about the transmit waveform only; the full chain comes later.
- Foreshadow that the *tone* burst will matter again in Notebook 05 (Doppler)
  and that the *sweep* buys range resolution.

### Notebook 02 — The sonar equation

**Learner goal:** understand why echoes in water are so weak and how the sonar
equation connects source level, range, and target properties to the received
level.

**Must contain:**

- Why echoes are weak: spreading on the way out, reflection, spreading on the
  way back, **and absorption** along the path.
- The sonar equation in receiver form: `RL = SL − 2·TL + TS` with every term
  explained (source level, transmission loss, target strength).
- Transmission loss `TL = 20·log10(R) + α·R`: spherical spreading twice (the
  `RL` drops 20 dB per decade, twice) plus absorption `α` that grows with
  frequency.
- Target strength `TS` in dB — the sonar descriptor of how much of the
  incident sound the target scatters back — and why it is not physical size.
- Computing the round-trip loss for the 75 m baseline and connecting it to the
  attenuation dB used in Notebook 03.

**Code cells should show:**

- The two-way loss curve vs range on a log axis (spreading slope `−40 dB` per
  decade plus absorption).
- Explicit TL and RL arithmetic by hand.
- Baseline round-trip attenuation in dB.

**Trainer companion notes:**

- This is the physics foundation for every receive-side notebook.
- Stress the round-trip nature of the loss and the frequency resolution-vs-range
  trade-off created by absorption — the defining knob of underwater sensing.
- Make clear the attenuation used later is derived here, not arbitrary.

### Notebook 03 — Channel model and echoes in water

**Learner goal:** understand how a transmitted ping becomes a delayed,
attenuated, noise-corrupted echo.

**Must contain:**

- Range-to-delay conversion with `c = 1500 m/s` (0.1 s → 1000 samples).
- The one-target channel model: place a shifted, scaled copy of the ping.
- Attenuation: the transmission loss from Notebook 02 as a dB scale factor.
- Noise: ambient noise modeled as AWGN to a chosen SNR, and a note that real
  sonar noise is ambient + reverberation.
- A transmit-ping / clean-echo / noisy-return three-panel comparison.

**Code cells should show:**

- `delay_samples_for_range` style arithmetic by hand.
- Echo placement in the received buffer (copy at sample 1000).
- Attenuation scaling + AWGN.
- Three-panel plot (transmit, echo, corrupted return).

**Trainer companion notes:**

- The echo is a *copy* of the ping — shifted and scaled, never reshaped — the
  noise is what makes it look different.
- Keep a second-target stretch optional (overlapping echoes).

### Notebook 04 — Correlation (matched filtering) and range estimation

**Learner goal:** understand correlation as the implementation of matched
filtering, and turn a compressed peak delay into a range in metres.

**Must contain:**

- Correlation with a replica of the ping as the matched-filter operation.
- Why the swept-ping peak is sharper than the tone-burst peak.
- Peak location → sample delay → `R = c·τ_delay / 2`.
- Raw echo vs compressed output comparison.
- Why thresholding the raw return fails.

**Code cells should show:**

- Correlation by hand (`y[k] = Σ x[n]·s*[n−k]`).
- Matched-filter output, peak detection, and the range read-out.
- Clean vs noisy return against the compressed peak.
- The two-target stretch: overlapping echoes resolved only by the sweep.

**Trainer companion notes:**

- Pause on "the filter is looking for a known shape".
- Point back to Notebook 01: this is where the promise of bandwidth pays off.

### Notebook 05 — Doppler and the range-Doppler map

**Learner goal:** understand fast time vs slow time and how Doppler turns
ping-to-ping phase advance into radial velocity.

**Must contain:**

- Fast time (inside one ping, 10 kHz) carries range; slow time (ping-to-ping,
  5 Hz) carries velocity — the two clocks of sonar.
- Why a moving target's echo *phase* advances from ping to ping
  (`f_d = 2v/λ`), while its magnitude stays steady.
- The 64-ping stack as a 2-D grid: rows are pings (slow time), columns are
  range bins (fast time), values are complex.
- Slow-time FFT at each range bin → range-Doppler map.
- Velocity resolution `Δv = λ/(2·N·T) ≈ 0.004 m/s` and the unambiguous band
  `±λ·PRF/4 = ±0.125 m/s`.
- The deliberate aliasing case: a 0.5 m/s target folds to a wrong speed.

**Code cells should show:**

- Building the ping stack with phase rotation `2π·f_d·T` per ping.
- The phase-advance plot at the target range bin.
- Correlation-based matched filtering for every ping into range profiles.
- FFT across pings at every range bin.
- The range-Doppler heatmap with one blob at 75 m, 0.1 m/s.
- The 0.5 m/s aliasing example for the "wrong speed" teaching point.

**Trainer companion notes:**

- This is the first major milestone of the track.
- Teach the physics note from §3.4: per-ping Doppler only works because the
  baseline is short-range with a 5 Hz ping rate; mention intra-ping Doppler on
  a long CW ping as the real-world alternative (stretch discussion only).
- Keep delay (fast time) vs phase rotation (slow time) explicit.
- Seed the capstone: point out that the ping stack is also a spatial dataset —
  each row is a ping from a slightly different platform position. The
  along-track dimension carries both Doppler *and* the spatial diversity that
  the capstone chapter will exploit as a synthetic aperture.

### Notebook 06 — Kalman tracking of contacts

**Learner goal:** see how noisy range-and-velocity contacts become a stable
track over time.

**Must contain:**

- One noisy contact is not enough; measurements wobble around the truth.
- State vector `x = [range, velocity]` and covariance `P` as the filter's belief.
- Predict step (constant-velocity model, `range += v·dt`) and update step
  (blend with the new contact via the Kalman gain `K`).
- Process noise `Q` vs measurement noise `R`, and how `K` balances model vs
  sensor trust.
- True vs measured vs tracked trajectories over ~8 CPIs (~100 s).

**Code cells should show:**

- A synthetic contact sequence from the range-Doppler map.
- Predict and update by hand for the first step (2×2 matrix visible).
- The full tracking loop.
- Track plot + Kalman-gain-over-time plot (high trust early, settling later).

**Trainer companion notes:**

- In sonar this is contact tracking and a step toward automatic target
  tracking and target motion analysis (TMA).
- Do not over-mathematize; keep the plot central.

### Notebook 07 — Hydrophone array geometry and beam patterns

**Learner goal:** understand how a line array of hydrophones measures bearing
and why beam patterns have main lobes, sidelobes, and grating lobes.

**Must contain:**

- A uniform linear array (ULA) of hydrophones at half-wavelength spacing
  `d = λ/2 = 5 cm`.
- Path difference `d·sin(θ)` and the inter-element phase step
  `Δφ = 2π·(d/λ)·sin(θ)` = `π·sin(θ)`.
- The steering vector `a(θ) = [1, e^{jΔφ}, …, e^{j(N−1)Δφ}]`.
- The array factor, main lobe, sidelobes, first-null beamwidth.
- Steering the beam and grating-lobe risk when `d > λ/2`.

**Code cells should show:**

- Manual phase-step arithmetic for the 20° target.
- Steering vector values at 20°.
- Beam-pattern sweep for `N = 8` hydrophones.
- A grating-lobe comparison (`d = λ/2` vs `d = 3λ/2`).

**Trainer companion notes:**

- Use geometry language before matrix language.
- Keep `N` small so the pattern is easy to read.
- This chapter carries the conceptual bridge to the capstone: resolution is set
  by total aperture length. A physical array is fixed and short (here 8
  elements, about 0.4 m), but a moving platform revisits that geometry with a
  synthetic aperture (Chapter 11). Teach the steering vector as the general
  tool — it applies with equal ease to the physical array and the synthetic one.

### Notebook 08 — Direction of arrival and interference

**Learner goal:** compare Bartlett and Capon scans, and see how a loud
interferer can mask a weak contact.

**Must contain:**

- Array snapshots → sample covariance `R`.
- Bartlett (delay-and-sum) scan and why its resolution is the array beamwidth.
- Capon/MVDR scan `P ≈ 1/(a^H R⁻¹ a)` and its adaptive nulls.
- Two targets 10° apart: Bartlett merges, Capon splits.
- A strong interferer (−30°, 30 dB stronger) masking the target at +20° in
  Bartlett; Capon recovers it.

**Code cells should show:**

- Covariance from snapshots (by hand first, then helper).
- Bartlett spectrum, Capon spectrum, side-by-side.
- The no-interferer / interferer before-and-after scan overlay.

**Trainer companion notes:**

- Frame interference honestly for sonar: another ship's echo, own-vessel noise,
  or a jamming projector.
- Capon needs enough snapshots — that's the stretch discussion.

### Notebook 09 — Beam steering and adaptive nulling

**Learner goal:** understand how steering plus LCMV nulling silences an
interferer while preserving the target.

**Must contain:**

- Combining hydrophone channels is choosing a weight vector `w`, output
  `y = w^H x`.
- Steering weights point the main lobe at +20°.
- Why steering alone leaves a sidelobe at −30° that the 30 dB-stronger
  interferer punches through.
- The LCMV constraint `C^H w = [1, 0]` forcing a null on the interferer.
- Applying the weights **before** the matched filter (correlation step), then showing the
  range-Doppler map before and after cancellation.

**Code cells should show:**

- Steering weights and the beam toward the target.
- LCMV weights and the beam with a deep null at −30°.
- Range-Doppler map before (interferer leaks through) and after (it drops to
  the noise floor; target survives).

**Trainer companion notes:**

- Explain why nulling is a spatial operation done before the temporal matched
  filter — the beamformer shapes the array response, the matched filter
  shapes delay resolution, and they must appear in that order.
- Emphasise the target must remain visible after cancellation.

### Notebook 10 — Integration and portfolio artifacts

**Learner goal:** connect the full sonar chain and produce the final portfolio
artifacts.

**Must contain:**

- End-to-end recap: ping → compress to range → FFT across pings to velocity →
  Kalman track → beamform for bearing → steer and null against interference.
- Four artifacts on one figure: the swept ping waveform, the range-Doppler map,
  the beam-null overlay, the DOA scan.
- Shared-baseline consistency check and PNG export.
- A "where we are going" pointer to the capstone chapter, which will re-use
  this same baseline and add the seafloor image.

**Code cells should show:**

- Short cells that reproduce each artifact from helpers (celebrating the
  helpers built in earlier notebooks).
- The composite portfolio figure.
- Saving the figure to `sonar_portfolio.png` and confirming it exists.

**Trainer companion notes:**

- Use this notebook as the final story review; ask the learner to explain the
  whole chain in their own words.

### Notebook 11 — Capstone: synthetic aperture imaging

**Learner goal:** combine the matched-filter / correlation step, the ping
stack, and the steering vector into a two-dimensional image of the seafloor —
the capstone project.

**Pedagogy frame:** nothing here is new. The capstone reuses three tools the
reader already holds: the matched filter / correlation step (Chapter 04), the ping stack (Chapter
05), and the steering-vector correlation (Chapters 07–09). Aperture compression
along the track is the *same* correlation the reader has already run in range —
only the axis changes. If it feels advanced, the framing is wrong; it must feel
like "we compress in the other direction now."

**Must contain:**

- Baseline extension: platform speed `v_platform = 0.25 m/s` along-track → a
  spatial sample every `Δx = v_platform·T = 0.05 m` (exactly `λ/2`, the
  grating-lobe-safe spacing from Chapter 07). 64 pings → synthetic aperture
  `L_SAS = 64·Δx = 3.2 m`.
- Geometry: a point target at 75 m appears in every ping at a slightly
  different delay because the platform moves; the phase history across the
  track is the *data* of the synthetic array.
- Range compression: correlation / matched filter each row (review + reuse of Chapter 04).
- Along-track (azimuth) compression: correlate the phase history with the
  steering/correlation kernel — the same operation as the matched filter,
  applied across the track.
- The resolution payoff, computed by hand:
  - Physical array cross-range at 75 m: `λ/(N·d)·R = (0.1/0.4)·75 ≈ 18.8 m`.
  - Synthetic aperture cross-range: `λ·R/(2·L_SAS) ≈ 1.2 m` — an order of
    magnitude better from nothing but platform motion.
- A 2-D image: range along one axis, cross-range along the other, with point
  targets turned into sharp lower-left blobs.
- Before/after: the physical-array beam pattern (broad) vs the synthetic-image
  point response (sharp).

**Code cells should show:**

- The moving-platform ping stack (stationary scene; platform travels at
  0.25 m/s).
- Range-compressed stack (correlation / matched filter per row).
- The along-track correlation by hand for one target range.
- The full 2-D synthetic-aperture image.
- A resolution comparison panel: physical array vs synthetic aperture.

**Trainer companion notes:**

- Do not introduce motion-compensation, autofocus, or imaging jargon. The
  beginner capstone assumes a straight, constant-speed track — nothing fancy.
- Emphasise "same tool, second axis": the seafloor image is a correlation /
  matched-filter operation in range and a correlation / matched-filter
  operation in cross-range. The chapter is the payoff of
  everything before it, not a new subject.
- Close the whole track by having the learner say the full one-breath arc,
  ending with "…synthesize an image of the seafloor."

---

## 6. Helper package (`notebooks/helpers/`)

Organise helpers so each module's purpose is obvious at a glance:

| Module | Provides |
|---|---|
| `constants.py` | Baseline sonar scene from §2 (carrier, bandwidth, ping width, `T`, `f_s`, `N`, `R`, `v`, bearings, `c`) |
| `waveforms.py` | `tone_burst`, `fm_sweep`, instantaneous frequency helpers |
| `equation.py` | `transmission_loss`, `two_way_loss_db`, `sonar_equation` (RL/TL/TS) |
| `channel.py` | `add_echo`, `awgn` (ambient noise model), `single_target_channel` |
| `math.py` | `matched_filter`, `range_from_delay_samples`, `delay_samples_for_range` |
| `doppler.py` | `build_ping_stack`, `range_doppler_map`, unambiguous velocity |
| `kalman.py` | `state_transition_matrix`, `predict`, `update`, `run_kalman_track` |
| `array.py` | `steering_vector`, `array_factor`, `first_null_angle_deg` |
| `doa.py` | `sample_covariance`, `bartlett_spectrum`, `mvdr_spectrum` |
| `steering.py` | `steering_weights`, `lcmv_weights` |
| `sas.py` | `along_track_positions`, `range_compress_stack`, `synthetic_aperture_image` (capstone, Chapter 11) |
| `plotting.py` | Shared plotting style and panel labels |

Rule from compliance item 5: each concept is written once in the notebook,
explained with its printed result, and then repeated in helper form so later
notebooks can reuse the same calculation without rewriting it.

---

## 7. Trainer packet per notebook

Keep a companion notes page per notebook with these fields:

- Notebook number and title.
- Lesson objective in one sentence.
- Prerequisites.
- 3–5 key talking points (including any sonar-specific point from §3).
- Suggested pacing.
- What to demo live.
- Likely learner confusions (e.g. treating target strength as physical size;
  confusing ambient noise with receiver noise; misreading the unambiguous
  velocity band).
- Checkpoint answer key.
- Optional stretch prompt.

Suggested trainer flow per notebook:

1. Start with the objective.
2. Define the one new concept.
3. Run the main plot or calculation.
4. Ask the checkpoint question.
5. Close with the takeaway and the next notebook.

---

## 8. Review gate (acceptance checklist)

Before a sonar notebook is considered done:

- The learner goal is explicit and stated as "you" (address the reader
  directly).
- The notebook teaches one primary concept.
- The math is visible, explained in plain language, and connected to physics.
- At least one cell computes the core quantity by hand; a helper reproduces the
  same result afterward.
- The notebook tells a clear story: physical setup, equation, code, printed
  result, helper reuse.
- Code cells are small, seeded, and include intermediate values.
- The plots reinforce the lesson (transmit/listen diagram, sweep ramp, echo
  panels, beam patterns, RD map, track, before/after nulling, portfolio, and
  the capstone's synthetic-aperture image).
- Checkpoint, common mistakes, stretch, closing-the-loop, and summary sections
  are present and sonar-faithful.
- The notebook also includes a student-facing answers section after the
  summary, with detailed explanations for the checkpoint questions, corrections
  for the common mistakes, and a runnable stretch snippet where appropriate.
- Later notebooks reuse `notebooks/helpers/` for repeated logic.
- The chapter fits the sequence 00–11 and links back to the sonar intro story.
- Notebook 11 re-uses the helpers and tools from earlier chapters; it does not
  introduce a new technique beyond the matched filter applied along a second
  axis.
- The notebook runs without errors from a clean restart.
- Notebook numbers, symbols, and baseline values stay consistent across the
  series (§2).

## 9. Future editorial pass (after notebook build is complete)

Once the notebook series is complete and stable, run one documentation
consolidation review:

- Review all companion documents in `docs/physics/`.
- Evaluate whether they should remain chapter-by-chapter only, or also be
  combined into a single student-facing reference document.
- Do not perform this consolidation during notebook drafting; treat it as a
  post-build editorial step.