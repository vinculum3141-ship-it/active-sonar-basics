# The Sonar Track: One Active Sonar, Built Layer by Layer

This story is a complete, self-contained introduction to active sonar — the art
of sensing underwater by sending a burst of sound into the sea and listening
for the echo. It is told in five acts, and each act will grow into its own
lesson. The whole arc is designed to run by itself; no other subject is
required to follow it.

The ocean is home territory for sound. Light and radio are swallowed by the
water within a short distance, but sound travels remarkably well through it at
about **1500 metres per second**. That simple fact is why sonar exists, and why
it works the way it does: every measurement the reader will make in this track
reduces, one way or another, to *timing a sound's journey through water*.

The planned chapters (00–11), in order:

1. **The ping** and the baseline sonar scene
2. The FM sweep — putting resolution into a long ping
3. The sonar equation — why echoes are so weak in water
4. The channel — what the water does to a ping
5. The matched filter — pulling the echo back out
6. Doppler and the range-Doppler map
7. Kalman tracking of contacts
8. Hydrophone arrays and beam patterns
9. Direction-of-arrival and interference
10. Beam steering and adaptive nulling
11. **Capstone: synthetic aperture imaging** — the seafloor picture

## Act 1 — The ping (00–02)

An active sonar transmits a short burst of sound into the water — a **ping** —
and then goes quiet to listen for the echo. Because sound travels at a known,
fixed speed, the delay between ping and return *is* the range measurement:

    R = c · τ_delay / 2

The `/2` appears because the sound makes a round trip. And the speed matters
physically: at ~1500 m/s the round trip is slow, so a useful sonar range of a
few tens to hundreds of metres takes tenths of a second, not microseconds.
Sonar measures *long delays*, and the first lessons live in that feel.

The plain tone burst of chapter 01 is replaced by an **FM sweep**: the same
ping length, but the frequency ramps during the ping, labelling every instant
with a unique frequency. This is the trick that makes modern sonar practical —
a long ping stays loud and reaches far, yet still sees fine detail, because
the bandwidth, not the length, sets the range resolution. The time-bandwidth
product prices exactly how much sharpness the sweep has bought.

Chapter 02 is the **sonar equation**, which says why an underwater echo comes
back so weak that raw listening is never enough. There are two losses at work.
First, geometric **spreading**: the sound spreads outward on the way there and
again on the way back, so the power that returns falls off far faster than the
range grows. Second, **absorption**: seawater drinks sound energy, and the
scarier part is that this loss grows steeply with frequency. High frequency
buys fine resolution but is absorbed within a few kilometres; low frequency
travels far but blurs. The equation is compactly written as

    RL = SL − 2·TL + TS

receive level equals source level, minus the two-way transmission loss, plus
the **target strength** — a target's signature in decibels. This one equation
is the foundation of everything on the receive side: it is why all the signal
processing that follows is necessary, because the echo simply does not come
back strong enough to be seen raw.

## Act 2 — Bringing the echo back (03–05)

The water does three things to every ping, and the channel chapter makes each
one visible: it **delays** it (range becomes a sample delay), it **weakens**
it (the transmission loss from the sonar equation, applied as a scale factor),
and it **corrupts** it. And here the noise is not the receiver's electronics —
it is the sea itself. **Ambient noise** — wind, waves, shipping, marine life —
fills the water, and the ping's own energy churns back as **reverberation**
off the surface, the floor, and the medium. That noisy, echoing water is what
a real echo must survive. One more thing the channel does, silently: the
sonar platform moves. Every ping is transmitted from a slightly different
position along the track, so successive echoes arrive from slightly different
angles. That motion is a nuisance for Doppler, but it is a gift for the
capstone — it builds a long virtual array out of nothing but time.

The **matched filter** is the tool that digs the echo out: slide a replica of
the transmitted sweep across the received signal, find where the two align,
and the noise washes away while the echo snaps into a sharp peak whose
position reads as range. The compression works because every instant of the
sweep has a distinctive frequency — only the true echo aligns sample for
sample.

Velocity follows from patience. Ping repeatedly, and a moving target's echo
does not move in range, but its *phase* rotates from ping to ping. An FFT
across pings — slow time, sampled at the ping rate — turns that rotation into
a Doppler frequency, which maps to a radial velocity. Stack the result as a
**range-Doppler map** and one glance shows both where a target is and how fast
it is moving. Doppler is a serious business underwater: a target's speed is a
meaningful fraction of the sound speed, so every knot of motion is clearly
visible — and so is the ambiguity when a target moves too fast for the ping
rate and folds over to a false speed.

## Act 3 — Staying sane over time (06)

Each ping cycle yields a fresh, noisy range-and-velocity **contact**. A single
contact is not to be trusted — it wobbles around the truth. The **Kalman
filter**, the contact tracker at the heart of a sonar operator's picture,
blends each new detection with a prediction from a model, weighing trust by
uncertainty. Noisy contacts in, a smooth, stable track out. This is the moment
the picture of the water stops being a single snapshot and becomes a
continuously updated story of where targets are and where they are going.

## Act 4 — Where is it bearing? (07–09)

A single hydrophone is a point: it can measure range and speed but never
*would a direction*. A **line array of hydrophones** — for example a towed
array — changes that. A wave arriving from off-broadside reaches each element
slightly out of phase, and the size of that phase step encodes the **bearing**.
From that geometry grow the steering vector, the beam pattern with its main
lobe and sidelobes, and the half-wavelength spacing that keeps false grating
lobes out of the picture.

This is where the capstone idea takes root. The array's resolution depends on
its total length: a longer array makes a narrower beam. But a physical array
cannot grow forever — a hundred hydrophones on a towed line would be
impractical. The capstone chapter shows what happens when the sonar platform
itself moves along the track: each ping is transmitted from a new position,
and those positions *are* the elements of an array that never physically
existed. The along-track ping stack becomes a **synthetic aperture**, and the
steering-vector math the reader just learned applies to it without change.

Scanning the beam finds directions — but naively. The **Bartlett** beamformer,
a simple delay-and-sum, cannot separate targets closer together than its own
beamwidth, and one loud interferer — another ship's echo, own-vessel noise, or
an enemy jamming projector — can **mask** a weak contact entirely. The
**Capon (MVDR)** scan listens adaptively instead: it drives deep nulls at every
source except the one being examined, splitting close targets and pulling a
masked contact back out of the noise. Finally, **LCMV** weights finish the job
by design: steer the main lobe onto the target while forcing a deep null on
the interferer at the same time. On the range-Doppler map the jammer's echo
collapses to the floor while the target survives untouched.

## Act 5 — The whole picture and the capstone (10–11)

Chapter 10 assembles the full chain onto one page: the swept ping, the
range-Doppler map, the beam-null overlay, and the bearing scan — all sharing
one baseline scene (15 kHz carrier, 1 kHz bandwidth FM sweep, 50 ms ping,
0.2 s inter-ping interval, target at 75 m, platform moving at 0.25 m/s) and
one set of helpers — exported as a single image.

Chapter 11 is the capstone: **synthetic aperture imaging**. Everything the
reader has built — the matched filter, the ping stack, the steering vector —
is reused without modification. The matched filter compresses in range (one
correlation, already learned). The along-track samples from the moving platform
are compressed with the same correlation applied across the track, and the
result is a two-dimensional image: range along one axis, cross-range along the
other. A physical array of 8 hydrophones sees a broad, blurry beam at 75 m;
the synthetic aperture, built from 64 pings at half-wavelength along-track
spacing, produces an image with cross-range resolution more than an order of
magnitude finer. The capstone is not new physics — it is every piece the
reader already holds, combined into a picture of the seafloor.

The arc, in one breath:

**Transmit a ping → compress it into range → FFT across pings into velocity →
track it with a Kalman filter → beamform the hydrophone array for bearing →
steer and null to hear past the noise and the jammer → synthesize an image of
the seafloor.**

If you can say that sentence and defend each step, you no longer hold seven
separate plots — you command one integrated sonar, from first principles to
a picture.

## Glossary

| Term | Definition |
|---|---|
| **Ping** | A short burst of sound transmitted into the water by an active sonar |
| **Inter-ping interval** | Time between the starts of consecutive pings; the "listen window" between transmissions |
| **Ping rate** | How many pings are sent per second (the sampling clock of slow time) |
| **Contact** | A detected, tracked object — the word sonar operators use for a target |
| **Bearing** | The angle of a contact, measured from broadside of the array |
| **Target strength (TS)** | How much of the incident sound a target scatters back, expressed in dB |
| **Source level (SL)** | The intensity of the transmitted ping, in dB |
| **Transmission loss (TL)** | What the water takes from the sound between the sonar and the target (spreading + absorption) |
| **Ambient noise** | The background water noise — wind, waves, shipping, marine life |
| **Reverberation** | Echoes of the ping scattered back from the water, surface, and floor |
| **Hydrophone** | An underwater microphone; the sonar's ear |
| **Doppler** | The apparent frequency shift caused by a contact's motion |
| **Range-Doppler map** | A two-dimensional picture of contacts by range (fast time) and velocity (slow time) |
| **Matched filter** | Correlation with a replica of the transmitted ping, used to pull an echo out of noise |
| **Beamforming** | Combining hydrophone channels with weights to listen in a chosen direction |
| **MVDR / Capon** | An adaptive scan that nulls all sources except the one being examined |
| **LCMV** | A constrained weight design that points at the target and nulls specified interferers |
| **Along-track** | The direction the sonar platform is moving; the axis sampled by successive pings |
| **Synthetic aperture** | An array built by moving a single hydrophone and recording pings at known positions along the track |
| **Cross-range resolution** | The finest detail the system can separate perpendicular to the line of sight |